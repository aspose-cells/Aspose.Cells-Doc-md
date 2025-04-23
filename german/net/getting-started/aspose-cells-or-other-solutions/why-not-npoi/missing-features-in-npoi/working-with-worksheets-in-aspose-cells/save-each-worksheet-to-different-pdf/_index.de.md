---
title: Jedes Arbeitsblatt als verschiedene PDF Datei speichern
type: docs
weight: 10
url: /de/net/save-each-worksheet-to-different-pdf/
---

## **Aspose.Cells - Jedes Arbeitsblatt als separate PDF speichern**
Aspose.Cells unterstützt die Konvertierung von XLS-Dateien (die Bilder, Diagramme usw. enthalten) in PDF-Dokumente. Aspose.Cells for .NET kann unabhängig arbeiten, um eine Tabelle in ein PDF-Dokument umzuwandeln, und Sie müssen Aspose.Pdf for .NET nicht mehr für die Konvertierung verwenden. Die Konvertierung erfordert auch nicht, temporäre Dateien zu erstellen oder zu verwenden, da der gesamte Prozess im Speicher durchgeführt werden kann.

**C#**

{{< highlight cs >}}

 //Instantiate a new workbook and open the Excel

//File from its location

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the count of the worksheets in the workbook

int sheetCount = workbook.Worksheets.Count;

//Make all sheets invisible except first worksheet

for (int i = 1; i < workbook.Worksheets.Count; i++)

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
## **Laufenden Code herunterladen**
Laden Sie **Jedes Arbeitsblatt als verschiedene PDF-Datei speichern** von einer der unten genannten Social-Coding-Websites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Save.Each.Worksheet.to.Different.PDF.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Für weitere Details besuchen Sie [Jedes Arbeitsblatt als verschiedene PDF-Datei speichern](https://docs.aspose.com/cells/net/save-each-worksheet-to-a-different-pdf-file/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
