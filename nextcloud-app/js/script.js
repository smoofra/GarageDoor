(function (OC, window, $, undefined) {
'use strict';

$(document).ready(function () {

    var update_status = function() {
        $.ajax({
            url: '/garagedoor',
            method: "GET"
        }).done(function (x) {
            $('#status').replaceWith('<span id="status">'+x+'<span>');
        }).fail( function() {
            $('#status').replaceWith('<span id="status">???<span>');
        });
    };

    update_status();

    $('button.refresh').click(update_status);

    $('button.click').click(function() {
        $.ajax({
            url: OC.generateUrl('/apps/garagedoor/click'),
            method: "POST"
        }).done(function (x) {
            alert(x);
        }).fail(function () {
            alert("failed");
        });
    });

});

})(OC, window, jQuery);
