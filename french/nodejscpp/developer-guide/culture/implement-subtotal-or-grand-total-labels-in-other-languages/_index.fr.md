---  
title: Implémentez les étiquettes de sous totaux ou de totaux généraux dans d autres langues avec Node.js via C++  
linktitle: Implémentez les étiquettes de sous totaux ou de totaux généraux dans d autres langues  
type: docs  
weight: 50  
url: /fr/nodejs-cpp/implement-subtotal-or-grand-total-labels-in-other-languages/  
---  

## **Scénarios d'utilisation possibles**  

Parfois, vous souhaitez afficher les étiquettes de sous-totaux et de totaux généraux dans des langues autres que l'anglais, comme le chinois, le japonais, l'arabe, l'hindi, etc. Aspose.Cells for Node.js via C++ vous permet de faire cela en utilisant la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) et la propriété [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/). Veuillez consulter cet article pour savoir comment utiliser la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings).  

- [Utilisation de la classe GlobalizationSettings pour des étiquettes de sous-total personnalisées et d'autres étiquettes du graphique circulaire](/cells/fr/nodejs-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)  

## **Implémentez les étiquettes de sous-totaux ou de totaux généraux dans d'autres langues**  

Le code d'exemple suivant charge le fichier Excel [exemple](5115151.xlsx) et implémente des noms de sous-totaux et de totaux dans la langue chinoise. Veuillez consulter le fichier Excel [de sortie](5115152.xlsx) généré par ce code pour référence. Nous créons d'abord une classe de [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) puis l'utilisons dans notre code.  

```javascript
const AsposeCells = require("aspose.cells.node");

class GlobalizationSettingsImp extends AsposeCells.GlobalizationSettings {
// This function will return the sub total name
getTotalName(functionType) {
return "Chinese Total - 可能的用法";
}

// This function will return the grand total name
getGrandTotalName(functionType) {
return "Chinese Grand Total - 可能的用法";
}
}
```  

Utilisez la classe ci-dessus dans le code comme suit :  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Set the globalization setting to change subtotal and grand total names
const globalizationSettings = new AsposeCells.GlobalizationSettings();
workbook.getSettings().setGlobalizationSettings(globalizationSettings);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Apply subtotal on A1:B10
const cellArea = AsposeCells.CellArea.createCellArea("A1", "B10");
worksheet.getCells().subtotal(cellArea, 0, AsposeCells.ConsolidationFunction.Sum, [2, 3, 4]);

// Set the width of the first column
worksheet.getCells().setColumnWidth(0, 40);

// Save the output excel file
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

