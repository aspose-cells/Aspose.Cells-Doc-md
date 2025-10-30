---  
title: Convertir fechas a fechas japonesas con Node.js a través de C++  
linktitle: Convertir Fechas a Fechas Japonesas  
type: docs  
weight: 350  
url: /es/nodejs-cpp/convert-dates-to-japanese-dates/  
description: Aprende cómo convertir fechas del calendario gregoriano a fechas japonesas usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

En el Calendario Japonés, una nueva era comienza con el reinado de un nuevo emperador. El 1 de mayo de 2019, un nuevo emperador tomó el poder con lo cual terminó la era Heisei y comenzó la era Reiwa.  

{{% /alert %}}  

Aspose.Cells ofrece una forma de convertir fechas gregorianas a fechas japonesas. Durante esta conversión, también se consideran los cambios en la era. El siguiente fragmento de código convierte el archivo [Excel fuente](90112015.xlsx) que contiene fechas gregorianas a un [PDF de salida](90112016.pdf) con fechas japonesas, como se muestra en la imagen abajo.  

![todo:image_alt_text](convert-dates-to-japanese-dates_1.jpg)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const options = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
options.setLanguageCode(AsposeCells.CountryCode.Japan);
options.setRegion(AsposeCells.CountryCode.Japan);

const workbook = new AsposeCells.Workbook(path.join(sourceDir, "JapaneseDates.xlsx"), options);
workbook.save(outputDir + "JapaneseDates.pdf", AsposeCells.SaveFormat.Pdf);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
