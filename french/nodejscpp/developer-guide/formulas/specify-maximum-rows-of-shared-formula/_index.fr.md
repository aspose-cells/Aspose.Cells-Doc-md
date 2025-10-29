---  
title: Spécifier le nombre maximum de lignes pour la formule partagée avec Node.js via C++  
linktitle: Spécifier le nombre maximum de lignes de formule partagée  
type: docs  
weight: 40  
url: /fr/nodejs-cpp/specify-maximum-rows-of-shared-formula/  
description: Apprenez comment spécifier le nombre maximum de lignes pour les formules partagées en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  

La valeur maximale par défaut pour le nombre de lignes dans une formule partagée est 64. Elle peut être n'importe quel nombre, par exemple elle peut être 1000. La performance d'une formule partagée varie en fonction du nombre de lignes. Par conséquent, Aspose.Cells propose la propriété [**WorkbookSettings.getMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRowsOfSharedFormula--) qui peut être utilisée pour spécifier le nombre maximum de lignes de la formule partagée. La formule partagée sera divisée en plusieurs formules partagées si le total de lignes de la formule dépasse cette valeur, comme illustré dans la capture d'écran suivante.  

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)  

## **Spécifier le nombre maximum de lignes de formule partagée**  

Le code d'exemple suivant explique l'utilisation de la propriété [**WorkbookSettings.getMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRowsOfSharedFormula--). Il définit le nombre maximum de lignes de la formule partagée à 5, ajoute la formule partagée en D1 pour 100 lignes, puis enregistre dans [fichier Excel de sortie](61767856.xlsx). Si vous extrayez le contenu du fichier Excel de sortie et consultez *sheet1.xml*, vous verrez la formule partagée se diviser après chaque 5 lignes, comme indiqué dans la capture d'écran ci-dessus.  

## **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create a new workbook
const wb = new AsposeCells.Workbook();

// Set the max rows of shared formula to 5
wb.getSettings().setMaxRowsOfSharedFormula(5);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell D1
const cell = ws.getCells().get("D1");

// Set the shared formula in 100 rows
cell.setSharedFormula("=Sum(A1:A2)", 100, 1);

// Save the output Excel file
wb.save("outputSpecifyMaximumRowsOfSharedFormula.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
