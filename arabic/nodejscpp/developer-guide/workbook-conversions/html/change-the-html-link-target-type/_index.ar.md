---
title: تغيير نوع هدف رابط HTML باستخدام Node.js عبر C++
linktitle: تغيير نوع الوجهة للرابط HTML
type: docs
weight: 320
url: /ar/nodejs-cpp/change-the-html-link-target-type/
description: تعرف على كيفية تغيير نوع هدف رابط HTML باستخدام Aspose.Cells for Node.js via C++. السيطرة على خاصية target في روابط HTML الخاصة بك.
---

{{% alert color="primary" %}}

تُتيح Aspose.Cells لك تغيير نوع الوجهة للرابط HTML. يبدو الرابط HTML على النحو التالي

{{< highlight javascript >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

كما ترى، خاصية target في الرابط HTML أعلاه هي **_self**. يمكنك التحكم في هذه الخاصية باستخدام الخاصية [**HtmlSaveOptions.getLinkTargetType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getLinkTargetType--). تأخذ هذه الخاصية في التقدير قيمة [**HtmlLinkTargetType**](https://reference.aspose.com/cells/nodejs-cpp/htmllinktargettype) من enum التي تحتوي على القيم التالية.

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

يوضح الرمز التالي استخدام الخاصية [**HtmlSaveOptions.getLinkTargetType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getLinkTargetType--). يغير نوع هدف الرابط إلى **blank**. بشكل افتراضي، يكون **parent**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Sample1.xlsx");
const outputPath = path.join(dataDir, "Output.out.html");

const workbook = new AsposeCells.Workbook(inputPath);

const opts = new AsposeCells.HtmlSaveOptions();
opts.setLinkTargetType(AsposeCells.HtmlLinkTargetType.Self);

workbook.save(outputPath, opts);
console.log(`File saved: ${outputPath}`);
```
