---  
title: Actualizar valores de formas enlazadas con Node.js a través de C++  
linktitle: Actualizar valores de formas vinculadas  
type: docs  
weight: 3200  
url: /es/nodejs-cpp/refresh-values-of-linked-shapes/  
description: Aprende cómo actualizar los valores de formas enlazadas en Excel usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

A veces, tienes una forma enlazada en tu archivo de Excel que está vinculada a alguna celda. En Microsoft Excel, cambiar el valor de la celda enlazada también cambia el valor de la forma enlazada. Esto funciona correctamente con Aspose.Cells for Node.js via C++ si quieres guardar tu libro en formato XLS o XLSX. Sin embargo, si quieres guardar tu libro en formato PDF o HTML, tendrás que llamar al método [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#updateSelectedValue--) para actualizar el valor de la forma enlazada.  

{{% /alert %}}  

## Ejemplo  

La siguiente captura muestra el archivo Excel fuente usado en el ejemplo de código a continuación. Tiene una imagen enlazada a las celdas A1 a E4. Cambiaremos el valor de la celda B4 con Aspose.Cells y luego llamaremos al método [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#updateSelectedValue--) para actualizar el valor de la imagen y guardarla en formato PDF.  

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)  

Puedes descargar el [archivo Excel fuente](95584291.xlsx) y el [PDF de salida](95584292.pdf) desde los enlaces proporcionados.  

### Código Node.js para actualizar los valores de formas enlazadas  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook from source file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleRefreshValueOfLinkedShapes.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Change the value of cell B4
const cell = worksheet.getCells().get("B4");
cell.putValue(100);

// Update the value of the Linked Picture which is linked to cell B4
worksheet.getShapes().updateSelectedValue();

// Save the workbook in PDF format
workbook.save(path.join(outputDir, "outputRefreshValueOfLinkedShapes.pdf"), AsposeCells.SaveFormat.Pdf);
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
