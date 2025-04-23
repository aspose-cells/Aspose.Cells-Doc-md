---  
title: Renderizar relleno de degradado para WordArt al convertir hojas de cálculo a HTML con Node.js mediante C++  
linktitle: Renderizar relleno degradado para WordArt al convertir hojas de cálculo a HTML  
type: docs  
weight: 90  
url: /es/nodejs-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/  
description: Aprende cómo renderizar relleno de degradado en WordArt al convertir hojas de cálculo a HTML usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  
Antes de Aspose.Cells 17.1, Aspose.Cells no renderizaba el relleno de degradado del WordArt al convertir el archivo de Excel a formato HTML. Desde el lanzamiento de Aspose.Cells 17.1, se soporta el relleno de WordArt con degradado. La siguiente captura de pantalla compara el efecto del relleno de degradado al convertir el archivo de Excel usando Aspose.Cells 17.1 y la versión más antigua.  

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)  

## **Renderizar relleno degradado para WordArt al convertir hojas de cálculo a HTML**  
El siguiente código de ejemplo convierte el [archivo de Excel fuente](22774111.xlsx) en [formato HTML de salida](22774109.zip). El archivo de Excel de origen contiene un objeto WordArt con relleno de degradado como se muestra en la captura anterior.  

## **Código de muestra**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sourceGradientFill.xlsx");

// Read the source excel file having text with gradient fill
const workbook = new AsposeCells.Workbook(filePath);

// Save workbook to html format
workbook.save(path.join(dataDir, "out_sourceGradientFill.html"));
```  

