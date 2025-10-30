---
title: Anwendung des erweiterten Filters von Microsoft Excel zur Anzeige von Datensätzen, die komplexe Kriterien erfüllen
type: docs
weight: 280
url: /de/python-net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Lernen Sie, wie Sie den erweiterten Filter von Microsoft Excel anwenden, um Datensätze anzuzeigen, die komplexe Kriterien erfüllen, unter Verwendung der Aspose.Cells für Python via .NET API
keywords: Python Excel Bibliothek, Python Erweiterter Filter anwenden, Python Erweiterter Filter festlegen, Python Erweiterten Filter hinzufügen, Python Erweiterten Filter erstellen, Wie man einen erweiterten Filter zu einem Bereich hinzufügt, indem man Python verwendet
---

## **Mögliche Verwendungsszenarien**

Microsoft Excel ermöglicht es Ihnen, den *Erweiterten Filter* auf Arbeitsblattdaten anzuwenden, um Datensätze anzuzeigen, die komplexe Kriterien erfüllen. Sie können den erweiterten Filter mit Microsoft Excel über den Befehl *Daten > Erweitert* anwenden, wie in diesem Screenshot gezeigt.

![todo:image_alt_text](1.png)

Aspose.Cells für Python via .NET ermöglicht es auch, den erweiterten Filter mit der Methode [**Worksheet.advancedFilter()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/advanced_filter/#bool-str-str-str-bool) anzuwenden. Genauso wie Microsoft Excel akzeptiert es die folgenden Parameter

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

![todo:image_alt_text](2.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ApplyAdvancedFilterOfMicrosoftExcel.py" >}}
{{< app/cells/assistant language="python-net" >}}
