---  
title: Arbeitsblatt Tab Farbe mit Node.js via C++ setzen  
linktitle: Registerkartenfarbe des Arbeitsblatts festlegen  
type: docs  
weight: 120  
url: /de/nodejs-cpp/set-worksheet-tab-color/  
description: Dieses Beispiel zeigt Code, der die Tab Farbe eines Excel Arbeitsblatts programmgesteuert mit Node.js via C++ setzt.  
keywords: Excel Tab Farbe Node.js über C++ setzen, Code zum Setzen der Excel Tab Farbe Node.js über C++  
---  

{{% alert color="primary" %}}  

Aspose.Cells ermöglicht es Ihnen, die Farbe einzelner Arbeitsblattregisterkarten zu ändern, um sie von anderen hervorzuheben. Zum Beispiel können Sie Ausgaben rot, Verkäufe grün, Vermögenswerte blau usw. machen.

{{% /alert %}}  
## **Verwenden von Microsoft Excel zur Festlegung der Registerkartenfarbe des Arbeitsblatts**  
1. Klicken Sie mit der rechten Maustaste auf eine Registerkarte im Registerblatt am unteren Rand des aktuellen Arbeitsblatts.  
1. Wählen Sie **Registerkartenfarbe**.  
1. Wählen Sie eine Farbe aus der Palette.  
1. Klicken Sie auf **OK**.  
## **Festlegen der Registerkartenfarbe mit Aspose.Cells**  
Der folgende Beispielscode zeigt, wie Sie die Registerkartenfarbe mit Aspose.Cells festlegen können.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));

// Get the first worksheet in the book
const worksheet = workbook.getWorksheets().get(0);

// Set the tab color
worksheet.setTabColor(AsposeCells.Color.Red);

// Save the Excel file
workbook.save(path.join(dataDir, "worksheettabcolor.out.xls"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
