---
title: تخصيص XML الشريط باستخدام Node.js عبر C++
linktitle: تخصيص قائمة Excel
type: docs
weight: 1500
url: /ar/nodejs-cpp/customizing-the-ribbon-xml/
description: تعلم كيفية تخصيص XML الشريط في إكسل باستخدام Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}} 

استبدلت Microsoft Office القوائم وشرائط الأدوات بشريط في الجزء العلوي من نافذة التطبيق منذ إصدار Office 2007. يمكن تخصيص الشريط. 
تمكنك Aspose.Cells for Node.js via C++ من

- الاحتفاظ برمز الشريط XML دون تحليله،
- قراءة وكتابة رمز الشريط XML دون تحليله،
- الحصول على بيانات رمز الشريط XML وتعيينها.

إذا كنت ترغب في تغيير رمز الشريط XML، عليك تحليله باستخدام محلل XML أو أداة أخرى لرمز الشريط XML.

{{% /alert %}} 

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "aspose-sample.xlsx");
// Loads the workbook
const workbook = new AsposeCells.Workbook(filePath);

const ribbonXml = `<customUI xmlns="http://schemas.microsoft.com/office/2006/01/customui"></customUI>`;
workbook.setRibbonXml(ribbonXml);
```
