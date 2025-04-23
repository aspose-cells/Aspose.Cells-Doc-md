---
title: Ajuster automatiquement la hauteur de la ligne lors du chargement du fichier avec Node.js via C++
linktitle: Ajuster automatiquement la hauteur de la ligne lorsque le fichier est chargé
type: docs
weight: 120
url: /fr/nodejs-cpp/autofit-row-height/
description: Apprenez comment ajuster la hauteur des lignes dont la hauteur n est pas personnalisée lors du chargement d un fichier avec Aspose.Cells for Node.js via C++.
keywords: Ajuster automatiquement la hauteur de la ligne lors du chargement du fichier Node.js via C++, en ajustant automatiquement la hauteur de la ligne lors de l ouverture d un fichier Excel. 
---

## **Scénarios d'utilisation possibles**
La hauteur de la ligne s'ajuste automatiquement pour correspondre à la police du contenu, mais lorsque la hauteur de la ligne mise en cache ne correspond pas à la hauteur du contenu dans le fichier, MS Excel ajuste automatiquement la hauteur de la ligne lors du chargement du fichier, tandis que Aspose.Cells for Node.js via C++ ne l'ajuste pas automatiquement pour améliorer les performances. Si vous souhaitez utiliser le programme Aspose.Cells pour ajuster automatiquement la hauteur des lignes lors du chargement, vous pouvez y parvenir via le paramètre [setAutoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setAutoFitterOptions-autofitteroptions-) dans votre code.

Veuillez vous référer à l'image suivante. Nous pouvons observer que la hauteur de la ligne en ligne 11 est de 15, mais Excel a automatiquement ajusté la hauteur de la ligne lors du chargement du fichier.
<br>
<img src="1.png" width=70% />

## **Ajuster la hauteur des lignes en utilisant Aspose.Cells for Node.js via C++**
Si vous chargez directement le fichier et l'enregistrez au format PDF, les données ne seront pas entièrement affichées dans le PDF parce que sa hauteur de ligne mise en cache n'est que de 15.
<br>
<img src="2.png" width=70% />
<br>
Si vous définissez le paramètre [setAutoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setAutoFitterOptions-autofitteroptions-) sur true lors du chargement du fichier, alors Aspose.Cells ajustera automatiquement la hauteur des lignes. La hauteur de ligne ajustée peut répondre efficacement aux exigences d'affichage du texte.
<br>
<img src="3.png" width=70% />

## **Code d'exemple Node.js**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
workbook.save(path.join(dataDir, "out.pdf"));

const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setAutoFitterOptions(new AsposeCells.AutoFitterOptions());
loadOptions.getAutoFitterOptions().setOnlyAuto(true);
const book = new AsposeCells.Workbook(filePath, loadOptions);
book.save(path.join(dataDir, "out2.pdf"));
```
