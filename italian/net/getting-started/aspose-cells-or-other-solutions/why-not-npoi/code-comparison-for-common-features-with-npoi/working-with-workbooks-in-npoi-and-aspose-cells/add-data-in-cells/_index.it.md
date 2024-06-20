---
title: Aggiungi dati nelle celle
type: docs
weight: 10
url: /it/net/add-data-in-cells/
description: Questo articolo spiega come Aggiungere Dati nelle Celle usando Aspose.Cells for .NET API.
keywords: C# Aggiungere Dati nelle Celle, C# Inserire Dati nel Foglio di Lavoro, C# Impostare Dati della Cella.
---


## **Come Aggiungere Dati nelle Celle Usando Aspose.Cells for .NET**
Aspose.Cells fornisce una classe, Workbook, che rappresenta un file Microsoft Excel. La classe Workbook contiene una WorksheetCollection che permette l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe Worksheet. La classe Worksheet fornisce una raccolta di celle. Ogni elemento nella collezione Cells rappresenta un oggetto della classe Cell.

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
## **NPOI HSSF XSSF - Aggiungere Dati nelle Celle**
In NPOI row.createCell(1).setCellValue può essere usato per aggiungere dati nelle celle.

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
## **Scarica il codice in esecuzione**
Scarica **Aggiungere Dati nelle Celle** da uno dei siti di codifica sociale menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Per ulteriori dettagli, visita [Aggiungere Dati alle Celle](/cells/it/net/add-data-in-cells/).

{{% /alert %}}
