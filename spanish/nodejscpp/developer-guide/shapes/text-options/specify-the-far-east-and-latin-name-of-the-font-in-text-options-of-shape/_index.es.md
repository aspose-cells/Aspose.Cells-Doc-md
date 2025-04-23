---  
title: Especificar el nombre del lejano Oriente y latino de la fuente en Opciones de texto de forma con Node.js vía C++  
linktitle: Especificar el nombre del Lejano Oriente y del Font en opciones de texto de forma  
type: docs  
weight: 1600  
url: /es/nodejs-cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/  
description: Aprende cómo especificar los nombres de fuentes del lejano Oriente y latino en las opciones de texto de formas usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  

A veces quieres mostrar el texto en una fuente del idioma del Lejano Oriente, por ejemplo, Japonés, Chino, Tailandés, etc. Aspose.Cells for Node.js via C++ proporciona la propiedad [**TextOptions.getFarEastName()**](https://reference.aspose.com/cells/nodejs-cpp/textoptions/#getFarEastName--) que puede usarse para especificar el nombre de la fuente del idioma del Lejano Oriente. Además, también puedes especificar el nombre de la fuente latina usando la propiedad [**TextOptions.getLatinName()**](https://reference.aspose.com/cells/nodejs-cpp/textoptions/#getLatinName--).  

## **Especificar el nombre del Lejano Oriente y del Font en opciones de texto de forma**  

El siguiente código de ejemplo crea un cuadro de texto y agrega algo de texto en japonés dentro de él. Luego especifica los nombres de fuente del latín y del Extremo Oriente del texto y guarda el libro de trabajo como [archivo de Excel de salida](67338274.xlsx). La siguiente captura de pantalla muestra los nombres de fuente del texto de salida en Microsoft Excel.  

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)  

## **Código de muestra**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Add textbox inside the worksheet.
const idx = ws.getTextBoxes().add(5, 5, 50, 200);
const tb = ws.getTextBoxes().get(idx);

// Set the text of the textbox.
tb.setText("こんにちは世界");

// Specify the Far East and Latin name of the font.
tb.getTextOptions().setLatinName("Comic Sans MS");
tb.getTextOptions().setFarEastName("KaiTi");

// Save the output Excel file.
wb.save("outputSpecifyFarEastAndLatinNameOfFontInTextOptionsOfShape.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

