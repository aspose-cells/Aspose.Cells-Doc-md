---
title: Speichern Sie jedes Arbeitsblatt mit Aspose.Cells in einem anderen PDF
type: docs
weight: 80
url: /de/java/save-each-worksheet-to-different-pdf-using-aspose-cells/
---
## **Aspose.Cells – Speichern Sie jedes Arbeitsblatt in einem anderen PDF**
Aspose.Cells unterstützt die Konvertierung von XLS-Dateien (die Bilder, Diagramme usw. enthalten) in PDF-Dokumente. Aspose.Cells for Java kann unabhängig arbeiten, um eine Tabelle in ein PDF-Dokument zu konvertieren, und Sie müssen Aspose.Pdf for Java nicht mehr für die Konvertierung verwenden. Für die Konvertierung müssen keine temporären Dateien erstellt / verwendet werden, da der gesamte Vorgang im Speicher durchgeführt werden kann.

**Java**

{{< highlight "java" >}}

//Pfad der Excel-Datei abrufen

String filePath = dataDir + "workbook.xlsx";

//Instanziieren Sie eine neue Arbeitsmappe und öffnen Sie Excel

//Datei von ihrem Speicherort

Arbeitsmappe Arbeitsmappe = neue Arbeitsmappe (Dateipfad);

//Ermittle die Anzahl der Arbeitsblätter in der Arbeitsmappe

int sheetCount = workbook.getWorksheets().getCount();

// Alle Blätter außer dem ersten Arbeitsblatt unsichtbar machen

 für (int i = 1; i< workbook.getWorksheets().getCount(); i++)

{

     workbook.getWorksheets().get(i).setVisible(false);

}

//Take Pdfs of each sheet

for (int j = 0; j < workbook.getWorksheets().getCount(); j++)

{

    Worksheet ws = workbook.getWorksheets().get(j);

    workbook.save(dataPath + ws.getName() + ".pdf");

    if (j < workbook.getWorksheets().getCount() - 1)

    {

       workbook.getWorksheets().get(j + 1).setVisible(true);

       workbook.getWorksheets().get(j).setVisible(false);

    }

}

{{< /highlight >}}
## **Laufcode herunterladen**
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/SaveEachWorksheetToDifferentPDF.java)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Speichern Sie jedes Arbeitsblatt in einer anderen PDF-Datei](/cells/de/java/save-each-worksheet-to-a-different-pdf-file).

{{% /alert %}}
