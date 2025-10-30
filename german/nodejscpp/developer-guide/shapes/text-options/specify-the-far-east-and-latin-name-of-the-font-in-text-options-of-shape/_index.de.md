---  
title: Angabe des Fernost und lateinischen Namens der Schriftart in Textoptionen von Shape mit Node.js über C++  
linktitle: Den Fernost und Lateinischen Namen der Schriftart in den Textoptionen der Form festlegen  
type: docs  
weight: 1600  
url: /de/nodejs-cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/  
description: Lernen Sie, wie Sie die Namen der Fernost und lateinischen Schriftarten in Textoptionen von Formen mit Aspose.Cells for Node.js via C++ angeben.  
---  

## **Mögliche Verwendungsszenarien**  

Manchmal möchten Sie Text in einer Fernost-Schriftsprache anzeigen, z.B. Japanisch, Chinesisch, Thailändisch usw. Aspose.Cells for Node.js via C++ bietet die [**TextOptions.getFarEastName()**](https://reference.aspose.com/cells/nodejs-cpp/textoptions/#getFarEastName--)-Eigenschaft, mit der Sie den Schriftartnamen der Fernost-Sprache angeben können. Außerdem können Sie auch den lateinischen Schriftartnamen mit der [**TextOptions.getLatinName()**](https://reference.aspose.com/cells/nodejs-cpp/textoptions/#getLatinName--)-Eigenschaft festlegen.  

## **Den Fernost- und Lateinischen Namen der Schriftart in den Textoptionen der Form festlegen**  

Das folgende Beispiel erstellt eine Textbox und fügt some Japanischen Text darin ein. Es gibt dann die lateinischen und Fernost-Schriftartnamen des Textes an und speichert die Arbeitsmappe als [Ausgabe-Excel](67338274.xlsx). Der folgende Screenshot zeigt die lateinischen und Fernost-Schriftartnamen der Ausgabetextbox in Microsoft Excel.  

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)  

## **Beispielcode**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Add textbox inside the worksheet.
const idx = ws.getTextBoxes().add(5, 5, 50, 200);
const tb = ws.getTextBoxes().get(idx);

// Set the text of the textbox.
tb.setText("こんにちは世界");

// Specify the Far East and Latin name of the font.
tb.getTextOptions().setLatinName("Comic Sans MS");
tb.getTextOptions().setFarEastName("KaiTi");

// Save the output Excel file.
wb.save("outputSpecifyFarEastAndLatinNameOfFontInTextOptionsOfShape.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
