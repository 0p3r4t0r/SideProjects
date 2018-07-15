/*eslint-env browser*/

/*
//Basic code to show an image
var myImage = new Image(250);
myImage.src = "img/hamster.jpg";
document.body.appendChild(myImage);
*/
        
//Create an object containing all the lost object data as attributes (testing purpose)
var image = {
    name: "hamster",
    colour1: "brown",
    colour2: "white",
    src: "img/hamster.jpg"
};
        
var not_found = new Image(250, 200);
not_found.src = "img/green_blob.png";




        
//Function that takes an attribute value and returns the corresponding image if a match exists, and "not found" otherwise.
//Note: at the moment only checks name and colours. Time and place checks need to be added.
function search_name(name, colour1, colour2) {
	"use strict";
    //test name attribute
//	if (name === image.name || name === "") {
//			//check if colour1 matches
//		if (colour1 === image.colour1 || colour1 === image.colour2 || colour1 === "") {
//			return image;
//		} else {
//			return not_found;
//		}
//	} else {
//		return not_found;
//	}
	//Check name. If not matching, exit. If matching or empty, proceed.
	if (name !== image.name && name !== "") {
		return not_found;
	} else {
		//Check colour1. If not matching, exit. If matching or empty, proceed.
		if (colour1 !== image.colour1 && colour1 !== image.colour2 && colour1 !== "") {
			return not_found;
		} else {
			//Check colour2. If not matching, exit. If matching or empty, proceed.
			if (colour2 !== image.colour1 && colour2 !== image.colour2 && colour2 !== "") {
				return not_found;
			} else {
				return image;
			}
		}
	}
}
        
//Print image at the end of body
//test call
var result1 = new Image(250);
result1.src = search_name("hamster", "brown", "").src;
document.body.appendChild(result1);
//alternative tests        
var result2 = new Image(250);
result2.src = search_name("wallet", "", "").src;
document.body.appendChild(result2);






//sets max date lost to today
var today = new Date().toISOString().slice(0, 10);
document.getElementById("datePicker_lost").setAttribute("max", today);

