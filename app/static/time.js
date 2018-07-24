/*eslint-env browser*/

//sets max date lost to today
var today = new Date().toISOString().slice(0, 10);
document.getElementById("datePicker_lost").setAttribute("max", today);

