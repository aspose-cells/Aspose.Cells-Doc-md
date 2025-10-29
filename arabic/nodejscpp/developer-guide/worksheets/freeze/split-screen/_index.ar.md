---
title: تقسيم شاشة ورقة إكسل باستخدام Node.js عبر C++
linktitle: شاشة مقسمة
type: docs
weight: 190
url: /ar/nodejs-cpp/how-to-split-screen-of-excel-worksheet
description: في هذا المقال، ستتعلم كيفية عرض صفوف و/أو أعمدة معينة في ألواح منفصلة عن طريق تقسيم ورقة العمل إلى جزءين أو أربعة أجزاء برمجيًا باستخدام إضافة Node.js C++.
keywords: تجميد الصفوف العليا، تجميد الصف العلوي.
---

## **مقدمة**

في هذا المقال، سوف نتعلم كيفية عرض صفوف و/أو أعمدة معينة في ألواح منفصلة عن طريق تقسيم ورقة العمل إلى جزأين أو أربعة أجزاء. عند العمل مع مجموعات البيانات الكبيرة، نحتاج إلى رؤية مناطق معينة من نفس ورقة العمل في وقت واحد للمقارنة بين مجموعات البيانات المختلفة. يمكن أن تلبي وظيفة تقسيم الشاشة احتياجاتك.

## **كيفية تقسيم الشاشة في إكسيل**
لتقسيم ورقة عمل إلى جزئين أو أربعة أجزاء، اتبع الخطوات التالية:

1. حدد الصف / العمود / الخلية قبل المكان الذي تريد وضع التقسيم فيه.
2. على علامة التبويب عرض، في مجموعة النوافذ، انقر فوق زر التقسيم.

**![شاشة مقسمة](Split-Screen.png)**

## **تقسيم ورقة العمل عمودياً على الأعمدة**

لفصل منطقتين في جدول البيانات بشكل عمودي، حدد العمود إلى اليمين من العمود الذي ترغب في ظهور التقسيم فيه، ثم انقر فوق زر التقسيم في Excel.

من السهل تقسيم ورقة العمل عموديًا على الأعمدة برمجيًا باستخدام Aspose.Cells for Node.js via C++، نحتاج فقط إلى اختيار خلية واحدة في الصف العلوي كخلية نشطة، ثم التقسيم باستخدام طريقة [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets C1 cell in the top row as the active cell.
sheet.setActiveCell("C1");

// Split worksheet vertically on columns
sheet.split();
```

## **تقسيم ورقة العمل أفقياً على الصفوف**
لفصل نافذة Excel أفقياً، حدد الصف أسفل الصف الذي ترغب في ظهور التقسيم فيه في Excel.

من السهل تقسيم ورقة العمل أفقيًا على الصفوف برمجياً باستخدام Aspose.Cells for Node.js via C++، نحتاج فقط إلى اختيار خلية واحدة في العمود الأيسر كخلية نشطة، ثم التقسيم باستخدام [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets A6 cell in the left column as the active cell.
sheet.setActiveCell("A6");

// Split worksheet horizontally on rows
sheet.split();

workbook.save("dest.xlsx");
```

## **تقسيم ورقة العمل إلى أربعة أجزاء**
لعرض أربعة أقسام مختلفة من نفس ورقة البيانات بشكل متزامن، قم بتقسيم الشاشة الخاصة بك عمودياً وأفقياً في Excel.

من السهل تقسيم ورقة العمل عموديًا على الأعمدة برمجياً باستخدام Aspose.Cells for Node.js via C++، نحتاج فقط إلى اختيار خلية واحدة ليست في الصف الأول والعمود كخلية نشطة، ثم التقسيم باستخدام [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets E6 cell as the active cell.
sheet.setActiveCell("E6");

// Split worksheet into four parts
sheet.split();
```

## **كيفية إزالة التقسيم**
لإزالة تقسيم ورقة العمل، فقط انقر مرة أخرى فوق زر التقسيم.

يوفر Aspose.Cells for Node.js via C++ طريقة [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit--) لإزالة إعداد التقسيم.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Remove split.
sheet.removeSplit();

// Split worksheet into four parts
sheet.split();
```

{{< app/cells/assistant language="nodejs-cpp" >}}
