---  
title: Load a Web Image from a URL into an Excel Worksheet with Node.js via C++  
linktitle: Load a Web Image from a URL into an Excel Worksheet  
type: docs  
weight: 30  
url: /nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/  
description: How to convert an Image from URL to actual Excel image using Aspose.Cells for Node.js via C++.  
keywords: excel show image from url, excel url to image, show image in excel from url, excel insert image from url, convert url to image in excel, excel image from url, load image from url in excel, Node.js, Excel  
---  

## Load an Image from a URL into an Excel Worksheet  

Aspose.Cells for Node.js via C++ provides a simple and easy way to load images from URLs into Excel Worksheets. This article explains downloading the image data into a stream and then inserting it into the worksheet using the Aspose.Cells API. Using this method, the images become a part of the Excel file and are not downloaded every time the worksheet is opened.  

## Sample Code  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
const https = require("https");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "webimagebook.out.xlsx");
const url = "http://www.aspose.com/Images/aspose-logo.jpg";

let objImage;

https.get(url, (res) => {
    const chunks = [];

    res.on("data", (chunk) => {
        chunks.push(chunk);
    });

    res.on("end", async () => {
        objImage = Buffer.concat(chunks);
        
        // Create a new workbook
        const wb = new AsposeCells.Workbook();

        // Get the first worksheet in the book
        const sheet = wb.getWorksheets().get(0);

        // Get the first worksheet pictures collection
        const pictures = sheet.getPictures();

        // Insert the picture from the stream to B2 cell
        pictures.add(1, 1, objImage);

        // Save the excel file
        await wb.saveAsync(filePath);
    });
}).on("error", (err) => {
    console.log(err.message);
});
```  

{{% alert color="primary" %}}  
There might be cases where you always want the updated image from a URL. To achieve this, you may follow the instructions given in the [Insert a Linked Picture from Web Address](/cells/nodejs-cpp/insert-a-linked-picture-from-web-address/) article. By following this method, the image is loaded from the URL each time the worksheet is opened.  
{{% /alert %}}  

  