#!/bin/bash

#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

# Build English and translated version of an RST document

set -e
set -x

DOCNAME=doc
DIRECTORY=doc

# This function sets the following global variables
# - LANG_INDEX : filename which contains the language index
# - HAS_LANG : 1 (there are languages other than English), 0 (English only)
function prepare_language_index {
    # Global variables
    HAS_LANG=0
    LANG_INDEX=`mktemp`
    trap "rm -f -- $LANG_INDEX" EXIT

    cat <<EOF >> $LANG_INDEX
[
\`English <__BASE__/__INDEX__>\`__
EOF

    # Generate language index file
    for locale in `find ${DIRECTORY}/source/locale/ -maxdepth 1 -type d` ; do
        # skip if it is not a valid language translation resource.
        if [ ! -e ${locale}/LC_MESSAGES/${DOCNAME}.po ]; then
            continue
        fi
        language=$(basename $locale)

        # Reference translated document from index file
        echo -n "| " >> $LANG_INDEX
        HAS_LANG=1
        get_lang_name_prog=$(dirname $0)/docstheme-lang-display-name.py
        name=`python3 $get_lang_name_prog $language`
        echo "\`$name <__BASE__/${language}/__INDEX__>\`__" >> $LANG_INDEX
    done

    cat <<EOF >> $LANG_INDEX
]

EOF
}

function _add_language_index {
    local target_file=$1
    local basepath=$2

    local basename
    basename=$(echo $target_file | sed -e "s|$DIRECTORY/source/||" -e "s|\.rst$||")
    path_to_top_level=$(dirname $basename | sed -e 's|[^./]\+|..|g')

    local _basepath
    if [ "$basepath" = "." -a "$path_to_top_level" = "." ]; then
        _basepath="."
    elif [ "$basepath" = "." ]; then
        _basepath=$path_to_top_level
    elif [ "$path_to_top_level" = "." ]; then
        _basepath=$basepath
    else
        _basepath="$basepath/$path_to_top_level"
    fi

    cp -p $target_file $target_file.backup
    sed -e "s|__BASE__|$_basepath|" -e "s|__INDEX__|$basename.html|" $LANG_INDEX > $target_file
    cat $target_file.backup >> $target_file
}

function add_language_index_to_localized {
    for f in `find $DIRECTORY/source -name '*.rst'`; do
        _add_language_index $f ..
    done
}

function add_language_index_to_original {
    for f in `find $DIRECTORY/source -name '*.rst'`; do
        cp -p $f.backup $f
        _add_language_index $REFERENCES $f .
    done
}

function recover_rst_files {
    for f in `find $DIRECTORY/source -name '*.rst'`; do
        mv $f.backup $f
    done
}

sphinx-build -a -W -b gettext \
    -d ${DIRECTORY}/build/doctrees.gettext \
    ${DIRECTORY}/source ${DIRECTORY}/source/locale/

prepare_language_index
if [ "$HAS_LANG" = "0" ]; then
    exit 0
fi
# Now add our references to the beginning of the index file. We cannot do this
# earlier since the sphinx commands will read this file.
# Ensure to revert any changes to the index file.
add_language_index_to_localized

# check all language translation resource
for locale in `find ${DIRECTORY}/source/locale/ -maxdepth 1 -type d` ; do
    # skip if it is not a valid language translation resource.
    if [ ! -e ${locale}/LC_MESSAGES/${DOCNAME}.po ]; then
        continue
    fi
    language=$(basename $locale)

    echo "===== Building $language translation ====="

    # prepare all translation resources
    for pot in ${DIRECTORY}/source/locale/*.pot ; do
        # get filename
        potname=$(basename $pot)
        resname=${potname%.pot}
        # merge all translation resources
        msgmerge --silent -o \
            ${DIRECTORY}/source/locale/${language}/LC_MESSAGES/${resname}.po \
            ${DIRECTORY}/source/locale/${language}/LC_MESSAGES/${DOCNAME}.po \
            ${DIRECTORY}/source/locale/${potname}
        # compile all translation resources
        msgfmt -o \
            ${DIRECTORY}/source/locale/${language}/LC_MESSAGES/${resname}.mo \
            ${DIRECTORY}/source/locale/${language}/LC_MESSAGES/${resname}.po
    done

    # build translated guide
    # TODO(amotoki): Enable -W option in translated version
    sphinx-build -a -b html -D language=${language} \
        -d ${DIRECTORY}/build/doctrees.languages/${language} \
        ${DIRECTORY}/source ${DIRECTORY}/build/html/${language}

    # remove newly created files
    git clean -f -q ${DIRECTORY}/source/locale/${language}/LC_MESSAGES/*.po
    git clean -f -x -q ${DIRECTORY}/source/locale/${language}/LC_MESSAGES/*.mo
    git clean -f -x -q ${DIRECTORY}/source/locale/.doctrees
    # revert changes to po file
    git reset -q ${DIRECTORY}/source/locale/${language}/LC_MESSAGES/${DOCNAME}.po
    git checkout -q -- ${DIRECTORY}/source/locale/${language}/LC_MESSAGES/${DOCNAME}.po
done

# remove newly created pot files
rm -f ${DIRECTORY}/source/locale/*.pot

add_language_index_to_original

# build English document
sphinx-build -a -W -b html \
    -d ${DIRECTORY}/build/doctrees \
    ${DIRECTORY}/source ${DIRECTORY}/build/html/

recover_rst_files
