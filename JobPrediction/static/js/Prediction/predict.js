var i=1;
        var l=1;
        // To add field dynamically
        $(document).ready(function(){
            function fn1(){
                i++;
                $('#dynamic_field').append('<tr id="row'+i+'"><td>\n' +
                    '                            <div class="form-group">\n' +
                    '                                <select class="form-control" id="softskill" onchange="fun()">\n' +
                    '                                    <option>Select</option>\n' +
                    '                                    <option>Communication Skill</option>\n' +
                    '                                    <option>TimeManagement Skill</option>\n' +
                    '                                    <option>Problem Solving Skill</option>\n' +
                    '                                    <option>Leadership Skill</option>\n' +
                    '                                    <option>Self Confidence</option>\n' +
                    '                                </select>\n' +
                    '                            </div>\n' +
                    '                            <td id="inherite1'+i+'">\n' +
                    '                            </td>\n' +
                    '                    </td>\n' +
                    '                    <td class="btn btn-danger btn_remove" name="remove" id="'+i+'">\n' +
                    '                        Remove\n' +
                    '                    </td></tr>')
            }
            function fn2(){
                l++;
                $('#dynamic_field2').append('<tr id="row'+l+'"><td>\n' +
                    '                            <div class="form-group">\n' +
                    '                                <select class="form-control" id="hardskill" onchange="fun2()">\n' +
                    '                                    <option>Select</option>\n' +
                    '                                    <option>Communication Skill</option>\n' +
                    '                                    <option>TimeManagement Skill</option>\n' +
                    '                                    <option>Problem Solving Skill</option>\n' +
                    '                                    <option>Leadership Skill</option>\n' +
                    '                                    <option>Self Confidence</option>\n' +
                    '                                </select>\n' +
                    '                            </div>\n' +
                    '                            <td id="inherite2'+l+'">\n' +
                    '                            </td>\n' +
                    '                    </td>\n' +
                    '                    <td class="btn btn-danger btn_remove" name="remove" id="'+l+'">\n' +
                    '                        Remove\n' +
                    '                    </td></tr>')
            }

            $("#add").click(fn1);
            $("#add2").click(fn2);

            $(document).on('click','.btn_remove',function(){
                var button_id = $(this).attr("id");
                $("#row"+button_id+"").remove();
            })
        });
        // For subcategory(Begineer,Medium,Expert)
        function fun(){
            var array;
            var a = document.getElementById('softskill').value;
            if(a!="Select"){
                array=["Begineer","Medium","Expert"]
            }
            else{
                array=[]
            }
            var string="";
            for(j=0;j<array.length;j++){
                string=string+"<option>"+array[j]+"</option>";
            }
            string="<select name='level' class='form-control'>"+string+"</select>"
            document.getElementById("inherite1"+i+"").innerHTML=string;
        }
        function fun2(){
            var array;
            var a = document.getElementById('softskill').value;
            if(a!="Select"){
                array=["Begineer","Medium","Expert"]
            }
            else{
                array=[]
            }
            var string="";
            for(k=0;k<array.length;k++){
                string=string+"<option>"+array[k]+"</option>";
            }
            string="<select name='level' class='form-control'>"+string+"</select>"
            //console.log("inherite2"+j+"");
            document.getElementById("inherite2"+l+"").innerHTML=string;
        }