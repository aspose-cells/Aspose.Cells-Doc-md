---
title: Fügen Sie Daten in Cells hinzu
type: docs
weight: 10
url: /de/net/add-data-in-cells/
---
## **Aspose.Cells - Fügen Sie Daten in Cells hinzu**
Aspose.Cells stellt eine Klasse Workbook bereit, die eine Microsoft Excel-Datei darstellt. Workbook-Klasse enthält eine WorksheetCollection, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Worksheet-Klasse repräsentiert. Die Worksheet-Klasse stellt eine Cells-Sammlung bereit. Jedes Element in der Sammlung Cells repräsentiert ein Objekt der Klasse Cell.

**C#**

{{< highlight "cs" >}}

 //Instanziieren eines Workbook-Objekts

Arbeitsmappe Arbeitsmappe = neue Arbeitsmappe();

//Auf das hinzugefügte Arbeitsblatt in der Excel-Datei zugreifen

Arbeitsblatt Arbeitsblatt = Arbeitsmappe.Arbeitsblätter[0];

Ganzzahl x = 1;

 für (int i = 1; i<= 15; i++)

{

    for (int j = 0; j < 15; j++)

    {

        worksheet.Cells[i, j].Value = x++;

    }

}

workbook.Save("test.xlsx");


{{< /highlight >}}
## **NPOI HSSF XSSF - Daten in Cells hinzufügen**
In NPOI kann row.createCell(1).setCellValue verwendet werden, um Daten in Zellen hinzuzufügen.

**C#**

{{< highlight "cs" >}}

 IWorkbook-Arbeitsmappe = new XSSFWorkbook();

ISheet sheet1 = Arbeitsmappe.CreateSheet("Sheet1");

sheet1.CreateRow(0).CreateCell(0).SetCellValue("Dies ist ein Beispiel");

Ganzzahl x = 1;

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
## **Laufcode herunterladen**
 Download**Fügen Sie Daten in Cells hinzu** Bilden Sie eine der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Hinzufügen von Daten zu Cells](/cells/de/net/add-data-in-cells/).

{{% /alert %}}
