---
title: إدراج شرارة نابضة بالحياة باستخدام Node.js عبر C++
linktitle: Sparklines
type: docs
weight: 160
url: /ar/nodejs-cpp/creating-sparklines/
description: إنشاء شرارة نابضة بالحياة لملف إكسل باستخدام Aspose.Cells for Node.js via C++.
---

## **إدراج شريط إشاري**
{{% alert color="primary" %}} 

الشرارة النابضة بالحياة هي رسم بياني صغير في خلية ورقة العمل يوفر تمثيلًا بصريًا للبيانات. استخدم الشرارات لعرض الاتجاهات في سلسلة من القيم، مثل الزيادات الموسمية أو الانخفاضات، الدورات الاقتصادية، أو لتسليط الضوء على القيم القصوى والدنيا. ضع الشرارة بالقرب من بياناتها لتحقيق أقصى تأثير. هناك ثلاثة أنواع من الشرارات: خط، عمود وطبقات.

{{% /alert %}} 

من السهل إنشاء شرارة نابضة بالحياة باستخدام Aspose.Cells for Node.js via C++ مع الأمثلة التالية:



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const book = new AsposeCells.Workbook(filePath);
const sheet = book.getWorksheets().get(0);

sheet.getCells().get("A1").putValue(5);
sheet.getCells().get("B1").putValue(2);
sheet.getCells().get("C1").putValue(1);
sheet.getCells().get("D1").putValue(3);

// Define the CellArea
const ca = AsposeCells.CellArea.createCellArea(0, 4, 0, 4);

const idx = sheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, `${sheet.getName()}!A1:D1`, false, ca);

const group = sheet.getSparklineGroups().get(idx);
group.getSparklines().add(`${sheet.getName()}!A1:D1`, 0, 4);

// Customize Sparklines

// Create CellsColor
const clr = book.createCellsColor();
clr.setColor(AsposeCells.Color.Orange);
group.setSeriesColor(clr);

// Set the high points are colored green and the low points are colored red
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.getHighPointColor().setColor(AsposeCells.Color.Green);
group.getLowPointColor().setColor(AsposeCells.Color.Red);
// Set line weight 
group.setLineWeight(1.0);

// Saving the Excel file
book.save(path.join(dataDir, "output.xlsx"));
```

## **مواضيع متقدمة**
- [استخدام الشرائط الإشارية وإعدادات تنسيق ثلاثي الأبعاد](/cells/ar/nodejs-cpp/using-sparklines-and-settings-3d-format/)
