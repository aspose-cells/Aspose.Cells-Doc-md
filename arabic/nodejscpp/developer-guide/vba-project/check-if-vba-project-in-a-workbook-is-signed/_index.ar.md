---
title: التحقق مما إذا كان مشروع VBA في مصنف موقعًا باستخدام Node.js عبر C++
linktitle: التحقق مما إذا كان مشروع VBA في كتاب عمل موقع بالتوقيع
type: docs
weight: 70
url: /ar/nodejs-cpp/check-if-vba-project-in-a-workbook-is-signed/
description: تعلم كيفية التحقق مما إذا كان مشروع VBA في مصنف موقعًا باستخدام Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

يمكنك التحقق مما إذا كان مشروع VBA الخاص بك موقع بالتوقيع أم لا باستخدام Microsoft Excel عبر أمر القائمة **Tools > Digital Signatures...**. على نفس النحو، يمكنك التحقق منه برمجيًا باستخدام خاصية Aspose.Cells [**Workbook.getVbaProject()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getVbaProject--).

{{% /alert %}}

## **التحقق مما إذا كان مشروع VBA في مصنف موقعًا في Node.js**

يحمّل الكود التالي دفتر العمل ويفحص ما إذا كان مشروع VBA الخاص به موقعًا باستخدام الخاصية [**Workbook.getVbaProject()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getVbaProject--). ستُرجع الخاصية **true** إذا كان المشروع موقعًا، وإلا ستُرجع **false**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
console.log("VBA Project is Signed: " + workbook.getVbaProject().isSigned());
```
