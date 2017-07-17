var express = require('express');
var router = express.Router();
var fs = require('fs');
var path = require('path');
var spawn = require('child_process').spawn;
var url = require('url')

/* GET home page. */
// router.get('/', function(req, res) {
//   res.render('index', { title: 'Express' });
// });
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



module.exports = router;
