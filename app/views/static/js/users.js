$(document).ready(function () {

    $('#show-id').click(function () {

        function show_id(user) {
            $("#user-id").text(user.id_)
            $("#modal-show-id").modal();
        }

        var user_id = 1;

        $.ajax({
            url: "/show_id/",
            type: "post",
            data: { 'user_id': user_id },
            success: function (user) {
                show_id(user)
            }
        });
    });

});