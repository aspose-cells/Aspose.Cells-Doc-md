---  
title: 使用Node.js通过C++在将Excel文件导出为HTML时实现文本从右到左的展开  
linktitle: 将Excel文件导出为HTML时从右向左扩展文本  
type: docs  
weight: 60  
url: /zh/nodejs-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/  
---  

{{% alert color="primary" %}}  

Aspose.Cells现在支持将Excel文件中从右向左扩展的文本导出为HTML。该功能自v8.9.0.0版本已经实现。现在，如果您的源Excel文件包含从右向左扩展的文本，那么Aspose.Cells将正确地将其导出为HTML。  

{{% /alert %}}  
## **在将Excel文件导出为HTML时，将文本从右向左扩展**  
下面的示例代码将[sample excel file](5115502.xlsx)转换成HTML。这张截图展示了示例 Excel 在 Microsoft Excel 2013 中的样子。  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)  

这张截图展示了使用较旧版本生成的[output HTML](5115509)。  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)  

这张截图展示了使用更新版本生成的[output HTML](5115508)。  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)  

正如您在屏幕截图中所看到的，新版本正确地将右对齐的文本向左扩展，就像Microsoft Excel一样。  


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load source excel file inside the workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save workbook in html format
wb.save(path.join(dataDir, `ExpandTextFromRightToLeft_out_${AsposeCells.CellsHelper.getVersion()}.html`), AsposeCells.SaveFormat.Html);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
