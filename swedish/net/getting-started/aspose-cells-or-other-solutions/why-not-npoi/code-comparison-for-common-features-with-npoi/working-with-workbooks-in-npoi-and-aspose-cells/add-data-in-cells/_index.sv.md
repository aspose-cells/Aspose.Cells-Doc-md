---
title: Lägg till data på Cells
type: docs
weight: 10
url: /sv/net/add-data-in-cells/
description: "Den här artikeln förklarar hur du lägger till data i Cells med Aspose.Cells for .NET API:er."
keywords: C# Add Data in Cells, C# Insert Data to Worksheet, C# Set Data of Cell.
---
##  **Hur lägger till data i Cells med Aspose.Cells for .NET**
Aspose.Cells tillhandahåller en klass, arbetsbok, som representerar en Microsoft Excel-fil. Workbook-klassen innehåller en WorksheetCollection som ger åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen Worksheet. Klassen Worksheet tillhandahåller en Cellscollection. Varje föremål i samlingen Cells representerar ett föremål i klassen Cell.

**C#**

{{< highlight "cs" >}}

 //Instantiering av ett arbetsboksobjekt

Arbetsbok arbetsbok = ny arbetsbok();

//Åtkomst till det tillagda kalkylbladet i Excel-filen

Arbetsblad arbetsblad = arbetsbok. Arbetsblad[0];

int x = 1;

för (int i = 1; i<= 15; i++)

{

    for (int j = 0; j < 15; j++)

    {

        worksheet.Cells[i, j].Value = x++;

    }

}

workbook.Save("test.xlsx");


{{< /highlight >}}
##  **NPOI HSSF XSSF - Lägg till data i Cells**
I NPOI kan row.createCell(1).setCellValue användas för att lägga till data i celler.

**C#**

{{< highlight "cs" >}}

 IWorkbook-arbetsbok = ny XSSFWorkbook();

ISark sheet1 = workbook.CreateSheet("Sheet1");

sheet1.CreateRow(0).CreateCell(0).SetCellValue("Detta är ett prov");

int x = 1;

för (int i = 1; i<= 15; i++)

{

	IRow row = sheet1.CreateRow(i);

	for (int j = 0; j < 15; j++)

	{

		row.CreateCell(j).SetCellValue(x++);

	}

}

FileStream sw = File.Create("test.xlsx");

workbook.Write(sw);

sw.Close();

{{< /highlight >}}
##  **Ladda ner Running Code**
 Ladda ner**Lägg till data på Cells** bilda någon av nedan nämnda sociala kodningswebbplatser:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 För mer information, besök[Lägger till data till Cells](/cells/sv/net/add-data-in-cells/).

{{% /alert %}}
