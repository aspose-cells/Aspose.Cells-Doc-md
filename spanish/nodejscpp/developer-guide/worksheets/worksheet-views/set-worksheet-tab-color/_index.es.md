---  
title: Establecer color de pestaña de hoja de trabajo con Node.js via C++  
linktitle: Establecer el color de la pestaña de la hoja de cálculo  
type: docs  
weight: 120  
url: /es/nodejs-cpp/set-worksheet-tab-color/  
description: Este artículo demuestra un código de ejemplo que establece el color de la pestaña de la hoja de Excel de forma programática usando Node.js vía C++.  
keywords: establecer color de pestaña de excel en Node.js vía C++, código para establecer color de pestaña de excel en Node.js vía C++  
---  

{{% alert color="primary" %}}  

Aspose.Cells te permite cambiar el color de las pestañas individuales de las hojas de cálculo para hacerlas más destacadas. Por ejemplo, puedes hacer que Gastos sean rojos, Ventas verdes, Activos azules, etc.

{{% /alert %}}  
## **Establecer el color de la pestaña de la hoja de cálculo con Microsoft Excel**  
1. Haz clic derecho en una pestaña en la hoja de pestañas en la parte inferior de la hoja de cálculo actual.  
1. Seleccione **Color de pestaña**.  
1. Selecciona un color de la paleta.  
1. Haz clic en **Aceptar**.  
## **Configurar el color de la pestaña de la hoja de cálculo con Aspose.Cells**  
El código de ejemplo a continuación muestra cómo configurar el color de la pestaña con Aspose.Cells.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));

// Get the first worksheet in the book
const worksheet = workbook.getWorksheets().get(0);

// Set the tab color
worksheet.setTabColor(AsposeCells.Color.Red);

// Save the Excel file
workbook.save(path.join(dataDir, "worksheettabcolor.out.xls"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
