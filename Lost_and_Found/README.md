Lost and Found
==============

## 2018/07/15
### Done:
- Added "Found Items" page stub and navigation links between the two pages.
- More search options, as discussed. I think that colours and locations are better choosen from a limited list to avoid confusion and improve searchability.
- The lost date has maximum = today. It works only in one page, though. To be fixed later.
- I used javascript to create a rudimentary search function. There is probably a cleaner way to write it, but it works!  
At the moment it tests only attributes: "name", "colour1" and "colour2". 
- The search function refers to a pool of two objects defined in the .js file. The data for each lost object is stored as the attributes of a (Javascript) object. For example:
```javascript
var image = {
    name: "hamster", 
    colour1: "brown",
    colour2: "white",
    src: "img/hamster.jpg"
};
```

### To do:
- Add warning about request of proof of ownership
- Complete search function to include all attribute
- Make "Advanced options" collapsible
- Improve general layout and looks
- Find a way to emulate a server database to store form data and to retrieve it
- Deal with the case of multiple hits in the search results
