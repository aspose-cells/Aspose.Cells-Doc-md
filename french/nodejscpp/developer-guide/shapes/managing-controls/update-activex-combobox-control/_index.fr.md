---
title: Mettre à jour le contrôle ComboBox ActiveX avec Node.js via C++
linktitle: Mettre à jour le contrôle ComboBox ActiveX
type: docs
weight: 170
url: /fr/nodejs-cpp/update-activex-combobox-control/
description: Apprenez comment lire et écrire les valeurs du contrôle ComboBox ActiveX en utilisant Aspose.Cells for Node.js via C++. 
---

## **Scénarios d'utilisation possibles**
Vous pouvez lire ou écrire les valeurs du contrôle ComboBox ActiveX en utilisant Aspose.Cells for Node.js via C++. Accédez au contrôle ActiveX via la propriété [Shape.getActiveXControl()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getActiveXControl--) et vérifiez son type via la propriété [ActiveXControlBase.getType()](https://reference.aspose.com/cells/nodejs-cpp/activexcontrolbase/#getType--), elle doit retourner la valeur [ControlType.ComboBox](https://reference.aspose.com/cells/nodejs-cpp/controltype/), puis effectuer une conversion de type en [ComboBoxActiveXControl](https://reference.aspose.com/cells/nodejs-cpp/comboboxactivexcontrol/) pour lire ou modifier ses diverses propriétés.

Veuillez télécharger le [fichier Excel exemple](5115124.xlsx) utilisé dans le code d'exemple suivant.
## **Mise à jour du contrôle ComboBox ActiveX**
La capture d'écran suivante montre l'effet du code d'exemple sur le [fichier Excel d'exemple](5115124.xlsx). Comme vous pouvez le constater, la valeur de la boîte combinée ActiveX a été mise à jour pour "Il s'agit d'un contrôle de boîte combinée".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Code d'exemple**
Le code d'exemple suivant met à jour la valeur du contrôle Boîte combi ActiveX présent dans le [fichier Excel d'exemple](5115124.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SourceFile_activex.xlsx");
// Create a workbook
const wb = new AsposeCells.Workbook(filePath);

// Access first shape from first worksheet
const shape = wb.getWorksheets().get(0).getShapes().get(0);

// Access ActiveX ComboBox Control and update its value
if (shape.getActiveXControl() != null)
{
// Access Shape ActiveX Control
const c = shape.getActiveXControl();

if (c instanceof AsposeCells.ComboBoxActiveXControl)
{
// Type cast ActiveXControl into ComboBoxActiveXControl and change its value
const comboBoxActiveX = new AsposeCells.ComboBoxActiveXControl(c);
comboBoxActiveX.setValue("This is combo box control with updated value.");

}

}

// Save the workbook
const outputFilePath = path.join(dataDir, "OutputFile_out.xlsx");
wb.save(outputFilePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
