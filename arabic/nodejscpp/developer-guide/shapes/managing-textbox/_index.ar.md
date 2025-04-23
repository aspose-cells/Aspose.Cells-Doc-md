---
title: إدارة مربع النص باستخدام Node.js عبر C++
linktitle: إدارة مربع النص
type: docs
weight: 50
url: /ar/nodejs-cpp/managing-textbox-of-excel/
description: تعلم كيفية إدارة مربع النص في Excel باستخدام Aspose.Cells for Node.js via C++. 
keywords: إدارة مربع النص في Excel باستخدام Node.js عبر C++ 
---


## **سيناريوهات الاستخدام المحتملة**
هناك سيناريوهات قد تحتاج فيها إلى إضافة أو تحديث أو تManipulate كائنات مربع النص داخل ورقة عمل Excel. يمكن أن يكون هذا مفيدًا لإضافة تعليق، نص إرشادي، أو أي معلومات إضافية تساعد في عرض البيانات. يوفر Aspose.Cells for Node.js via C++ وظائف قوية لإدارة مربع النص في مستندات Excel. 

## **إدارة مربع النص باستخدام Aspose.Cells for Node.js via C++**
يوضح هذا المثال كيف:

1. إنشاء ورقة عمل جديدة.
2. أضف شكل WordArt.
3. عدِّل خصائص مربع النص حسب الحاجة.

```javascript
const Cells = require("aspose.cells"); // Ensure you have linked the Aspose.Cells library correctly

// Create a new workbook
let workbook = new Cells.Workbook();
// Access the first worksheet
let worksheet = workbook.getWorksheets().get(0);

// Adding a TextBox shape
let textBox = worksheet.getShapes().addTextBox(2, 2, 100, 100);

// Set TextBox properties
textBox.setText("This is a TextBox.");
textBox.setFontSize(12);
textBox.setFillColor(Cells.Color.fromArgb(255, 255, 255)); // White background

// Save the workbook
workbook.save("TextBoxExample.xlsx");
```

توضح هذه الرموز كيفية إنشاء وتكوين مربع النص داخل ورقة عمل Excel، مع إظهار كيفية تعديل حجمه وموقعه وتنسيقه وفقًا لمتطلباتك.

ضع في اعتبارك أن التفاعلات مع مربعات النص قد تختلف حسب حالات الاستخدام المحددة، لذا يرجى الرجوع إلى توثيق Aspose.Cells for Node.js via C++ لمزيد من الطرق والخصائص.

---
