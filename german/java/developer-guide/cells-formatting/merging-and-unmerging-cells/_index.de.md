---
title: Zusammenführen und Trennen Cells
type: docs
weight: 140
url: /de/java/merging-and-unmerging-cells/
---
{{% alert color="primary" %}}

Sie möchten nicht immer die gleiche Anzahl von Zellen in jeder Zeile oder Spalte haben. Beispielsweise möchten Sie möglicherweise einen Titel in eine Zelle einfügen, die sich über mehrere Spalten erstreckt. Oder wenn Sie eine Rechnung erstellen, möchten Sie möglicherweise weniger Spalten für die Gesamtsumme. Um aus zwei oder mehr Zellen eine Zelle zu machen, führen Sie sie zusammen. Microsoft Mit Excel können Benutzer Zellen auswählen und zusammenführen, um die Tabelle nach ihren Wünschen zu strukturieren.

**Das Ergebnis des Zusammenführens und anschließenden Teilens einer Reihe von Zellen, die wie die Zellen auf der linken Seite in Microsoft Excel formatiert sind** 

![todo: Bild_alt_Text](merging-and-unmerging-cells_1.png)

Aspose.Cells unterstützt diese Funktion und kann auch Zellen in einem Arbeitsblatt zusammenführen. Sie können die verbundenen Zellen auch aufheben oder teilen. Die Zellreferenz einer verbundenen Zelle ist die Referenz für die Zelle oben links im ursprünglich ausgewählten Bereich.

Beachten Sie, dass beim Verbinden von Zellen nur die Daten in der linken oberen Zelle beibehalten werden. Wenn in den anderen Zellen des Bereichs Daten vorhanden sind, werden diese Daten gelöscht.

Die Formatierung basiert ebenfalls auf der Referenzzelle, sodass beim Verbinden von Zellen die Formatierungseinstellungen der Zelle oben links im Bereich auf die verbundene Zelle angewendet werden. Wenn die Zelle geteilt wird, behalten die neuen Zellen ihre ursprünglichen Formateinstellungen.

{{% /alert %}}

## **Zusammenführen von Cells in einem Arbeitsblatt.**

### **Mit Microsoft Excel**

Die folgenden Schritte beschreiben, wie Sie Zellen im Arbeitsblatt mit Microsoft Excel zusammenführen.

1. Kopieren Sie die gewünschten Daten in die oberste linke Zelle innerhalb des Bereichs.
1. Wählen Sie die Zellen aus, die Sie zusammenführen möchten.
1.  Um Zellen in einer Zeile oder Spalte zusammenzuführen und den Zelleninhalt zu zentrieren, klicken Sie**Zusammenführen und zentrieren** Symbol auf der**Formatierung** Symbolleiste.

### **Mit Aspose.Cells**

 Das[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Klasse hat einige nützliche Methoden für die Aufgabe. Zum Beispiel die Methode[**verschmelzen()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)) führt die Zellen innerhalb eines angegebenen Zellbereichs zu einer einzigen Zelle zusammen.

Die folgende Ausgabe wird nach Ausführung des folgenden Codes generiert.

**Die Zellen (C6:E7) wurden zusammengeführt** 

![todo: Bild_alt_Text](merging-and-unmerging-cells_2.png)

#### **Codebeispiel**

Das folgende Beispiel zeigt, wie Zellen (C6:E7) in einem Arbeitsblatt zusammengeführt werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}

## **Aufheben (Aufteilen) Zusammengeführt Cells**

### **Mit Microsoft Excel**

Die folgenden Schritte beschreiben, wie verbundene Zellen mit Microsoft Excel geteilt werden.

1.  Wählen Sie die verbundene Zelle aus.
 Wenn Zellen kombiniert wurden,**Zusammenführen und zentrieren** auf ausgewählt ist**Formatierung** Symbolleiste.
1.  Klicken**Zusammenführen und zentrieren** auf der**Formatierung** Symbolleiste.

#### **Mit Aspose.Cells**

 Das[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Klasse hat eine Methode namens[**Zusammenführen aufheben ()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unMerge(int,%20int,%20int,%20int)), der Zellen in ihren ursprünglichen Zustand aufteilt. Die Methode trennt die Zellen unter Verwendung des Zellbezugs im verbundenen Zellbereich.

#### **Codebeispiel**

Das folgende Beispiel zeigt, wie die verbundenen Zellen geteilt werden (C6). Das Beispiel verwendet die im vorherigen Beispiel erstellte Datei und teilt die verbundenen Zellen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UnMergingCellsInWorksheet-UnMergingCellsInWorksheet.java" >}}

## **Zum Thema passende Artikel**

- [Zusammengeführte Zellen finden und teilen](/cells/de/java/detect-merged-cells-in-a-worksheet/).
- [Verbinden und teilen Sie einen Zellbereich mit den Methoden Range.merge() und Range.unMerge()](/cells/de/java/merge-or-unmerge-range-of-cells/).

