---
title: Empêcher l exportation du contenu des feuilles masquées lors de l enregistrement en HTML avec Node.js via C++
linktitle: Empêcher l exportation du contenu de la feuille de calcul masqué lors de l enregistrement en HTML
type: docs
weight: 210
url: /fr/nodejs-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Apprenez comment empêcher l exportation du contenu des feuilles masquées lors de la sauvegarde de fichiers Excel en HTML en utilisant Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Vous pouvez enregistrer des classeurs Excel en HTML. Cependant, si le classeur contient des feuilles de calcul masquées, Aspose.Cells exporte par défaut le contenu des feuilles de calcul masquées dans le répertoire de sortie HTML (_files) qui contient des fichiers tels que des feuilles de calcul, des images, tabstrip.htm, stylesheet.css, etc. Parfois, exporter le contenu des feuilles de calcul masquées de cette manière n'est pas approprié. Par exemple, si la feuille de calcul masquée contient des images qui ne doivent pas être exportées dans le répertoire _files.

{{% /alert %}}

Aspose.Cells for Node.js via C++ fournit la propriété [**HtmlSaveOptions.getExportHiddenWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportHiddenWorksheet--). Par défaut, elle est définie à **true** et les feuilles masquées sont exportées en HTML. Si vous la définissez à **false**, Aspose.Cells n'exportera pas le contenu des feuilles masquées.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "WorkbookWithHiddenContent.xlsx"));

// Do not export hidden worksheet contents
const options = new AsposeCells.HtmlSaveOptions();
options.setExportHiddenWorksheet(false);

// Save the workbook
workbook.save(path.join(dataDir, "HtmlWithoutHiddenContent_out.html"), options);
```

