---  
title: 通过C++和Node.js获取或设置嵌入式OLE对象的类标识符  
linktitle: 获取或设置嵌入式OLE对象的类标识符  
type: docs  
weight: 200  
url: /zh/nodejs-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/  
description: 学习如何通过C++在Node.js中使用Aspose.Cells获取或设置嵌入式OLE对象的类标识符。  
---  

## **可能的使用场景**  
Aspose.Cells提供[OleObject.getClassIdentifier()](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getClassIdentifier--)属性，可用于获取或设置嵌入式OLE对象的类标识符。OLE对象类标识符实际上是GUID（全局唯一标识符），长度为16字节，通常在Windows注册表中找到，用于指示主应用程序如何打开包含各种嵌入资源的OLE对象。

## **获取或设置嵌入的OLE对象的类标识符**  
下面的截图显示了从[示例Excel文件](5115190.xls)中读取的OLE对象类标识符（GUID）。

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)  
### **示例代码**  
请参见用[示例Excel文件](5115190.xls)执行的以下示例代码及其控制台输出，输出打印了OLE对象的类标识符（GUID），与截图中显示的完全相同。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your sample workbook which contains embedded PowerPoint ole object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xls"));

// Access its first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first ole object inside the worksheet
const oleObject = worksheet.getOleObjects().get(0);

// Convert 16-bytes array into GUID
const guid = new Uint8Array(oleObject.getClassIdentifier()).reduce((acc, byte) => acc + String.fromCharCode(byte), '');

// Print the GUID
console.log(guid.toUpperCase());
```  
### **控制台输出**  
以上示例代码执行后生成的控制台输出。

{{< highlight java >}}  
 DC020317-E6E2-4A62-B9FA-B3EFE16626F4  
{{< /highlight >}}  

