---
title: Insertar hipervínculos en la hoja de trabajo
type: docs
weight: 20
url: /es/net/insert-hyperlinks-in-worksheet/
---

## **Aspose.Cells - Insertar hipervínculos en la hoja de trabajo**
**Agregar un enlace a una celda en el mismo archivo**

Es posible agregar hipervínculos a celdas en el mismo archivo de Excel llamando al método Agregar de la colección de hipervínculos. El método Agregar funciona tanto para hipervínculos internos como externos.

**C#**

{{< highlight cs >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

Worksheet sheet = workbook.Worksheets.Add("Hyperlinks");

HyperlinkCollection hyperlinks = sheet.Hyperlinks;

Style style = new Style();

style.Font.Underline = FontUnderlineType.Single;

style.Font.Color = System.Drawing.Color.Blue;

sheet.Cells[0, 0].Value = "URL Link";

hyperlinks.Add(0, 0, 1, 1, "http://www.aspose.com");

sheet.Cells[0, 0].SetStyle(style);

//link to a file in the current directory

sheet.Cells[1, 0].Value = "File Link";

hyperlinks.Add(1, 0, 1, 1, "book1.xls");

sheet.Cells[1, 0].SetStyle(style);

//e-mail link

sheet.Cells[2, 0].Value = "Email Link";

hyperlinks.Add(2, 0, 1, 1, "mailto:marketplace@aspose.com?subject=Hyperlinks");

sheet.Cells[2, 0].SetStyle(style);

//link to a place in this workbook

Worksheet sheet2 = workbook.Worksheets.Add("Target ISheet");

HyperlinkCollection hyperlinks2 = sheet2.Hyperlinks;

sheet2.Cells[3, 0].Value = "Worksheet Link";

hyperlinks2.Add(3, 0, 1, 1, "Target ISheet!A4");

sheet2.Cells[3, 0].SetStyle(style);

workbook.Save("test.xlsx");


{{< /highlight >}}

**Agregar un enlace a un archivo externo**

Es posible agregar hipervínculos a celdas en el mismo archivo de Excel llamando al método Agregar de la colección de hipervínculos. El método Agregar funciona tanto para hipervínculos internos como externos. Una versión del método sobrecargado toma los siguientes parámetros:

- Nombre de la celda, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas en este rango de hipervínculo.
- URL, la dirección de la celda de destino.

**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the first (default) worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in

//the same Excel file

worksheet.Hyperlinks.Add("B3", 1, 1, "Sheet2!B9");

//Saving the Excel file

workbook.Save("C:\\book1.xls");

{{< /highlight >}}
## **NPOI - HSSF XSSF - Insertar hipervínculos en la hoja de trabajo**
**C#**

{{< highlight cs >}}

 IWorkbook workbook = new XSSFWorkbook();

////cell style for hyperlinks

////by default hyperlinks are blue and underlined

ICellStyle hlink_style = workbook.CreateCellStyle();

IFont hlink_font = workbook.CreateFont();

hlink_font.Underline = FontUnderlineType.Single;

hlink_font.Color = HSSFColor.Blue.Index;

hlink_style.SetFont(hlink_font);

ICell cell;

ISheet sheet = workbook.CreateSheet("Hyperlinks");

//URL

cell = sheet.CreateRow(0).CreateCell(0);

cell.SetCellValue("URL Link");

XSSFHyperlink link = new XSSFHyperlink(HyperlinkType.Url);

link.Address = ("http://poi.apache.org/");

cell.Hyperlink = (link);

cell.CellStyle = (hlink_style);

//link to a file in the current directory

cell = sheet.CreateRow(1).CreateCell(0);

cell.SetCellValue("File Link");

link = new XSSFHyperlink(HyperlinkType.File);

link.Address = ("link1.xls");

cell.Hyperlink = (link);

cell.CellStyle = (hlink_style);

//e-mail link

cell = sheet.CreateRow(2).CreateCell(0);

cell.SetCellValue("Email Link");

link = new XSSFHyperlink(HyperlinkType.Email);

//note, if subject contains white spaces, make sure they are url-encoded

link.Address = ("mailto:poi@apache.org?subject=Hyperlinks");

cell.Hyperlink = (link);

cell.CellStyle = (hlink_style);

//link to a place in this workbook

//Create a target sheet and cell

ISheet sheet2 = workbook.CreateSheet("Target ISheet");

sheet2.CreateRow(0).CreateCell(0).SetCellValue("Target ICell");

cell = sheet.CreateRow(3).CreateCell(0);

cell.SetCellValue("Worksheet Link");

link = new XSSFHyperlink(HyperlinkType.Document);

link.Address = ("'Target ISheet'!A1");

cell.Hyperlink = (link);

cell.CellStyle = (hlink_style);

FileStream sw = File.Create("test.xlsx");

workbook.Write(sw);

sw.Close();

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Insertar hipervínculos en la hoja de trabajo** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Insert.Hyperlinks.In.Worksheet.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Para obtener más detalles, visita [Agregar hipervínculos para vincular datos](/cells/es/net/adding-hyperlinks-to-link-data-in-aspose-cells/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
