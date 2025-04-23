---
title: Node.js kullanarak HTML Bağlantı Hedef Türünü Değiştirin  C++
linktitle: HTML Bağlantısı Hedef Türünü Değiştirme
type: docs
weight: 320
url: /tr/nodejs-cpp/change-the-html-link-target-type/
description: Aspose.Cells for Node.js via C++ kullanarak HTML bağlantısının hedef türünü nasıl değiştireceğinizi öğrenin. HTML bağlantılarındaki hedef özniteliğini kontrol edin.
---

{{% alert color="primary" %}}

Aspose.Cells, HTML bağlantı hedef türünü değiştirmenize olanak tanır. HTML bağlantısı şuna benzer

{{< highlight javascript >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Yukarıdaki HTML bağlantısında hedef özniteliği **_self**. Bu hedef özniteliğini [**HtmlSaveOptions.getLinkTargetType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getLinkTargetType--) özelliği ile kontrol edebilirsiniz. Bu özellik, aşağıdaki değerleri alan [**HtmlLinkTargetType**](https://reference.aspose.com/cells/nodejs-cpp/htmllinktargettype) enum'ünü kabul eder.

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

Aşağıdaki kod [**HtmlSaveOptions.getLinkTargetType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getLinkTargetType--) özelliğinin kullanımını gösterir. Bağlantı hedef türünü **blank** yapar. Varsayılan ise **parent**.

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
