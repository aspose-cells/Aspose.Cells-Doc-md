---
title: Aggiungi dati in Cells
type: docs
weight: 10
url: /it/net/add-data-in-cells/
---
## **Aspose.Cells - Aggiungi dati in Cells**
Aspose.Cells fornisce una classe, Workbook, che rappresenta un file Excel Microsoft. La classe Workbook contiene un WorksheetCollection che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe Worksheet. La classe Worksheet fornisce una raccolta Cells. Ogni elemento nella raccolta Cells rappresenta un oggetto della classe Cell.

**C#**

{{< highlight "cs" >}}

 //Creazione di un'istanza di un oggetto Workbook

Cartella di lavoro cartella di lavoro = nuova cartella di lavoro();

//Accesso al foglio di lavoro aggiunto nel file Excel

Foglio di lavoro foglio di lavoro = workbook.Worksheets[0];

intero x = 1;

 per (int i = 1; i<= 15; i++)

{

    for (int j = 0; j < 15; j++)

    {

        worksheet.Cells[i, j].Value = x++;

    }

}

workbook.Save("test.xlsx");


{{< /highlight >}}
## **NPOI HSSF XSSF - Aggiungi dati in Cells**
In NPOI row.createCell(1).setCellValue può essere utilizzato per aggiungere dati nelle celle.

**C#**

{{< highlight "cs" >}}

 Cartella di lavoro IWorkbook = new XSSFWorkbook();

ISheet foglio1 = cartella di lavoro.CreateSheet("Foglio1");

sheet1.CreateRow(0).CreateCell(0).SetCellValue("Questo è un esempio");

intero x = 1;

 per (int i = 1; i<= 15; i++)

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
 Scaricamento**Aggiungi dati in Cells** formare uno dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Aggiunta di dati a Cells](/cells/it/net/add-data-in-cells/).

{{% /alert %}}
