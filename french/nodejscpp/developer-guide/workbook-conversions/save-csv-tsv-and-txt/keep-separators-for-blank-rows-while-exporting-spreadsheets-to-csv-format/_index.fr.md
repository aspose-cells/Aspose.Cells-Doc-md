---  
title: Garder les séparateurs pour les lignes vides lors de l exportation de feuilles de calcul en format CSV avec Node.js via C++  
linktitle: Conserver les séparateurs pour les lignes vides lors de l exportation de feuilles de calcul au format CSV  
type: docs  
weight: 160  
url: /fr/nodejs-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/  
---  

## **Conserver les séparateurs pour les lignes vides lors de l'exportation de feuilles de calcul au format CSV**  

Aspose.Cells offre la possibilité de conserver les séparateurs de ligne lors de la conversion de feuilles de calcul en format CSV. Pour cela, vous pouvez utiliser la propriété [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) de [**TxtSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/). [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) est une propriété booléenne. Pour garder les séparateurs pour les lignes vides lors de la conversion du fichier Excel en CSV, définissez la propriété [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) à **true**.  

Le code d'exemple suivant charge le [fichier Excel source](84378743.xlsx). Il définit la propriété [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) à **true** et le sauvegarde en tant que [output.csv](84378744.csv). La capture d'écran montre la comparaison entre le fichier Excel source, la sortie par défaut générée lors de la conversion en CSV, et la sortie générée en définissant [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) à **true**.  

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)  

## **Code d'exemple**  

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

// Set KeepSeparatorsForBlankRow to true to show separators in blank rows
options.setKeepSeparatorsForBlankRow(true);

// Save the file with the options
wb.save(path.join(dataDir, "output.csv"), options);
```  

