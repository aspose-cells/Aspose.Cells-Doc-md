---
title: Désactiver l exportation des scripts de cadres et des propriétés du document avec Node.js via C++
linktitle: Désactiver l exportation des scripts de trame et des propriétés du document
type: docs
weight: 310
url: /fr/nodejs-cpp/disable-exporting-frame-scripts-and-document-properties/
description: Apprenez comment désactiver l exportation des scripts de cadres et des propriétés du document lors de la conversion d un classeur en HTML en utilisant Aspose.Cells for Node.js via C++.
--- 

{{% alert color="primary" %}}

Aspose.Cells exporte les scripts de cadres et les propriétés du document lors de la conversion d'un classeur en HTML. La version 8.6.0 de Aspose.Cells for Node.js via C++ introduit une option permettant de désactiver l'exportation optionnelle des scripts de cadres et des propriétés du document. Veuillez utiliser la propriété `HtmlSaveOptions.exportFrameScriptsAndProperties` pour désactiver l'export.

{{% /alert %}}

## **Désactiver l'exportation des scripts de trame et des propriétés du document**

Le code d'exemple suivant vous permet de désactiver l'exportation des scripts de trame et des propriétés du document. Une fois que vous avez converti un classeur en HTML, le fichier de sortie ne contiendra aucun script de trame et aucune propriété du document.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the required workbook to convert
const filePath = path.join(dataDir, "Sample1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Disable exporting frame scripts and document properties
const options = new AsposeCells.HtmlSaveOptions();
options.setExportFrameScriptsAndProperties(false);

// Save workbook as HTML
workbook.save(path.join(dataDir, "output.out.html"), options);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
