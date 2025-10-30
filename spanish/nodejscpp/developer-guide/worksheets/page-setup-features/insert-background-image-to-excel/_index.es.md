---
title: Insertar imagen de fondo en Excel con Node.js usando C++
linktitle: Insertar imagen de fondo en Excel
type: docs
weight: 90
url: /es/nodejs-cpp/insert-background-image-to-excel/
description: "Cómo insertar una imagen de fondo en Excel usando Aspose.Cells for Node.js via C++."
---

{{% alert color="primary" %}} 

Puede hacer que una hoja de cálculo sea más atractiva agregando una imagen como fondo de la hoja. Esta función puede ser muy efectiva si tiene un gráfico corporativo especial que agrega un toque del fondo sin ocultar los datos en la hoja. Puede establecer una imagen de fondo para una hoja utilizando la API de Aspose.Cells.

{{% /alert %}} 

## **Establecer fondo de hoja en Microsoft Excel**

Para establecer una imagen de fondo de hoja en Microsoft Excel (por ejemplo, Microsoft Excel 2019):

1. Desde el menú **Diseño de página**, encontrar la opción **Configurar página**, y luego hacer clic en la opción **Fondo**.
1. Seleccionar una imagen para establecer la imagen de fondo de la hoja.

   **Establecer un fondo de hoja**

![todo:image_alt_text](insert-background-to-excel.jpg)

## **Configurar fondo de hoja con Aspose.Cells for Node.js via C++**

El código a continuación establece una imagen de fondo utilizando una imagen de un flujo.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const backgroundImagePath = path.join(dataDir, "background.jpg");

// Create a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Set the background image for the worksheet.
sheet.setBackgroundImage(fs.readFileSync(backgroundImagePath).buffer);

// Save the Excel file
workbook.save("outputBackImageSheet.xlsx");

// Save the HTML file
workbook.save("outputBackImageSheet.html", AsposeCells.SaveFormat.Html);
```

## Artículos relacionados

- [Trabajar con fondo en archivos ODS](/cells/es/nodejs-cpp/working-with-background-in-ods-files/)

{{< app/cells/assistant language="nodejs-cpp" >}}
