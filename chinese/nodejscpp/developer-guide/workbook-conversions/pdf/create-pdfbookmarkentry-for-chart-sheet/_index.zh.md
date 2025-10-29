---  
title: 使用C++ via Node.js为图表工作表创建PdfBookmarkEntry  
linktitle: 为图表工作表创建PdfBookmarkEntry  
type: docs  
weight: 50  
url: /zh/nodejs-cpp/create-pdfbookmarkentry-for-chart-sheet/  
description: 了解如何使用Aspose.Cells for Node.js via C++为图表工作表创建PdfBookmarkEntry。  
---  

## **可能的使用场景**  

 早期，Aspose.Cells为普通工作表创建了[**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry)。但现在，Aspose.Cells也可以为图表工作表创建[**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry)。由于图表工作表没有除A1单元格之外的其他单元格，它只会为A1单元格创建[**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry)。  

## **为图表工作表创建PdfBookmarkEntry**  

以下示例代码加载了具有四个工作表的[示例Excel文件](61767756.xlsx)，其中两个是普通工作表，另外两个是图表工作表。它创建了四个书签条目，如下所示  

- 书签I  
- 书签II-Chart1  
- 书签III  
- 书签IV-Chart2  

以下屏幕截图显示了示例代码生成的[输出PDF](61767757.pdf)以供参考。  

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)  

## **示例代码**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleCreatePdfBookmarkEntryForChartSheet.xlsx");

// Load sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access all four worksheets
const sheet1 = workbook.getWorksheets().get(0);
const sheet2 = workbook.getWorksheets().get(1);
const sheet3 = workbook.getWorksheets().get(2);
const sheet4 = workbook.getWorksheets().get(3);

// Create Pdf Bookmark Entry for Sheet1
const ent1 = new AsposeCells.PdfBookmarkEntry();
ent1.setDestination(sheet1.getCells().get("A1"));
ent1.setText("Bookmark-I");

// Create Pdf Bookmark Entry for Sheet2 - Chart
const ent2 = new AsposeCells.PdfBookmarkEntry();
ent2.setDestination(sheet2.getCells().get("A1"));
ent2.setText("Bookmark-II-Chart1");

// Create Pdf Bookmark Entry for Sheet3
const ent3 = new AsposeCells.PdfBookmarkEntry();
ent3.setDestination(sheet3.getCells().get("A1"));
ent3.setText("Bookmark-III");

// Create Pdf Bookmark Entry for Sheet4 - Chart
const ent4 = new AsposeCells.PdfBookmarkEntry();
ent4.setDestination(sheet4.getCells().get("A1"));
ent4.setText("Bookmark-IV-Chart2");

// Arrange all Bookmark Entries
const lst = [];
lst.push(ent2);
lst.push(ent3);
lst.push(ent4);

// Create Pdf Save Options with Bookmark Entries
const opts = new AsposeCells.PdfSaveOptions();
opts.setBookmark(ent1);

// Save the output Pdf
workbook.save("outputCreatePdfBookmarkEntryForChartSheet.pdf", opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
