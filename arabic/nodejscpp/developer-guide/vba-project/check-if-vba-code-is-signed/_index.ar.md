---
title: تحقق مما إذا كان رمز VBA موقعًا باستخدام Node.js عبر C++
linktitle: التحقق مما إذا كان كود VBA موقع بالتوقيع
type: docs
weight: 100
url: /ar/nodejs-cpp/check-if-vba-code-is-signed/
description: تعلم كيفية التحقق مما إذا كان مشروع رمز VBA موقعًا باستخدام Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

يتيح Aspose.Cells للمستخدم التحقق مما إذا كان مشروع كود VBA موقع بالتوقيع أم لا. يرجى استخدام خاصية [**VbaProject.isSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isSigned--) للتحقق مما إذا كان مشروع كود VBA موقع بالتوقيع أم لا.

{{% /alert %}}

 يوضح الرمز التالي كيفية التحقق مما إذا كان رمز VBA موقعًا أم لا باستخدام خاصية [**VbaProject.isSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isSigned--). يمكنك استخدام أي من ملفات Excel الخاصة بك لاختبار هذا الرمز. للاختبار، يمكنك استخدام [ملف Excel هذا المستخدم في الكود](5115032.xlsm).

## **التحقق مما إذا كان رمز VBA موقعًا في Node.js**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleVBAProjectSigned.xlsm");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

console.log("Is VBA Code Project Signed: " + workbook.getVbaProject().isSigned());
```

## مخرج الكونسول

أدناه مخرج الكونسول للكود أعلاه باستخدام [ملف Excel عينة](5115032.xlsm) المقدم من خلال الرابط.

{{< highlight java >}}

Is VBA Code Project Signed: True

{{< /highlight >}}
