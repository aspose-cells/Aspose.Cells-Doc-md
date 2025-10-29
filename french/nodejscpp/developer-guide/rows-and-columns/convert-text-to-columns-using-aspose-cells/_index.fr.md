---  
title: Convertir du texte en colonnes en utilisant Aspose.Cells for Node.js via C++  
linktitle: Convertir le texte en colonnes  
type: docs  
weight: 30  
url: /fr/nodejs-cpp/convert-text-to-columns-using-aspose-cells/  
description: Apprenez à convertir du texte en colonnes dans Excel en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  

Vous pouvez convertir votre texte en colonnes en utilisant Microsoft Excel. Cette fonctionnalité est disponible dans *Outils de données* sous l’onglet *Données*. Pour diviser le contenu d’une colonne en plusieurs colonnes, les données doivent contenir un délimiteur spécifique tel qu’une virgule (ou tout autre caractère) selon lequel Microsoft Excel divise le contenu d’une cellule en plusieurs cellules. Aspose.Cells for Node.js via C++ propose également cette fonctionnalité via [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-).  

## **Convertir du texte en colonnes en utilisant Aspose.Cells for Node.js via C++**  

Le code d’exemple suivant explique l’utilisation de la méthode [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-). Le code commence par ajouter des noms de personnes dans la colonne A de la première feuille de calcul. Le prénom et le nom de famille sont séparés par un espace. Ensuite, il applique la méthode [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-) sur la colonne A et l’enregistre en tant que fichier Excel de sortie. Si vous ouvrez le [fichier Excel de sortie](25395213.xlsx), vous verrez que les prénoms sont dans la colonne A tandis que les noms de famille sont dans la colonne B, comme illustré dans cette capture d’écran.  

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)  

## **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create a workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Add people name in column A. First name and last name are separated by space.
ws.getCells().get("A1").putValue("John Teal");
ws.getCells().get("A2").putValue("Peter Graham");
ws.getCells().get("A3").putValue("Brady Cortez");
ws.getCells().get("A4").putValue("Mack Nick");
ws.getCells().get("A5").putValue("Hsu Lee");

// Create text load options with space as separator.
const opts = new AsposeCells.TxtLoadOptions();
opts.setSeparator(' ');

// Split the column A into two columns using TextToColumns() method.
// Now column A will have first name and column B will have second name.
ws.getCells().textToColumns(0, 0, 5, opts);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputTextToColumns.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
