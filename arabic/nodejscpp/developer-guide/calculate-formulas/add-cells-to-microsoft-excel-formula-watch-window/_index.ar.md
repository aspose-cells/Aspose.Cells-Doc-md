---
title: إضافة خلايا إلى نافذة مراقبة الصيغ في Microsoft Excel باستخدام Node.js عبر C++
linktitle: إضافة الخلايا إلى نافذة مراقبة الصيغ في Microsoft Excel
description: كيفية استخدام مكتبة Aspose.Cells لإضافة خلايا إلى نافذة مراقبة الصيغ في Excel باستخدام Node.js عبر C++. عن طريق تحميل ملف Excel موجود أو إنشاء واحد جديد، يمكننا التلاعب بالخلايا فيه وتعيين الصيغ. أخيرًا، نحفظ ملف Excel المعدل على القرص.
keywords: Aspose.Cells، Excel، نافذة مراقبة الصيغ، خلايا، الإضافة، Node.js عبر C++
type: docs
weight: 60
url: /ar/nodejs-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **سيناريوهات الاستخدام المحتملة**

نافذة مراقبة Excel من Microsoft هي أداة مفيدة لمراقبة قيم الخلايا وصيغها بسهولة في نافذة. يمكنك فتح *نافذة المراقبة* باستخدام Excel من Microsoft بالنقر على *الصيغ > مراقبة > نافذة*. تحتوي على زر *إضافة مراقبة* الذي يمكن استخدامه لإضافة خلايا للفحص. بالمثل، يمكنك استخدام [**CellWatchCollection.add(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cellwatchcollection/#add-number-number-) لإضافة خلايا إلى *نافذة المراقبة* باستخدام API الخاص بـ Aspose.Cells.

## **إضافة الخلايا إلى نافذة مراقبة صيغ Microsoft Excel**

يعتمد الكود النموذجي التالي تعيين صيغة للخلايا C1 و E1 وإضافتهما إلى نافذة المراقبة. ثم نحفظ المصنف كـ ملف إكسل ناتج. إذا فتحت الملف الناتج وتطلعت على *نافذة المراقبة*، سترى كلا الخليتين كما هو موضح في لقطة الشاشة هذه.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Put some integer values in cell A1 and A2.
ws.getCells().get("A1").putValue(10);
ws.getCells().get("A2").putValue(30);

// Access cell C1 and set its formula.
const c1 = ws.getCells().get("C1");
c1.setFormula("=Sum(A1,A2)");

// Add cell C1 into cell watches by name.
ws.getCellWatches().add(c1.getName());

// Access cell E1 and set its formula.
const e1 = ws.getCells().get("E1");
e1.setFormula("=A2*A1");

// Add cell E1 into cell watches by its row and column indices.
ws.getCellWatches().add(e1.getRow(), e1.getColumn());

// Save workbook to output XLSX format.
wb.save("outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", AsposeCells.SaveFormat.Xlsx);
```
