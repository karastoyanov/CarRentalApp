const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
  e.preventDefault();
  let mysql = require('mysql');
  let RDS_HOSTNAME = "carrentalapp-db.cvwquqtl5fz5.eu-central-1.rds.amazonaws.com";
  // let RDS_USERNAME = "admin";
  let RDS_USERNAME = loginForm.username.value;
  let RDS_PASSWORD = loginForm.password.value;
  let RDS_PORT = "3306";


  let connection = mysql.createConnection({

    host     : RDS_HOSTNAME,
    user     : RDS_USERNAME,
    password : RDS_PASSWORD,
    port     : RDS_PORT
  });

  connection.connect(function(err) {
    if (err) {
      // console.error('Database connection failed: ' + err.stack);
      loginErrorMsg.style.opacity = 1;
      // return;
    }
    alert("You have successfully logged in.");
    location.reload();
    console.log('Connected to database.');
  });

  // connection.end();
})