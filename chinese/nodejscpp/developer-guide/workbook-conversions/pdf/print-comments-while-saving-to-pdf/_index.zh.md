---  
title: 使用Node.js通过C++在保存为PDF时打印评论  
linktitle: 保存为PDF时打印注释  
type: docs  
weight: 10  
url: /zh/nodejs-cpp/print-comments-while-saving-to-pdf/  
description: 了解在将Excel文档保存为PDF时如何打印评论，使用编号Aspose.Cells for Node.js via C++。  
---  

{{% alert color="primary" %}}  

Microsoft Excel允许您在打印或保存为PDF格式时打印注释，具有以下选项  

- 无  
- 工作表末尾  
- 如在工作表上显示的那样  

Aspose.Cells提供了支持相同功能的[**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype)枚举。[**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype)枚举具有以下成员：  

- PrintNoComments  
- PrintInPlace  
- PrintSheetEnd  

{{% /alert %}}  

## **保存为PDF时打印注释**  

以下示例代码说明了如何使用[**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype)在保存为PDF时打印批注。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook from the source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleWorkbookWithComments.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

/*
* For print no comments use "PrintCommentsType.PrintNoComments"
* and for print the comments as displayed on sheet use "PrintCommentsType.PrintInPlace"
* For Print the comments at the end of sheet we use "PrintCommentsType.PrintSheetEnd"
*/
worksheet.getPageSetup().setPrintComments(AsposeCells.PrintCommentsType.PrintSheetEnd);

// Save workbook in pdf format
workbook.save(path.join(dataDir, "PrintCommentWhileSavingToPdf_out.pdf"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
