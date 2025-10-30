---  
title: Determinar si una Forma es una Forma de Arte Inteligente con Node.js vía C++  
linktitle: Determinar si la Forma es una Forma de Arte Inteligente  
type: docs  
weight: 400  
url: /es/nodejs-cpp/determine-if-shape-is-smart-art-shape/  
description: Aprende cómo determinar si una forma en Excel es una forma de arte inteligente usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  

Las formas de arte inteligente son formas especiales en Microsoft Excel que permiten crear diagramas complejos automáticamente. Puedes verificar si la forma es una forma de arte inteligente o una forma normal usando la propiedad [**Shape.isSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#isSmartArt--).  

## **Determinar si la Forma es una Forma de Arte Inteligente**  

El siguiente código de ejemplo carga el [archivo Excel de ejemplo](55541792.xlsx) que contiene una forma de arte inteligente como se muestra en esta captura de pantalla. Luego imprime el valor de la propiedad [**Shape.isSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#isSmartArt--) de la primera forma. Por favor, consulta la salida de la consola del código de ejemplo a continuación.  

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)  

## **Código de muestra**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSmartArtShape.xlsx");

// Load the sample smart art shape - Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Determine if shape is smart art
console.log("Is Smart Art Shape: " + shape.isSmartArt());
```  

## **Salida de la consola**  

{{< highlight java >}}  

Is Smart Art Shape: True  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
