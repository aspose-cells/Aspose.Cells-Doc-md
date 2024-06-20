---
title: Jedes Arbeitsblatt in xlsx4j als separate PDF speichern
type: docs
weight: 50
url: /de/java/save-each-worksheet-to-different-pdf-in-xlsx4j/
---

## **Aspose.Cells - Jedes Arbeitsblatt als separate PDF speichern**
Aspose.Cells unterstützt die Konvertierung von XLS-Dateien (die Bilder, Diagramme usw. enthalten) in PDF-Dokumente. Aspose.Cells for Java kann unabhängig arbeiten, um eine Arbeitsmappe in ein PDF-Dokument zu konvertieren, und Sie müssen nicht mehr Aspose.Pdf for Java für die Konvertierung verwenden. Der Vorgang erfordert auch nicht das Erstellen/Verwenden von temporären Dateien, da der gesamte Prozess im Speicher ausgeführt werden kann.

**Java**

{{< highlight java >}}

 //Get the Excel file path

String filePath = dataDir + "workbook.xlsx";

//Instantiate a new workbook and open the Excel

//File from its location

Workbook workbook = new Workbook(filePath);

//Get the count of the worksheets in the workbook

int sheetCount = workbook.getWorksheets().getCount();

//Make all sheets invisible except first worksheet

for (int i = 1; i < workbook.getWorksheets().getCount(); i++)

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
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/saveeachworksheettopdf/AsposeSaveEachWorksheetToDifferentPDF.java)

{{% alert color="primary" %}} 

Für weitere Details besuchen Sie [Jedes Arbeitsblatt in eine separate PDF-Datei speichern](/cells/de/java/save-each-worksheet-to-a-different-pdf-file).

{{% /alert %}}
