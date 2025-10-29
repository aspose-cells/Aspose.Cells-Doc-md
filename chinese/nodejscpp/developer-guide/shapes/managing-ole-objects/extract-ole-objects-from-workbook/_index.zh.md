---  
title: 通过C++和Node.js从工作簿中提取OLE对象  
linktitle: 从工作簿中提取OLE对象  
type: docs  
weight: 110  
url: /zh/nodejs-cpp/extract-ole-objects-from-workbook/  
---  

{{% alert color="primary" %}}  
有时，您确实需要从工作簿中提取OLE对象。Aspose.Cells支持提取和保存这些OLE对象。

本文展示了如何通过C++在Node.js中创建控制台应用程序，并通过几行简单代码从工作簿中提取不同的OLE对象。  
{{% /alert %}}  

## **从工作簿中提取OLE对象**  

### **创建模板工作簿**  

1. 在Microsoft Excel中创建一个工作簿。  
1. 在第一个工作表上添加Microsoft Word文档、Excel工作簿和PDF文档作为OLE对象。  

|**带有OLE对象的模板文档（OleFile.xls)**|  
| :- |  
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|  

接下来，提取OLE对象并保存到硬盘，保留其各自的文件类型。  

### **下载并安装Aspose.Cells**  

[下载Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp)。  
1. 在您的开发计算机上安装它。  

所有Aspose组件在安装后都处于评估模式。评估模式没有时间限制，只会在生成的文档中插入水印。  

### **创建一个项目**  

启动**Node.js**并创建一个新的控制台应用程序。本示例将演示一个Node.js控制台应用程序，但你也可以使用任何兼容JavaScript的环境。  

1. 添加依赖项  
   1. 在你的项目中添加Aspose.Cells组件的引用，例如使用`require`函数引入包：  
   ```javascript  
   const { Cells } = require("aspose.cells");  
   ```

### **从工作簿中提取OLE对象**  

以下代码实际完成了查找和提取OLE对象的工作。OLE对象（DOC、XLS和PDF文件）会被保存到硬盘。  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
