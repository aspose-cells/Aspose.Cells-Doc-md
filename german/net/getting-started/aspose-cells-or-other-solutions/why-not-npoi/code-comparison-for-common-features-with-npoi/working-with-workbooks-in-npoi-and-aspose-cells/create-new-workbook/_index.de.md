---
title: Neues Arbeitsblatt erstellen
type: docs
weight: 20
url: /de/net/create-new-workbook/
---

## **Aspose.Cells - Neues Arbeitsblatt erstellen**
Die Workbook-Klasse ist für die einfache Verwendung verfügbar

**C#**

{{< highlight cs >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

workbook.Save("test.xlsx", SaveFormat.Xlsx); //Workbooks can be saved in many formats

{{< /highlight >}}
## **NPOI - HSSF XSSF - Neuer Arbeitsbereich erstellen**
Erstellen Sie ein neues Arbeitsblatt mit der Workbook-Klasse und speichern Sie es mithilfe von FileOutputStream.

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
## **Laufenden Code herunterladen**
Laden Sie das Formular **Neuen Arbeitsbereich erstellen** von einer der unten genannten Social-Coding-Websites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Create.New.Workbook.Aspose.Cells.zip)
{{< app/cells/assistant language="csharp" >}}
