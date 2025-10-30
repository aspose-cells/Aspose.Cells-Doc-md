---
title: Wenden Sie den erweiterten Filter von Microsoft Excel an, um Datensätze anzuzeigen, die komplexen Kriterien entsprechen, mit Golang via C++
linktitle: Anwendung des erweiterten Filters von Microsoft Excel zur Anzeige von Datensätzen, die komplexe Kriterien erfüllen
type: docs
weight: 280
url: /de/go-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Erfahren Sie, wie Sie den erweiterten Filter von Microsoft Excel anwenden, um Datensätze entsprechend komplexer Kriterien mit der API Aspose.Cells for C++ anzuzeigen.
keywords: Erweiterten Filter anwenden, Erweiterten Filter festlegen, Erweiterten Filter hinzufügen, Erweiterten Filter erstellen, Wie man einen erweiterten Filter auf einen Bereich anwendet
---

## **Mögliche Verwendungsszenarien**

Microsoft Excel ermöglicht es, *Erweiterte Filter* auf Tabellenblatt-Daten anzuwenden, um Datensätze zu filtern, die komplexen Kriterien entsprechen. Sie können den erweiterten Filter in Excel über den Befehl *Daten > Erweitert* ausführen, wie im Screenshot gezeigt.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells ermöglicht ebenfalls die Anwendung des erweiterten Filters mit der [**GetAdvancedFilter()**](https://reference.aspose.com/cells/go-cpp/worksheet/getadvancedfilter/)-Methode. Genau wie Microsoft Excel akzeptiert sie die folgenden Parameter.

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

Der folgende Beispielcode wendet den erweiterten Filter auf die [Beispiel-Excel-Datei](48496692.xlsx) an und erstellt die [Ausgabe-Excel-Datei](48496691.xlsx). Der Screenshot zeigt beide Dateien zum Vergleich. Wie im Screenshot sichtbar ist, wurden die Daten innerhalb der Ausgabedatei entsprechend komplexer Kriterien gefiltert.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyAdvancedFilterOfMicrosoftExcelToDisplayRecordsMeetingComplexCriteria.go" >}}
