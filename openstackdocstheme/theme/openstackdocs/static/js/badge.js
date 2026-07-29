function showBadge(html, repoName) {
    var container = $('#deprecated-badge-container');
    container.html(html);
    if (repoName) {
        container.find('a[href]').each(function() {
            var href = $(this).attr('href');
            if (href && /^\/(\d{4}\.\d+|[a-z]+)\/$/.test(href)) {
                $(this).attr('href', '/' + repoName + href);
            }
        });
    }
}

if (typeof module !== 'undefined') {
    module.exports = { showBadge };
}
