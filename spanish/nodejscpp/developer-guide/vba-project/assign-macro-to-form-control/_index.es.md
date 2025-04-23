---
title: Asignar Macro a Control de formulario con Node.js vía C++
linktitle: Asigna Macro a Control de Formulario
type: docs
weight: 60
url: /es/nodejs-cpp/assign-macro-to-form-control/
description: Aprende cómo asignar un código Macro a un Control de formulario como un Botón usando Aspose.Cells for Node.js via C++. 
keywords: Asignar Macro a Control de formulario Node.js vía C++, Código Macro para Control de formulario Node.js vía C++, Macro integrada en XLSM Node.js vía C++
---

{{% alert color="primary" %}}

Aspose.Cells te permite asignar un Código de Macro a un Control de Formulario como un Botón. Por favor utiliza la propiedad [**Shape.getMacroName()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getMacroName--) para asignar un nuevo Código de Macro a un Control de Formulario dentro del libro.

{{% /alert %}}

El siguiente ejemplo de código crea un nuevo libro de trabajo, asigna un Código Macro a un Botón de formulario y guarda el resultado en formato XLSM. Una vez que abres el archivo XLSM en Microsoft Excel, verás el siguiente código macro.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Asignar Macro a Control de formulario en Node.js**

Aquí tienes el ejemplo de código para generar el archivo XLSM de salida con Código Macro.

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
