---
title: Daten in Zellen hinzufügen
type: docs
weight: 10
url: /de/net/add-data-in-cells/
description: In diesem Artikel erfahren Sie, wie Sie Daten in Zellen mit Aspose.Cells for .NET APIs hinzufügen.
keywords: C# Daten in Zellen hinzufügen, C# Daten in Arbeitsblatt einfügen, C# Daten der Zelle setzen.
---


## **So fügen Sie Daten in Zellen mit Aspose.Cells for .NET hinzu**
Aspose.Cells bietet eine Klasse Workbook, die eine Microsoft Excel-Datei darstellt. Die Klasse Workbook enthält eine WorksheetCollection, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse Worksheet dargestellt. Die Klasse Worksheet bietet eine Cells-Sammlung. Jedes Element in der Cells-Sammlung repräsentiert ein Objekt der Klasse Cell.

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
## **NPOI HSSF XSSF - Daten in Zellen hinzufügen**
In NPOI kann row.createCell(1).setCellValue verwendet werden, um Daten in Zellen hinzuzufügen.

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
## **Laufenden Code herunterladen**
Laden Sie das Formular **Daten in Zellen hinzufügen** von einer der unten genannten Social-Coding-Websites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Für weitere Details besuchen Sie [Daten zu Zellen hinzufügen](/cells/de/net/daten-in-zellen-hinzufuegen/).

{{% /alert %}}
