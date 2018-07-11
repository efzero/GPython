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


function createCustomCell(ev){
    cell_name_ = cell_name.enter_name.value;
    console.log(cell_name.enter_name.value);
    pos = $('.nametag').position()
    left_pos = pos.left;
    top_pos = pos.top;
    $(".nametag").hide();

    var state = document.getElementById('display_option').value;

    console.log(state);
    if (state == 'circle'){
        var cell = RFcell(cell_name_, left_pos, top_pos - 350);
        graph.addCell(cell);
    }
    else if (state == 'rectangle'){
        var cell  = RCcell(cell_name_, left_pos, top_pos - 350);
        graph.addCell(cell);
    }

    else if (state == 'dlink'){
        var link = createLink(left_pos, top_pos - 350, cell_name_);
        graph.addCell(link);
        console.log('yes')
    }

    else if (state == 'link'){
        var link = create_ano_Link(left_pos, top_pos - 350);
        graph.addCell(link);
    }


}
function create_ano_Link(x, y){

    var link = new joint.dia.Link({
      attrs: {
         '.marker-target': { d: 'M 10 0 L 0 5 L 10 10 z' }},
      smooth: true,
      source: {x: x, y:y},
      target: {x: x + 200, y:y},
      vertices: []             
    });
    console.log(link);
    return link;
  }

function createLink(x, y, name){

    var link = new joint.dia.Link({
      attrs: {
         '.marker-target': { d: 'M 10 0 L 0 5 L 10 10 z' }},
      labels: [{position: .5, attrs: {
        text: {text: name}
      }}],
      smooth: true,
      source: {x: x, y:y},
      target: {x: x + 200, y:y},
      vertices: []                
    });
    console.log(link);
    return link;
  }


function RFcell(name, x, y){
    var circle = new joint.shapes.basic.Circle({})
    circle.position(x, y);
    circle.attr({
      circle: {fill: 'white', 'magnet': true},
      text: {fill: 'black', text:name}
    });
    circle.size({width: 100, height: 100});
    return circle;
  }

  function RCcell(name, x, y){
    var rect = new joint.shapes.basic.Rect({});
    rect.position(x,y);
    rect.attr({
      rect: {fill : 'white', 'magnet': true},
      text: {fill: 'black', text: name}

    });
    rect.size({width: 100, height: 100})
    return rect;
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

function dragElement(elmnt) {
    var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
    if (document.getElementById(elmnt.id + "header")) {
      /* if present, the header is where you move the DIV from:*/
      document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown;
    } else {
      /* otherwise, move the DIV from anywhere inside the DIV:*/
      elmnt.onmousedown = dragMouseDown;
    }

function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    // get the mouse cursor position at startup:
    pos3 = e.clientX;
    pos4 = e.clientY;
    document.onmouseup = closeDragElement;
    // call a function whenever the cursor moves:
    document.onmousemove = elementDrag;
}

function elementDrag(e) {
    e = e || window.event;
    e.preventDefault();
    // calculate the new cursor position:
    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY;
    // set the element's new position:
    elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
    elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
}

function closeDragElement() {
    /* stop moving when mouse button is released:*/
    document.onmouseup = null;
    document.onmousemove = null;
}
}


function editor(){
    edit = document.getElementById('edit');
    editor_ = document.getElementById('editor')
    if (edit.value == 'show the graph editor'){
        edit.value = 'hide the graph editor';
        editor_.style.display =  'inline'

    }
    else{
        edit.value = 'show the graph editor';
        editor_.style.display =  'none';
    }
}


function change_state(ev){
    option = document.getElementById('display_option');
    buttons = []
    i = 1
    while (true){
        id = 'close_image' + i.toString();
        button = document.getElementById(id);
        if (button != undefined){
            buttons.push(button);
            i ++;
        }
        else{
            break;
        }
    }
    
    var state = option.value;
    if (state == ev.value){
        option.value = 'NaN';
        ev.style.filter = 'brightness(1.0)';
        console.log(ev.style);
    }
    else{
        option.value = ev.value;
        console.log(ev.style);
        buttons.forEach(element => {
            element.style.filter = 'brightness(1.0)';
        });
        ev.style.filter = 'brightness(0.75)';
    }
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

