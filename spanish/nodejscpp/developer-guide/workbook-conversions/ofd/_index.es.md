---
title: Conversión de Excel a formato OFD
linktitle: Conversión de Excel a formato OFD
description: Aspose.Cells es una biblioteca de Node.js para trabajar con archivos de hojas de cálculo que admite la conversión de libros de trabajo de Excel a formato OFD (Open Fixed-layout Document). Este artículo demuestra cómo crear contenido de Excel y exportarlo como OFD, así como cómo convertir archivos Excel existentes a OFD utilizando Aspose.Cells.
keywords: Aspose.Cells, biblioteca Node.js, hoja de cálculo, Excel a OFD, conversión OFD, SaveFormat.Ofd, documento de diseño fijo, exportación de libro de trabajo
type: docs
weight: 195
url: /es/nodejs-cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells admite la conversión de libros de trabajo de Excel directamente al formato OFD (Open Fixed-layout Document) utilizando el valor de enumeración `SaveFormat.Ofd`. El documento OFD resultante conserva el diseño visible, el contenido, las celdas combinadas, los anchos de columna, las alturas de fila, las fuentes, los colores, los bordes y los formatos de número del libro de trabajo. Esto hace que Aspose.Cells sea adecuado para flujos de trabajo de archivado, impresión, presentación regulatoria y trámites gubernamentales que requieren una salida de diseño fijo.

{{% /alert %}}
## **Introducción**
OFD (Open Fixed-layout Document) es un estándar nacional chino (GB/T 33190-2016) para representar documentos digitales en un diseño fijo basado en páginas. Cumple un papel similar al de PDF en casos de uso donde la apariencia visual del documento de origen debe conservarse exactamente como fue creado. OFD es ampliamente adoptado para presentaciones gubernamentales, presentaciones regulatorias, facturas electrónicas y archivado a largo plazo en la República Popular China.

Convertir libros de trabajo de Excel a OFD es un requisito común en escenarios donde el contenido de la hoja de cálculo debe distribuirse como un artefacto de solo lectura y diseño bloqueado en lugar de como una hoja de cálculo editable. Los ejemplos incluyen enviar una factura finalizada a un cliente, archivar un informe financiero trimestral o presentar una hoja de cálculo de presupuesto a una autoridad reguladora. Aspose.Cells aborda este requisito a través del valor de enumeración `SaveFormat.Ofd`, que escribe el libro de trabajo directamente a OFD sin necesidad de un paso de conversión intermedio. La salida OFD conserva los valores de celda, los rangos combinados, las fuentes, los colores, los bordes, los formatos de número y las opciones de configuración de página configuradas en el libro de trabajo.

{{% alert color="primary" %}}

La salida OFD generada por Aspose.Cells conserva el diseño visible del libro de trabajo de origen, incluyendo el contenido de las celdas, las celdas combinadas, los anchos de columna y las alturas de fila. El formato de celda como fuentes, colores, bordes, alineación y formatos de número también se representa en la salida de diseño fijo. Las opciones de configuración de página configuradas en la hoja de cálculo, como el tamaño del papel, la orientación y el área de impresión, influyen en el diseño del documento OFD resultante.

{{% /alert %}}
## **Crear un libro de trabajo de Excel y guardar como OFD**
Aspose.Cells le permite crear un libro de trabajo mediante programación, rellenarlo con datos y luego guardarlo directamente en formato OFD utilizando la enumeración `SaveFormat.Ofd`. El siguiente ejemplo crea una factura desde cero. Añade un logotipo de la empresa, información de encabezado, una sección de facturación, líneas de detalle y totales calculados, y luego exporta el libro de trabajo a un documento OFD.
### **Crear una factura con un logotipo**
El ejemplo construye una hoja de cálculo de factura insertando una imagen de logotipo en el área superior izquierda, rellenando el nombre de la empresa y los datos de contacto, añadiendo un título "INVOICE" a través de celdas combinadas, registrando el número y la fecha de la factura, listando el cliente facturado, construyendo una tabla de líneas de detalle con columnas de descripción, cantidad, precio unitario y total, y calculando el subtotal, el impuesto y el total general utilizando fórmulas de celda. El formato, como encabezados en negrita, formato de moneda para precios, bordes y anchos de columna, se aplica utilizando los objetos `Style` y `Font`. Finalmente, el libro de trabajo se guarda con la extensión `.ofd` utilizando `SaveFormat.Ofd`.

```javascript
let dataDir = "C:\\Temp\\";

// Crear un nuevo Workbook
let workbook = new AsposeCells.Workbook();

// Obtener la primera hoja de trabajo
let worksheet = workbook.getWorksheets().get(0);

// Establecer anchos de columna
worksheet.getCells().setColumnWidth(0, 5);
worksheet.getCells().setColumnWidth(1, 35);
worksheet.getCells().setColumnWidth(2, 12);
worksheet.getCells().setColumnWidth(3, 15);
worksheet.getCells().setColumnWidth(4, 15);
worksheet.getCells().setColumnWidth(5, 5);

// Insertar el logo de la empresa
worksheet.getPictures().add(1, 1, dataDir + "logo.png");

// Nombre de la empresa y datos de contacto
worksheet.getCells().get("B3").putValue("Acme Corporation");
worksheet.getCells().get("B4").putValue("123 Business Street");
worksheet.getCells().get("B5").putValue("City, State 12345");
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567");

// Título FACTURA - combinar celdas
worksheet.getCells().merge(7, 1, 2, 4);
let titleCell = worksheet.getCells().get("B8");
titleCell.putValue("INVOICE");

let titleStyle = workbook.createStyle();
titleStyle.getFont().setIsBold(true);
titleStyle.getFont().setSize(20);
titleStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
titleCell.setStyle(titleStyle);

// Número de factura y fecha
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
let now = new Date();
let dateStr = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')}`;
worksheet.getCells().get("C12").putValue(dateStr);

// Sección de facturación
worksheet.getCells().get("B14").putValue("Bill To:");
worksheet.getCells().get("B15").putValue("Client Name");
worksheet.getCells().get("B16").putValue("Client Address");
worksheet.getCells().get("B17").putValue("Client City, State");

// Encabezado de líneas de detalle
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
headerStyle.getFont().setColor(AsposeCells.Color.White);
headerStyle.setBackgroundColor(AsposeCells.Color.Navy);
headerStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);

headerDesc.setStyle(headerStyle);
headerQty.setStyle(headerStyle);
headerPrice.setStyle(headerStyle);
headerTotal.setStyle(headerStyle);

// Estilo de moneda con bordes
let currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);

// Estilo de borde simple para celdas de descripción/cantidad
let borderStyle = workbook.createStyle();
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);

// Filas de líneas de detalle
let lineItems = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
];

for (let i = 0; i < lineItems.length; i++) {
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

// Subtotal, impuesto, total general
worksheet.getCells().get("B24").putValue("Subtotal:");
let subtotalCell = worksheet.getCells().get("E24");
subtotalCell.setFormula("SUM(E20:E22)");

worksheet.getCells().get("B25").putValue("Tax (10%):");
let taxCell = worksheet.getCells().get("E25");
taxCell.setFormula("E24*0.1");

worksheet.getCells().get("B26").putValue("Grand Total:");
let grandTotalCell = worksheet.getCells().get("E26");
grandTotalCell.setFormula("E24+E25");

// Estilo negrita + moneda para valores totales
let totalStyle = workbook.createStyle();
totalStyle.getFont().setIsBold(true);
totalStyle.setCustom("\"$\"#,##0.00");

subtotalCell.setStyle(totalStyle);
taxCell.setStyle(totalStyle);
grandTotalCell.setStyle(totalStyle);

// Estilo negrita para etiquetas de totales
let boldStyle = workbook.createStyle();
boldStyle.getFont().setIsBold(true);

worksheet.getCells().get("B24").setStyle(boldStyle);
worksheet.getCells().get("B25").setStyle(boldStyle);
worksheet.getCells().get("B26").setStyle(boldStyle);

// Guardar el libro como archivo OFD
workbook.save(dataDir + "Invoice.ofd", AsposeCells.SaveFormat.Ofd);
```
## **Convertir un archivo Excel existente a OFD**
Aspose.Cells también puede cargar un libro de trabajo de Excel existente desde el disco y exportarlo directamente a formato OFD. Esto resulta útil para pipelines de conversión por lotes, flujos de trabajo de archivado y escenarios donde el libro de trabajo de origen fue producido por otra herramienta y solo necesita ser reemitido como un artefacto de diseño fijo. El siguiente ejemplo carga un libro de trabajo `.xlsx` existente, lee datos de sus celdas, aplica ajustes opcionales de configuración de página y guarda el resultado como un documento OFD.

```javascript
let workbook = new AsposeCells.Workbook(dataDir + "SampleBook.xlsx");

// (1) Leer y mostrar valores de las celdas seleccionadas para confirmar que el archivo fue cargado
let firstSheet = workbook.getWorksheets().get(0);
console.log("First sheet name: " + firstSheet.getName());
console.log("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
console.log("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
console.log("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());

// (2) Iterar sobre la colección de Worksheets para enumerar las hojas disponibles
console.log("\nAvailable worksheets:");
for (let i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    let ws = workbook.getWorksheets().get(i);
    console.log("  [" + i + "] " + ws.getName());
}

// (3) Opcionalmente actualizar una celda con marca de tiempo para reflejar la conversión
firstSheet.getCells().get("A1").putValue("Converted on: " + formatDate(new Date()));

// Agregar una fila de encabezado de resumen en la parte superior del bloque de datos
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");
firstSheet.getCells().get("A2").putValue("Generated: " + formatDate(new Date()));

// (4) Configurar las propiedades de PageSetup en la hoja de cálculo
let pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(AsposeCells.PageOrientationType.Landscape);
pageSetup.setPaperSize(AsposeCells.PaperSizeType.PaperA4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);

// (5) Opcionalmente establecer el área de impresión para la salida OFD
let lastRow = firstSheet.getCells().getMaxDataRow();
let lastCol = firstSheet.getCells().getMaxDataColumn();
let lastColLetter = AsposeCells.CellsHelper.columnIndexToName(lastCol);
let printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
console.log("\nPrint area set to: " + printArea);

// (6) Guardar el libro de trabajo como un archivo OFD
workbook.save(dataDir + "SampleBook.ofd", AsposeCells.SaveFormat.Ofd);
console.log("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **Artículos relacionados**
- [Dividir archivos Excel en varios archivos](/cells/es/nodejs-cpp/splitting-excel-files-into-multiple-files/)
- [Insertar una imagen en una celda](/cells/es/nodejs-cpp/inserting-an-image-into-a-cell/)
- [Leer y escribir archivos DBF](/cells/es/nodejs-cpp/dbf/)
- [Convertir minigráfico a imagen y HTML en Aspose.Cells for Node.js mediante C++](/cells/es/nodejs-cpp/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="javascript" >}}