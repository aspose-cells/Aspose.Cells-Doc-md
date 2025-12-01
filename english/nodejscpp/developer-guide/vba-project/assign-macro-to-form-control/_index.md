---
title: Assign Macro to Form Control with Node.js via C++
linktitle: Assign Macro to Form Control
type: docs
weight: 60
url: /nodejs-cpp/assign-macro-to-form-control/
description: Learn how to assign a Macro Code to a Form Control like a Button using Aspose.Cells for Node.js via C++. 
keywords: Assign Macro to Form Control Node.js via C++, Macro Code for Form Control Node.js via C++, Integrated Macro in XLSM Node.js via C++
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells allows you to assign a Macro Code to a Form Control like a Button. Please use the [**Shape.getMacroName()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getMacroName--) property to assign a new Macro Code to a Form Control inside the workbook.

{{% /alert %}}

The following sample code creates a new workbook, assigns a Macro Code to a Form Button, and saves the output in the XLSM format. Once you open the output XLSM file in Microsoft Excel, you will see the following macro code.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Assign Macro to Form Control in Node.js**

Here is the sample code to generate the output XLSM file with Macro Code.

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
