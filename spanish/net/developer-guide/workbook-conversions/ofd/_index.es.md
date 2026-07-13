---
title: Conversión de Excel a formato OFD
linktitle: Conversión de Excel a formato OFD
description: Aspose.Cells es una biblioteca .NET para trabajar con archivos de hojas de cálculo que admite la conversión de libros de trabajo Excel al formato OFD (Open Fixed-layout Document). Este artículo muestra cómo crear contenido de Excel y exportarlo como OFD, así como cómo convertir archivos Excel existentes a OFD usando Aspose.Cells.
keywords: Aspose.Cells, biblioteca .NET, hoja de cálculo, Excel a OFD, conversión OFD, SaveFormat.Ofd, documento de diseño fijo, exportación de libro de trabajo
type: docs
weight: 195
url: /es/net/converting-excel-to-ofd-format/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells admite la conversión de libros de trabajo Excel directamente al formato OFD (Open Fixed-layout Document) utilizando el valor de enumeración `SaveFormat.Ofd`. El documento OFD resultante conserva el diseño visible del libro de trabajo, el contenido, las celdas combinadas, los anchos de columna, los altos de fila, las fuentes, los colores, los bordes y los formatos de número. Esto hace que Aspose.Cells sea adecuado para flujos de trabajo de archivo, impresión, presentación regulatoria y envío a organismos gubernamentales que requieren una salida de diseño fijo.

{{% /alert %}}
## **Introducción**
OFD (Open Fixed-layout Document) es un estándar nacional chino (GB/T 33190-2016) para representar documentos digitales en un diseño fijo basado en páginas. Cumple un papel similar al de PDF para casos de uso en los que la apariencia visual del documento de origen debe conservarse exactamente como fue creada. OFD es ampliamente adoptado para presentaciones ante organismos gubernamentales, declaraciones regulatorias, facturas electrónicas y archivo a largo plazo en la República Popular China.

Convertir libros de trabajo Excel a OFD es un requisito común en escenarios en los que el contenido de la hoja de cálculo debe distribuirse como un artefacto de solo lectura con diseño bloqueado en lugar de como una hoja de cálculo editable. Algunos ejemplos incluyen el envío de una factura finalizada a un cliente, el archivo de un informe financiero trimestral o la presentación de una hoja de cálculo de presupuesto a una autoridad regulatoria. Aspose.Cells aborda este requisito mediante el valor de enumeración `SaveFormat.Ofd`, que escribe el libro de trabajo directamente en OFD sin necesidad de un paso de conversión intermedio. La salida OFD conserva los valores de celda, los rangos combinados, las fuentes, los colores, los bordes, los formatos de número y las opciones de configuración de página configuradas en el libro de trabajo.

{{% alert color="primary" %}}

La salida OFD generada por Aspose.Cells conserva el diseño visible del libro de trabajo de origen, incluido el contenido de las celdas, las celdas combinadas, los anchos de columna y los altos de fila. El formato de celda, como fuentes, colores, bordes, alineación y formatos de número, también se representa en la salida de diseño fijo. Las opciones de configuración de página configuradas en la hoja de cálculo, como el tamaño del papel, la orientación y el área de impresión, influyen en el diseño del documento OFD resultante.

{{% /alert %}}
## **Creación de un libro de Excel y guardado como OFD**
Aspose.Cells permite crear un libro de trabajo mediante programación, rellenarlo con datos y luego guardarlo directamente en formato OFD utilizando la enumeración `SaveFormat.Ofd`. El siguiente ejemplo crea una factura desde cero. Añade un logotipo de la empresa, información de encabezado, una sección de facturación, líneas de detalle y totales calculados, y luego exporta el libro de trabajo a un documento OFD.
### **Construcción de una factura con un logotipo**
El ejemplo construye una hoja de cálculo de factura insertando una imagen de logotipo en el área superior izquierda, rellenando el nombre de la empresa y los datos de contacto, añadiendo un título "INVOICE" en celdas combinadas, registrando el número y la fecha de la factura, listando el cliente facturado, construyendo una tabla de líneas de detalle con columnas de descripción, cantidad, precio unitario y total, y calculando el subtotal, el impuesto y el total general mediante fórmulas de celda. Se aplica formato como encabezados en negrita, formato de moneda para los precios, bordes y anchos de columna utilizando objetos `Style` y `Font`. Finalmente, el libro de trabajo se guarda con la extensión `.ofd` utilizando `SaveFormat.Ofd`.

```csharp
using System;
using Aspose.Cells;
using System.Drawing;

string dataDir = "C:\\Temp\\";

// Crear un nuevo Workbook
Workbook workbook = new Workbook();

// Obtener la primera hoja de trabajo
Worksheet worksheet = workbook.Worksheets[0];

// Establecer anchos de columna
worksheet.Cells.SetColumnWidth(0, 5);
worksheet.Cells.SetColumnWidth(1, 35);
worksheet.Cells.SetColumnWidth(2, 12);
worksheet.Cells.SetColumnWidth(3, 15);
worksheet.Cells.SetColumnWidth(4, 15);
worksheet.Cells.SetColumnWidth(5, 5);

// Insertar logo de la empresa
worksheet.Pictures.Add(1, 1, dataDir + "logo.png");

// Nombre de la empresa y datos de contacto
worksheet.Cells["B3"].PutValue("Acme Corporation");
worksheet.Cells["B4"].PutValue("123 Business Street");
worksheet.Cells["B5"].PutValue("City, State 12345");
worksheet.Cells["B6"].PutValue("Phone: (555) 123-4567");

// Título FACTURA - combinar celdas
worksheet.Cells.Merge(7, 1, 2, 4);
Cell titleCell = worksheet.Cells["B8"];
titleCell.PutValue("INVOICE");

Style titleStyle = workbook.CreateStyle();
titleStyle.Font.IsBold = true;
titleStyle.Font.Size = 20;
titleStyle.HorizontalAlignment = TextAlignmentType.Center;
titleCell.SetStyle(titleStyle);

// Número de factura y fecha
worksheet.Cells["B11"].PutValue("Invoice Number:");
worksheet.Cells["C11"].PutValue("INV-2024-001");
worksheet.Cells["B12"].PutValue("Date:");
worksheet.Cells["C12"].PutValue(DateTime.Now.ToString("yyyy-MM-dd"));

// Sección Facturar a
worksheet.Cells["B14"].PutValue("Bill To:");
worksheet.Cells["B15"].PutValue("Client Name");
worksheet.Cells["B16"].PutValue("Client Address");
worksheet.Cells["B17"].PutValue("Client City, State");

// Encabezado de líneas de detalle
Cell headerDesc = worksheet.Cells["B19"];
Cell headerQty = worksheet.Cells["C19"];
Cell headerPrice = worksheet.Cells["D19"];
Cell headerTotal = worksheet.Cells["E19"];

headerDesc.PutValue("Description");
headerQty.PutValue("Quantity");
headerPrice.PutValue("Unit Price");
headerTotal.PutValue("Total");

Style headerStyle = workbook.CreateStyle();
headerStyle.Font.IsBold = true;
headerStyle.Font.Color = Color.White;
headerStyle.BackgroundColor = Color.Navy;
headerStyle.HorizontalAlignment = TextAlignmentType.Center;
headerStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

headerDesc.SetStyle(headerStyle);
headerQty.SetStyle(headerStyle);
headerPrice.SetStyle(headerStyle);
headerTotal.SetStyle(headerStyle);

// Estilo de moneda con bordes
Style currencyStyle = workbook.CreateStyle();
currencyStyle.Custom = "\"$\"#,##0.00";
currencyStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

// Estilo de borde simple para celdas de descripción/cantidad
Style borderStyle = workbook.CreateStyle();
borderStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

// Filas de líneas de detalle
object[,] lineItems = new object[,] {
    {"Product A - Widget", 2, 50.00},
    {"Product B - Gadget", 3, 75.00},
    {"Product C - Service", 1, 100.00}
};

for (int i = 0; i < lineItems.GetLength(0); i++)
{
    int row = 20 + i;
    Cell descCell = worksheet.Cells[row, 1];
    Cell qtyCell = worksheet.Cells[row, 2];
    Cell priceCell = worksheet.Cells[row, 3];
    Cell totalCell = worksheet.Cells[row, 4];

    descCell.PutValue(lineItems[i, 0]);
    qtyCell.PutValue(lineItems[i, 1]);
    priceCell.PutValue(lineItems[i, 2]);
    totalCell.Formula = "C" + row + "*D" + row;

    descCell.SetStyle(borderStyle);
    qtyCell.SetStyle(borderStyle);
    priceCell.SetStyle(currencyStyle);
    totalCell.SetStyle(currencyStyle);
}

// Subtotal, impuesto, total general
worksheet.Cells["B24"].PutValue("Subtotal:");
Cell subtotalCell = worksheet.Cells["E24"];
subtotalCell.Formula = "SUM(E20:E22)";

worksheet.Cells["B25"].PutValue("Tax (10%):");
Cell taxCell = worksheet.Cells["E25"];
taxCell.Formula = "E24*0.1";

worksheet.Cells["B26"].PutValue("Grand Total:");
Cell grandTotalCell = worksheet.Cells["E26"];
grandTotalCell.Formula = "E24+E25";

// Estilo negrita + moneda para valores totales
Style totalStyle = workbook.CreateStyle();
totalStyle.Font.IsBold = true;
totalStyle.Custom = "\"$\"#,##0.00";

subtotalCell.SetStyle(totalStyle);
taxCell.SetStyle(totalStyle);
grandTotalCell.SetStyle(totalStyle);

// Estilo negrita para etiquetas de totales
Style boldStyle = workbook.CreateStyle();
boldStyle.Font.IsBold = true;

worksheet.Cells["B24"].SetStyle(boldStyle);
worksheet.Cells["B25"].SetStyle(boldStyle);
worksheet.Cells["B26"].SetStyle(boldStyle);

// Guardar el libro como archivo OFD
workbook.Save(dataDir + "Invoice.ofd", SaveFormat.Ofd);
```
## **Conversión de un archivo Excel existente a OFD**
Aspose.Cells también puede cargar un libro de trabajo Excel existente desde el disco y exportarlo directamente al formato OFD. Esto resulta útil para canalizaciones de conversión por lotes, flujos de trabajo de archivo y escenarios en los que el libro de trabajo de origen fue producido por otra herramienta y solo necesita volver a emitirse como un artefacto de diseño fijo. El siguiente ejemplo carga un libro de trabajo `.xlsx` existente, lee los datos de sus celdas, aplica ajustes opcionales de configuración de página y guarda el resultado como un documento OFD.

```csharp
using System;
using Aspose.Cells;

string dataDir = "C:\\Examples\\";

// Abrir un libro de Excel existente desde el disco
Workbook workbook = new Workbook(dataDir + "SampleBook.xlsx");

// (1) Leer y mostrar valores de celdas seleccionadas para confirmar que el archivo se cargó
Worksheet firstSheet = workbook.Worksheets[0];
Console.WriteLine("First sheet name: " + firstSheet.Name);
Console.WriteLine("Cell A1: " + firstSheet.Cells["A1"].StringValue);
Console.WriteLine("Cell B1: " + firstSheet.Cells["B1"].StringValue);
Console.WriteLine("Cell C1: " + firstSheet.Cells["C1"].StringValue);

// (2) Iterar sobre la colección Worksheets para enumerar las hojas disponibles
Console.WriteLine("\nAvailable worksheets:");
for (int i = 0; i < workbook.Worksheets.Count; i++)
{
    Worksheet ws = workbook.Worksheets[i];
    Console.WriteLine("  [" + i + "] " + ws.Name);
}

// (3) Opcionalmente actualizar una celda de marca de tiempo para reflejar la conversión
firstSheet.Cells["A1"].PutValue("Converted on: " + DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));

// Agregar una fila de encabezado de resumen en la parte superior del bloque de datos
firstSheet.Cells.InsertRow(0);
firstSheet.Cells["A1"].PutValue("Conversion Summary");
firstSheet.Cells["A2"].PutValue("Generated: " + DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));

// (4) Configurar las propiedades de PageSetup en la hoja de cálculo
PageSetup pageSetup = firstSheet.PageSetup;
pageSetup.Orientation = PageOrientationType.Landscape;
pageSetup.PaperSize = PaperSizeType.PaperA4;
pageSetup.FitToPagesTall = 1;
pageSetup.FitToPagesWide = 1;

// (5) Opcionalmente establecer el área de impresión para la salida OFD
int lastRow = firstSheet.Cells.MaxDataRow;
int lastCol = firstSheet.Cells.MaxDataColumn;
string lastColLetter = CellsHelper.ColumnIndexToName(lastCol);
string printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.PageSetup.PrintArea = printArea;
Console.WriteLine("\nPrint area set to: " + printArea);

// (6) Guardar el libro como un archivo OFD
workbook.Save(dataDir + "SampleBook.ofd", SaveFormat.Ofd);
Console.WriteLine("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **Artículos relacionados**
- [Splitting Excel Files into Multiple Files](/cells/es/net/splitting-excel-files-into-multiple-files/)
- [Inserting an Image into a Cell](/cells/es/net/inserting-an-image-into-a-cell/)
- [Reading and Writing DBF Files](/cells/es/net/dbf/)
- [Convert Sparkline to Image and HTML in Aspose.Cells for .NET](/cells/es/net/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="csharp" >}}