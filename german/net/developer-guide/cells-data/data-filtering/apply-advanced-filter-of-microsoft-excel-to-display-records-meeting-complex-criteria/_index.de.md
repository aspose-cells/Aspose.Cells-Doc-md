---
title: Anwendung des erweiterten Filters von Microsoft Excel zur Anzeige von Datensätzen, die komplexe Kriterien erfüllen
type: docs
weight: 280
url: /de/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Erfahren Sie, wie Sie das erweiterte Filtern von Microsoft Excel anwenden, um Datensätze mit komplexen Kriterien anzuzeigen, indem Sie die Aspose.Cells for .NET API verwenden.
keywords: Erweiterten Filter anwenden, Erweiterten Filter festlegen, Erweiterten Filter hinzufügen, Erweiterten Filter erstellen, Wie man einen erweiterten Filter auf einen Bereich anwendet 
---

## **Mögliche Verwendungsszenarien**

Microsoft Excel ermöglicht es Ihnen, den *Erweiterten Filter* auf Arbeitsblattdaten anzuwenden, um Datensätze anzuzeigen, die komplexe Kriterien erfüllen. Sie können den erweiterten Filter mit Microsoft Excel über den Befehl *Daten > Erweitert* anwenden, wie in diesem Screenshot gezeigt.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells ermöglicht es Ihnen auch, den erweiterten Filter mit der Methode [**Worksheet.AdvancedFilter()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/advancedfilter) zu verwenden. Genauso wie bei Microsoft Excel akzeptiert sie die folgenden Parameter.

**isFilter**

Gibt an, ob die Liste am gleichen Ort gefiltert wird.

**listRange**

Der Listenbereich.

**criteriaRange**

Der Kriterienbereich.

**copyTo**

Der Bereich, in den Daten kopiert werden.

**uniqueRecordOnly**

Nur eindeutige Zeilen anzeigen oder kopieren.

## **Erweiterten Filter von Microsoft Excel anwenden, um Datensätze anhand komplexer Kriterien anzuzeigen**

Der folgende Beispielcode wendet den erweiterten Filter auf die [Beispiel-Excel-Datei](48496692.xlsx) an und erstellt die [Ausgabedatei-Excel-Datei](48496691.xlsx). Der Screenshot zeigt beide Dateien zum Vergleich. Wie im Screenshot zu sehen ist, wurden die Daten in der Ausgabedatei entsprechend komplexer Kriterien gefiltert.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-ApplyAdvancedFilterOfMicrosoftExcel.cs" >}}
