---  
title: Repetir imagen de mosaico como textura dentro de la forma con Node.js mediante C++  
linktitle: Colocar imagen como textura dentro de la forma  
type: docs  
weight: 1700  
url: /es/nodejs-cpp/tile-picture-as-a-texture-inside-the-shape/  
description: Aprende cómo tiled una imagen pequeña como textura dentro de una forma usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  

Cuando la imagen es pequeña y no cubre toda la superficie de la forma sin perder su calidad, entonces tiene la opción de colocarla como textura. Colocar como textura llena la superficie de la forma con una imagen pequeña repitiéndola como si fueran azulejos.  

## **Colocar imagen como textura dentro de la forma**  

Puedes llenar la superficie de la forma con alguna imagen y tiled usando la propiedad [**Shape.isTiling()**](https://reference.aspose.com/cells/nodejs-cpp/texturefill/#isTiling--) y configurándola en **true**. Por favor, consulta el siguiente código de ejemplo, su [archivo Excel de ejemplo](46465050.xlsx) así como la captura de pantalla para referencia.  

## **Captura de pantalla**  

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)  

## **Código de muestra**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleTextureFill_IsTiling.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape inside the worksheet
const shape = worksheet.getShapes().get(0);

// Tile Picture as a Texture inside the Shape 
shape.getFill().getTextureFill().setIsTiling(true);

// Save the output Excel file
workbook.save(path.join(outputDir, "outputTextureFill_IsTiling.xlsx"));
```  

