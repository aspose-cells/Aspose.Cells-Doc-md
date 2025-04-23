---
title: Obteniendo encabezados o pies de página con Node.js vía C++
linktitle: Obteniendo Encabezados o Pies de Página
type: docs
weight: 30
url: /es/nodejs-cpp/get-headers-or-footers/
description: Este artículo explica cómo obtener programáticamente encabezados y pies de página de archivos de Excel u OpenOffice usando la API de Node.js vía C++.
---

{{% alert color="primary" %}}

Los encabezados y pies de página se muestran solo en la vista Diseño de página, en la vista previa de impresión y en las páginas impresas. 

También puedes usar el cuadro de diálogo Configurar página si deseas ver encabezados o pies de página para más de una hoja de cálculo a la vez. 

Para otros tipos de hojas, como hojas de gráficos o gráficos, solo puedes insertar encabezados y pies de página mediante el cuadro de diálogo Configurar página.

{{% /alert %}}

## **Obteniendo Encabezados y Pies de Página en MS Excel**
1. Haz clic en la hoja de cálculo donde deseas ver o cambiar los encabezados o pies de página.
2. En la pestaña Vista, en el grupo Vistas del libro, haga clic en Diseño de página.
   Excel muestra la hoja de cálculo en la vista Diseño de página.
3. Para ver o editar un encabezado o pie de página, haz clic en el cuadro de texto de encabezado o pie de página izquierdo, central o derecho en la parte superior o inferior de la página de la hoja de cálculo (debajo de Encabezado, o encima de Pie de página).


## **Obteniendo encabezados y pies de página usando Aspose.Cells for Node.js via C++**
Con los métodos [**PageSetup.getHeader(number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getHeader-number-) y [**PageSetup.getFooter(number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFooter-number-), los desarrolladores en Node.js pueden simplemente obtener encabezados o pies de página del archivo.

1. Construya un libro de trabajo para abrir el archivo.
2. Obtenga la hoja de cálculo donde desea obtener encabezados o pies de página.
3. Obtenga el encabezado o pie de página con un ID de sección específico.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "HeaderFooter.xlsx");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Gets left section of header
console.log(sheet.getPageSetup().getHeader(0));
// Gets center section of header
console.log(sheet.getPageSetup().getHeader(1));
// Gets right section of header
console.log(sheet.getPageSetup().getHeader(2));
// Gets center section of footer
console.log(sheet.getPageSetup().getFooter(1));
```

## **Analizar Encabezados y Pies de Página para Lista de Comandos**
El texto del encabezado o pie de página puede contener comandos especiales, por ejemplo, un marcador de posición para el número de página, fecha actual o atributos de formato de texto.

Los comandos especiales están representados por una sola letra con un símbolo ampersand inicial ("&").

Las cadenas de encabezado y pie de página se construyen usando la gramática ABNF. No es fácil de entender sin un visor.

Aspose.Cells for Node.js via C++ proporciona el método [**PageSetup.getCommands(string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getCommands-string-) para analizar encabezados y pies de página como una lista de comandos.

El siguiente código muestra cómo analizar el encabezado o pie de página como una lista de comandos y procesar los comandos:

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "HeaderFooter.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Gets left section of header
const headerSection = sheet.getPageSetup().getHeader(0);
const commands = sheet.getPageSetup().getCommands(headerSection) || [];

commands.forEach(c => {
switch (c.getType()) {
case AsposeCells.HeaderFooterCommandType.SheetName:
// embedded the name of the sheet to header or footer
break;
}
```
