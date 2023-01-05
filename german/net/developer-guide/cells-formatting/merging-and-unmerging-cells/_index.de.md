---
title: Zusammenführen und Trennen Cells
type: docs
weight: 190
url: /de/net/merging-and-unmerging-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells unterstützt diese Funktion und kann auch Zellen in einem Arbeitsblatt zusammenführen. Sie können die verbundenen Zellen auch aufheben oder teilen. Die Zellreferenz einer verbundenen Zelle ist die Referenz für die obere linke Zelle im ursprünglich ausgewählten Bereich.

{{% /alert %}} 
## **Einführung**
Sie möchten nicht immer die gleiche Anzahl von Zellen in jeder Zeile oder Spalte haben. Beispielsweise möchten Sie möglicherweise einen Titel in eine Zelle einfügen, die sich über mehrere Spalten erstreckt. Oder wenn Sie eine Rechnung erstellen, möchten Sie möglicherweise weniger Spalten für die Gesamtsumme. Um aus zwei oder mehr Zellen eine Zelle zu machen, führen Sie sie zusammen. Microsoft Mit Excel können Benutzer Dateien auswählen und zusammenführen, um die Tabelle nach ihren Wünschen zu strukturieren.

{{% alert color="primary" %}} 

Beachten Sie, dass beim Verbinden von Zellen nur die Daten in den Zellen oben links beibehalten werden. Wenn in den anderen Zellen des Bereichs Daten vorhanden sind, werden diese Daten gelöscht.
Die Formatierung basiert ebenfalls auf der Referenzzelle, sodass beim Verbinden von Zellen die Formatierungseinstellungen der oberen linken Zelle im Bereich auf die verbundene Zelle angewendet werden. Wenn die Zelle geteilt wird, behalten die neuen Zellen ihre ursprünglichen Formateinstellungen.

{{% /alert %}} 
## **Zusammenführen von Cells in einem Arbeitsblatt**
### **Zusammenführen von Cells in Microsoft Excel**
Die folgenden Schritte beschreiben, wie Sie Zellen im Arbeitsblatt mit MS Excel zusammenführen.

1. Kopieren Sie die gewünschten Daten in die oberste linke Zelle innerhalb des Bereichs.
1. Wählen Sie die Zellen aus, die Sie zusammenführen möchten.
1.  Um Zellen in einer Zeile oder Spalte zusammenzuführen und den Zelleninhalt zu zentrieren, klicken Sie**Zusammenführen und zentrieren** Symbol auf der**Formatierung** Symbolleiste.
### **Zusammenführen von Cells mit Aspose.Cells**
Die Klasse Aspose.Cells.Cells hat einige nützliche Methoden für diese Aufgabe. Beispielsweise führt die Methode Merge() die Zellen innerhalb eines bestimmten Bereichs zu einer einzigen Zelle zusammen.

Das folgende Beispiel zeigt, wie Zellen (C6:E7) in einem Arbeitsblatt zusammengeführt werden.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}
## **Aufheben (Aufteilen) Zusammengeführt Cells**
### **Mit Microsoft Excel**
Die folgenden Schritte beschreiben, wie verbundene Zellen mit Microsoft Excel geteilt werden.

1. Wählen Sie die verbundene Zelle aus.
 Wenn Zellen kombiniert wurden,**Zusammenführen und zentrieren** auf ausgewählt ist**Formatierung** Symbolleiste.
1.  Klicken**Zusammenführen und zentrieren** auf der**Formatierung** Symbolleiste.
### **Mit Aspose.Cells**
Die Klasse Aspose.Cells.Cells hat eine Methode namens UnMerge(), die die Zellen in ihren ursprünglichen Zustand aufteilt. Die Methode trennt die Zellen unter Verwendung des Zellbezugs im verbundenen Zellbereich.

Das folgende Beispiel zeigt, wie die verbundenen Zellen geteilt werden (C6). Das Beispiel verwendet die im vorherigen Beispiel erstellte Datei und teilt die verbundenen Zellen.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-UnMergingtheMergedCells-1.cs" >}}


## **Themen vorantreiben**
- [Zusammengeführte Cells in einem Arbeitsblatt erkennen](/cells/de/net/detect-merged-cells-in-a-worksheet/)
