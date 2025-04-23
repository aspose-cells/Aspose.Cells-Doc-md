---
title: Anwendung des erweiterten Filters von Microsoft Excel zur Anzeige von Datensätzen, die komplexe Kriterien erfüllen
type: docs
weight: 190
url: /de/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
---

## **Mögliche Verwendungsszenarien**
Microsoft Excel ermöglicht es Ihnen, den *Erweiterten Filter* auf Arbeitsblattdaten anzuwenden, um Datensätze anzuzeigen, die komplexe Kriterien erfüllen. Sie können den erweiterten Filter mit Microsoft Excel über den Befehl *Daten > Erweitert* anwenden, wie in diesem Screenshot gezeigt.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells ermöglicht auch die Anwendung des erweiterten Filters mit der [Worksheet.advancedFilter()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#advancedFilter-boolean-java.lang.String-java.lang.String-java.lang.String-boolean-) Methode. Genau wie Microsoft Excel akzeptiert es die folgenden Parameter.

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
Der folgende Beispielscode wendet den erweiterten Filter auf die [Beispiel-Excel-Datei](48496702.xlsx) an und generiert die [Ausgabe-Excel-Datei](48496705.xlsx). Der Screenshot zeigt beide Dateien zum Vergleich. Wie im Screenshot zu sehen ist, wurde die Datensätze innerhalb der Ausgabe-Excel-Datei nach komplexen Kriterien gefiltert.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ApplyAdvancedFilterOfMicrosoftExcel.java" >}}
{{< app/cells/assistant language="java" >}}
