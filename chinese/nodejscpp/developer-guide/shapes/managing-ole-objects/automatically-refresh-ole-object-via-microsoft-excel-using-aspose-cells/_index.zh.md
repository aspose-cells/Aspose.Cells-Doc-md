---  
title: 使用Aspose.Cells for Node.js via C++通过Microsoft Excel自动刷新OLE对象  
linktitle: 使用Aspose.Cells自动刷新OLE对象通过Microsoft Excel  
type: docs  
weight: 270  
url: /zh/nodejs-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/  
description: 学习如何使用Aspose.Cells for Node.js via C++在Excel中自动刷新OLE对象。  
---  

{{% alert color="primary" %}}  
Aspose.Cells提供 [**OleObject.getAutoLoad()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getAutoLoad--) 属性，在Microsoft Excel中打开excel文件时刷新OLE对象。由于该属性，OLE对象将显示由Microsoft Excel生成的正确OLE图像。  
{{% /alert %}}  

以下样本代码加载了包含非真实OLE图像的 [样本excel文件](5115231.xlsx)。OLE对象实际上是一个Microsoft Word文档，但样本excel文件显示的是动物图像，而不是Microsoft Word图像。但是，如果打开 [输出excel文件](5115225.xlsx)，您将看到Microsoft Excel显示了正确的OLE图像。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object from your sample excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample_oleobject.xlsx"));

// Access first worksheet
const sheet = workbook.getWorksheets().get(0);

// Set auto load property of first ole object to true
sheet.getOleObjects().get(0).setAutoLoad(true);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "RefreshOLEObjects_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
