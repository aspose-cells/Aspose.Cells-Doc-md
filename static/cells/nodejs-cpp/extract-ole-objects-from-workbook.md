##Extract OLE Objects from Workbook with Node.js via C++
Sometimes, you do need to extract OLE objects from a workbook. Aspose.Cells supports extracting and saving those OLE objects.
This article shows how to create a console application in Node.js via C++ and extract different OLE objects from a workbook with a few simple lines of code.
## **Extract OLE Objects from a Workbook**
### **Creating a Template Workbook**
1. Create a workbook in Microsoft Excel.
1. Add a Microsoft Word document, an Excel workbook, and a PDF document as OLE objects on the first worksheet.
|**Template document with OLE objects (OleFile.xls)**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|
Next, extract the OLE objects and save them to the hard disk with their respective file types.
### **Download and Install Aspose.Cells**
1. [Download Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp).
1. Install it on your development computer.
All Aspose components, when installed, work in evaluation mode. The evaluation mode has no time limit and it only injects watermarks into produced documents.
### **Create a Project**
Start **Node.js** and create a new console application. This example will show a Node.js console application, but you can use any JavaScript-compatible environment as well.
1. Add Dependencies
1. Add a reference to Aspose.Cells component to your project, for example, include the package using `require` function:
```javascript
const { Cells } = require("aspose.cells");
```
### **Extract OLE Objects**
The code below does the actual work of finding and extracting OLE objects. The OLE objects (DOC, XLS, and PDF files) are saved to disk.
```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "oleFile.xlsx"));
// Get the OleObject Collection in the first worksheet.
const oles = workbook.getWorksheets().get(0).getOleObjects();
// Loop through all the oleobjects and extract each object in the worksheet.
for (let i = 0; i < oles.getCount(); i++) {
const ole = oles.get(i);
// Specify the output filename.
let fileName = path.join(dataDir, "outOle" + i + ".");
// Specify each file format based on the oleobject format type.
switch (ole.getFileFormatType()) {
case AsposeCells.FileFormatType.Doc:
fileName += "doc";
break;
case AsposeCells.FileFormatType.Excel97To2003:
fileName += "Xlsx";
break;
case AsposeCells.FileFormatType.Ppt:
fileName += "Ppt";
break;
case AsposeCells.FileFormatType.Pdf:
fileName += "Pdf";
break;
case AsposeCells.FileFormatType.Unknown:
fileName += "Jpg";
break;
default:
//........
break;
}
// Save the oleobject as a new excel file if the object type is xls.
if (ole.getFileFormatType() === AsposeCells.FileFormatType.Xlsx) {
const ms = Buffer.from(ole.getObjectData());
if (ole.getObjectData() != null) {
const oleBook = new AsposeCells.Workbook(ms);
oleBook.getSettings().setIsHidden(false);
oleBook.save(path.join(dataDir, "outOle" + i + ".out.xlsx"));
}
} else {
if (ole.getObjectData() != null) {
fs.writeFileSync(fileName, ole.getObjectData());
}
}
}
```
