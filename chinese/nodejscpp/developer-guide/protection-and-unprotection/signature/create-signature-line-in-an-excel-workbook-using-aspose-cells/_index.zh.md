---  
title: 使用Aspose.Cells for Node.js via C++在Excel工作簿中创建签名线  
linktitle: 使用Aspose.Cells在Excel工作簿中创建签名行  
type: docs  
weight: 150  
url: /zh/nodejs-cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/  
description: 这篇文章介绍了如何使用Aspose.Cells for Node.js via C++和Node.js在Excel工作簿中创建签名线。  
keywords: 使用Node.js通过C++在Excel工作簿中创建签名线，如何创建签名线，如何添加签名线，如何在Excel文件中添加签名线  
---  

## **介绍**  

Microsoft Excel提供了在Excel工作簿中添加 **签名行** 的功能。您可以通过单击 **插入** 选项卡，然后从 **文本** 组中选择 **签名行** 来添加签名行。  

## **如何为Excel创建签名行**  

 Aspose.Cells for Node.js via C++也提供此功能，并为此暴露了[**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--)属性。本文将介绍如何使用此属性通过Aspose.Cells添加签名线。  

 以下示例代码使用[**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--)属性添加签名线，并保存工作簿。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Create signature line object
const signatureLine = new AsposeCells.SignatureLine();
signatureLine.setSigner("John Doe");
signatureLine.setTitle("Development Lead");
signatureLine.setEmail("john.doe@aspose.com");

// Adds a Signature Line to the worksheet.
workbook.getWorksheets().get(0).getShapes().addSignatureLine(1, 1, signatureLine);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
