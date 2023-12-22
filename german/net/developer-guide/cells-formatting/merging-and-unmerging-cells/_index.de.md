---
title: Zusammenführen und Aufheben der Zusammenführung Cells
description: Aspose.Cells ist eine .NET-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien, die das Zusammenführen und Aufheben der Zusammenführung von Zellen unterstützt. In diesem Artikel erfahren Sie, wie Sie Zellen mithilfe der Bibliothek Aspose.Cells zusammenführen und wieder aufheben und wie Sie den Stil für zusammengeführte Zellen anpassen.
keywords: Aspose.Cells, NET library, spreadsheet, merge cells, unmerge cells, style settings, custom styles
type: docs
weight: 190
url: /de/net/merging-and-unmerging-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells unterstützt diese Funktion und kann auch Zellen in einem Arbeitsblatt zusammenführen. Sie können die verbundenen Zellen auch aufheben oder teilen. Der Zellbezug einer verbundenen Zelle ist der Bezug für die obere linke Zelle im ursprünglich ausgewählten Bereich.

{{% /alert %}} 
##  **Einführung**
Sie möchten nicht immer die gleiche Anzahl von Zellen in jeder Zeile oder Spalte haben. Beispielsweise möchten Sie möglicherweise einen Titel in eine Zelle einfügen, die sich über mehrere Spalten erstreckt. Wenn Sie eine Rechnung erstellen, möchten Sie möglicherweise weniger Spalten für die Gesamtsumme. Um aus zwei oder mehr Zellen eine Zelle zu machen, führen Sie diese zusammen. Microsoft Mit Excel können Benutzer Dateien auswählen und zusammenführen, um die Tabelle nach ihren Wünschen zu strukturieren.

{{% alert color="primary" %}} 

Beachten Sie, dass beim Zusammenführen von Zellen nur die Daten in den Zellen oben links erhalten bleiben. Wenn in den anderen Zellen des Bereichs Daten vorhanden sind, werden diese Daten gelöscht.
Die Formatierung basiert ebenfalls auf der Referenzzelle, sodass beim Zusammenführen von Zellen die Formatierungseinstellungen der oberen linken Zelle im Bereich auf die verbundene Zelle angewendet werden. Wenn die Zelle geteilt wird, behalten die neuen Zellen ihre ursprünglichen Formateinstellungen.

{{% /alert %}} 
##  **Zusammenführen von Cells in einem Arbeitsblatt**
###  **Zusammenführen von Cells in Microsoft Excel**
Die folgenden Schritte beschreiben, wie Sie Zellen im Arbeitsblatt mit MS Excel zusammenführen.

1. Kopieren Sie die gewünschten Daten in die Zelle ganz oben links innerhalb des Bereichs.
1. Wählen Sie die Zellen aus, die Sie zusammenführen möchten.
1.  Um Zellen in einer Zeile oder Spalte zusammenzuführen und den Zellinhalt zu zentrieren, klicken Sie auf**Zusammenführen und zentrieren** Symbol auf der**Formatierung** Symbolleiste.
###  **Zusammenführung von Cells mit Aspose.Cells**
Die Klasse Aspose.Cells.Cells verfügt über einige nützliche Methoden für diese Aufgabe. Beispielsweise führt die Methode Merge() die Zellen innerhalb eines angegebenen Bereichs zu einer einzigen Zelle zusammen.

Das folgende Beispiel zeigt, wie Zellen (C6:E7) in einem Arbeitsblatt zusammengeführt werden.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}
##  **Zusammenführung aufheben (Splitting) Zusammengeführt Cells**
###  **Mit Microsoft Excel**
In den folgenden Schritten wird beschrieben, wie Sie verbundene Zellen mit Microsoft Excel teilen.

1. Wählen Sie die verbundene Zelle aus.
 Wenn Zellen kombiniert wurden,**Zusammenführen und zentrieren** wird auf der ausgewählt**Formatierung** Symbolleiste.
1.  Klicken**Zusammenführen und zentrieren** auf der**Formatierung** Symbolleiste.
###  **Verwenden Sie Aspose.Cells**
Die Klasse Aspose.Cells.Cells verfügt über eine Methode namens UnMerge(), die die Zellen in ihren ursprünglichen Zustand aufteilt. Die Methode trennt die Zellen unter Verwendung der Zellreferenz im zusammengeführten Zellbereich.

Das folgende Beispiel zeigt, wie die zusammengeführten Zellen (C6) geteilt werden. Das Beispiel verwendet die im vorherigen Beispiel erstellte Datei und teilt die zusammengeführten Zellen.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-UnMergingtheMergedCells-1.cs" >}}


##  **Vorabthemen**
- [Erkennen Sie zusammengeführte Cells in einem Arbeitsblatt](/cells/de/net/detect-merged-cells-in-a-worksheet/)
