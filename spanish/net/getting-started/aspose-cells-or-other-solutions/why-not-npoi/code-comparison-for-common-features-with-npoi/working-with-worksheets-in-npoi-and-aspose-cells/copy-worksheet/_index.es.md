---
title: Copiar Hoja de Cálculo
type: docs
weight: 40
url: /es/net/copy-worksheet/
---

## **Aspose.Cells - Copiar Hoja de Cálculo**
**C#**

{{< highlight cs >}}

 //Create a new Workbook by excel file path

Workbook wb = new Workbook("../../data/workbook.xlsx");

//Create a Worksheets object with reference to the sheets of the Workbook.

WorksheetCollection sheets = wb.Worksheets;

//Copy data to a new sheet from an existing sheet within the Workbook.

sheets.AddCopy("Sheet1");

wb.Save("../../data/workbook.xlsx");


{{< /highlight >}}
## **NPOI - HSSF XSSF - Copiar Hoja de Cálculo**
**C#**

{{< highlight cs >}}

 IWorkbook wb = new XSSFWorkbook();

wb.CreateSheet("new sheet");

wb.CreateSheet("second sheet");

ISheet cloneSheet = wb.CloneSheet(0);

FileStream sw = File.Create("newWorksheet.xls");

wb.Write(sw);

sw.Close();


{{< /highlight >}}
## **Descargar Código en Ejecución**
Descarga **Copiar Hoja de Cálculo** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.2/Copy.Worksheet.zip)

{{% alert color="primary" %}} 

Para más detalles, visita [Trabajando con Hojas de Cálculo](/cells/es/net/working-with-worksheets-in-npoi-and-aspose-cells/).

{{% /alert %}}
