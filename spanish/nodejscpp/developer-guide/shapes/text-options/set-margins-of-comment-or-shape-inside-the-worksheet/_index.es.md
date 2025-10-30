---  
title: Establecer márgenes del comentario o forma dentro de la hoja de cálculo con Node.js vía C++  
linktitle: Establecer márgenes de comentario o forma dentro de la hoja de cálculo  
type: docs  
weight: 1500  
url: /es/nodejs-cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: Aprende cómo establecer los márgenes de comentarios o formas dentro de una hoja de cálculo de Excel usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  

Aspose.Cells te permite establecer los márgenes de cualquier forma o comentario usando la propiedad [**Shape.textBody.textAlignment**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/). Esta propiedad devuelve el objeto de la clase [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment) que tiene diferentes propiedades, por ejemplo, [**ShapeTextAlignment.getTopMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getTopMarginPt--), [**ShapeTextAlignment.getLeftMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getLeftMarginPt--), [**ShapeTextAlignment.getBottomMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getBottomMarginPt--), [**ShapeTextAlignment.getRightMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRightMarginPt--), etc., que se pueden usar para establecer los márgenes superior, izquierdo, inferior y derecho.  

## **Establecer márgenes de comentario o forma dentro de la hoja de cálculo**  

Consulta el siguiente código de ejemplo. Carga el [archivo de Excel de muestra](61767851.xlsx) que contiene dos formas. El código accede a las formas una por una y establece sus márgenes superior, izquierdo, inferior y derecho. Consulta el [archivo de Excel de salida](61767852.xlsx) generado por el código y la captura de pantalla que muestra el efecto del código en el archivo de Excel de salida.  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **Código de muestra**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx");
// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

const shapes = ws.getShapes();
for (let i = 0; i < shapes.getCount(); i++) {
const sh = shapes.get(i);
// Access the text alignment
const txtAlign = sh.getTextBody().getTextAlignment();

// Set auto margin false
txtAlign.setIsAutoMargin(false);

// Set the top, left, bottom and right margins
txtAlign.setTopMarginPt(10);
txtAlign.setLeftMarginPt(10);
txtAlign.setBottomMarginPt(10);
txtAlign.setRightMarginPt(10);
}

// Save the output Excel file
workbook.save("outputSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
