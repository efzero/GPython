function save_json(data){
    var json = JSON.stringify(data);
    blob = new Blob([json], {type: "octet/stream"});
    saveAs(new Blob([json], {type: "octet/stream"}), "graph.json")

}

function save_svg(){
    $(".marker-arrowhead").css("display", "none");
    $(".tool-remove").css("display", "none");
    $(".tool-options").css("display", "none");
    $(".marker-vertices").css("display", "none");
    $(".link-tools").css("display", "none");
    $(".connection-wrap").css("fill", "none");
    $(".connection").css("fill", "none");
    var svgDoc = paper.svg;
    var serializer=  new XMLSerializer();
    var svgString = serializer.serializeToString(svgDoc);
    saveAs(new Blob([svgString], {type:"application/svg+xml"}), "graph.svg") ;
    $(".tool-remove").show()
    $(".tool-options").show();
    $(".link-tools").show();
    console.log('done');

}

function save_png(){
    $(".marker-arrowhead").css("display", "none");
    $(".tool-remove").css("display", "none");
    $(".tool-options").css("display", "none");
    $(".marker-vertices").css("display", "none");
    $(".link-tools").css("display", "none");
    $(".connection-wrap").css("fill", "none");
    $(".connection").css("fill", "none")

    // var data = { x: 42, s: "hello, world", d: new Date() },
    // fileName = prompt("please enter the file name you want to save as");
    // // saveData(data, fileName);
    // var a = document.createElement("a");
    // a.style = "display: none";

    var svgDoc = paper.svg;
    var serializer=  new XMLSerializer();
    var svgString = serializer.serializeToString(svgDoc);
    console.log(svgString);
    // saveAs(new Blob([svgString], {type:"application/svg+xml"}), "graph.svg") ;
    encodedData = window.btoa(unescape(encodeURIComponent(svgString)));
    // encodedData = svgString;
    var canvas = document.getElementById('canvas');
    var ctx = canvas.getContext('2d');
    console.log(ctx);
    ctx.drawSvg('data:image/svg+xml;base64,' + encodedData, 0, 0);
    canvas.toBlob(function(blob) {
        saveAs(blob, "MyCanvas.png");
    });

    $(".tool-remove").show()
    $(".tool-options").show();
    $(".link-tools").show();
    console.log('done');

    // var json = JSON.stringify(data),
    // blob = new Blob([json], {type: "octet/stream"}),
    // url = window.URL.createObjectURL(blob);
    // console.log(url);
    // a.href = url;
    // a.download = fileName;
    // a.click();
    // window.URL.revokeObjectURL(url);

}



function createCustomCell(ev){
    cell_name_ = cell_name.enter_name.value;
    console.log(cell_name.enter_name.value);
    pos = $('.nametag').position()
    left_pos = pos.left;
    top_pos = pos.top;
    $(".nametag").hide();

    var state = document.getElementById('display_option').value;
    var color = $('#cell_color')[0].value;
    console.log(color);

    console.log(state);
    if (state == 'circle'){
        var cell = RFcell(cell_name_, left_pos, top_pos - 410, color);
        graph.addCell(cell);
    }
    else if (state == 'rectangle'){
        var cell  = RCcell(cell_name_, left_pos, top_pos - 410, color);
        graph.addCell(cell);
    }

    else if (state == 'c_d_link'){
        var link = create_ano_Link(left_pos, top_pos - 410, color);
        graph.addCell(link);
        console.log('yes')
    }

    else if (state == 'link'){
        var link = create_ano_st_Link(left_pos, top_pos - 410, color);
        graph.addCell(link);
    }

    else if (state == 'w_c_d_link'){
        var link = createLink(left_pos, top_pos - 410, cell_name_, color);
        graph.addCell(link);
    }

    else if (state == 'w_d_link'){
        var link = create_st_Link(left_pos, top_pos -410, cell_name_, color);
        graph.addCell(link);
    }

    else if (state == 'line'){
        var link = create_Line(left_pos, top_pos -410, false, cell_name_, color);
        graph.addCell(link);
    }

    else if (state == 'c_line'){
        var link = create_Line(left_pos, top_pos -410, true, cell_name_, color);
        graph.addCell(link);
    }

    else if (state == 'w_line'){
        var link = create_Line(left_pos, top_pos -410, false, cell_name_, color);
        graph.addCell(link);
    }

    else if (state == 'w_c_line'){
        var link = create_Line(left_pos, top_pos -410, true, cell_name_, color);
        graph.addCell(link);
    }


}

function create_Line(x, y, smooth, name, color){
    var link = new joint.dia.Link({
        attrs: {},
        labels: [{position: .5, attrs: {
            text: {text: name, 'font-size': 17}
          }}],
        smooth: smooth,
        source: {x: x, y:y},
        target: {x: x + 200, y:y},
        vertices: []             
      });
    //   link.prop('attrs/text/text', name);
      console.log(link);
      return link;
}





function create_ano_Link(x, y, color){

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

function createLink(x, y, name, color){

    var link = new joint.dia.Link({
      attrs: {
         '.marker-target': { d: 'M 10 0 L 0 5 L 10 10 z' }},
      labels: [{position: .5, attrs: {
        text: {text: name, 'font-size': 17}
      }}],
      smooth: true,
      source: {x: x, y:y},
      target: {x: x + 200, y:y},
      vertices: []                
    });
    console.log(link);
    return link;
  }

  function create_ano_st_Link(x, y, color){

    var link = new joint.dia.Link({
      attrs: {
         '.marker-target': { d: 'M 10 0 L 0 5 L 10 10 z' }},
      source: {x: x, y:y},
      target: {x: x + 200, y:y},
      vertices: []             
      
    });
    console.log(link);
    return link;
  }

  function create_st_Link(x,y, name, color){
    var link = new joint.dia.Link({
        attrs: {
           '.marker-target': { d: 'M 10 0 L 0 5 L 10 10 z' }},
        labels: [{position: .5, attrs: {
          text: {text: name, 'font-size': 17}
        }}],
        source: {x: x, y:y},
        target: {x: x + 200, y:y},
        vertices: []                
      });
      console.log(link);
      return link;

  }


function RFcell(name, x, y, color){
    var circle = new joint.shapes.basic.Circle({})
    circle.position(x, y);
    circle.attr({
      circle: {fill: color, 'magnet': 'passive'},
      text: {fill: 'black', text: name, 'font-size': 17}
    });
    circle.size({width: 100, height: 100});
    return circle;
  }
1

  function RCcell(name, x, y, color){
    var rect = new joint.shapes.basic.Rect({});
    rect.position(x,y);
    rect.attr({
      rect: {fill : color, 'magnet': 'passive'},
      text: {fill: 'black', text: name, 'font-size': 17}

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
    console.log(buttons);
    
    var state = option.value;
    if (state == ev.value){
        option.value = 'NaN';
        ev.style.filter = 'brightness(1.0)';
        ev.style.backgroundColor = 'transparent';
        console.log(ev.style);
    }
    else{
        option.value = ev.value;
        console.log(ev.style);
        buttons.forEach(element => {
            element.style.filter = 'brightness(1.0)';
            // element.style.backgroundColor = 'none';
        });
        ev.style.filter = 'brightness(0.75)';
        ev.style.backgroundColor = 'white';
    }
}



function growTree(x, y, node, dist, color, maxlayers){
    if (dist > maxlayers){
        return
    }
    var rf_left = RFcell('', x + 300*1/dist, y + 200, color)
    var rf_right = RFcell('', x - 300*1/dist, y + 200, color)
    graph.addCell(rf_left);
    graph.addCell(rf_right);

    var link_left = create_st_Link(x, y, '', color)
    var link_right = create_st_Link(x,y, '', color)

    link_left.prop('source/id', node.id);
    link_left.prop('target/id', rf_left.id);
    link_right.prop('source/id', node.id);
    link_right.prop('target/id', rf_right.id);
    graph.addCell(link_left);
    graph.addCell(link_right);
    setTimeout(function(){growTree(x + 300*1/dist, y + 200, rf_left, dist + 1, color, maxlayers);}, 500);
    setTimeout(function(){growTree(x - 300*1/dist, y + 200, rf_right, dist + 1, color, maxlayers);}, 750);

}


function grow(){
    layers = parseInt(prompt('enter the number of layers'))
    if (isNaN(layers)){
        alert('input must be an integer');
        return;
    }
    if (layers > 6 || layers < 0){
        alert('illegal numbers of layers');
        return;
    }
    x = 700, y = 50;
    color =  $('#cell_color')[0].value;
    node = RFcell('', x,y, color);
    graph.addCell(node);
    growTree(x , y, node, 1, color, layers)
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

