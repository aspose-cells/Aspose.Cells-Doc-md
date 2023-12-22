---
title: Aggiungi dati in Cells
type: docs
weight: 10
url: /it/net/add-data-in-cells/
description: Questo articolo spiega come aggiungere dati in Cells utilizzando le API Aspose.Cells for .NET.
keywords: C# Add Data in Cells, C# Insert Data to Worksheet, C# Set Data of Cell.
---
##  **Come aggiungere dati in Cells utilizzando Aspose.Cells for .NET**
Aspose.Cells fornisce una classe, Workbook, che rappresenta un file Excel Microsoft. La classe Workbook contiene un WorksheetCollection che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe Worksheet. La classe Worksheet fornisce una raccolta Cells. Ogni elemento della collezione Cells rappresenta un oggetto della classe Cell.

**C#**

{{< highlight "cs" >}}

 //Creazione di un'istanza di un oggetto cartella di lavoro

Cartella di lavoro cartella di lavoro = nuova cartella di lavoro();

//Accesso al foglio di lavoro aggiunto nel file Excel

Foglio di lavoro foglio di lavoro = cartella di lavoro.Fogli di lavoro[0];

intero x = 1;

for (int i = 1; i<= 15; i++)

{

    for (int j = 0; j < 15; j++)

    {

        worksheet.Cells[i, j].Value = x++;

    }

}

workbook.Save("test.xlsx");


{{< /highlight >}}
##  **NPOI HSSF XSSF - Aggiungi dati in Cells**
In NPOI row.createCell(1).setCellValue può essere utilizzato per aggiungere dati nelle celle.

**C#**

{{< highlight "cs" >}}

 Cartella di lavoro IWorkbook = nuova XSSFWorkbook();

ISheet foglio1 = workbook.CreateSheet("Foglio1");

sheet1.CreateRow(0).CreateCell(0).SetCellValue("Questo è un esempio");

intero x = 1;

for (int i = 1; i<= 15; i++)

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
##  **Scarica il codice in esecuzione**
 Scaricamento**Aggiungi dati in Cells** formare uno dei siti di social coding indicati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visitare[Aggiunta Dati allo Cells](/cells/it/net/add-data-in-cells/).

{{% /alert %}}
