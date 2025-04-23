---  
title: حفظ ملف العمل بصيغة جدول بيانات XML الصارمة باستخدام Node.js عبر C++  
linktitle: حفظ الدفتر إلى تنسيق جدول بيانات إكس الإكس إم الصارم  
type: docs  
weight: 150  
url: /ar/nodejs-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/  
description: تعلم كيفية حفظ ملف العمل بتنسيق XML الصارم باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

 يتيح لك Aspose.Cells for Node.js via C++ حفظ ملف العمل بالتنسيق *XML الصارم*. لهذا الغرض، يوفر الخاصية [**WorkbookSettings.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCompliance--). إذا قمت بتعيين قيمتها إلى [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompliance)، فسيتم حفظ الملف Excel الناتج بتنسيق XML الصارم.  

## **حفظ الدفتر إلى تنسيق جدول بيانات إكس الإكس إم الصارم**  

 ينشئ رمز العينة التالي ملف عمل ويضبط قيمة الخاصية [**WorkbookSettings.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCompliance--) إلى [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompliance) ويحفظه كـ [ملف Excel المخرج](67338272.xlsx). إذا فتحت ملف Excel المخرج في Microsoft Excel وفتحت مربع الحوار Save As...، سترى تنسيقه كـ *Open XML الصارم* كما هو موضح في هذه الصورة.  

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)  

## **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook.
const wb = new AsposeCells.Workbook();

// Specify - Strict Open XML Spreadsheet - Format.
wb.getSettings().setCompliance(AsposeCells.OoxmlCompliance.Iso29500_2008_Strict);

// Add message in cell B4 of first worksheet.
const b4 = wb.getWorksheets().get(0).getCells().get("B4");
b4.putValue("This Excel file has Strict Open XML Spreadsheet format.");

// Save to output Excel file.
wb.save("outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

