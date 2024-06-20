---
title: Copia foglio di lavoro
type: docs
weight: 40
url: /it/net/copy-worksheet/
---

## **Aspose.Cells - Copia foglio di lavoro**
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
## **NPOI - HSSF XSSF - Copia foglio di lavoro**
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
## **Scarica il codice in esecuzione**
Scarica **Copia foglio di lavoro** da uno dei siti di codifica sociale menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.2/Copy.Worksheet.zip)

{{% alert color="primary" %}} 

Per ulteriori dettagli, visita [Working with Worksheets](/cells/it/net/working-with-worksheets-in-npoi-and-aspose-cells/).

{{% /alert %}}
