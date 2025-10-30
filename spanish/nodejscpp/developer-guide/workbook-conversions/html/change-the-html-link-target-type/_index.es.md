---
title: Cambiar el tipo de destino del enlace HTML con Node.js mediante C++
linktitle: Cambiar el tipo de destino del enlace HTML
type: docs
weight: 320
url: /es/nodejs-cpp/change-the-html-link-target-type/
description: Aprende cómo cambiar el tipo de destino del enlace HTML usando Aspose.Cells for Node.js via C++. Controla el atributo target en tus enlaces HTML.
---

{{% alert color="primary" %}}

Aspose.Cells te permite cambiar el tipo de destino del enlace HTML. El enlace HTML luce así

{{< highlight javascript >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Como puedes ver, el atributo target en el enlace HTML anterior es **_self**. Puedes controlar este atributo target usando la propiedad [**HtmlSaveOptions.getLinkTargetType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getLinkTargetType--). Esta propiedad toma el enum [**HtmlLinkTargetType**](https://reference.aspose.com/cells/nodejs-cpp/htmllinktargettype) que tiene los siguientes valores.

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

El siguiente código ilustra el uso de la propiedad [**HtmlSaveOptions.getLinkTargetType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getLinkTargetType--). Cambia el tipo de destino del enlace a **blank**. Por defecto, es **parent**.

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
{{< app/cells/assistant language="nodejs-cpp" >}}
