const $ = require('jquery');
global.$ = $;
const { showBadge } = require('../../openstackdocstheme/theme/openstackdocs/static/js/badge.js');

beforeEach(() => {
    document.body.innerHTML = '<div id="deprecated-badge-container"></div>';
});

test('inserts HTML into the container', () => {
    showBadge('<a href="/2026.1/">2026.1</a>', '');
    expect($('#deprecated-badge-container').html()).toContain('2026.1');
});

test('rewrites numeric series href when repoName is set', () => {
    showBadge('<a href="/2026.1/">link</a>', 'nova');
    expect($('#deprecated-badge-container a').attr('href')).toBe('/nova/2026.1/');
});

test('rewrites codename series href when repoName is set', () => {
    showBadge('<a href="/flamingo/">link</a>', 'nova');
    expect($('#deprecated-badge-container a').attr('href')).toBe('/nova/flamingo/');
});

test('does not rewrite multi-segment href', () => {
    showBadge('<a href="/nova/2026.1/page/">link</a>', 'nova');
    expect($('#deprecated-badge-container a').attr('href')).toBe('/nova/2026.1/page/');
});

test('does not rewrite when repoName is empty', () => {
    showBadge('<a href="/2026.1/">link</a>', '');
    expect($('#deprecated-badge-container a').attr('href')).toBe('/2026.1/');
});

test('does not rewrite uppercase path', () => {
    showBadge('<a href="/Nova/">link</a>', 'nova');
    expect($('#deprecated-badge-container a').attr('href')).toBe('/Nova/');
});
