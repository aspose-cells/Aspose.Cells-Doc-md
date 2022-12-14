---
title: Speichern Sie jedes Arbeitsblatt in einem anderen PDF
type: docs
weight: 10
url: /de/net/save-each-worksheet-to-different-pdf/
---
## **Aspose.Cells – Speichern Sie jedes Arbeitsblatt in einem anderen PDF**
Aspose.Cells unterstützt die Konvertierung von XLS-Dateien (die Bilder, Diagramme usw. enthalten) in PDF-Dokumente. Aspose.Cells for .NET kann unabhängig arbeiten, um eine Tabelle in ein PDF-Dokument zu konvertieren, und Sie müssen Aspose.Pdf for .NET nicht mehr für die Konvertierung verwenden. Für die Konvertierung müssen keine temporären Dateien erstellt / verwendet werden, da der gesamte Vorgang im Speicher durchgeführt werden kann.

**C#**

{{< highlight "cs" >}}

 //Instanziieren Sie eine neue Arbeitsmappe und öffnen Sie Excel

//Datei von ihrem Speicherort

Arbeitsmappe Arbeitsmappe = neue Arbeitsmappe(../../data/test.xlsx");

//Ermittle die Anzahl der Arbeitsblätter in der Arbeitsmappe

int sheetCount = Arbeitsmappe.Arbeitsblätter.Anzahl;

// Alle Blätter außer dem ersten Arbeitsblatt unsichtbar machen

 für (int i = 1; i< workbook.Worksheets.Count; i++)

{

    workbook.Worksheets[i].IsVisible = false;

}

//Take Pdfs of each sheet

for (int j = 0; j < workbook.Worksheets.Count; j++)

{

    Worksheet ws = workbook.Worksheets[j];

    workbook.Save(ws.Name + ".pdf");

    if (j < workbook.Worksheets.Count - 1)

    {

        workbook.Worksheets[j + 1].IsVisible = true;

        workbook.Worksheets[j].IsVisible =false;

    }

}

{{< /highlight >}}
## **Laufcode herunterladen**
 Download**Speichern Sie jedes Arbeitsblatt in einem anderen PDF** Bilden Sie eine der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Save.Each.Worksheet.to.Different.PDF.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Speichern Sie jedes Arbeitsblatt in einer anderen PDF-Datei](https://docs.aspose.com/cells/net/save-each-worksheet-to-a-different-pdf-file/).

{{% /alert %}}
