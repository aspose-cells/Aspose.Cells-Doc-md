---  
title: Especificar conjuntos individuales o privados de fuentes para renderizado de libros de trabajo con Node.js vía C++  
linktitle: Especificar un Conjunto Individual o Privado de Fuentes para la Representación del Libro  
type: docs  
weight: 40  
url: /es/nodejs-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/  
description: Aprende cómo especificar conjuntos individuales o privados de fuentes para el renderizado de libros de trabajo usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  

Generalmente, especificas el directorio de fuentes o una lista de ellas para todos los libros de trabajo, pero a veces necesitas especificar conjuntos individuales o privados de fuentes para tus libros de trabajo. Aspose.Cells for Node.js via C++ proporciona la clase [**IndividualFontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/individualfontconfigs) que puede usarse para especificar conjuntos individuales o privados de fuentes para tu libro de trabajo.  

## **Especificar un Conjunto Individual o Privado de Fuentes para la Representación del Libro**  

El siguiente código de ejemplo carga el [archivo de Excel de muestra](67338268.xlsx) con su conjunto individual o privado de fuentes que se especifica usando la clase [**IndividualFontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/individualfontconfigs). Consulta también la [fuente de muestra](67338271.zip) utilizada dentro del código y el [PDF de salida](67338269.pdf) generado por él. La siguiente captura de pantalla muestra cómo se ve el PDF de salida si la fuente se encuentra correctamente.  

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)  

## **Código de muestra**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Path of your custom font directory.
const customFontsDir = "C:\\TempDir\\CustomFonts";

// Specify individual font configs custom font directory.
const fontConfigs = new AsposeCells.IndividualFontConfigs();

// If you comment this line or if custom font directory is wrong or 
// if it does not contain required font then output pdf will not be rendered correctly.
fontConfigs.setFontFolder(customFontsDir, false);

// Specify load options with font configs.
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
opts.setFontConfigs(fontConfigs);

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.xlsx");
// Output directory
const outputDir = path.join(__dirname, "output");
// Load the sample Excel file with individual font configs. 
const wb = new AsposeCells.Workbook(filePath, opts);

// Save to PDF format.
wb.save(outputDir + "outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf", AsposeCells.SaveFormat.Pdf);
```  

