---
title: Zugriff auf das Textfeld nach Name mit Node.js via C++
linktitle: Greifen Sie auf die Textbox über den Namen zu
type: docs
weight: 230
url: /de/nodejs-cpp/access-the-text-box-by-the-name/
description: Lernen Sie, wie man ein Textfeld anhand des Namens aus der Sammlung in Aspose.Cells for Node.js via C++ zugreift. 
---

##Greifen Sie über den Namen auf die Textbox zu

 Früher wurden Textfelder anhand ihres Index aus der [**Worksheet.getTextBoxes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getTextBoxes--)-Sammlung zugegriffen, jetzt können Sie auch auf das Textfeld nach Name aus dieser Sammlung zugreifen. Dies ist eine bequeme und schnelle Methode, um auf Ihr Textfeld zuzugreifen, wenn Sie bereits seinen Namen kennen.

Der folgende Beispielcode erstellt zunächst eine Textbox und weist ihr einen Text und einen Namen zu. Anschließend greifen wir in den nächsten Zeilen auf dieselbe Textbox anhand ihres Namens zu und drucken ihren Text aus.

### Node.js-Code zum Zugriff auf das Textfeld nach Name

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the TextBox to the worksheet
const idx = sheet.getTextBoxes().add(10, 10, 10, 10);

// Access newly created TextBox using its index & name it
const tb1 = sheet.getTextBoxes().get(idx);
tb1.setName("MyTextBox");

// Set text for the TextBox
tb1.setText("This is MyTextBox");

// Access the same TextBox via its name
const tb2 = sheet.getTextBoxes().get("MyTextBox");

// Display the text of the TextBox accessed via name
console.log(tb2.getText());

console.log("Press any key to continue...");
```

### Von der Beispiellösung generierte Konsolenausgabe

Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight javascript >}}
This is MyTextBox
{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
