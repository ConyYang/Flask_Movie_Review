$(function () {
    function render_time() {
        return moment($(this).data('timestamp')).format('llll')
    }
    $('[data-toggle="tooltip"]').tooltip(
        {title: render_time}
    );
});
