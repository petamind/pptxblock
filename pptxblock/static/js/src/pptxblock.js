/* Javascript for PptXBlock. */
function PptXBlock(runtime, element) {

    // Settings---------------------------
    function updateVideoUrl(result) {
        $('.submited_video_url', element).text(result.video_url);
    }

    var handlerSubmitUrl = runtime.handlerUrl(element, 'submit_video_url');

    $('.video_url', element).submit(function(eventObject) {
        var video_url = $('#video_url').val();
        $.ajax({
            type: "POST",
            url: handlerSubmitUrl,
            data: JSON.stringify({"video_url": video_url}),
            success: updateVideoUrl
        });
    });
    // Demo---------------------------
    // function updateCount(result) {
    //     $('.count', element).text(result.count);
    // }

    // var handlerUrl = runtime.handlerUrl(element, 'increment_count');

    // $('p', element).click(function(eventObject) {
    //     $.ajax({
    //         type: "POST",
    //         url: handlerUrl,
    //         data: JSON.stringify({"hello": "world"}),
    //         success: updateCount
    //     });
    // });

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
}
