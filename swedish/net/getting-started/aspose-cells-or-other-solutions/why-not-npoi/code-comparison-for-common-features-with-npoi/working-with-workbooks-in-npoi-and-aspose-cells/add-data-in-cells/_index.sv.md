---
title: Lägg till data i celler
type: docs
weight: 10
url: /sv/net/add-data-in-cells/
description: Den här artikeln förklarar hur man lägger till data i celler med hjälp av Aspose.Cells for .NET API er.
keywords: C# Lägg till data i celler, C# Infoga data i arbetsblad, C# Ange data för cell.
---


## **Hur lägger man till data i celler med hjälp av Aspose.Cells for .NET**
Aspose.Cells tillhandahåller en klass, Workbook, som representerar en Microsoft Excel-fil. Workbook-klassen innehåller en WorksheetCollection som ger åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av klassen Worksheet. Worksheet-klassen tillhandahåller en Cells-samling. Varje objekt i Cells-samlingen representerar ett objekt av klassen Cell.

**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the added worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

int x = 1;

for (int i = 1; i <= 15; i++)

{

    for (int j = 0; j < 15; j++)

    {

        worksheet.Cells[i, j].Value = x++;

    }

}

workbook.Save("test.xlsx");


{{< /highlight >}}
## **NPOI HSSF XSSF - Lägg till data i celler**
I NPOI kan row.createCell(1).setCellValue användas för att lägga till data i celler.

**C#**

{{< highlight cs >}}

 IWorkbook workbook = new XSSFWorkbook();

ISheet sheet1 = workbook.CreateSheet("Sheet1");

sheet1.CreateRow(0).CreateCell(0).SetCellValue("This is a Sample");

int x = 1;

for (int i = 1; i <= 15; i++)

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
## **Ladda ned körbar kod**
Ladda ner **Lägg till data i celler** från någon av de nedan angivna sociala kodningssidorna:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

För mer information, besök [Lägga till data i celler](/cells/sv/net/laegga-till-data-i-celler/).

{{% /alert %}}
