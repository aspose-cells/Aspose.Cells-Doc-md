---
title: Weisen Sie einem Formularsteuerung Makro mit Node.js via C++ zu
linktitle: Weisen Sie einem Formularsteuerelement einen Makrocode zu.
type: docs
weight: 60
url: /de/nodejs-cpp/assign-macro-to-form-control/
description: Erfahren Sie, wie Sie einen Makro Code einer Formularsteuerung wie z.B. einem Button mit Aspose.Cells for Node.js via C++ zuweisen. 
keywords: Weisen Sie einem Formularsteuerung Makro Node.js via C++ zu, Makro Code für Formularsteuerung Node.js via C++, Integriertes Makro in XLSM Node.js via C++
---

{{% alert color="primary" %}}

Mit Aspose.Cells können Sie einem Formularsteuerelement wie einer Schaltfläche einen Makrocode zuweisen. Verwenden Sie die Eigenschaft [**Shape.getMacroName()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getMacroName--), um einem Formularsteuerelement in der Arbeitsmappe einen neuen Makrocode zuzuweisen.

{{% /alert %}}

Der folgende Beispielcode erstellt eine neue Arbeitsmappe, weist einer Formularschaltfläche einen Makro-Code zu und speichert die Ausgabe im XLSM-Format. Sobald Sie die ausgegebene XLSM-Datei in Microsoft Excel öffnen, sehen Sie den folgenden Makro-Code.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Makro einer Formularsteuerung in Node.js zuweisen**

Hier ist der Beispielcode zur Erzeugung der Ausgabedatei XLSM mit Makro-Code.

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
