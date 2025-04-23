---  
title: Agregar Partes XML Personalizadas y Seleccionarlas por ID con Node.js via C++  
linktitle: Agregar partes XML personalizadas y seleccionarlas por ID  
type: docs  
weight: 70  
url: /es/nodejs-cpp/add-custom-xml-parts-and-select-them-by-id/  
description: Aprende cómo agregar partes XML personalizadas a documentos Excel y seleccionarlas por ID usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  

Las Partes XML Personalizadas son los datos XML que se almacenan dentro de los documentos Microsoft Excel y son utilizados por las aplicaciones que trabajan con ellos. Actualmente no hay una forma directa de agregarlas usando la interfaz de Microsoft Excel. Sin embargo, puedes agregarlas programáticamente de varias maneras, por ejemplo, usando VSTO, Aspose.Cells, etc. Por favor, usa el método [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--) si deseas agregar una Parte XML Personalizada utilizando la API de Aspose.Cells. También puedes establecer su ID usando la propiedad [**CustomXmlPart.getID()**](https://reference.aspose.com/cells/nodejs-cpp/customxmlpart/#getID--). De manera similar, si deseas seleccionar una Parte XML Personalizada por ID, puedes usar el método [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--).  

## **Agregar partes XML personalizadas y seleccionarlas por ID**  

El siguiente código de ejemplo primero agrega cuatro Partes XML Personalizadas usando el método [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--). Luego, asigna sus IDs usando la propiedad [**CustomXmlPart.getID()**](https://reference.aspose.com/cells/nodejs-cpp/customxmlpart/#getID--). Finalmente, encuentra o selecciona una de las Partes XML Personalizadas agregadas usando el método [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--). También consulte la salida de la consola del código a continuación para referencia.  

## **Código de muestra**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Some data in the form of byte array.
// Please use correct XML and Schema instead.
const btsData = new Uint8Array([1, 2, 3]);
const btsSchema = new Uint8Array([1, 2, 3]);

// Create four custom xml parts.
wb.getCustomXmlParts().add(btsData, btsSchema);
wb.getCustomXmlParts().add(btsData, btsSchema);
wb.getCustomXmlParts().add(btsData, btsSchema);
wb.getCustomXmlParts().add(btsData, btsSchema);

// Assign ids to custom xml parts.
wb.getCustomXmlParts().get(0).setID("Fruit");
wb.getCustomXmlParts().get(1).setID("Color");
wb.getCustomXmlParts().get(2).setID("Sport");
wb.getCustomXmlParts().get(3).setID("Shape");

// Specify search custom xml part id.
let srchID = "Fruit";
srchID = "Color";
srchID = "Sport";

// Search custom xml part by the search id.
const cxp = wb.getCustomXmlParts().selectByID(srchID);

// Print the found or not found message on console.
if (cxp.isNull()) {
console.log(`Not Found: CustomXmlPart ID ${srchID}`);
} else {
console.log(`Found: CustomXmlPart ID ${srchID}`);
}

console.log("AddCustomXMLPartsAndSelectThemByID executed successfully.");
```  

## **Salida de la consola**  

{{< highlight java >}}  
 Found: CustomXmlPart ID Sport  
{{< /highlight >}}  

