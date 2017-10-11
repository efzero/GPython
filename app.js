var express = require('express');
var path = require('path');
var favicon = require('static-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
var http = require('http');
var routes_main = require('./routes/index');
// var users = require('./routes/users');
var fs = require('fs');
var path = require('path');
var spawn = require('child_process').spawn;

//mean auth
var expressSession = require('express-session');
var mongoose = require('mongoose');
var hash = require('bcrypt-nodejs');
var passport = require('passport');
var localStrategy = require('passport-local' ).Strategy;

// mongoose
mongoose.connect('mongodb://localhost/mean-auth');

// user schema/model
var User = require('./routes/users');

// create instance of express
var app = express();

// require routes
var routes = require('./routes/api');

// define middleware
app.use(express.static(path.join(__dirname, '/client')));

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(favicon());
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(require('express-session')({
    secret: 'keyboard cat',
    resave: false,
    saveUninitialized: false
}));
app.use(passport.initialize());
app.use(passport.session());
app.use(express.static(path.join(__dirname, 'public')));
//try delete

app.use('/', routes_main );
app.use('/users', User);


// configure passport
passport.use(new localStrategy(User.authenticate()));
passport.serializeUser(User.serializeUser());
passport.deserializeUser(User.deserializeUser());
// app.use(multer({ dest: '/tmp/'}));

// app.post('/regression', function(req, res){
//   console.log("doing regression");
//   runpython('/compute_input.py', req, res);
// })
//

// routes
app.use('/user/', routes);

app.get('/', function(req, res) {
  res.sendfile(path.join(__dirname, './client', 'index.html'));
});



/// catch 404 and forwarding to error handler
app.use(function(req, res, next) {
    var err = new Error('Not Found');
    err.status = 404;
    next(err);
});


/// error handlers

// development error handler
// will print stacktrace
if (app.get('env') === 'development') {
    app.use(function(err, req, res, next) {
        res.status(err.status || 500);
        res.render('error', {
            message: err.message,
            error: err
        });
    });
}

// production error handler
// no stacktraces leaked to user
app.use(function(err, req, res, next) {
    res.status(err.status || 500);
    res.render('error', {
        message: err.message,
        error: {}
    });
});



// var debug = require('debug')('passport-mongo');
// app.set('port', process.env.PORT || 3000);
//
// var server = app.listen(app.get('port'), function() {
//   debug('Express server listening on port ' + server.address().port);
// });


var server = http.createServer(app);

server.listen(9090, '0.0.0.0', function(){
  console.log("Server running at http://localhost:9090");
});


module.exports = app;
