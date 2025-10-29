---  
title: 通过 C++ 管理Node.js中的OLE对象  
linktitle: 管理OLE对象  
type: docs  
weight: 50  
url: /zh/nodejs-cpp/managing-ole-objects/  
description: 学习如何在Aspose.Cells for Node.js via C++中管理OLE对象。添加、提取和操作工作表中的OLE对象。  
---  

## **介绍**  

OLE（对象链接与嵌入）是一种复合文档技术框架。简而言之，复合文档类似于一个显示桌面，可以包含各种视觉和信息对象：文本、日历、动画、声音、运动视频、3D、不断更新的新闻、控件等等。每个桌面对象都是一个独立的程序实体，可以与用户交互，也可以与桌面上的其他对象通信。  

OLE 受到许多不同程序的支持，并用来让一个程序中创建的内容可以在另一个程序中使用。例如，你可以在 Microsoft Excel 中插入一个 Microsoft Word 文档。要查看你可以插入的内容类型，请点击**插入**菜单中的**对象**。只有电脑上已安装且支持OLE对象的程序会出现在**对象类型**框中。  

### **将OLE对象插入工作表**  

Aspose.Cells for Node.js via C++ 支持在工作表中添加、提取和操作OLE对象。因此，Aspose.Cells拥有[**OleObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/oleobjectcollection)类，用于向集合中添加新的OLE对象。另一个类，[**OleObject**](https://reference.aspose.com/cells/nodejs-cpp/oleobject)，代表一个OLE对象。它具有一些重要的成员：  

- [**getImageData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getImageData--)属性指定图像（图标）的字节数组数据。图像将显示在工作表中，用于展示OLE对象。  
- [**getObjectData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getObjectData--)属性指定对象的数据，形式为字节数组。当双击OLE对象图标时，将在相关程序中显示这些数据。  

下面的示例演示了如何将一个或多个OLE对象添加到工作表中。  

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

### **从工作簿中提取OLE对象**  

以下示例显示了如何从工作簿中提取OLE对象。该示例从现有的XLS文件中获取不同的OLE对象，并根据OLE对象的文件格式类型保存不同的文件(DOC、XLS、PPT、PDF等)。  

运行代码后，我们可以根据各自OLE对象的格式类型保存不同的文件。  

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

### **提取嵌入的MOL文件**  

Aspose.Cells for Node.js via C++ 支持提取非常规类型的对象，比如 MOL（分子数据文件，包含关于原子和键的信息）。以下代码片段展示了如何提取嵌入的 MOL 文件并用[此示例Excel文件](94896196.xlsx)将其保存到磁盘。  

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

## **高级主题**  
- [访问和修改链接的OLE对象的显示标签](/cells/zh/nodejs-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)  
- [使用Aspose.Cells自动刷新OLE对象通过Microsoft Excel](/cells/zh/nodejs-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)  
- [从工作簿中提取OLE对象](/cells/zh/nodejs-cpp/extract-ole-objects-from-workbook/)  
- [获取或设置嵌入的OLE对象的类标识符](/cells/zh/nodejs-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)  
- [将WAV文件插入为一个OLE对象。](/cells/zh/nodejs-cpp/inserting-a-wav-file-as-an-ole-object/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
