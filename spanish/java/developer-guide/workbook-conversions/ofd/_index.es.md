---
title: Conversión de Excel al formato OFD
linktitle: Conversión de Excel al formato OFD
description: Aspose.Cells es una biblioteca de Java para trabajar con archivos de hojas de cálculo que admite convertir libros de trabajo de Excel al formato OFD (Open Fixed-layout Document). Este artículo muestra cómo crear contenido de Excel y exportarlo como OFD, así como cómo convertir archivos de Excel existentes a OFD utilizando Aspose.Cells.
keywords: Aspose.Cells, biblioteca de Java, hoja de cálculo, Excel a OFD, conversión OFD, SaveFormat.Ofd, documento de diseño fijo, exportación de libro de trabajo
type: docs
weight: 195
url: /es/java/converting-excel-to-ofd-format/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells admite convertir libros de trabajo de Excel directamente al formato OFD (Open Fixed-layout Document) utilizando el valor de enumeración `SaveFormat.Ofd`. El documento OFD resultante preserva el diseño visible del libro de trabajo, el contenido, las celdas combinadas, los anchos de columna, las alturas de fila, las fuentes, los colores, los bordes y los formatos de número. Esto hace que Aspose.Cells sea adecuado para flujos de trabajo de archivo, impresión, presentación regulatoria y gubernamental que requieran una salida de diseño fijo.

{{% /alert %}}
## **Introducción**
OFD (Open Fixed-layout Document) es un estándar nacional chino (GB/T 33190-2016) para representar documentos digitales en un diseño fijo basado en páginas. Cumple un papel similar al de PDF en casos de uso donde la apariencia visual del documento fuente debe preservarse exactamente como se creó. OFD se adopta ampliamente para presentaciones gubernamentales, presentaciones regulatorias, facturas electrónicas y archivado a largo plazo en la República Popular China.

Convertir libros de trabajo de Excel a OFD es un requisito común en escenarios donde el contenido de la hoja de cálculo debe distribuirse como un artefacto de solo lectura con diseño bloqueado en lugar de como una hoja de cálculo editable. Ejemplos incluyen enviar una factura finalizada a un cliente, archivar un informe financiero trimestral o enviar una hoja de cálculo de presupuesto a una autoridad regulatoria. Aspose.Cells aborda este requisito mediante el valor de enumeración `SaveFormat.Ofd`, que escribe el libro de trabajo directamente en OFD sin requerir un paso de conversión intermedio. La salida OFD preserva los valores de las celdas, los rangos combinados, las fuentes, los colores, los bordes, los formatos de número y las opciones de configuración de página configuradas en el libro de trabajo.

{{% alert color="primary" %}}

La salida OFD generada por Aspose.Cells preserva el diseño visible del libro de trabajo fuente, incluyendo el contenido de las celdas, las celdas combinadas, los anchos de columna y las alturas de fila. El formato de las celdas, como fuentes, colores, bordes, alineación y formatos de número, también se representa en la salida de diseño fijo. Las opciones de configuración de página configuradas en la hoja de cálculo, como el tamaño del papel, la orientación y el área de impresión, influyen en el diseño del documento OFD resultante.

{{% /alert %}}
## **Crear un libro de trabajo de Excel y guardar como OFD**
Aspose.Cells le permite construir un libro de trabajo mediante programación, rellenarlo con datos y luego guardarlo directamente en formato OFD utilizando la enumeración `SaveFormat.Ofd`. El siguiente ejemplo crea una factura desde cero. Agrega un logotipo de empresa, información de encabezado, una sección de facturación, líneas de detalle y totales calculados, luego exporta el libro de trabajo a un documento OFD.
### **Construir una factura con un logotipo**
El ejemplo construye una hoja de cálculo de factura insertando una imagen de logotipo en el área superior izquierda, rellenando el nombre de la empresa y los datos de contacto, agregando un título "FACTURA" en celdas combinadas, registrando el número y la fecha de la factura, listando el cliente a facturar, construyendo una tabla de líneas de detalle con columnas de descripción, cantidad, precio unitario y total, y calculando el subtotal, el impuesto y el total general usando fórmulas en las celdas. Se aplica formato, como encabezados en negrita, formato de moneda para precios, bordes y anchos de columna, utilizando los objetos `Style` y `Font`. Finalmente, el libro de trabajo se guarda con la extensión `.ofd` utilizando `SaveFormat.Ofd`.

```java
import com.aspose.cells.*;
import java.text.SimpleDateFormat;
import java.util.Date;

String dataDir = "C:\\Temp\\";

// Crear un nuevo Workbook
Workbook workbook = new Workbook();

// Obtener la primera hoja de cálculo
Worksheet worksheet = workbook.getWorksheets().get(0);

// Establecer anchos de columna
worksheet.getCells().setColumnWidth(0, 5);
worksheet.getCells().setColumnWidth(1, 35);
worksheet.getCells().setColumnWidth(2, 12);
worksheet.getCells().setColumnWidth(3, 15);
worksheet.getCells().setColumnWidth(4, 15);
worksheet.getCells().setColumnWidth(5, 5);

// Insertar logo de la empresa
worksheet.getPictures().add(1, 1, dataDir + "logo.png");

// Nombre de la empresa y datos de contacto
worksheet.getCells().get("B3").putValue("Acme Corporation");
worksheet.getCells().get("B4").putValue("123 Business Street");
worksheet.getCells().get("B5").putValue("City, State 12345");
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567");

// Título de FACTURA - combinar celdas
worksheet.getCells().merge(7, 1, 2, 4);
Cell titleCell = worksheet.getCells().get("B8");
titleCell.putValue("INVOICE");

Style titleStyle = workbook.createStyle();
titleStyle.getFont().setBold(true);
titleStyle.getFont().setSize(20);
titleStyle.setHorizontalAlignment(TextAlignmentType.CENTER);
titleCell.setStyle(titleStyle);

// Número de factura y fecha
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
worksheet.getCells().get("C12").putValue(new SimpleDateFormat("yyyy-MM-dd").format(new Date()));

// Sección de facturar a
worksheet.getCells().get("B14").putValue("Bill To:");
worksheet.getCells().get("B15").putValue("Client Name");
worksheet.getCells().get("B16").putValue("Client Address");
worksheet.getCells().get("B17").putValue("Client City, State");

// Encabezado de líneas de detalle
Cell headerDesc = worksheet.getCells().get("B19");
Cell headerQty = worksheet.getCells().get("C19");
Cell headerPrice = worksheet.getCells().get("D19");
Cell headerTotal = worksheet.getCells().get("E19");

headerDesc.putValue("Description");
headerQty.putValue("Quantity");
headerPrice.putValue("Unit Price");
headerTotal.putValue("Total");

Style headerStyle = workbook.createStyle();
headerStyle.getFont().setBold(true);
headerStyle.getFont().setColor(Color.getWhite());
headerStyle.setBackgroundColor(Color.getNavy());
headerStyle.setHorizontalAlignment(TextAlignmentType.CENTER);
headerStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);

headerDesc.setStyle(headerStyle);
headerQty.setStyle(headerStyle);
headerPrice.setStyle(headerStyle);
headerTotal.setStyle(headerStyle);

// Estilo de moneda con bordes
Style currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);

// Estilo de borde simple para celdas de descripción/cantidad
Style borderStyle = workbook.createStyle();
borderStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);

// Filas de líneas de detalle
Object[][] lineItems = new Object[][] {
    {"Product A - Widget", 2, 50.00},
    {"Product B - Gadget", 3, 75.00},
    {"Product C - Service", 1, 100.00}
};

for (int i = 0; i < lineItems.length; i++)
{
    int row = 20 + i;
    Cell descCell = worksheet.getCells().get(row, 1);
    Cell qtyCell = worksheet.getCells().get(row, 2);
    Cell priceCell = worksheet.getCells().get(row, 3);
    Cell totalCell = worksheet.getCells().get(row, 4);

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
Cell subtotalCell = worksheet.getCells().get("E24");
subtotalCell.setFormula("SUM(E20:E22)");

worksheet.getCells().get("B25").putValue("Tax (10%):");
Cell taxCell = worksheet.getCells().get("E25");
taxCell.setFormula("E24*0.1");

worksheet.getCells().get("B26").putValue("Grand Total:");
Cell grandTotalCell = worksheet.getCells().get("E26");
grandTotalCell.setFormula("E24+E25");

// Estilo en negrita + moneda para valores totales
Style totalStyle = workbook.createStyle();
totalStyle.getFont().setBold(true);
totalStyle.setCustom("\"$\"#,##0.00");

subtotalCell.setStyle(totalStyle);
taxCell.setStyle(totalStyle);
grandTotalCell.setStyle(totalStyle);

// Estilo en negrita para etiquetas de totales
Style boldStyle = workbook.createStyle();
boldStyle.getFont().setBold(true);

worksheet.getCells().get("B24").setStyle(boldStyle);
worksheet.getCells().get("B25").setStyle(boldStyle);
worksheet.getCells().get("B26").setStyle(boldStyle);

// Guardar el libro como un archivo OFD
workbook.save(dataDir + "Invoice.ofd", SaveFormat.Ofd);
```
## **Conversión de un archivo de Excel existente a OFD**
Aspose.Cells también puede cargar un libro de trabajo de Excel existente desde el disco y exportarlo directamente al formato OFD. Esto es útil para pipelines de conversión por lotes, flujos de trabajo de archivado y escenarios donde el libro de trabajo fuente fue producido por otra herramienta y solo necesita ser reemitido como un artefacto de diseño fijo. El siguiente ejemplo carga un libro de trabajo `.xlsx` existente, lee datos de sus celdas, aplica ajustes opcionales de configuración de página y guarda el resultado como un documento OFD.

```java
import com.aspose.cells.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

String dataDir = "C:\\Examples\\";

// Abrir un libro de Excel existente desde el disco
Workbook workbook = new Workbook(dataDir + "SampleBook.xlsx");

// (1) Leer y mostrar valores de celdas seleccionadas para confirmar que el archivo se cargó
Worksheet firstSheet = workbook.getWorksheets().get(0);
System.out.println("First sheet name: " + firstSheet.getName());
System.out.println("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
System.out.println("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
System.out.println("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());

// (2) Iterar sobre la colección Worksheets para enumerar las hojas disponibles
System.out.println("\nAvailable worksheets:");
for (int i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    Worksheet ws = workbook.getWorksheets().get(i);
    System.out.println("  [" + i + "] " + ws.getName());
}

// (3) Opcionalmente actualizar una celda con marca de tiempo para reflejar la conversión
String timestamp1 = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
firstSheet.getCells().get("A1").putValue("Converted on: " + timestamp1);

// Agregar una fila de encabezado de resumen en la parte superior del bloque de datos
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");

String timestamp2 = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
firstSheet.getCells().get("A2").putValue("Generated: " + timestamp2);

// (4) Configurar las propiedades de PageSetup en la hoja de cálculo
PageSetup pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(PageOrientationType.LANDSCAPE);
pageSetup.setPaperSize(PaperSizeType.PAPER_A_4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);

// (5) Opcionalmente establecer el área de impresión para la salida OFD
int lastRow = firstSheet.getCells().getMaxDataRow();
int lastCol = firstSheet.getCells().getMaxDataColumn();
String lastColLetter = CellsHelper.columnIndexToName(lastCol);
String printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
System.out.println("\nPrint area set to: " + printArea);

// (6) Guardar el libro como un archivo OFD
workbook.save(dataDir + "SampleBook.ofd", SaveFormat.Ofd);
System.out.println("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **Artículos relacionados**
- [División de archivos de Excel en varios archivos](/cells/es/java/splitting-excel-files-into-multiple-files/)
- [Inserción de una imagen en una celda](/cells/es/java/inserting-an-image-into-a-cell/)
- [Lectura y escritura de archivos DBF](/cells/es/java/dbf/)
- [Convertir minigráfico a imagen y HTML en Aspose.Cells for Java](/cells/es/java/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="java" >}}