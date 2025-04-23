---  
title: Dibuja una Línea de Tiempo al renderizar Excel a PDF con Node.js vía C++  
linktitle: Dibujar línea de tiempo al renderizar Excel a PDF  
type: docs  
weight: 60  
url: /es/nodejs-cpp/draw-timeline-while-rendering-excel-to-pdf/  
description: Gestionar líneas de tiempo de archivos de Excel con Aspose.Cells for Node.js via C++.  
keywords: Renderizando línea de tiempo a pdf sin Office 2013, Office 2016, Office 2019 y Office 365 Node.js vía C++  
---  

## **Dibuje una línea de tiempo mientras renderiza Excel a PDF**  
Si tienes un archivo Excel al que se le ha aplicado una línea de tiempo y deseas exportar el Excel a PDF con la configuración de la línea de tiempo, Aspose.Cells for Node.js via C++ ahora soporta esto por defecto. Solo exporta el archivo Excel con línea de tiempo a PDF, y el PDF generado mostrará la línea de tiempo aplicada.  

El siguiente código de muestra carga el [archivo Excel de muestra](input.xlsx) que contiene una línea de tiempo existente. Luego guarda el libro de trabajo como [archivo PDF de salida](out.pdf). La siguiente captura de pantalla compara el archivo Excel fuente y el archivo PDF generado.  

<img src="out.png" width="60%">  

## **Código de muestra**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
// Load sample Excel file
const workbook = new AsposeCells.Workbook(filePath);
// Save file to pdf
workbook.save("out.pdf", AsposeCells.SaveFormat.Pdf);
```  

