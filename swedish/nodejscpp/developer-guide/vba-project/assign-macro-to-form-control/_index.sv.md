---
title: Tilldela makro till formulärkontroll med Node.js via C++
linktitle: Tilldela Makro till Formulärkontroll
type: docs
weight: 60
url: /sv/nodejs-cpp/assign-macro-to-form-control/
description: Lär dig hur man tilldelar ett makrokod till en formulärkontroll som en knapp med hjälp av Aspose.Cells for Node.js via C++. 
keywords: Tilldela makro till formulärkontroll Node.js via C++, makrokod för formulärkontroll Node.js via C++, integrerat makro i XLSM Node.js via C++
---

{{% alert color="primary" %}}

Aspose.Cells låter dig tilldela ett makro kod till en formulärkontroll som en knapp. Använd [**Shape.getMacroName()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getMacroName--) -egenskapen för att tilldela en ny makro kod till en formulärkontroll i arbetsboken.

{{% /alert %}}

Följande kodexempel skapar en ny arbetsbok, tilldelar ett makrokod till en formulärknapp och sparar resultatet i XLSM-format. När du öppnar XLSM-filen i Microsoft Excel, kommer du att se följande makrokod.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Tilldela makro till formulärkontroll i Node.js**

Här är kodexemplet för att generera utdata XLSM-filen med makrokod.

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
