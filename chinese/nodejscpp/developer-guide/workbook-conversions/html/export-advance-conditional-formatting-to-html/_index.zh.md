---  
title: 在使用Node.js通过C++将Excel转换为HTML时导出数据条、颜色刻度和图标集条件格式  
linktitle: 在将Excel转换为HTML时，导出数据条、颜色刻度和图标集条件格式  
type: docs  
weight: 30  
url: /zh/nodejs-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/  
---  

{{% alert color="primary" %}} 

 您可以在将Excel文件转换为HTML时导出数据条、颜色刻度和图标集条件格式。此功能Microsoft Excel部分支持，但Aspose.Cells for Node.js via C++完全支持此功能。

{{% /alert %}}  

## **在将Excel转换为HTML时，导出数据条、颜色刻度和图标集条件格式**  
下面的截图展示了具有 DataBar、ColorScale 和 IconSet 有条件格式的[sample excel file](5115558.xlsx)。您可以从给定的链接下载[sample excel file](5115558.xlsx)。  

![todo:image_alt_text](conversion_1.png)  

下面的截图展示了 Aspose.Cells 输出的 HTML 文件，显示了 DataBar、ColorScale 和 IconSet 有条件格式。正如您所看到的，它看起来与[sample excel file](5115558.xlsx)完全一样。  

![todo:image_alt_text](conversion_2.png)  

### **示例代码**  
 以下示例代码将示例Excel文件转换为HTML，仅为普通[Excel转HTML](/cells/zh/nodejs-cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml)。  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in HTML format
wb.save(path.join(dataDir, "ConvertingToHTMLFiles_out.html"), AsposeCells.SaveFormat.Html);
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
