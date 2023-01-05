---
title: Neue Arbeitsmappe erstellen
type: docs
weight: 20
url: /de/net/create-new-workbook/
---
## **Aspose.Cells – Neue Arbeitsmappe erstellen**
Die Workbook-Klasse ist für die einfache Verwendung verfügbar

**C#**

{{< highlight "cs" >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

workbook.Save("test.xlsx", SaveFormat.Xlsx); //Workbooks can be saved in many formats

{{< /highlight >}}
## **NPOI - HSSF XSSF - Neue Arbeitsmappe erstellen**
Erstellen Sie eine neue Arbeitsmappe mit der Workbook-Klasse und speichern Sie sie mit FileOutputStream.

**C#**

{{< highlight "cs" >}}

 IWorkbook workbook = new XSSFWorkbook();

workbook.CreateSheet("Sheet A1");

workbook.CreateSheet("Sheet A2");

workbook.CreateSheet("Sheet A3");

FileStream sw = File.Create("test.xlsx");

workbook.Write(sw);

sw.Close();

{{< /highlight >}}
## **Laufcode herunterladen**
 Download**Neue Arbeitsmappe erstellen** Bilden Sie eine der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Create.New.Workbook.Aspose.Cells.zip)
