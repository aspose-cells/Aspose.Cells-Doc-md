---  
title: Définir la bordure de la plage avec Node.js via C++  
linktitle: Définir la bordure de la plage  
type: docs  
weight: 600  
url: /fr/nodejs-cpp/set-range-border/  
---  

## **Scénarios d'utilisation possibles**  
Lorsque vous souhaitez définir la bordure d'une plage, vous n'avez pas besoin de définir chaque cellule individuellement. Vous pouvez définir la bordure sur la plage. Aspose.Cells for Node.js via C++ propose cette fonctionnalité.  
Cet article fournit un code d'exemple utilisant Aspose.Cells for Node.js via C++ pour définir la bordure d'une plage.  

## **Définir la bordure de la plage dans Excel**  
Pour définir la bordure d'une plage dans Excel, vous pouvez suivre ces étapes :  
1. Sélectionnez la plage de cellules sur laquelle vous souhaitez appliquer la bordure.  
2. Dans l'onglet « Accueil » du ruban, localisez le groupe « Police ».  
3. Dans le groupe « Police », cliquez sur le bouton déroulant « Bordures ».  
<br>  
<img src="border.png" />  
4. Choisissez le type de bordure que vous souhaitez appliquer parmi les options du menu déroulant. Vous pouvez choisir parmi les styles de bordure prédéfinis ou personnaliser votre propre bordure.  
5. Une fois que vous avez sélectionné le style de bordure souhaité, la bordure sera appliquée à la plage de cellules sélectionnée.  

## **Définir la bordure d'une plage en utilisant Aspose.Cells for Node.js via C++**  
Cet exemple montre comment :  

1. Créer un classeur.  
2. Ajouter des données aux cellules de la première feuille de calcul.  
3. Créer un [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range).  
4. Définir la bordure intérieure de la plage.  
5. Définir la bordure extérieure de la plage.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Obtaining the reference of the newly added worksheet
const ws = workbook.getWorksheets().get(0);
const cells = ws.getCells();

// Setting the value to the cells
let cell = cells.get("A1");
cell.putValue("Fruit");
cell = cells.get("B1");
cell.putValue("Count");
cell = cells.get("C1");
cell.putValue("Price");

cell = cells.get("A2");
cell.putValue("Apple");
cell = cells.get("A3");
cell.putValue("Mango");
cell = cells.get("A4");
cell.putValue("Blackberry");
cell = cells.get("A5");
cell.putValue("Cherry");

cell = cells.get("B2");
cell.putValue(5);
cell = cells.get("B3");
cell.putValue(3);
cell = cells.get("B4");
cell.putValue(6);
cell = cells.get("B5");
cell.putValue(4);

cell = cells.get("C2");
cell.putValue(5);
cell = cells.get("C3");
cell.putValue(20);
cell = cells.get("C4");
cell.putValue(30);
cell = cells.get("C5");
cell.putValue(60);

// Create a range (A1:C5).
const range = cells.createRange("A1", "C5");

// set inner border of range
const innerColor = workbook.createCellsColor();
innerColor.setColor(AsposeCells.Color.Red);
range.setInsideBorders(AsposeCells.BorderType.Vertical, AsposeCells.CellBorderType.Thin, innerColor);
innerColor.setColor(AsposeCells.Color.Green);
range.setInsideBorders(AsposeCells.BorderType.Horizontal, AsposeCells.CellBorderType.Thin, innerColor);

// set outer border of range
const outerColor = workbook.createCellsColor();
outerColor.setColor(AsposeCells.Color.Blue);
range.setOutlineBorders(AsposeCells.CellBorderType.Thin, outerColor);

workbook.save("out.xlsx");
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
