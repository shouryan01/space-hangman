function cipherRot10(str) {
    var output = "";
    for (var i = 0; i < str.length; i++) {
        var charCode = str.charCodeAt(i);
        output = output + String.fromCharCode(charCode - 10);
    }
    return output
}
  

// test the function above
console.log(cipherRot10("Hello World!"));