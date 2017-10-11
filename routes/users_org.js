var express = require('express');
var router = express.Router();
// var mongoose = require('mongoose');
//
// var userSchema = new.mongoose.Schema({
//   username: {type: String, unique: true},
//   password: {type: String},
//   email: {type: String}
// })

/* GET users listing. */
router.get('/', function(req, res) {
  res.send('respond with a resource');
});

module.exports = router;
