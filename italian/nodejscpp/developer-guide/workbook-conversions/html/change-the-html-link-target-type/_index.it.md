---
title: Modifica il tipo di destinazione del link HTML con Node.js tramite C++
linktitle: Modifica il Tipo di Destinazione del Link HTML
type: docs
weight: 320
url: /it/nodejs-cpp/change-the-html-link-target-type/
description: Scopri come cambiare il tipo di destinazione del link HTML usando Aspose.Cells for Node.js via C++. Controlla l attributo target nei tuoi link HTML.
---

{{% alert color="primary" %}}

Aspose.Cells ti permette di cambiare il tipo di destinazione del link HTML. Il link HTML appare così

{{< highlight javascript >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Come puoi vedere, l'attributo target nel link HTML sopra è **_self**. Puoi controllare questo attributo target usando la proprietà [**HtmlSaveOptions.getLinkTargetType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getLinkTargetType--). Questa proprietà accetta l'enumerazione [**HtmlLinkTargetType**](https://reference.aspose.com/cells/nodejs-cpp/htmllinktargettype), che ha i seguenti valori.

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

Il codice seguente illustra l'uso della proprietà [**HtmlSaveOptions.getLinkTargetType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getLinkTargetType--). Cambia il tipo di destinazione del link in **blank**. Di default, è **parent**.

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
