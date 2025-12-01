---  
title: Managing OLE Objects with Node.js via C++  
linktitle: Managing OLE Objects  
type: docs  
weight: 50  
url: /nodejs-cpp/managing-ole-objects/  
description: Learn how to manage OLE objects in Aspose.Cells for Node.js via C++. Add, extract, and manipulate OLE objects within worksheets.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Introduction**  

OLE (Object Linking and Embedding) is a framework for compound document technology. Briefly, a compound document is something like a display desktop that can contain visual and information objects of all kinds: text, calendars, animations, sound, motion video, 3D, continually updated news, controls, and so forth. Each desktop object is an independent program entity that can interact with a user and also communicate with other objects on the desktop.  

OLE is supported by many different programs and is used to make content created in one program available in another. For example, you can insert a Microsoft Word document into Microsoft Excel. To see what types of content you can insert, click **Object** on the **Insert** menu. Only programs that are installed on the computer and that support OLE objects appear in the **Object type** box.  

### **Inserting OLE Objects into the Worksheet**  

Aspose.Cells for Node.js via C++ supports adding, extracting, and manipulating OLE objects in worksheets. For this reason, Aspose.Cells has the [**OleObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/oleobjectcollection) class, used to add a new OLE Object to the collection. Another class, [**OleObject**](https://reference.aspose.com/cells/nodejs-cpp/oleobject), represents an OLE Object. It has some important members:  

- The [**getImageData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getImageData--) property specifies the image (icon) data of byte array type. The image will be displayed to show the OLE Object in the worksheet.  
- The [**getObjectData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getObjectData--) property specifies the object data in the form of a byte array. This data will be shown in its related program when you double-click on the OLE Object icon.  

The following example shows how to add an OLE Object(s) into a worksheet.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define a string variable to store the image path.
const imageUrl = path.join(dataDir, "logo.jpg");

// Get the picture into the streams.
const imageData = fs.readFileSync(imageUrl);

// Get an excel file path in a variable.
const filePath = path.join(dataDir, "book1.xls");

// Get the file into the streams.
const objectData = fs.readFileSync(filePath);

// Add an Ole object into the worksheet with the image
// Shown in MS Excel.
sheet.getOleObjects().add(14, 3, 200, 220, imageData);

// Set embedded ole object data.
sheet.getOleObjects().get(0).setObjectData(objectData);

// Save the excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

### **Extracting OLE Objects in the Workbook**  

The following example shows how to extract OLE Objects in a Workbook. The example gets different OLE objects from an existing XLS file and saves different files (DOC, XLS, PPT, PDF, etc.) based on the OLE object’s file format type.  

After running the code, we can save different files based on their respective OLE Objects format types.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Get the OleObject Collection in the first worksheet.
const oles = workbook.getWorksheets().get(0).getOleObjects();

// Loop through all the oleobjects and extract each object.
for (let i = 0; i < oles.getCount(); i++) {
const ole = oles.get(i);

// Specify the output filename.
let fileName = path.join(dataDir, `ole_${i}.`);

// Specify each file format based on the oleobject format type.
switch (ole.getFileFormatType()) {
case AsposeCells.FileFormatType.Doc:
fileName += "doc";
break;
case AsposeCells.FileFormatType.Xlsx:
fileName += "xlsx";
break;
case AsposeCells.FileFormatType.Ppt:
fileName += "ppt";
break;
case AsposeCells.FileFormatType.Pdf:
fileName += "pdf";
break;
case AsposeCells.FileFormatType.Unknown:
fileName += "jpg";
break;
default:
//........
break;
}

// Save the oleobject as a new excel file if the object type is xls.
if (ole.getFileFormatType() === AsposeCells.FileFormatType.Xlsx) {
const ms = new Uint8Array(ole.getObjectData());
const oleBook = new AsposeCells.Workbook(ms);
oleBook.getSettings().setIsHidden(false);
oleBook.save(path.join(dataDir, `Excel_File${i}.out.xlsx`));
}

// Create the files based on the oleobject format types.
else {
fs.writeFileSync(fileName, ole.getObjectData());
}
}
```  

### **Extracting Embedded MOL File**  

Aspose.Cells for Node.js via C++ supports extracting objects of uncommon types like MOL (Molecular data file containing information about atoms and bonds). The following code snippet demonstrates extracting an embedded MOL file and saving it to disk by using this [sample excel file](94896196.xlsx).  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// Directories
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "EmbeddedMolSample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
let index = 1;

const worksheets = workbook.getWorksheets();
const sheetCount = worksheets.getCount();
for (let i = 0; i < sheetCount; i++) {
const sheet = worksheets.get(i);
const oles = sheet.getOleObjects();
const oleCount = oles.getCount();
for (let j = 0; j < oleCount; j++) {
const ole = oles.get(j);
const fileName = path.join(outputDir, `OleObject${index}.mol`);
const fileStream = fs.createWriteStream(fileName);
fileStream.write(Buffer.from(ole.getObjectData()));
fileStream.end();
index++;
}
}
```  

## **Advance topics**  
- [Access and Modify the Display Label of the Linked Ole Object](/cells/nodejs-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)  
- [Automatically refresh OLE object via Microsoft Excel using Aspose.Cells](/cells/nodejs-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)  
- [Extract OLE Objects from Workbook](/cells/nodejs-cpp/extract-ole-objects-from-workbook/)  
- [Get or Set the Class Identifier of the Embedded OLE Object](/cells/nodejs-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)  
- [Inserting a WAV file as an Ole Object](/cells/nodejs-cpp/inserting-a-wav-file-as-an-ole-object/)  

  
{{< app/cells/assistant language="nodejs-cpp" >}}
