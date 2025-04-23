---
title: Skapa ny arbetsbok
type: docs
weight: 20
url: /sv/net/create-new-workbook/
---

## **Aspose.Cells - Skapa ny arbetsbok**
Workbook-klass är tillgänglig för enkel användning

**C#**

{{< highlight cs >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

workbook.Save("test.xlsx", SaveFormat.Xlsx); //Workbooks can be saved in many formats

{{< /highlight >}}
## **NPOI - HSSF XSSF - Skapa ny arbetsbok**
Skapa ny arbetsbok med hjälp av Workbook-klassen och spara med FileOutputStream.

**C#**

{{< highlight cs >}}

 IWorkbook workbook = new XSSFWorkbook();

workbook.CreateSheet("Sheet A1");

workbook.CreateSheet("Sheet A2");

workbook.CreateSheet("Sheet A3");

FileStream sw = File.Create("test.xlsx");

workbook.Write(sw);

sw.Close();

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ner **Skapa ny arbetsbok** från någon av de nedan angivna sociala kodningssidorna:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Create.New.Workbook.Aspose.Cells.zip)
{{< app/cells/assistant language="csharp" >}}
