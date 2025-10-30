---
title: Configurar opciones de impresión con Node.js vía C++
linktitle: Configuración de Opciones de Impresión
type: docs
weight: 40
url: /es/nodejs-cpp/setting-print-options/
description: Este artículo demuestra cómo configurar programáticamente las opciones de impresión de la función de configuración de página de hojas de cálculo de Excel usando la API de Node.js y la biblioteca C++. Puedes establecer el área de impresión, títulos de impresión y orden de página.
keywords: establecer área de impresión en excel desde Node.js vía C++, establecer títulos de impresión en excel desde Node.js vía C++, establecer orden de página en excel desde Node.js vía C++
---

{{% alert color="primary" %}}

La configuración de página de Microsoft Excel proporciona varias opciones de impresión (también conocidas como opciones de hoja) que permiten a los usuarios controlar cómo se imprimen las páginas de la hoja de cálculo.

{{% /alert %}}

## **Configuración de Opciones de Impresión**

Estas opciones de impresión permiten a los usuarios:

- Seleccionar un área de impresión específica en una hoja de cálculo.
- Títulos de impresión.
- Líneas de cuadrícula de impresión.
- Encabezados de fila/columna de impresión.
- Lograr calidad de borrador.
- Comentarios de impresión.
- Errores de celda de impresión.
- Definir el orden de páginas.

Aspose.Cells for Node.js via C++ soporta todas las opciones de impresión ofrecidas por Microsoft Excel y los desarrolladores pueden configurar fácilmente estas opciones para las hojas de cálculo usando las propiedades ofrecidas por la clase [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup). Cómo se usan estas propiedades se discute a continuación con más detalle.

### **Establecer Área de Impresión**

De forma predeterminada, el área de impresión abarca todas las áreas de la hoja de cálculo que contienen datos. Los desarrolladores pueden establecer un área de impresión específica de la hoja de cálculo.

Para seleccionar un área de impresión específica, utilice la propiedad [**PageSetup.getPrintArea()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintArea--) de la clase [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup). Asigne un rango de celdas que defina el área de impresión a esta propiedad.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Specifying the cells range (from A1 cell to T35 cell) of the print area
pageSetup.setPrintArea("A1:T35");

// Save the workbook.
workbook.save(path.join(dataDir, "SetPrintArea_out.xls"));
```

### **Establecer Títulos de Impresión**

Aspose.Cells le permite designar encabezados de fila y columna para repetir en todas las páginas de una hoja de cálculo impresa. Para hacerlo, utilice las propiedades [**PageSetup.getPrintTitleColumns()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintTitleColumns--) y [**PageSetup.getPrintTitleRows()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintTitleRows--) de la clase [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup).

Las filas o columnas que se repetirán se definen pasando sus números de fila o columna. Por ejemplo, las filas se definen como $1:$2 y las columnas se definen como $A:$B.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Defining column numbers A & B as title columns
pageSetup.setPrintTitleColumns("$A:$B");

// Defining row numbers 1 & 2 as title rows
pageSetup.setPrintTitleRows("$1:$2");

// Save the workbook.
workbook.save(path.join(dataDir, "SetPrintTitle_out.xls"));
```

### **Establecer Otras Opciones de Impresión**

La clase [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) también proporciona varias otras propiedades para establecer opciones generales de impresión como sigue:

- [**PageSetup.getPrintGridlines()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintGridlines--): una propiedad booleana que define si imprimir o no las líneas de cuadrícula.
- [**PageSetup.getPrintHeadings()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintHeadings--): una propiedad booleana que define si imprimir o no encabezados de filas y columnas.
- [**PageSetup.getBlackAndWhite()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getBlackAndWhite--): una propiedad booleana que define si imprimir la hoja de cálculo en modo blanco y negro o no.
- [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--): define si mostrar los comentarios de impresión en la hoja de cálculo o al final de la hoja.
- [**PageSetup.getPrintDraft()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintDraft--): una propiedad booleana que define si imprimir la hoja sin gráficos.
- [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--): define si se deben imprimir los errores de celda como se muestra, en blanco, como guion o N/A.

Para configurar las propiedades [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--) y [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--), Aspose.Cells for Node.js via C++ también proporciona dos enumeraciones, [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) y [**PrintErrorsType**](https://reference.aspose.com/cells/nodejs-cpp/printerrorstype) que contienen valores predefinidos para asignar a las propiedades [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--) y [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--) respectivamente.

Los valores predefinidos en la enumeración [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) se muestran a continuación con sus descripciones.

|**Tipos de Imprimir Comentarios**|**Descripción**|
| :- | :- |
|PrintInPlace| Especifica imprimir comentarios como se muestra en la hoja de cálculo.
|PrintNoComments| Especifica no imprimir comentarios.
|PrintSheetEnd| Especifica imprimir comentarios al final de la hoja de cálculo.

Los valores predefinidos de la enumeración [**PrintErrorsType**](https://reference.aspose.com/cells/nodejs-cpp/printerrorstype) se muestran a continuación con sus descripciones.

|**Tipos de Imprimir Errores**|**Descripción**|
| :- | :- |
|PrintErrorsBlank| Especifica no imprimir errores.
|PrintErrorsDash| Especifica imprimir errores como "--".
|PrintErrorsDisplayed| Especifica imprimir errores como se muestra.
|PrintErrorsNA| Especifica imprimir errores como "#N/A".

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Allowing to print gridlines
pageSetup.setPrintGridlines(true);

// Allowing to print row/column headings
pageSetup.setPrintHeadings(true);

// Allowing to print worksheet in black & white mode
pageSetup.setBlackAndWhite(true);

// Allowing to print comments as displayed on worksheet
pageSetup.setPrintComments(AsposeCells.PrintCommentsType.PrintInPlace);

// Allowing to print worksheet with draft quality
pageSetup.setPrintDraft(true);

// Allowing to print cell errors as N/A
pageSetup.setPrintErrors(AsposeCells.PrintErrorsType.PrintErrorsNA);

// Save the workbook.
workbook.save(path.join(dataDir, "OtherPrintOptions_out.xls"));
```

### **Establecer Orden de Páginas**

La clase [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) proporciona la propiedad [**PageSetup.getOrder()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getOrder--) que se usa para ordenar varias páginas de su hoja de cálculo para su impresión. Hay dos posibilidades para ordenar las páginas de la siguiente manera.

- **Hacia abajo y luego hacia la derecha:** imprime todas las páginas hacia abajo antes de imprimir cualquier página hacia la derecha.
- **Hacia la derecha y luego hacia abajo:** imprime las páginas de izquierda a derecha antes de imprimir las páginas por debajo.

Aspose.Cells proporciona una enumeración, [**PrintOrderType**](https://reference.aspose.com/cells/nodejs-cpp/printordertype) que contiene todos los tipos de orden predefinidos.

Los valores predefinidos de la enumeración [**PrintOrderType**](https://reference.aspose.com/cells/nodejs-cpp/printordertype) se muestran a continuación.

|**Tipos de Orden de Impresión**|**Descripción**|
| :- | :- |
|DownThenOver|Representa el orden de impresión como primero hacia abajo y luego hacia adelante.|
|OverThenDown|Representa el orden de impresión como primero hacia adelante y luego hacia abajo.|

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Setting the printing order of the pages to over then down
pageSetup.setOrder(AsposeCells.PrintOrderType.OverThenDown);

// Save the workbook.
workbook.save(path.join(dataDir, "SetPageOrder_out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
