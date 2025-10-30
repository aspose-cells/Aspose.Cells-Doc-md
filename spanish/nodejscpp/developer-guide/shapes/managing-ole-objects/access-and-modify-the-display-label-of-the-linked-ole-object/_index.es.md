---
title: Acceder y modificar la etiqueta de visualización del objeto Ole vinculado con Node.js vía C++
linktitle: Acceder y Modificar la Etiqueta de Visualización del Objeto Ole Vinculado
type: docs
weight: 100
url: /es/nodejs-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: Aprenda cómo acceder y modificar la etiqueta de visualización de un objeto Ole vinculado usando Aspose.Cells for Node.js via C++. 
---

## **Escenarios de uso posibles**

Microsoft Excel permite cambiar la etiqueta de visualización del objeto Ole, como se muestra en la siguiente captura de pantalla. También puede acceder o modificar la etiqueta de visualización del objeto Ole usando las APIs de Aspose.Cells con la propiedad [**OleObject.getLabel()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getLabel--).

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **Acceder y Modificar la Etiqueta de Visualización del Objeto Ole Vinculado**

Por favor, vea el siguiente código de ejemplo, carga el [archivo Excel de muestra](64716810.xlsx) que contiene el objeto Ole. El código accede al objeto Ole y cambia su etiqueta de Sample APIs a Aspose APIs. Por favor, vea la salida de consola dada a continuación que muestra el efecto del código de ejemplo en el archivo Excel de muestra para referencia.

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleAccessAndModifyLabelOfOleObject.xlsx");

// Load the sample Excel file 
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access first Ole Object
let oleObject = ws.getOleObjects().get(0);

// Display the Label of the Ole Object
console.log("Ole Object Label - Before: " + oleObject.getLabel());

// Modify the Label of the Ole Object
oleObject.setLabel("Aspose APIs");

// Save workbook to memory stream
const ms = wb.save(AsposeCells.SaveFormat.Xlsx);

// Set the workbook reference to null
wb.dispose();

// Load workbook from memory stream
const wbFromStream = new AsposeCells.Workbook(ms);

// Access first worksheet
const wsFromStream = wbFromStream.getWorksheets().get(0);

// Access first Ole Object
oleObject = wsFromStream.getOleObjects().get(0);

// Display the Label of the Ole Object that has been modified earlier
console.log("Ole Object Label - After: " + oleObject.getLabel());
```

## **Salida de la consola**

{{< highlight javascript >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
