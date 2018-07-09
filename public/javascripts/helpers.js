// import { format } from "util";

function save_graph(data){
    // var data = { x: 42, s: "hello, world", d: new Date() },
    fileName = prompt("please enter the file name you want to save as");
    // saveData(data, fileName);
    var a = document.createElement("a");
    a.style = "display: none";
    var json = JSON.stringify(data),
    blob = new Blob([json], {type: "octet/stream"}),
    url = window.URL.createObjectURL(blob);
    console.log(url);
    a.href = url;
    a.download = fileName;
    a.click();
    window.URL.revokeObjectURL(url);

}


function upload(){
    console.log(graph);
    var files = $('#uploadjson')[0].files;
    var fr = new FileReader();
    fr.onload = function(e) { 

          try  {
                console.log(e);
                var result = JSON.parse(e.target.result);
                var formatted = JSON.stringify(result, null, 2);
                console.log(formatted);
                graph.fromJSON(result);
          }
          catch(err){
              alert(err.message);
          }
            //   document.getElementById('result').value = formatted;
        }
    fr.readAsText(files.item(0));
      
}


// var saveData = (function () {
//     var a = document.createElement("a");
//     document.body.appendChild(a);
//     a.style = "display: none";
//     return function (data, fileName) {
        // var json = JSON.stringify(data),
        //     blob = new Blob([json], {type: "octet/stream"}),
        //     url = window.URL.createObjectURL(blob);
//         a.href = url;
//         a.download = fileName;
//         a.click();
//         window.URL.revokeObjectURL(url);
//     };
// }());

// var data = { x: 42, s: "hello, world", d: new Date() },
//     fileName = "my-download.json";

// saveData(data, fileName);

