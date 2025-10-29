---
title: Modifier le type de cible du lien HTML avec Node.js via C++
linktitle: Changer le type de lien HTML cible
type: docs
weight: 320
url: /fr/nodejs-cpp/change-the-html-link-target-type/
description: Apprenez comment changer le type de cible du lien HTML en utilisant Aspose.Cells for Node.js via C++. Contrôlez l attribut target dans vos liens HTML.
---

{{% alert color="primary" %}}

Aspose.Cells vous permet de changer le type de lien HTML cible. Le lien HTML ressemble à ceci

{{< highlight javascript >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Comme vous pouvez le voir, l'attribut target dans le lien HTML ci-dessus est **_self**. Vous pouvez contrôler cet attribut target en utilisant la propriété [**HtmlSaveOptions.getLinkTargetType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getLinkTargetType--). Cette propriété accepte l'énumération [**HtmlLinkTargetType**](https://reference.aspose.com/cells/nodejs-cpp/htmllinktargettype) qui possède les valeurs suivantes.

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

Le code suivant illustre l'utilisation de la propriété [**HtmlSaveOptions.getLinkTargetType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getLinkTargetType--). Il change le type de cible du lien en **blank**. Par défaut, il est **parent**.

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
