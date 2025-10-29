---
title: استخدم خاصية Sheet.SheetId من OpenXml باستخدام Aspose.Cells for Node.js via C++
linktitle: استخدام خاصية Sheet.SheetId في OpenXml باستخدام Aspose.Cells
type: docs
weight: 200
url: /ar/nodejs-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: يُوضح هذا المقال كيفية استخدام خاصية Sheet.SheetId من OpenXml برمجياً باستخدام Excel مع Aspose.Cells for Node.js via C++.
keywords: معرف ورقة العمل الخاص بـ openxml عبر node.js باستخدام C++، معرف ورقة العمل في Excel عبر node.js باستخدام C++
---

## **سيناريوهات الاستخدام المحتملة**

خاصية *Sheet.SheetId* متاحة داخل وحدة *DocumentFormat.OpenXml.Spreadsheet* وهي جزء من OpenXml. يمكنك رؤية هذه الخاصية وقيمتها داخل *workbook.xml* كما هو موضح في لقطة الشاشة التالية. توفر Aspose.Cells الخاصية المعادلة [**Worksheet.getTabId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getTabId--).

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **استخدم خاصية Sheet.SheetId من OpenXml باستخدام Aspose.Cells for Node.js via C++**

يقوم الكود البرمجي العيني التالي بتحميل [ملف Excel عيني](51740716.xlsx)، يقرأ تعريف معرف ورقتها أو تبويبها، ثم يعين له معرف تبويب جديد ويحفظه ك[ملف Excel الناتج](51740717.xlsx). يرجى أيضاً النظر إلى مخرجات الكونسول المعروضة في الكود أدناه للإشارة.

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSheetId.xlsx");

// Load source Excel file
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Print its Sheet or Tab Id on console
console.log("Sheet or Tab Id: " + ws.getTabId());

// Change Sheet or Tab Id
ws.setTabId(358);

// Save the workbook
wb.save("outputSheetId.xlsx");
```

## **مخرجات الوحدة**

{{< highlight text >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
