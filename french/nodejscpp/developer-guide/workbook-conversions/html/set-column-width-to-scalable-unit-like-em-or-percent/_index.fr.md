---
title: Définir la largeur de la colonne en unité évolutive comme em ou pourcentage avec Node.js via C++
linktitle: Définir la largeur de la colonne en unité évolutive comme em ou pourcentage
type: docs
weight: 130
url: /fr/nodejs-cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Apprenez comment définir la largeur de colonne en unités évolutives comme em ou en pourcentage en Aspose.Cells for Node.js via C++. Améliorez la présentation des tableaux HTML générés.
---

Générer un fichier HTML à partir d'une feuille de calcul est très courant. La taille des colonnes est définie en "pt," ce qui fonctionne dans de nombreux cas. Cependant, il peut arriver que cette taille fixe ne soit pas souhaitée. Par exemple, si la largeur du panneau conteneur est de 600px, où cette page HTML s’affiche, vous pouvez obtenir une barre de défilement horizontale si la largeur du tableau généré est plus grande. Il était nécessaire que cette taille fixe soit remplacée par une unité évolutive comme em ou pourcentage pour une meilleure présentation. Le code d'exemple suivant peut être utilisé où [**HtmlSaveOptions.getWidthScalable()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getWidthScalable--) est défini à **true** pour créer une largeur évolutive.

Le fichier source d'exemple et les fichiers de sortie peuvent être téléchargés à partir des liens suivants:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample source file
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleForScalableColumns.xlsx");
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Specify Html Save Options
const options = new AsposeCells.HtmlSaveOptions();

// Set the property for scalable width
options.setWidthScalable(true);

// Specify image save format
options.setExportImagesAsBase64(true);

// Save the workbook in Html format with specified Html Save Options
const outputFilePath = path.join(dataDir, "outsampleForScalableColumns.html");
workbook.save(outputFilePath, options);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
