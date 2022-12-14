---
title: Öffnen und speichern Sie die Tabelle in xlsx4j
type: docs
weight: 40
url: /de/java/open-and-save-spreadsheet-in-xlsx4j/
---
## **Aspose.Cells – Tabelle öffnen und speichern**
Entwickler verwenden Aspose.Cells, um Dateien für verschiedene Zwecke zu öffnen. Öffnen Sie beispielsweise eine Datei, um Daten daraus abzurufen, oder verwenden Sie eine vordefinierte Designer-Tabellenkalkulationsdatei, um Ihren Entwicklungsprozess zu beschleunigen. Aspose.Cells ermöglicht es Entwicklern, verschiedene Arten von Quelldateien zu öffnen. Diese Quelldateien können Microsoft Excel-Berichte, SpreadsheetML-, CSV- oder tabulatorgetrennte Dateien sein.

**Aspose.Cells**ermöglicht Entwicklern, Excel-Dateien mit dem flexiblen API von Grund auf neu zu erstellen. Sobald Sie Excel-Dateien erstellt haben, müssen Sie auch Ihre Arbeitsmappe (Datei) speichern. Aspose.Cells bietet verschiedene Möglichkeiten, diese Dateien zu speichern.

**Java**

{{< highlight "java" >}}

 //Creating an Workbook object with an Excel file path

Workbook workbook = new Workbook(dataDir + "pivot.xlsm");

//Saving the Excel file

workbook.save(dataDir + "pivot-rtt-Aspose.xlsm");

{{< /highlight >}}
## **xlsx4j - Tabelle öffnen und speichern**
Das folgende Beispiel zeigt, wie Sie Tabellenkalkulationen öffnen und speichern, während Sie xlsx4j verwenden.

**Java**

{{< highlight "java" >}}

 String inputfilepath  = dataDir + "pivot.xlsm";

boolean save = true;

String outputfilepath = dataDir + "pivot-rtt-xlsx4j.xlsm";

// Open a document from the file system

// 1. Load the Package

OpcPackage pkg = OpcPackage.load(new java.io.File(inputfilepath));

// Save it

if (save) {

    SaveToZipFile saver = new SaveToZipFile(pkg);

    saver.save(outputfilepath);

}

{{< /highlight >}}
## **Laufcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/opensavespreadsheet)
