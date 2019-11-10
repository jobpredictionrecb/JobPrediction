$(function(){
            setTimeout(function () {
                $('#loading').css('display','none');
            },300);
            setTimeout(function () {
                $('#popUpMain').css('display','block');
            },2000);
            $('#closeId').click(function () {
                $('#popUpMain').css('display','none');
            });

            $('#closeId2').click(function () {
                $('#popUpMain2').css('display','none');
            });
        });


	function loaderHide(){
        $('#loading').css('display','hide');
    }