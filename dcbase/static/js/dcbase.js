$.cookie('_tz_offset', (new Date()).getTimezoneOffset());
var dcbase = {
    createUrl: function (urlPattern) {
        var parts = urlPattern.split('0');
        var finalUrl = '';
        for (var i = 0; i < (parts.length - 1); i++) {
            finalUrl += parts[i];
            finalUrl += arguments[i + 1];
        }
        finalUrl += parts[parts.length - 1];
        return finalUrl;
    },

    createUserTypeahead: function(inputElement) {
        var usersFetch = new Bloodhound({
            datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value'),
            queryTokenizer: Bloodhound.tokenizers.whitespace,
            remote: '/accounts/match/?q=%QUERY'
        });
        usersFetch.initialize();

        $(inputElement).typeahead(null, {
            displayKey: 'value',
            source: usersFetch.ttAdapter(),
            templates: {
                suggestion: function(data) {
                    return '<img class="gravatar" src="' + data.avatar_url + '" width="25" height="25" /> ' + data.value;
                }
            }
        });
    }
};
