---
title: Convertir un classeur Excel en Ods, Sxc et Fods (OpenOffice / LibreOffice Calc) via Node.js
linktitle: Ods
type: docs
weight: 20
url: /fr/nodejs-cpp/convert-excel-to-ods/
description: Comment convertir Excel en Ods (OpenOffice / LibreOffice Calc) ou convertir Ods (OpenOffice / LibreOffice Calc) en Excel avec Aspose.Cells for Node.js via C++.
---

## **À propos du format OpenDocument**
Le [format OpenDocument (ODF)](https://en.wikipedia.org/wiki/OpenDocument) est un format de fichier gratuit et ouvert pour les documents de bureau électroniques initialement développé par Sun pour la suite Open Office. OpenDocument Spreadsheet (ODS) est le format de fichier pour les documents Excel. OpenDocument est actuellement une norme OASIS et ISO.

## **Convertir Ods (OpenOffice / LibreOffice calc) en Excel**
Aspose.Cells for Node.js via C++ supporte le chargement d’Ods, Sxc et Fods, pris en charge par OpenOffice / LibreOffice Calc, et convertir [Ods](book1.ods), [Sxc](book1.sxc) et [Fods](book1.fods) en fichiers Excel.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load Excel workbook
const excelFilePath = path.join(__dirname, "book1.xlsx");
let workbook = new AsposeCells.Workbook(excelFilePath);

// Save as ods file
workbook.save("ods_out.ods");

// Save as sxc file
workbook.save("sxc_out.sxc");

// Save as fods file
workbook.save("fods_out.fods");
```

## **Convertir Excel en Ods (OpenOffice / LibreOffice Calc)**
Aspose.Cells for Node.js via C++ supporte la conversion de fichiers Excel en fichiers Ods, Sxc et Fods. L’exemple de code ci-dessous montre comment convertir le [modèle](book1.xlsx) en fichiers Ods, Sxc et Fods.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath1 = path.join(dataDir, "book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath1);
// Save as ods file 
workbook.save("Out.ods");
// Save as sxc file 
workbook.save("Out.sxc");
// Save as fods file 
workbook.save("Out.fods");
```

## **Sujets avancés**
- [Enregistrer un fichier ODS selon les spécifications ODF 1.1 et 1.2.](/cells/fr/nodejs-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/)
- [Travailler avec l'arrière-plan dans les fichiers ODS](/cells/fr/nodejs-cpp/working-with-background-in-ods-files/)
{{< app/cells/assistant language="nodejs-cpp" >}}
