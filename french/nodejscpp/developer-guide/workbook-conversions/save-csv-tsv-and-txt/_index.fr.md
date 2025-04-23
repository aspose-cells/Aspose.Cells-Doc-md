---
title: Convertir Excel en CSV, TSV et Txt avec Node.js via C++
linktitle: Enregistrer en CSV, TSV et Txt
type: docs
weight: 40
url: /fr/nodejs-cpp/convert-excel-to-csv-tsv-and-txt/
description: Apprenez comment convertir des fichiers Excel en formats CSV, TSV, et TXT en utilisant Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Aspose.Cells permet de convertir des fichiers Excel, ODS, JSON, et autres formats en CSV, TSV, et TXT.

{{% /alert %}}

## **Enregistrer le classeur au format texte ou CSV**

Parfois, vous souhaitez convertir ou enregistrer un classeur avec plusieurs feuilles de calcul au format texte. Pour les formats texte (par exemple TXT, TabDelim, CSV, etc.), par défaut, Microsoft Excel et Aspose.Cells enregistrent uniquement le contenu de la feuille active.

L’exemple de code suivant explique comment sauvegarder l’intégralité du classeur au format texte. Chargez le classeur source, qui peut être n’importe quel fichier de feuille de calcul Microsoft Excel ou OpenOffice (XLS, XLSX, XLSM, XLSB, ODS, etc.) avec n’importe quel nombre de feuilles.

Lorsque le code est exécuté, il convertit les données de toutes les feuilles du classeur au format TXT

Vous pouvez modifier le même exemple pour enregistrer votre fichier au format CSV. Par défaut, [**TxtSaveOptions.getSeparator()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getSeparator--) est une virgule, alors ne spécifiez pas de séparateur si vous enregistrez au format CSV.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Text save options. You can use any type of separator
const opts = new AsposeCells.TxtSaveOptions();
opts.setSeparator('\t');
opts.setExportAllSheets(true);

// Save entire workbook data into file
workbook.save(path.join(dataDir, "out.txt"), opts);
```

## **Enregistrement de fichiers texte avec séparateur personnalisé**

Les fichiers texte contiennent des données de feuille de calcul sans mise en forme. Le fichier est un type de fichier texte brut qui peut avoir des délimiteurs personnalisés entre ses données

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath);

// Instantiate Text File's Save Options
const options = new AsposeCells.TxtSaveOptions();

// Specify the separator
options.setSeparator(";");

// Save the file with the options
wb.save(path.join(dataDir, "output.csv"), options);
```


## **Sujets avancés**
- [Conserver les séparateurs pour les lignes vides lors de l'exportation de feuilles de calcul au format CSV](/cells/fr/nodejs-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Supprimer les lignes et colonnes vides en tête lors de l'exportation de feuilles de calcul au format CSV](/cells/fr/nodejs-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
