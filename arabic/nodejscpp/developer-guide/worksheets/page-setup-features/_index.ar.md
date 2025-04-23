---
title: خصائص إعداد الصفحة مع Node.js عبر C++
linktitle: ميزات إعداد الصفحة
type: docs
weight: 60
url: /ar/nodejs-cpp/page-setup-features/
description: استكشف خصائص إعداد الصفحة باستخدام Aspose.Cells for Node.js via C++. تعلم كيفية تكوين أبعاد الصفحة، الاتجاهات، والإعدادات.
keywords: خصائص إعداد الصفحة عبر Node.js عبر C++، تكوين أبعاد الصفحة عبر Node.js عبر C++، إعدادات اتجاه الصفحة عبر Node.js عبر C++
---



## **مقدمة**
باستخدام Aspose.Cells for Node.js via C++، يمكنك تعديل ميزات إعداد الصفحة المختلفة لمصنف إكسل. تشمل هذه الميزات ضبط حجم الصفحة، الاتجاه، الهوامش، وأكثر. يتيح التكوين الصحيح لهذه الميزات تجربة طباعة وعرض أفضل.

## **ضبط حجم الصفحة والاتجاه**
يمكنك تحديد حجم الصفحة واتجاهها في ورقة العمل باستخدام فئة `PageSetup`. توفر خصائص متعددة لإدارة أبعاد الصفحة وتخطيطها.

### **مثال على الكود**
إليك مثال على رمز يوضح كيفية ضبط حجم الصفحة والاتجاه.

```javascript
const { Workbook } = require("aspose.cells");

// Create a new workbook
let workbook = new Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Set the page size
worksheet.getPageSetup().setPaperSize(0); // A4 size

// Set the page orientation
worksheet.getPageSetup().setOrientation(1); // Landscape orientation

// Save the workbook
workbook.save("PageSetupExample.xlsx");
```

## **ضبط الهوامش**
يمكنك أيضًا ضبط الهوامش للصفحة باستخدام نفس فئة `PageSetup`. يمكن تعديل الهوامش للجوانب اليسار، اليمين، الأعلى، والأسفل.

### **مثال على الكود**
إليك كيفية ضبط هوامش ورقة العمل.

```javascript
// Set the margins
worksheet.getPageSetup().setLeftMargin(0.5);
worksheet.getPageSetup().setRightMargin(0.5);
worksheet.getPageSetup().setTopMargin(1.0);
worksheet.getPageSetup().setBottomMargin(1.0);

// Save the workbook
workbook.save("PageMarginsExample.xlsx");
```

## **الاستنتاج**
في هذا المستند، تعلمت كيفية التلاعب بميزات إعداد الصفحة في Excel باستخدام Aspose.Cells for Node.js via C++. من خلال الاستخدام الفعال لفئة `PageSetup`، يمكنك التحكم في كيفية طباعة وعرض أوراق العمل الخاصة بك، مما يعزز العرض العام للمعلومات.

---
