---
title: Actualizar control ComboBox ActiveX con Node.js vía C++
linktitle: Actualizar el control de cuadro combinado ActiveX
type: docs
weight: 170
url: /es/nodejs-cpp/update-activex-combobox-control/
description: Aprenda cómo leer y escribir valores del control ComboBox ActiveX usando Aspose.Cells for Node.js via C++. 
---

## **Escenarios de uso posibles**
Puede leer o escribir los valores del control ComboBox ActiveX usando Aspose.Cells for Node.js via C++. Por favor, acceda al control ActiveX a través de la propiedad [Shape.getActiveXControl()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getActiveXControl--) y verifique su tipo mediante [ActiveXControlBase.getType()](https://reference.aspose.com/cells/nodejs-cpp/activexcontrolbase/#getType--), que debe devolver el valor [ControlType.ComboBox](https://reference.aspose.com/cells/nodejs-cpp/controltype/) y luego convertirlo al objeto [ComboBoxActiveXControl](https://reference.aspose.com/cells/nodejs-cpp/comboboxactivexcontrol/) para leer o modificar sus diversas propiedades.

Descargue el [archivo de Excel de ejemplo](5115124.xlsx) utilizado en el siguiente código de ejemplo.
## **Actualizar control ActiveX ComboBox**
La siguiente captura de pantalla muestra el efecto del código de ejemplo en el [archivo de Excel de ejemplo](5115124.xlsx). Como puede ver, el valor del Control Combo Box ActiveX se ha actualizado a "Este es un control de combo box".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Código de muestra**
El siguiente código de ejemplo actualiza el valor del Control Combo Box ActiveX presente dentro del [archivo de Excel de ejemplo](5115124.xlsx).

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
