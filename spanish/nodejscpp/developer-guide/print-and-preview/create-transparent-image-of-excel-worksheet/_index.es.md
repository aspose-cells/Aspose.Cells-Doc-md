---  
title: Crear imagen transparente de la hoja de trabajo de Excel con Node.js vía C++  
linktitle: Create Transparent Image of Excel Worksheet  
type: docs  
weight: 170  
url: /es/nodejs-cpp/create-transparent-image-of-excel-worksheet/  
description: Aprenda cómo generar una imagen transparente de una hoja de trabajo de Excel usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

A veces, es necesario generar la imagen de la hoja de cálculo como una imagen transparente. Desea aplicar transparencia a todas las celdas que no tienen colores de relleno. Aspose.Cells proporciona la propiedad [**ImageOrPrintOptions.getTransparent()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTransparent--) para aplicar transparencia a la imagen de la hoja de cálculo. Cuando esta propiedad es **false**, entonces las celdas sin colores de relleno se dibujan con color blanco, y cuando es **true**, las celdas sin colores de relleno se dibujan transparentes.  

{{% /alert %}}  

En la siguiente imagen de la hoja de cálculo, no se ha aplicado transparencia. Las celdas sin colores de relleno se dibujan de color blanco.  

|**Resultado sin transparencia: el fondo de la celda es blanco**|  
| :- |  
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|  

Mientras que, en la siguiente imagen de la hoja de cálculo, se ha aplicado transparencia. Las celdas sin colores de relleno son transparentes.  

|**Resultado con transparencia habilitada**|  
| :- |  
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|  

El siguiente código de ejemplo genera una imagen transparente a partir de una hoja de cálculo de Excel.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook object from source file
const wb = new AsposeCells.Workbook(path.join(sourceDir, "sampleCreateTransparentImage.xlsx"));

// Apply different image or print options
const imgOption = new AsposeCells.ImageOrPrintOptions();
imgOption.setImageType(AsposeCells.ImageType.Png);
imgOption.setHorizontalResolution(200);
imgOption.setVerticalResolution(200);
imgOption.setOnePagePerSheet(true);

// Apply transparency to the output image
imgOption.setTransparent(true);

// Create image after applying image or print options
const sr = new AsposeCells.SheetRender(wb.getWorksheets().get(0), imgOption);
sr.toImage(0, path.join(outputDir, "outputCreateTransparentImage.png"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
