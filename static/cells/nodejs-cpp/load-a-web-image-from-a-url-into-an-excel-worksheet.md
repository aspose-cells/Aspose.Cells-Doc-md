##Load a Web Image from a URL into an Excel Worksheet with Node.js via C++
How to convert an Image from URL to actual Excel image using Aspose.Cells for Node.js via C++.
## Load an Image from a URL into an Excel Worksheet
Aspose.Cells for Node.js via C++ provides a simple and easy way to load images from URLs into Excel Worksheets. This article explains downloading the image data into a stream and then inserting it into the worksheet using the Aspose.Cells API. Using this method, the images become a part of the Excel file and are not downloaded every time the worksheet is opened.
## Sample Code
```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");
const https = require("https");
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "webimagebook.out.xlsx");
const url = "https://www.aspose.com/Images/aspose-logo.jpg"; // Changed http to https
let objImage;
https.get(url, (res) => {
const chunks = [];
res.on("data", (chunk) => {
chunks.push(chunk);
```
There might be cases where you always want the updated image from a URL. To achieve this, you may follow the instructions given in the [Insert a Linked Picture from Web Address](https://docs.aspose.com/cells/nodejs-cpp/insert-a-linked-picture-from-web-address/) article. By following this method, the image is loaded from the URL each time the worksheet is opened.
