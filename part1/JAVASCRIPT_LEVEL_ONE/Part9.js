var fname=prompt("Enter first name");
var lname=prompt("Enter last name")
var age=prompt("enter age")
var height=prompt("Enter height")
var pname=prompt("Enter Pet Name")
alert("thank you so much for the information")


var nameCond=null;
var ageCond=null;
var heightCond=null;
var petCond=null;


//NAME CONDITION
if (fname[0]===lname[0]) {
  nameCond=true;
}else {
  nameCond=false;
}

//AGE CONDITION
if (age>20 && age<30) {
  ageCond=true;
}else {
  ageCond=false;
}

//HEIGHT CONDITION
if (height>=170) {
  heightCond=true;
}else {
  heightCond=false;
}

//PET Name
if (pname[pname.length-1]==="y") {
  petCond=true;
}else {
  petCond=false;
}

//CHECK ALL CONDITIONS
if (nameCond && ageCond && heightCond && petCond) {
  console.log("WELCOME SPY");
}else {
  console.log("Nothing to see here");
}
