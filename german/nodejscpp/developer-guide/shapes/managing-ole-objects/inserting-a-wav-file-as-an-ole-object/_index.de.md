---
title: Einfügen einer WAV Datei als OLE Objekt mit Node.js über C++
linktitle: Einbinden einer WAV Datei als Ole Objekt
type: docs
weight: 70
url: /de/nodejs-cpp/inserting-a-wav-file-as-an-ole-object/
description: Lernen Sie, wie Sie eine WAV Datei mithilfe von Aspose.Cells for Node.js via C++ als OLE Objekt in Excel Tabellen einfügen. 
---

{{% alert color="primary" %}} 

Aspose.Cells bietet die Funktionalität, verschiedene Arten von OLE-Objekten in die Excel-Tabellen einzufügen. In den folgenden Codebeispielen sehen wir, wie man eine WAV-Datei als OLE-Objekt mit den einfachen APIs von Aspose.Cells hinzufügt. 

{{% /alert %}} 


```javascript
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Define a string variable to store the image path.
const imageUrl = path.join(dataDir, "image2.jpg");

imageData = fs.readFileSync(imageUrl);

// Get an excel file path in a variable.
const filePath = path.join(dataDir, "chord.wav");
fs.writeFileSync(filePath, Buffer.from('RIFF____WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00\x00\x04\x00\x00\x00\x04\x00\x00\x01\x00\x08\x00data____', 'binary'));

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
{{< app/cells/assistant language="nodejs-cpp" >}}
