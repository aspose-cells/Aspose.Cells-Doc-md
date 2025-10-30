---
title: Node.js ve C++ kullanarak WAV dosyasını OLE Nesnesi olarak Ekleme
linktitle: Ole Nesnesi Olarak Bir WAV Dosyası Eklemek
type: docs
weight: 70
url: /tr/nodejs-cpp/inserting-a-wav-file-as-an-ole-object/
description: Aspose.Cells for Node.js via C++ kullanarak Excel çalışma sayfalarına WAV dosyasını OLE nesnesi olarak nasıl ekleyeceğinizi öğrenin. 
---

{{% alert color="primary" %}} 

Node.js ve C++ kullanarak Hücre Metni ile Koşullu Simgeler Kümesi Ekleme 

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
