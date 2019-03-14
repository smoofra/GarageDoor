(function (OC, window, $, undefined) {
'use strict';

$(document).ready(function () {

    $('button').click(function() {

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
