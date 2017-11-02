var express = require('express');
var session  = require('express-session');
var path = require('path');
var favicon = require('static-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
var morgan = require('morgan');
var http = require('http');
var routes = require('./routes/index');
var users = require('./routes/users');
var fs = require('fs');
var path = require('path');
var spawn = require('child_process').spawn;
var hbs = require('hbs');
var passport = require('passport');
var flash = require('connect-flash');

var app = express();
//add
var port = process.env.PORT || 8080;


// configuration ===============================================================
// connect to our database

require('./config/passport')(passport); // pass passport for configuration


// view engine setup
hbs.registerPartials(__dirname + '/views/partials');
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'hbs'); // set up ejs for templating

// set up our express application
app.use(morgan('dev')); // log every request to the console

app.use(favicon());
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
	extended: true
}));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));	//don't comment this, it will help you find the css for hbs files
app.use('/', routes);
app.use('/users', users);

// required for passport
app.use(session({
	secret: 'vidyapathaisalwaysrunning',
	resave: true,
	saveUninitialized: true
 } )); // session secret
app.use(passport.initialize());
app.use(passport.session()); // persistent login sessions
app.use(flash()); // use connect-flash for flash messages stored in session

// routes ======================================================================
require('./app/routes.js')(app, passport); // load our routes and pass in our app and fully configured passport



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


var server = http.createServer(app);

server.listen(8080, '0.0.0.0', function(){
  console.log("Server running at http://localhost:8080");
});


module.exports = app;
