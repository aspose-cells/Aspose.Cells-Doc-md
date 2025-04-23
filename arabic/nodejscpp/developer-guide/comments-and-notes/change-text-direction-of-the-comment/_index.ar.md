---
title: تغيير اتجاه نص التعليق باستخدام Node.js عبر C++
linktitle: تم إرفاق [ملف الإخراج](102662195.xlsx) الذي تم إنشاؤه بواسطة الرمز العينة أعلاه للإشارة الخاصة بك.
type: docs
weight: 10
url: /ar/nodejs-cpp/change-text-direction-of-the-comment/
description: تعلم كيفية تغيير اتجاه نص التعليقات باستخدام Aspose.Cells for Node.js via C++. قم بتخصيص إعدادات محاذاة التعليق بشكل فعال.
---

{{% alert color="primary" %}}

يتيح Microsoft Excel للمستخدمين إضافة تعليقات إلى الخلايا لإضافة معلومات إضافية وتسليط الضوء على البيانات. قد يحتاج المطورون إلى تخصيص التعليق لتحديد إعدادات المحاذاة واتجاه النص. توفر Aspose.Cells for Node.js via C++ APIs لإنجاز المهمة.

{{% /alert %}}

توفر Aspose.Cells for Node.js via C++ خاصية [**Shape.getTextDirection()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextDirection--) لضبط اتجاه نص التعليق. يوضح الكود التالي استخدام الخاصية [**Shape.getTextDirection()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextDirection--) لضبط اتجاه النص في التعليق.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const wb = new AsposeCells.Workbook();

// Get the first worksheet
const sheet = wb.getWorksheets().get(0);

// Add a comment to A1 cell
const commentIndex = sheet.getComments().add("A1");
const comment = sheet.getComments().get(commentIndex);

// Set its vertical alignment setting            
comment.getCommentShape().setTextVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Set its horizontal alignment setting
comment.getCommentShape().setTextHorizontalAlignment(AsposeCells.TextAlignmentType.Right);

// Set the Text Direction - Right-to-Left
comment.getCommentShape().setTextOrientationType(AsposeCells.TextDirectionType.RightToLeft);

// Set the Comment note
comment.setNote("This is my Comment Text. This is test");

const outputFilePath = path.join(dataDir, "OutCommentShape.out.xlsx");
// Save the Excel file
wb.save(outputFilePath);
```
