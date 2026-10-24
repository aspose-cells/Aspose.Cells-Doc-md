---
title: Conversión de Excel al formato OFD
linktitle: Conversión de Excel al formato OFD
description: Aspose.Cells es una biblioteca .NET para trabajar con archivos de hojas de cálculo que admite la conversión de libros de trabajo de Excel al formato OFD (Open Fixed-layout Document). Este artículo demuestra cómo crear contenido en Excel y exportarlo como OFD, así como convertir archivos de Excel existentes a OFD mediante Aspose.Cells.
keywords: Aspose.Cells, biblioteca .NET, hoja de cálculo, conversión de Excel a OFD, conversión a OFD, SaveFormat.Ofd, documento de diseño fijo, exportación de libros de trabajo
type: docs
weight: 195
url: /es/net/converting-excel-to-ofd-format/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells admite la conversión directa de libros de trabajo de Excel al formato OFD (Open Fixed-layout Document) mediante el valor de enumeración `SaveFormat.Ofd`. El documento OFD resultante conserva la disposición visible del libro de trabajo, su contenido, las celdas combinadas, los anchos de columna, las alturas de fila, las fuentes, los colores, los bordes y los formatos de número. Esto hace que Aspose.Cells sea adecuado para flujos de trabajo de archivado e impresión, así como para la presentación de documentación ante organismos reguladores o gubernamentales, cuando se requiere una salida de diseño fijo.
{{% /alert %}}

## **Introducción**
OFD (Open Fixed-layout Document) es un estándar nacional chino (GB/T 33190-2016) para representar documentos digitales con una disposición fija basada en páginas. Cumple una función similar a la de PDF en casos de uso en los que la apariencia visual del documento de origen debe conservarse exactamente como se creó. OFD se utiliza ampliamente en la presentación de documentación ante organismos gubernamentales y reguladores, la facturación electrónica y el archivado a largo plazo en la República Popular China.
La conversión de libros de trabajo de Excel a OFD es una necesidad habitual en escenarios en los que el contenido de las hojas de cálculo deba distribuirse como un documento de solo lectura con la disposición bloqueada, en lugar de como una hoja de cálculo editable. Entre los casos se encuentran enviar una factura finalizada a un cliente, archivar un informe financiero trimestral o presentar una hoja de cálculo presupuestaria a una autoridad reguladora. Aspose.Cells responde a esta necesidad mediante el valor de enumeración `SaveFormat.Ofd`, que escribe el libro de trabajo directamente en formato OFD sin necesidad de un paso de conversión intermedio. El documento OFD resultante conserva los valores de las celdas, los rangos combinados, las fuentes, los colores, los bordes, los formatos de número y las opciones de configuración de página definidas en el libro de trabajo.

{{% alert color="primary" %}}
El documento OFD generado por Aspose.Cells conserva la disposición visible del libro de trabajo de origen, incluido el contenido de las celdas, las celdas combinadas, los anchos de columna y las alturas de fila. También se representa en la salida de diseño fijo el formato de las celdas, como las fuentes, los colores, los bordes, la alineación y los formatos de número. Las opciones de configuración de página definidas en la hoja de cálculo, como el tamaño del papel, la orientación y el área de impresión, influyen en la disposición del documento OFD resultante.
{{% /alert %}}

## **Creación de un libro de trabajo de Excel y guardado como OFD**
Aspose.Cells permite crear un libro de trabajo de forma programática, rellenarlo con datos y guardarlo directamente en formato OFD mediante el valor de enumeración `SaveFormat.Ofd`. El siguiente ejemplo crea una factura desde cero, le añade un logotipo corporativo, información de encabezado, una sección de datos de facturación, partidas y totales calculados y, a continuación, exporta el libro de trabajo a un documento OFD.

### **Creación de una factura con un logotipo**
El ejemplo construye la hoja de cálculo de una factura insertando una imagen de logotipo en el área superior izquierda, introduciendo el nombre de la empresa y los datos de contacto, añadiendo el título "INVOICE" en celdas combinadas, registrando el número y la fecha de la factura, indicando el cliente destinatario, creando una tabla de partidas con columnas de descripción, cantidad, precio unitario y total, y calculando el subtotal, el impuesto y el total general mediante fórmulas. Se aplica formato, como los encabezados en negrita, el formato de moneda de los precios, los bordes y los anchos de las columnas, mediante los objetos `Style` y `Font`. Finalmente, el libro de trabajo se guarda con la extensión `.ofd` usando `SaveFormat.Ofd`.

```csharp
using System;
using Aspose.Cells;
using System.Drawing;
string dataDir = "C:\\Temp\\";
// Crear un nuevo libro de trabajo
Workbook workbook = new Workbook();
// Obtener la primera hoja de cálculo
Worksheet worksheet = workbook.Worksheets[0];
// Establecer los anchos de las columnas
worksheet.Cells.SetColumnWidth(0, 5);
worksheet.Cells.SetColumnWidth(1, 35);
worksheet.Cells.SetColumnWidth(2, 12);
worksheet.Cells.SetColumnWidth(3, 15);
worksheet.Cells.SetColumnWidth(4, 15);
worksheet.Cells.SetColumnWidth(5, 5);
// Insertar el logotipo de la empresa
worksheet.Pictures.Add(1, 1, dataDir + "logo.png");
// Nombre de la empresa y datos de contacto
worksheet.Cells["B3"].PutValue("Acme Corporation");
worksheet.Cells["B4"].PutValue("123 Business Street");
worksheet.Cells["B5"].PutValue("City, State 12345");
worksheet.Cells["B6"].PutValue("Phone: (555) 123-4567");
// Título INVOICE: combinar celdas
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
// Sección de destinatario de la factura
worksheet.Cells["B14"].PutValue("Bill To:");
worksheet.Cells["B15"].PutValue("Client Name");
worksheet.Cells["B16"].PutValue("Client Address");
worksheet.Cells["B17"].PutValue("Client City, State");
// Encabezado de los artículos de línea
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
headerStyle.ForegroundColor = Color.Navy;
headerStyle.Pattern = BackgroundType.Solid;
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
// Estilo de borde simple para las celdas de descripción/cantidad
Style borderStyle = workbook.CreateStyle();
borderStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
// Filas de artículos de línea
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
    totalCell.Formula = "C" + (row + 1) + "*D" + (row + 1);
    descCell.SetStyle(borderStyle);
    qtyCell.SetStyle(borderStyle);
    priceCell.SetStyle(currencyStyle);
    totalCell.SetStyle(currencyStyle);
}
// Subtotal, impuesto y total general
worksheet.Cells["B24"].PutValue("Subtotal:");
Cell subtotalCell = worksheet.Cells["E24"];
subtotalCell.Formula = "SUM(E21:E23)";
worksheet.Cells["B25"].PutValue("Tax (10%):");
Cell taxCell = worksheet.Cells["E25"];
taxCell.Formula = "E24*0.1";
worksheet.Cells["B26"].PutValue("Grand Total:");
Cell grandTotalCell = worksheet.Cells["E26"];
grandTotalCell.Formula = "E24+E25";
// Estilo de negrita y moneda para los valores totales
Style totalStyle = workbook.CreateStyle();
totalStyle.Font.IsBold = true;
totalStyle.Custom = "\"$\"#,##0.00";
subtotalCell.SetStyle(totalStyle);
taxCell.SetStyle(totalStyle);
grandTotalCell.SetStyle(totalStyle);
// Estilo de negrita para las etiquetas de total
Style boldStyle = workbook.CreateStyle();
boldStyle.Font.IsBold = true;
worksheet.Cells["B24"].SetStyle(boldStyle);
worksheet.Cells["B25"].SetStyle(boldStyle);
worksheet.Cells["B26"].SetStyle(boldStyle);
// Guardar el libro de trabajo como un archivo OFD
workbook.Save(dataDir + "Invoice.ofd", SaveFormat.Ofd);
```

## **Conversión de un archivo de Excel existente a OFD**
Aspose.Cells también puede cargar un libro de trabajo de Excel existente desde el disco y exportarlo directamente al formato OFD. Esto resulta útil para flujos de conversión por lotes, flujos de archivado y escenarios en los que el libro de trabajo de origen fue generado por otra herramienta y solo necesita volver a exportarse como un artefacto de diseño fijo. El siguiente ejemplo carga un libro de trabajo `.xlsx` existente, lee los datos de sus celdas, aplica ajustes opcionales a la configuración de página y guarda el resultado como un documento OFD.

```csharp
using System;
using Aspose.Cells;
string dataDir = "C:\\Examples\\";
// Abrir un libro de Excel existente desde el disco
Workbook workbook = new Workbook(dataDir + "SampleBook.xlsx");
// (1) Leer y mostrar los valores de celdas seleccionadas para confirmar que el archivo se cargó
Worksheet firstSheet = workbook.Worksheets[0];
Console.WriteLine("First sheet name: " + firstSheet.Name);
Console.WriteLine("Cell A1: " + firstSheet.Cells["A1"].StringValue);
Console.WriteLine("Cell B1: " + firstSheet.Cells["B1"].StringValue);
Console.WriteLine("Cell C1: " + firstSheet.Cells["C1"].StringValue);
// (2) Recorrer la colección Worksheets para enumerar las hojas disponibles
Console.WriteLine("\nAvailable worksheets:");
for (int i = 0; i < workbook.Worksheets.Count; i++)
{
    Worksheet ws = workbook.Worksheets[i];
    Console.WriteLine("  [" + i + "] " + ws.Name);
}
// (3) Opcionalmente, actualizar una celda de marca de tiempo para reflejar la conversión
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
// (5) Opcionalmente, establecer el área de impresión para la salida OFD
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
- [División de archivos de Excel en varios archivos](/cells/es/net/splitting-excel-files-into-multiple-files/)
- [Inserción de una imagen en una celda](/cells/es/net/inserting-an-image-into-a-cell/)
- [Lectura y escritura de archivos DBF](/cells/es/net/dbf/)

{{< app/cells/assistant language="csharp" >}}