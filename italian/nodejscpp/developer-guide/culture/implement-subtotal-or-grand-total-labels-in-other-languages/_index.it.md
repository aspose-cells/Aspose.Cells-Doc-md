---  
title: Implementa etichette Subtotal o Grand Total in altre lingue con Node.js via C++  
linktitle: Implementa etichette Subtotal o Grand Total in altre lingue  
type: docs  
weight: 50  
url: /it/nodejs-cpp/implement-subtotal-or-grand-total-labels-in-other-languages/  
---  

## **Possibili Scenari di Utilizzo**  

A volte vuoi mostrare etichette di subtotale e totale generale in lingue non inglesi come cinese, giapponese, arabo, Hindi, ecc. Aspose.Cells for Node.js via C++ ti permette di farlo usando la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) e la proprietà [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/). Vedi questo articolo su come usare la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings).  

- [Utilizzo della classe GlobalizationSettings per le etichette Subtotali personalizzate e altre etichette del grafico a torta](/cells/it/nodejs-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)  

## **Implementa etichette Subtotal o Grand Total in altre lingue**  

Il seguente esempio di codice carica il [file excel di esempio](5115151.xlsx) e implementa nomi di subtotale e totale generale in cinese. Consulta il [file Excel di output](5115152.xlsx) generato da questo codice come riferimento. Prima creiamo una classe di [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) e poi la usiamo nel nostro codice.  

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

Ora usa la classe creata sopra nel codice come segue:  

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

