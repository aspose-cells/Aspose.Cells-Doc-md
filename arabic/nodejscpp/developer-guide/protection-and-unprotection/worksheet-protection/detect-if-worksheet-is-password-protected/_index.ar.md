---
title: كشف ما إذا كانت ورقة العمل محمية بكلمة مرور باستخدام Node.js عبر C++
linktitle: الكشف عما إذا كانت ورقة العمل محمية بكلمة مرور
type: docs
weight: 360
url: /ar/nodejs-cpp/detect-if-worksheet-is-password-protected/
description: تعرف على كيفية اكتشاف ما إذا كانت ورقة العمل محمية بكلمة مرور باستخدام Aspose.Cells for Node.js via C++. 
keywords: كشف حماية كلمة مرور ورقة العمل باستخدام Node.js عبر C++، تحقق مما إذا كانت ورقة العمل محمية بكلمة مرور Node.js عبر C++، Aspose.Cells for Node.js via C++
---

{{% alert color="primary" %}}

من الممكن حماية دفاتر العمل وورقات العمل بشكل منفصل. على سبيل المثال، قد تحتوي ورقة عمل على واحدة أو أكثر من أوراق العمل التي تكون محمية بكلمة مرور، ومع ذلك، قد يكون دفتر العمل محميًا أو لا. توفر واجهة برمجة تطبيقات Aspose.Cells الوسائل للكشف إذا كانت ورقة العمل محمية بكلمة مرور أم لا. يوضح هذا المقال استخدام API Aspose.Cells for Node.js via C++ لتحقيق ذلك.

{{% /alert %}}

لقد قام Aspose.Cells for Node.js via C++ بكشف خاصية [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--) للتمكن من تحديد ما إذا كانت ورقة العمل محمية بكلمة مرور أم لا. الخاصية Boolean [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--) تعيد **true** إذا كانت ورقة العمل محمية بكلمة مرور و**false** إذا لم تكن كذلك.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an instance of Workbook and load a spreadsheet
const book = new AsposeCells.Workbook(filePath);

// Access the protected Worksheet
const sheet = book.getWorksheets().get(0);

// Check if Worksheet is password protected
if (sheet.getProtection().isProtectedWithPassword()) {
console.log("Worksheet is password protected");
} else {
console.log("Worksheet is not password protected");
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
