const express = require('express');
const router = express.Router();
const fs = require('fs');
const path = require('path');
const spawn = require('child_process').spawn;
const url = require('url')
const fileUpload = require('express-fileupload');
const multer = require('multer');
const formidable = require('formidable');
router.use(fileUpload());



/* GET home page. */
router.get('/loha', function(req, res) {
  res.render('index2', { dropstyle: 'display:none;' });
});
//
// router.get('/run', function(req, res){
//   res.sendfile('index.html');
// });

var runregression = function(name, req, res){
  var thepath;
  let path_ = url.parse(req.url).pathname;
  path_ = path_.substring(1);
  thepath = path.resolve('./public/'+name);
  console.log(thepath);
  let dataString = '';
  var py = spawn('python3',['-u', thepath]);
  py.stdout.on('data', function(data){
        dataString += data.toString();
        console.log("has red");
        console.log(dataString);
  });

  py.stdout.on('close', function(){
        res.render('index', {result:dataString, title: path_, path1:'/images/catterRegression_0.png', path2: '/images/catterRegression_1.png', path3: '/images/catterRegression_0.png'});
        console.log('end');
  });
}



router.post('/regression', function(req, res){
  console.log("doing regression");
  runregression('compute_input.py', req, res);
})

router.post('/qiangke', function(req, res){
  console.log("qiangke");
  runregression('qiangke.py', req, res);
})

router.post('/plot', function(req, res){
  runregression('wanttoplot.py', req, res);
})

router.post('/index', function(req, res){
  function savePersonToPublicFolder(person, callback) {
  fs.writeFile('./public/person.json', JSON.stringify(person), callback);
}
  // console.log(req.body);
  var j = req.body['JSON file'];
  var thepath;
  let path_ = url.parse(req.url).pathname;
  path_ = path_.substring(1);
  thepath = path.resolve('./public/'+'flowAssistant.py');
  // console.log(thepath);
  let dataString = '';
  var py = spawn('python3',['-u', thepath]);
  py.stdin.write(j);
  py.stdin.end();
  py.stdout.on('data', function(data){
    dataString += data.toString();
  })
  py.stdout.on('end', function(){

    console.log(dataString);
    // res.end(j);
    if (dataString != ''){
      console.log(__dirname);
      fs.writeFile('./public/test.json', j);
      res.render('index2',{output:dataString,path3:'/images/corrHeatmap.png' });
    }
    else{
      console.log(__dirname);
      fs.writeFile('./public/test.json', j);
      res.render('index2', {output: 'NOTHING!'});
    }
  })

})


router.post('/shishi', function(req, res){
  let r = req.body['haha'];
  // fs.writeFile('./test.json', r);
  console.log(r);
  let thepath = path.resolve('./public/'+'flow.py');
  console.log(thepath);
  let dataString = '';
  var py = spawn('python3',['-u',thepath]);
  // py.stdin.write(r);
  // py.stdin.end();
  py.stdin.write(r);
  py.stdin.end();
  py.stdout.on('data',function(data){
    console.log('python running');
    dataString += data.toString();
  })
  py.stdout.on('end', function(){
    console.log(dataString);
    if (dataString != ''){
      res.send(dataString);
    }
    else{
      res.send('NOTHING,');
    }
  })

})


router.post('/file_upload', function(req, res){
  console.log(__dirname);

  console.log(req.files.foo);
  let sampleFile = req.files.foo;
  let uploadDir = '/home/bowen/GPython/mydata.csv';
  sampleFile.mv(uploadDir,function(err){
    if (err)
      return res.status(500).send(err);
  })
  console.log(req.files.foo.mimetype);
  console.log(req.files.foo.path);
  res.render('index2', {message: "File has been uploaded! You can view the names variables by clicking the 'summary button'"});
  // fs.writeFile('hello.csv')
});



router.post('/show_summary', function(req, res){
  thepath = '/home/bowen/GPython/public/show_summary.py';
  let dataString = '';
  var py = spawn('python3',['-u', thepath]);

  py.stdout.on('data', function(data){
        dataString += data.toString();
        console.log("has red");
        console.log(dataString);
  });
  py.stdout.on('end', function(data){
      res.send(dataString);
  });

});

router.post('/sharp', function(req,res){
  console.log(req.body['bar']);
  res.render('index2', {datainfo: req.body['bar']});
});



module.exports = router;
