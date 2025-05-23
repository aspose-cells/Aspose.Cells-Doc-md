---
title: كيفية التحكم في عرض المصنف باستخدام Node.js عبر C++
linktitle: كيفية التحكم في عرض دفتر العمل
type: docs
weight: 600
url: /ar/nodejs-cpp/how-to-control-workbook-view/
description: تعلم كيفية التحكم في عرض المصنف من خلال واجهة برمجة التطبيقات Aspose.Cells for Node.js via C++.
keywords: كيفية التحكم في عرض المصنف باستخدام Node.js عبر C++، تعيين عرض إكسل باستخدام Node.js عبر C++، تشغيل عرض المصنف باستخدام Node.js عبر C++، تعيين عرض المصنف باستخدام Node.js عبر C++، التحكم في عرض إكسل باستخدام Node.js عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**
عندما تحتاج إلى ضبط عرض صفحات إكسل، تحتاج إلى معرفة كيفية التحكم في كل وحدة، مثل أشرطة التمرير أفقياً وعمودياً، سواء كان يجب إخفاء ملفات إكسل المفتوحة، وما إلى ذلك. تقدم Aspose.Cells for Node.js via C++ هذه الميزة. توفر Aspose.Cells for Node.js via C++ الخصائص والطرق التالية لمساعدتك على تحقيق أهدافك.

- [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--)
- [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--)
- [**WorkbookSettings.isHidden()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHidden--)
- [**WorkbookSettings.isMinimized()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isMinimized--)
- [**WorkbookSettings.getWindowHeight()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowHeight--)
- [**WorkbookSettings.getWindowWidth()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowWidth--)
- [**WorkbookSettings.getWindowLeft()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowLeft--)
- [**WorkbookSettings.getWindowTop()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowTop--)

## **كيفية التحكم في عرض المصنف باستخدام Aspose.Cells for Node.js via C++**
يوضح هذا المثال كيف:

1. إنشاء دفتر عمل.
1. إضافة بيانات إلى الخلايا في ورقة العمل الأولى.
1. إخفاء شرائط التمرير الأفقية والعمودية لعرض دفتر العمل.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating an Workbook object
const workbook = new AsposeCells.Workbook();
// Obtaining the reference of the newly added worksheet
const ws = workbook.getWorksheets().get(0);
const cells = ws.getCells();

// Setting the value to the cells
let cell = cells.get("A1");
cell.putValue("Fruit");
cell = cells.get("B1");
cell.putValue("Count");
cell = cells.get("C1");
cell.putValue("Price");

cell = cells.get("A2");
cell.putValue("Apple");
cell = cells.get("A3");
cell.putValue("Mango");
cell = cells.get("A4");
cell.putValue("Blackberry");
cell = cells.get("A5");
cell.putValue("Cherry");

cell = cells.get("B2");
cell.putValue(5);
cell = cells.get("B3");
cell.putValue(3);
cell = cells.get("B4");
cell.putValue(6);
cell = cells.get("B5");
cell.putValue(4);

cell = cells.get("C2");
cell.putValue(5);
cell = cells.get("C3");
cell.putValue(20);
cell = cells.get("C4");
cell.putValue(30);
cell = cells.get("C5");
cell.putValue(60);

cell = cells.get("E10");
const temp = workbook.createStyle();
temp.getFont().setColor(AsposeCells.Color.Red);
cell.setStyle(temp);

// Hide horizontal and vertical scrollbars
workbook.getSettings().setIsHScrollBarVisible(false);
workbook.getSettings().setIsVScrollBarVisible(false);

workbook.save("out.xlsx");
```

معاينة ملف النتائج:
<br>
<image src="result.png" width="70%" />

