---
title: Öffnen und Speichern von Arbeitsmappen in xlsx4j
type: docs
weight: 40
url: /de/java/open-and-save-spreadsheet-in-xlsx4j/
---

## **Aspose.Cells - Arbeitsmappe öffnen und speichern**
Entwickler verwenden Aspose.Cells, um Dateien für verschiedene Zwecke zu öffnen. Zum Beispiel, um Daten daraus abzurufen oder eine vordefinierte Designer-Arbeitsmappendatei zu verwenden, um Ihren Entwicklungsprozess zu beschleunigen. Aspose.Cells ermöglicht Entwicklern, verschiedene Arten von Quelldateien zu öffnen. Diese Quelldateien können Microsoft Excel-Berichte, SpreadsheetML, CSV- oder Tabulator-getrennte Dateien sein. 

**Aspose.Cells** ermöglicht Entwicklern, Excel-Dateien von Grund auf zu erstellen, indem sie ihre flexible API nutzen. Sobald Sie Excel-Dateien erstellen, müssen Sie auch Ihre Arbeitsmappe (Datei) speichern. Aspose.Cells bietet verschiedene Möglichkeiten, um diese Dateien zu speichern.

**Java**

{{< highlight java >}}

 //Creating an Workbook object with an Excel file path

Workbook workbook = new Workbook(dataDir + "pivot.xlsm");

//Saving the Excel file

workbook.save(dataDir + "pivot-rtt-Aspose.xlsm");

{{< /highlight >}}
## **xlsx4j - Arbeitsmappe öffnen und speichern**
Das folgende Beispiel zeigt, wie Arbeitsmappen geöffnet und gespeichert werden, während xlsx4j verwendet wird.

**Java**

{{< highlight java >}}

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
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/opensavespreadsheet)
