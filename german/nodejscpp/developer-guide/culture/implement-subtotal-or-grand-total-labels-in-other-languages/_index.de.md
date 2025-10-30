---  
title: Implementieren Sie Subtotal oder Gesamtsummen Labels in anderen Sprachen mit Node.js über C++  
linktitle: Implementieren Sie Subtotal oder Gesamtsummen Labels in anderen Sprachen  
type: docs  
weight: 50  
url: /de/nodejs-cpp/implement-subtotal-or-grand-total-labels-in-other-languages/  
---  

## **Mögliche Verwendungsszenarien**  

Manchmal möchten Sie Subtotal- und Gesamtsummen-Labels in nicht-englischen Sprachen wie Chinesisch, Japanisch, Arabisch, Hindi usw. anzeigen. Aspose.Cells for Node.js via C++ ermöglicht dies mit der [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)-Klasse und der [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/)-Eigenschaft. Bitte lesen Sie diesen Artikel, um zu erfahren, wie man die [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)-Klasse nutzt.  

- [Verwendung der GlobalizationSettings-Klasse für benutzerdefinierte Teilergebnisbeschriftungen und andere Beschriftungen des Kuchendiagramms](/cells/de/nodejs-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)  

## **Implementieren Sie Subtotal- oder Gesamtsummen-Labels in anderen Sprachen**  

Das folgende Beispiel lädt die [Beispiel-Excel-Datei](5115151.xlsx) und implementiert Subtotal- und Gesamtsummen-Namen in chinesischer Sprache. Bitte prüfen Sie die [Ausgabe-Excel-Datei](5115152.xlsx), die durch diesen Code erzeugt wurde, zur Referenz. Zuerst erstellen wir eine Klasse von [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) und verwenden sie in unserem Code.  

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

Verwenden Sie die oben erstellte Klasse im folgenden Code:  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
