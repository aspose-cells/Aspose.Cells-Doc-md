---
title: Ändern Sie den Link Target Typ im HTML mit Node.js über C++
linktitle: Ändern Sie den HTML Linkzieltyp
type: docs
weight: 320
url: /de/nodejs-cpp/change-the-html-link-target-type/
description: Erfahren Sie, wie Sie den Ziel Attribut im HTML Link mit Aspose.Cells for Node.js via C++ ändern. Kontrollieren Sie das target Attribut in Ihren HTML Links.
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, den Typ des HTML-Links zu ändern. Ein HTML-Link sieht so aus

{{< highlight javascript >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

 Wie Sie sehen, ist das target-Attribut im oben genannten HTML-Link **_self**. Sie können dieses Zielattribut mit der Eigenschaft [**HtmlSaveOptions.getLinkTargetType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getLinkTargetType--) steuern. Diese Eigenschaft nimmt den [**HtmlLinkTargetType**](https://reference.aspose.com/cells/nodejs-cpp/htmllinktargettype)-Enum-Wert an, der die folgenden Werte hat.

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

 Der folgende Code zeigt die Verwendung der [**HtmlSaveOptions.getLinkTargetType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getLinkTargetType--)-Eigenschaft. Er ändert den Link-Target-Typ zu **blank**. Standardmäßig ist es **parent**.

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
