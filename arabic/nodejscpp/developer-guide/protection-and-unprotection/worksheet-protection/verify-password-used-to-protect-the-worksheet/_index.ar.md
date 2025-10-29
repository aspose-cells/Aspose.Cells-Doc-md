---
title: التحقق من كلمة المرور المستخدمة لحماية ورقة العمل مع Node.js عبر C++
linktitle: التحقق من الكلمة المستخدمة لحماية ورقة العمل
type: docs
weight: 370
url: /ar/nodejs-cpp/verify-password-used-to-protect-the-worksheet/
description: تعلم كيفية التحقق من كلمة المرور المستخدمة لحماية ورقة العمل باستخدام Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

قامت واجهات برمجة تطبيقات Aspose.Cells بتحسين فئة [**Protection**](https://reference.aspose.com/cells/nodejs-cpp/protection) من خلال تقديم بعض الخصائص والطرق المفيدة. أحد هذه الطرق هو [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-) الذي يسمح بتحديد كلمة مرور كمثال على *السلسلة* ويقوم بالتحقق مما إذا تم استخدام نفس كلمة المرور لحماية [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

{{% /alert %}}

ترجع طريقة [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-) **true** إذا كانت كلمة المرور المحددة تتطابق مع كلمة المرور المستخدمة لحماية ورقة العمل المعطاة، وتُرجع **false** إذا لم تتطابق. يستخدم الكود التالي طريقة [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-) مع الخاصية [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--) لاكتشاف حماية بكلمة مرور والتحقق من كلمة المرور.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample.xlsx");
// Create an instance of Workbook and load a spreadsheet
const workbook = new AsposeCells.Workbook(filePath);

// Access the protected Worksheet
const sheet = workbook.getWorksheets().get(0);

// Check if Worksheet is password protected
if (sheet.getProtection().isProtectedWithPassword()) {
// Verify the password used to protect the Worksheet
if (sheet.getProtection().verifyPassword("1234")) {
console.log("Specified password has matched");
} else {
console.log("Specified password has not matched");
}
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
