---
title: Inserting a WAV file as an Ole Object with Node.js via C++
linktitle: Inserting a WAV file as an Ole Object
type: docs
weight: 70
url: /nodejs-cpp/inserting-a-wav-file-as-an-ole-object/
description: Learn how to insert a WAV file as an OLE object in Excel worksheets using Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}} 

Aspose.Cells provides the functionality to add different types of OLE objects to the Excel worksheets. We will see in the following code examples, how to add a WAV file as an OLE object using simple APIs provided by Aspose.Cells. 

{{% /alert %}} 


```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Define a string variable to store the image path.
const imageUrl = path.join(dataDir, "image2.jpg");

// Get the picture into the streams.
const fs = require("fs");
const imageData = fs.readFileSync(imageUrl);

// Get an excel file path in a variable.
const filePath = path.join(dataDir, "chord.wav");

// Get the file into the streams.
const objectData = fs.readFileSync(filePath);
const intIndex = 0;

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

const sheet = workbook.getWorksheets().get(0);

// Add Ole Object
sheet.getOleObjects().add(14, 3, 200, 220, imageData);
workbook.getWorksheets().get(0).getOleObjects().get(intIndex).setFileFormatType(AsposeCells.FileFormatType.Unknown);
workbook.getWorksheets().get(0).getOleObjects().get(intIndex).setObjectData(objectData);
workbook.getWorksheets().get(0).getOleObjects().get(intIndex).setObjectSourceFullName(filePath);

// Save the excel file
workbook.save(path.join(dataDir, "testWAV.out.xlsx"));
```
