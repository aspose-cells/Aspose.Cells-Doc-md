---
title: Cómo imprimir Excel como páginas ajustadas anchas y altas con Node.js a través de C++
linktitle: Cómo imprimir Excel como páginas ajustadas en ancho y alto
type: docs
weight: 200
url: /es/nodejs-cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Este artículo te muestra un código que explica cómo establecer FitToPagesWide y FitToPagesTall usando Aspose.Cells for Node.js via C++.
keywords: Node.js a través de C++ Cómo establecer FitToPagesWide y FitToPagesTall, Cómo agregar FitToPagesWide y FitToPagesTall en Node.js, Cómo establecer FitToPagesWide y FitToPagesTall en Excel, Cómo borrar FitToPagesWide y FitToPagesTall en Excel, Cómo imprimir Excel como páginas ajustadas anchas y altas, Cómo imprimir la hoja como una sola página, Cómo imprimir todas las columnas de la hoja en una sola página.
---

## **Introducción**

Las configuraciones FitToPagesWide y FitToPagesTall se usan en aplicaciones de hojas de cálculo (como Microsoft Excel) para controlar cómo se escala una hoja de cálculo al imprimir. Estas configuraciones ayudan a garantizar que tu salida impresa quepa dentro de un número específico de páginas, tanto en horizontal como en vertical. Aquí hay una descripción de cada configuración:

1. FitToPagesWide: Esta configuración especifica el número de páginas de ancho en las que la salida impresa debe ajustarse. Por ejemplo, establecer FitToPagesWide en 1 significa que el contenido se escalará para ajustarse dentro de una sola anchura de página, sin importar cuán ancha sea la hoja de cálculo.
2. FitToPagesTall: Esta configuración especifica el número de páginas de alto en las que la salida impresa debe ajustarse. Por ejemplo, configurar FitToPagesTall en 1 significa que el contenido se escalará para caber dentro de una sola página de altura, sin importar el número de filas.

## **Por qué usar FitToPagesWide y FitToPagesTall**
Aquí hay algunas razones para configurar FitToPagesWide y FitToPagesTall:
1. Control sobre el diseño impreso: Al especificar el número de páginas de ancho y alto, puedes asegurarte de que tu documento impreso sea fácil de leer y esté bien organizado, sin que columnas o filas se dividan de manera incómoda en las páginas.
2. Consistencia: Si imprimes varias hojas o informes, usar estas configuraciones ayuda a mantener un formato consistente, facilitando la comparación y análisis de los documentos impresos.
3. Presentación profesional: Escalar y ajustar correctamente el contenido a un número específico de páginas puede dar lugar a una presentación más profesional y pulida de tus datos.

## **Cómo imprimir un archivo como páginas ajustadas en ancho y alto en Excel**

Para configurar FitToPagesWide y FitToPagesTall en Microsoft Excel, sigue estos pasos:

1. Abre tu libro de Excel y ve a la hoja que deseas imprimir.
2. Ve a la pestaña Diseño de página en la Cinta de opciones.
3. En el grupo Configuración de página, haz clic en la pequeña flecha en la esquina inferior derecha para abrir el cuadro de diálogo Configuración de página.
4. En el cuadro de diálogo Configuración de página, ve a la pestaña Página.
5. En Escalado, selecciona la opción "Ajustar a" y luego especifica el número de páginas de ancho y alto que deseas: Ingresa el número de páginas de ancho en la primera casilla (Ajustar a x páginas de ancho). Ingresa el número de páginas de alto en la segunda casilla (Ajustar a y páginas de alto).
<br>
<img src="2.png" width=60% />

6. Haz clic en Aceptar para aplicar la configuración.

## **Cómo imprimir Excel como páginas ajustadas anchas y altas usando Aspose.Cells for Node.js via C++**

Para establecer FitToPagesWide y FitToPagesTall en una hoja de trabajo específica: primero, carga el [archivo de ejemplo](input.xlsx), y luego necesitas modificar las propiedades [**PageSetup.getFitToPagesTall()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesTall--) y [**PageSetup.getFitToPagesWide()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesWide--) del objeto [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/) para la hoja de trabajo deseada. Aquí un ejemplo en Node.js:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the number of pages to which the length of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesTall(1);

// Setting the number of pages to which the width of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesWide(1);

// Save the workbook
workbook.save("out_net.pdf");
```

El resultado de la salida:
<br>
<img src="1.png" width=60% />

## **Cómo imprimir la hoja de trabajo como una sola página usando Aspose.Cells for Node.js via C++**

Para imprimir la hoja de trabajo como una sola página: primero, carga el [archivo de ejemplo](sample.xlsx), y luego debes configurar la propiedad [**PdfSaveOptions.getOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOnePagePerSheet--) del objeto [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/). Aquí un ejemplo en Node.js:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setOnePagePerSheet(true);

// Save the workbook.
workbook.save("OnePagePerSheet.pdf", options);
```

El resultado de la salida:
<br>
<img src="3.png" width=60% />

## **Cómo imprimir todas las columnas de una hoja en una sola página usando Aspose.Cells for Node.js via C++**

Para imprimir todas las columnas de la hoja en una sola página: primero, carga el [archivo de ejemplo](sample.xlsx), y luego necesitas configurar la propiedad [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) del objeto [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/). Aquí un ejemplo en Node.js:

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setAllColumnsInOnePagePerSheet(true);

// Save the workbook.
workbook.save("AllColumnsInOnePagePerSheet.pdf", options);
```

El resultado de la salida:
<br>
<img src="4.png" width=60% />
