---  
title: Convertir gráfico a imagen en formato SVG con Node.js mediante C++  
linktitle: Conversión de gráfico a imagen en formato SVG  
type: docs  
weight: 240  
url: /es/nodejs-cpp/converting-chart-to-image-in-svg-format/  
description: Aprende cómo convertir un gráfico a una imagen en formato SVG usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Scalable Vector Graphics (SVG) es un formato de imagen vectorial en XML para gráficos bidimensionales que también admite interactividad y animación. La especificación SVG es un estándar abierto desarrollado por el World Wide Web Consortium (W3C) desde 1999.  

Las imágenes SVG y sus comportamientos se definen en archivos de texto XML. Esto significa que pueden ser buscados, indexados, escritos en script y comprimidos. Como archivos XML, las imágenes SVG pueden ser creadas y editadas con cualquier editor de texto, pero más a menudo se crean con software de dibujo.  

Aspose.Cells puede guardar gráficos en imágenes en varios formatos como BMP, JPEG, PNG, GIF, SVG, etc. Este artículo explica cómo guardar un gráfico en formato SVG.  

{{% /alert %}}  

El siguiente código de ejemplo explica cómo usar Aspose.Cells para convertir un gráfico en una imagen en formato SVG. El código carga el archivo de Microsoft Excel fuente y luego guarda el primer gráfico encontrado en la primera hoja de cálculo como SVG.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object from source file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleChartBook.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Set image or print options
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Svg);

// Save the chart to svg format
chart.toImage(path.join(dataDir, "Image_out.svg"), opts);
```  

