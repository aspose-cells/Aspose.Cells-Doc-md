---
title: Fügen Sie Daten in Cells hinzu
type: docs
weight: 10
url: /de/net/add-data-in-cells/
description: In diesem Artikel wird erläutert, wie Sie Daten in Cells mithilfe der APIs Aspose.Cells for .NET hinzufügen.
keywords: C# Add Data in Cells, C# Insert Data to Worksheet, C# Set Data of Cell.
---
##  **So fügen Sie Daten in Cells mit Aspose.Cells for .NET hinzu**
Aspose.Cells stellt eine Klasse, Workbook, bereit, die eine Microsoft Excel-Datei darstellt. Die Workbook-Klasse enthält eine WorksheetCollection, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Worksheet-Klasse dargestellt. Die Worksheet-Klasse stellt eine Cells-Sammlung bereit. Jedes Element in der Cells-Sammlung stellt ein Objekt der Cell-Klasse dar.

**C#**

{{< highlight "cs" >}}

 //Instanziierung eines Workbook-Objekts

Arbeitsmappe Arbeitsmappe = new Workbook();

//Zugriff auf das hinzugefügte Arbeitsblatt in der Excel-Datei

Arbeitsblatt worksheet = workbook.Worksheets[0];

int x = 1;

für (int i = 1; i<= 15; i++)

{

    for (int j = 0; j < 15; j++)

    {

        worksheet.Cells[i, j].Value = x++;

    }

}

workbook.Save("test.xlsx");


{{< /highlight >}}
##  **NPOI HSSF XSSF – Daten in Cells hinzufügen**
In NPOI kann row.createCell(1).setCellValue verwendet werden, um Daten in Zellen hinzuzufügen.

**C#**

{{< highlight "cs" >}}

 IWorkbook workbook = new XSSFWorkbook();

ISheet sheet1 = workbook.CreateSheet("Sheet1");

sheet1.CreateRow(0).CreateCell(0).SetCellValue("Dies ist ein Beispiel");

int x = 1;

für (int i = 1; i<= 15; i++)

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
##  **Laden Sie Running Code herunter**
 Herunterladen**Fügen Sie Daten in Cells hinzu** Bilden Sie eine der unten aufgeführten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Daten zu Cells hinzufügen](/cells/de/net/add-data-in-cells/).

{{% /alert %}}
