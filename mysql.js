var mysql = require('mysql');

var con = mysql.createConnection({
    host: "localhost",
    user: "owncloud",
    password: "testcloud"
});

con.connect(function(err) {
    if (err) throw err;
    console.log("Connected!");
    con.query("CREATE DATABASE owncloud", function (err, results) {
        if(err) throw err;
        console.log("Database created")
    })
});
