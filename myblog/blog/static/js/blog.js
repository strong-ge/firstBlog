$(function () {
    $("#txtShow").click(function () {
        // $("#divShade").show();
        funShowDivCenter("#div_show");
        $("#txtSiteID").focus();
    });
    $("#btnCancel").click(function () {
        // $("#divShade").hide();
        $("#div_show").hide();
    });
});

//让指定的DIV始终显示在屏幕正中间
function funShowDivCenter(div) {
    var top = ($(window).height() - $(div).height()) / 2;
    var left = ($(window).width() - $(div).width()) / 2;
    var scrollTop = $(document).scrollTop();
    var scrollLeft = $(document).scrollLeft();
    $(div).css({ position: 'absolute', 'top': top + scrollTop, left: left + scrollLeft }).show();
}