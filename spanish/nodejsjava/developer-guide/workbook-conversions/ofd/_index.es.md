---
title: Convertir Excel a formato OFD
linktitle: Convertir Excel a formato OFD
description: Aspose.Cells for Node.js via Java es una biblioteca de hojas de cálculo para trabajar con archivos de hojas de cálculo que admite la conversión de libros de trabajo de Excel al formato OFD (Open Fixed-layout Document). Este artículo demuestra cómo crear contenido de Excel y exportarlo como OFD, así como cómo convertir archivos de Excel existentes a OFD utilizando Aspose.Cells.
keywords: Aspose.Cells, biblioteca de Node.js via Java, hoja de cálculo, Excel a OFD, conversión OFD, SaveFormat.Ofd, documento de diseño fijo, exportación de libro de trabajo
type: docs
weight: 195
url: /es/nodejs-java/converting-excel-to-ofd-format/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells admite la conversión de libros de trabajo de Excel directamente al formato OFD (Open Fixed-layout Document) utilizando el valor de enumeración `SaveFormat.Ofd`. El documento OFD resultante preserva el diseño visible del libro de trabajo, el contenido, las celdas combinadas, los anchos de columna, los altos de fila, las fuentes, los colores, los bordes y los formatos de número. Esto hace que Aspose.Cells sea adecuado para flujos de trabajo de archivado, impresión, presentación regulatoria y gubernamental que requieren un resultado con diseño fijo.

{{% /alert %}}
## **Introducción**
OFD (Open Fixed-layout Document) es un estándar nacional chino (GB/T 33190-2016) para representar documentos digitales en un diseño fijo basado en páginas. Cumple un rol similar al de PDF para casos de uso en los que la apariencia visual del documento de origen debe preservarse exactamente como fue creado. OFD se adopta ampliamente para presentaciones gubernamentales, presentaciones regulatorias, facturas electrónicas y archivado a largo plazo en la República Popular China.

Convertir libros de trabajo de Excel a OFD es un requisito común en escenarios en los que el contenido de la hoja de cálculo debe distribuirse como un artefacto de solo lectura con diseño bloqueado en lugar de como una hoja de cálculo editable. Ejemplos de esto incluyen el envío de una factura finalizada a un cliente, el archivado de un informe financiero trimestral o la presentación de una hoja de cálculo de presupuesto a una autoridad reguladora. Aspose.Cells aborda este requisito mediante el valor de enumeración `SaveFormat.Ofd`, que escribe el libro de trabajo directamente en OFD sin requerir un paso de conversión intermedio. El resultado OFD preserva los valores de las celdas, los rangos combinados, las fuentes, los colores, los bordes, los formatos de número y las opciones de configuración de página configuradas en el libro de trabajo.

{{% alert color="primary" %}}

El resultado OFD generado por Aspose.Cells preserva el diseño visible del libro de trabajo de origen, incluyendo el contenido de las celdas, las celdas combinadas, los anchos de columna y los altos de fila. El formato de celda, como fuentes, colores, bordes, alineación y formatos de número, también se representa en el resultado con diseño fijo. Las opciones de configuración de página configuradas en la hoja de cálculo, como el tamaño del papel, la orientación y el área de impresión, influyen en el diseño del documento OFD resultante.

{{% /alert %}}
## **Crear un libro de trabajo de Excel y guardar como OFD**
Aspose.Cells le permite construir un libro de trabajo mediante programación, llenarlo con datos y luego guardarlo directamente en formato OFD utilizando la enumeración `SaveFormat.Ofd`. El siguiente ejemplo crea una factura desde cero. Agrega un logotipo de la empresa, información de encabezado, una sección de facturación, líneas de artículos y totales calculados, luego exporta el libro de trabajo a un documento OFD.
### **Construir una factura con un logotipo**
El ejemplo construye una hoja de cálculo de factura insertando una imagen de logotipo en el área superior izquierda, completando el nombre de la empresa y los datos de contacto, agregando un título "INVOICE" a través de celdas combinadas, registrando el número y la fecha de la factura, listando los datos del cliente a facturar, construyendo una tabla de líneas de artículos con columnas de descripción, cantidad, precio unitario y total, y calculando el subtotal, el impuesto y el total general mediante fórmulas de celda. Se aplica formato como encabezados en negrita, formato de moneda para precios, bordes y anchos de columna utilizando los objetos `Style` y `Font`. Finalmente, el libro de trabajo se guarda con la extensión `.ofd` utilizando `SaveFormat.Ofd`.

```javascript
let dataDir = "C:\\Temp\\";

// Create a new Workbook
let workbook = new AsposeCells.Workbook();

// Obtain the first worksheet
let worksheet = workbook.getWorksheets().get(0);

// Set column widths
worksheet.getCells().setColumnWidth(0, 5);
worksheet.getCells().setColumnWidth(1, 35);
worksheet.getCells().setColumnWidth(2, 12);
worksheet.getCells().setColumnWidth(3, 15);
worksheet.getCells().setColumnWidth(4, 15);
worksheet.getCells().setColumnWidth(5, 5);

// Insert company logo
worksheet.getPictures().add(1, 1, dataDir + "logo.png");

// Company name and contact details
worksheet.getCells().get("B3").putValue("Acme Corporation");
worksheet.getCells().get("B4").putValue("123 Business Street");
worksheet.getCells().get("B5").putValue("City, State 12345");
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567");

// INVOICE title - merge cells
worksheet.getCells().merge(7, 1, 2, 4);
let titleCell = worksheet.getCells().get("B8");
titleCell.putValue("INVOICE");

let titleStyle = workbook.createStyle();
titleStyle.getFont().setIsBold(true);
titleStyle.getFont().setSize(20);
titleStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.CENTER);
titleCell.setStyle(titleStyle);

// Invoice number and date
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
worksheet.getCells().get("C12").putValue(new Date().toISOString().slice(0, 10));

// Bill-to section
worksheet.getCells().get("B14").putValue("Bill To:");
worksheet.getCells().get("B15").putValue("Client Name");
worksheet.getCells().get("B16").putValue("Client Address");
worksheet.getCells().get("B17").putValue("Client City, State");

// Line items header
let headerDesc = worksheet.getCells().get("B19");
let headerQty = worksheet.getCells().get("C19");
let headerPrice = worksheet.getCells().get("D19");
let headerTotal = worksheet.getCells().get("E19");

headerDesc.putValue("Description");
headerQty.putValue("Quantity");
headerPrice.putValue("Unit Price");
headerTotal.putValue("Total");

let headerStyle = workbook.createStyle();
headerStyle.getFont().setIsBold(true);
headerStyle.getFont().setColor(AsposeCells.Color.getWhite());
headerStyle.setBackgroundColor(AsposeCells.Color.getNavy());
headerStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.CENTER);
headerStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
headerStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
headerStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
headerStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);

headerDesc.setStyle(headerStyle);
headerQty.setStyle(headerStyle);
headerPrice.setStyle(headerStyle);
headerTotal.setStyle(headerStyle);

// Currency style with borders
let currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
currencyStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
currencyStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
currencyStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);

// Plain border style for description/quantity cells
let borderStyle = workbook.createStyle();
borderStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
borderStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
borderStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
borderStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);

// Line items rows
let lineItems = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
];

for (let i = 0; i < lineItems.length; i++)
{
    let row = 20 + i;
    let descCell = worksheet.getCells().get(row, 1);
    let qtyCell = worksheet.getCells().get(row, 2);
    let priceCell = worksheet.getCells().get(row, 3);
    let totalCell = worksheet.getCells().get(row, 4);

    descCell.putValue(lineItems[i][0]);
    qtyCell.putValue(lineItems[i][1]);
    priceCell.putValue(lineItems[i][2]);
    totalCell.setFormula("C" + row + "*D" + row);

    descCell.setStyle(borderStyle);
    qtyCell.setStyle(borderStyle);
    priceCell.setStyle(currencyStyle);
    totalCell.setStyle(currencyStyle);
}

// Subtotal, tax, grand total
worksheet.getCells().get("B24").putValue("Subtotal:");
let subtotalCell = worksheet.getCells().get("E24");
subtotalCell.setFormula("SUM(E20:E22)");

worksheet.getCells().get("B25").putValue("Tax (10%):");
let taxCell = worksheet.getCells().get("E25");
taxCell.setFormula("E24*0.1");

worksheet.getCells().get("B26").putValue("Grand Total:");
let grandTotalCell = worksheet.getCells().get("E26");
grandTotalCell.setFormula("E24+E25");

// Bold + currency style for total values
let totalStyle = workbook.createStyle();
totalStyle.getFont().setIsBold(true);
totalStyle.setCustom("\"$\"#,##0.00");

subtotalCell.setStyle(totalStyle);
taxCell.setStyle(totalStyle);
grandTotalCell.setStyle(totalStyle);

// Bold style for total labels
let boldStyle = workbook.createStyle();
boldStyle.getFont().setIsBold(true);

worksheet.getCells().get("B24").setStyle(boldStyle);
worksheet.getCells().get("B25").setStyle(boldStyle);
worksheet.getCells().get("B26").setStyle(boldStyle);

// Save the workbook as an OFD file
workbook.save(dataDir + "Invoice.ofd", AsposeCells.SaveFormat.Ofd);
```
## **Convertir un archivo de Excel existente a OFD**
Aspose.Cells también puede cargar un libro de trabajo de Excel existente desde el disco y exportarlo directamente a formato OFD. Esto es útil para canalizaciones de conversión por lotes, flujos de trabajo de archivado y escenarios en los que el libro de trabajo de origen fue producido por otra herramienta y solo necesita ser reemitido como un artefacto de diseño fijo. El siguiente ejemplo carga un libro de trabajo `.xlsx` existente, lee datos de sus celdas, aplica ajustes opcionales de configuración de página y guarda el resultado como un documento OFD.

```javascript
const AsposeCells = require("aspose.cells");

const dataDir = "C:\\Examples\\";

// Abrir un libro de Excel existente desde el disco
const workbook = new AsposeCells.Workbook(dataDir + "SampleBook.xlsx");

// (1) Leer y mostrar valores de celdas seleccionadas para confirmar que el archivo fue cargado
const firstSheet = workbook.getWorksheets().get(0);
console.log("First sheet name: " + firstSheet.getName());
console.log("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
console.log("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
console.log("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());

// (2) Iterar sobre la colección de hojas de trabajo para enumerar las hojas disponibles
console.log("\nAvailable worksheets:");
for (let i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    const ws = workbook.getWorksheets().get(i);
    console.log("  [" + i + "] " + ws.getName());
}

// (3) Opcionalmente actualizar una celda de marca de tiempo para reflejar la conversión
firstSheet.getCells().get("A1").putValue("Converted on: " + formatDate(new Date()));

// Agregar una fila de encabezado de resumen en la parte superior del bloque de datos
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");
firstSheet.getCells().get("A2").putValue("Generated: " + formatDate(new Date()));

// (4) Configurar propiedades de PageSetup en la hoja de trabajo
const pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(AsposeCells.PageOrientationType.Landscape);
pageSetup.setPaperSize(AsposeCells.PaperSizeType.PaperA4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);

// (5) Opcionalmente establecer el área de impresión para la salida OFD
const lastRow = firstSheet.getCells().getMaxDataRow();
const lastCol = firstSheet.getCells().getMaxDataColumn();
const lastColLetter = AsposeCells.CellsHelper.columnIndexToName(lastCol);
const printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
console.log("\nPrint area set to: " + printArea);

// (6) Guardar el libro como un archivo OFD
workbook.save(dataDir + "SampleBook.ofd", AsposeCells.SaveFormat.Ofd);
console.log("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");

function formatDate(date) {
    const pad = (n) => n.toString().padStart(2, '0');
    return date.getFullYear() + "-" + pad(date.getMonth() + 1) + "-" + pad(date.getDate()) + " " + pad(date.getHours()) + ":" + pad(date.getMinutes()) + ":" + pad(date.getSeconds());
}
```

## **Artículos relacionados**
- [Dividir archivos de Excel en varios archivos](/cells/es/nodejs-java/splitting-excel-files-into-multiple-files/)
- [Insertar una imagen en una celda](/cells/es/nodejs-java/inserting-an-image-into-a-cell/)
- [Leer y escribir archivos DBF](/cells/es/nodejs-java/dbf/)
- [Convertir minigráfico a imagen y HTML en Aspose.Cells for Node.js via Java](/cells/es/nodejs-java/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="javascript" >}}