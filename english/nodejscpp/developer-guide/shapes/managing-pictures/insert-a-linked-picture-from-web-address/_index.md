---  
title: Insert a Linked Picture from Web Address with Node.js via C++  
linktitle: Insert a Linked Picture from Web Address  
type: docs  
weight: 450  
url: /nodejs-cpp/insert-a-linked-picture-from-web-address/  
description: Learn how to insert a linked picture from a web address into a worksheet using Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"  
---  

{{% alert color="primary" %}}  
Sometimes you need to insert a picture from the web (http://) into a worksheet. To do so, specify the picture’s URL and the picture will be downloaded every time the spreadsheet is opened in Excel. The image is not physically embedded into the Excel document, but points to a web resource.  
{{% /alert %}}  

## **Using Microsoft Excel**  

In Microsoft Excel (for example, 2007):  

1. Click the **Insert** menu and select **Picture**.  
2. Specify the web address for the picture in the Insert Picture dialog.  

## **Using Aspose.Cells for Node.js via C++**  

Aspose.Cells for Node.js via C++ supports adding a linked image using the [**ShapeCollection.addLinkedPicture(upperLeftRow, upperLeftColumn, heightPixels, widthPixels, sourceFullName)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLinkedPicture-number-number-number-number-string-). The method returns a [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture) object.  

The following example shows how to add a linked picture from a web address to a worksheet.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();
// Insert a linked picture (from Web Address) to B2 cell.
const pic = workbook.getWorksheets().get(0).getShapes().addLinkedPicture(1, 1, 100, 100, "http://www.aspose.com/Images/aspose-logo.jpg");
// Set the height and width of the inserted image.
pic.setHeightInch(1.04);
pic.setWidthInch(2.6);
// Save the Excel file.
workbook.save(path.join(dataDir, "outLinkedPicture.out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
