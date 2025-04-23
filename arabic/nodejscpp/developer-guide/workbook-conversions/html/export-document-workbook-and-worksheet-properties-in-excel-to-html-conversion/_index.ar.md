---  
title: تصدير خصائص دفتر العمل وورقة العمل والملف في تحويل Excel إلى HTML باستخدام Node.js عبر C++  
linktitle: تصدير خصائص ورقة عمل ومصنف الوثيقة في تحويل Excel إلى HTML  
type: docs  
weight: 50  
url: /ar/nodejs-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/  
description: تعلم كيفية تصدير خصائص المستند ودفتر العمل وورقة العمل في Excel إلى HTML باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

عند تصدير ملف Microsoft Excel إلى HTML باستخدام Microsoft Excel أو Aspose.Cells for Node.js via C++، يتم تصدير أنواع مختلفة من خصائص المستند ودفتر العمل وورقة العمل كما هو موضح في لقطة الشاشة التالية. يمكنك تجنب تصدير هذه الخصائص بضبط [**HtmlSaveOptions.getExportDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportDocumentProperties--) و [**HtmlSaveOptions.getExportWorkbookProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorkbookProperties--) و [**HtmlSaveOptions.getExportWorksheetProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetProperties--) على **false**. القيمة الافتراضية لهذه الخصائص هي **true**. تظهر اللقطة التالية كيف تبدو هذه الخصائص في HTML المصدر.  

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)  

## **تصدير خصائص الوثيقة والمصنف وورق العمل في تحويل Excel إلى HTML**  

يحمل رمز المثال التالي ملف Excel النموذجي ويحوّله إلى HTML بدون تصدير خصائص المستند ودفتر العمل وورقة العمل في [HTML الناتج](61767779.zip).  

## **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExportDocumentWorkbookAndWorksheetPropertiesInHTML.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Specify Html Save Options
const options = new AsposeCells.HtmlSaveOptions();

// We do not want to export document, workbook and worksheet properties
options.setExportDocumentProperties(false);
options.setExportWorkbookProperties(false);
options.setExportWorksheetProperties(false);

// Export the Excel file to Html with Html Save Options
workbook.save("outputExportDocumentWorkbookAndWorksheetPropertiesInHTML.html", options);
```  

