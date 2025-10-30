---
title: Assegna Macro a un controllo modulo con Node.js via C++
linktitle: Assegna Macro a Controllo Modulo
type: docs
weight: 60
url: /it/nodejs-cpp/assign-macro-to-form-control/
description: Impara come assegnare un codice macro a un controllo modulo come un pulsante usando Aspose.Cells for Node.js via C++. 
keywords: Assegna Macro a un controllo modulo Node.js via C++, Codice Macro per controllo modulo Node.js via C++, Macro integrata in XLSM Node.js via C++
---

{{% alert color="primary" %}}

Aspose.Cells ti consente di assegnare un codice Macro a un Controllo Modulo come un Pulsante. Si prega di utilizzare la proprietà [**Shape.getMacroName()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getMacroName--) per assegnare un nuovo codice Macro a un Controllo Modulo all'interno del workbook.

{{% /alert %}}

Il seguente esempio di codice crea un nuovo workbook, assegna un Codice Macro a un Pulsante di Modulo e salva l’output in formato XLSM. Una volta aperto il file XLSM in Microsoft Excel, vedrai il seguente codice macro.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Assegna Macro a controllo modulo in Node.js**

Ecco il codice di esempio per generare il file XLSM di output con il codice Macro.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);

const moduleIdx = workbook.getVbaProject().getModules().add(sheet);
const module = workbook.getVbaProject().getModules().get(moduleIdx);
module.setCodes(
"Sub ShowMessage()" + "\r\n" +
"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +
"End Sub"
);

const button = sheet.getShapes().addButton(2, 0, 2, 0, 28, 80);
button.setPlacement(AsposeCells.PlacementType.FreeFloating);
button.getFont().setName("Tahoma");
button.getFont().setIsBold(true);
button.getFont().setColor(AsposeCells.Color.Blue);
button.setText("Aspose");

button.setMacroName(sheet.getName() + ".ShowMessage");

const outputFilePath = path.join(dataDir, "Output.out.xlsm");
workbook.save(outputFilePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
