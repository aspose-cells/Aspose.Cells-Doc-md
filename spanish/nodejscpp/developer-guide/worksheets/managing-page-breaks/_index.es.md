---
title: Gestión de saltos de página con Node.js vía C++
linktitle: Gestionar Saltos de Página
type: docs
weight: 30
url: /es/nodejs-cpp/managing-page-breaks/
description: Este artículo proporciona código de ejemplo y explica cómo agregar, limpiar o eliminar saltos de página específicos en hojas de Excel de forma programática usando Aspose.Cells for Node.js via C++.
keywords: saltos de página Node.js vía C++, saltos de página en Excel Node.js vía C++, limpiar salto de página Node.js vía C++, eliminar salto de página específico Node.js vía C++
---

{{% alert color="primary" %}}

Según la definición, un salto de página es un lugar en un flujo de texto donde una página termina y comienza la siguiente. Microsoft Excel permite a los usuarios agregar saltos de página en cualquier celda seleccionada de una hoja de cálculo.

La ubicación de la celda donde se agrega el salto de página, la página termina y el resto de los datos después del salto de página se imprime en la siguiente página al imprimir. En pocas palabras, los saltos de página dividen su hoja de cálculo en múltiples páginas de acuerdo con sus especificaciones. También puedes agregar saltos de página a tus hojas de trabajo en tiempo de ejecución utilizando Aspose.Cells. Aspose.Cells permite a los desarrolladores agregar dos tipos de saltos de página:

- Salto de página horizontal
- Salto de página vertical

En el resto de la discusión, describiremos cómo puedes agregar saltos de página horizontales o verticales en tus hojas de cálculo usando Aspose.Cells.

{{% /alert %}}

## **Saltos de página**

Aspose.Cells proporciona una clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una colección [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) que permite acceder a cada hoja de cálculo en el archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) proporciona una amplia gama de propiedades y métodos utilizados para gestionar una hoja de cálculo.

Para agregar los saltos de página, utiliza las propiedades [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) y [**Worksheet.getHorizontalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHorizontalPageBreaks--) de la clase,.

Las propiedades [**Worksheet.getHorizontalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHorizontalPageBreaks--) y [**Worksheet.getVerticalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getVerticalPageBreaks--) son colecciones que pueden contener varios saltos de página. Cada colección contiene varios métodos para gestionar saltos de página horizontales y verticales.

### **Añadir Saltos de Página**

Para agregar un salto de página en una hoja de trabajo, inserte saltos de página verticales y horizontales en la celda especificada llamando a los métodos [**HorizontalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/horizontalpagebreakcollection/#add-number-number-number-) y [**VerticalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/verticalpagebreakcollection/#add-number-number-number-). Cada método **add** toma el nombre de la celda donde se añadirá el salto.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Add a page break at cell Y30
workbook.getWorksheets().get(0).getHorizontalPageBreaks().add("Y30");
workbook.getWorksheets().get(0).getVerticalPageBreaks().add("Y30");

// Save the Excel file.
workbook.save(path.join(dataDir, "AddingPageBreaks_out.xls"));
```

{{% alert color="primary" %}}

En la vista preliminar de saltos de página o en la vista preliminar de impresión, puedes ver cómo funcionan los saltos de página.

{{% /alert %}}

### **Eliminación de un salto de página específico**

Para eliminar un salto de página específico, llama a los métodos [**HorizontalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/nodejs-cpp/horizontalpagebreakcollection/#removeAt-number-) y [**VerticalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/nodejs-cpp/verticalpagebreakcollection/#removeAt-number-). Cada método **removeAt** toma el índice del salto de página a eliminar.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "PageBreaks.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Removing a specific page break
workbook.getWorksheets().get(0).getHorizontalPageBreaks().removeAt(0);
workbook.getWorksheets().get(0).getVerticalPageBreaks().removeAt(0);

// Save the Excel file.
workbook.save(path.join(dataDir, "RemoveSpecificPageBreak_out.xls"));
```

## **Importante saber**

Cuando configura las propiedades **fitToPages** (que son [**PageSetup.getFitToPagesTall()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesTall--) y [**PageSetup.getFitToPagesWide()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesWide--)) en la configuración de la página, la configuración del salto de página se ve afectada, por lo que, si imprime la hoja de trabajo, la configuración del salto de página no se tendrá en cuenta aunque sigan establecidos.
