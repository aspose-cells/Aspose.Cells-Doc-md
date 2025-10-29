---
title: Attribuer une macro à un contrôle de formulaire avec Node.js via C++
linktitle: Attribuer une macro à une commande de formulaire
type: docs
weight: 60
url: /fr/nodejs-cpp/assign-macro-to-form-control/
description: Apprenez comment attribuer un code macro à un contrôle de formulaire comme un bouton utilisant Aspose.Cells for Node.js via C++. 
keywords: Attribuer une macro au contrôle de formulaire Node.js via C++, code macro pour contrôle de formulaire Node.js via C++, macro intégrée dans XLSM Node.js via C++
---

{{% alert color="primary" %}}

Aspose.Cells vous permet d'attribuer un code de macro à une Commande de formulaire comme un bouton. Veuillez utiliser la propriété [**Shape.getMacroName()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getMacroName--) pour attribuer un nouveau code de macro à une Commande de formulaire à l'intérieur du classeur.

{{% /alert %}}

Le code d'exemple suivant crée un nouveau classeur, attribue un code macro à un bouton de formulaire, et sauvegarde le résultat au format XLSM. Une fois que vous ouvrez le fichier XLSM dans Microsoft Excel, vous verrez le code macro suivant.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Attribuer une macro au contrôle de formulaire en Node.js**

Voici le code d'exemple pour générer le fichier XLSM de sortie avec le code macro.

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
