---
title: إطلاق الموارد غير المُدارة من دفتر العمل باستخدام Node.js عبر C++
linktitle: تحرير الموارد غير المُدارة لدفتر العمل
type: docs
weight: 310
url: /ar/nodejs-cpp/release-unmanaged-resources-of-the-workbook/
description: تعلّم كيفية تحرير الموارد غير المُدارة لعنصر دفتر العمل باستخدام Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

يقدم Aspose.Cells طريقة [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--) لتحرير الموارد غير المُدارة لكائن [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). يُستخدم نمط التدمير فقط للكائنات التي تصل إلى موارد غير مُدارة، مثل مؤشرات الملفات والأنابيب وقيم السجل ومفاتيح الانتظار أو مؤشرات لكتل الذاكرة غير المُدارة. ويعود ذلك إلى كفاءة جامع القمامة في استرداد الكائنات المُدارة غير المستخدمة، ولكنه غير قادر على استرداد الأوائل غير المُدارة.

{{% /alert %}}

الكيان [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) الآن يطبق واجهة *System.IDisposable* التي تحتوي على طريقة واحدة [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--). يمكنك إما استدعاء طريقة [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--) مباشرة أو استخدام عبارة *Using* لاستدعاء هذه الطريقة تلقائيًا.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create workbook object
const wb1 = new AsposeCells.Workbook();

// Call Dispose method
wb1.dispose();

// Call Dispose method via a scoped approach
(async () => {
const wb2 = new AsposeCells.Workbook();
// Any other code goes here
wb2.dispose();
})();
```
{{< app/cells/assistant language="nodejs-cpp" >}}
