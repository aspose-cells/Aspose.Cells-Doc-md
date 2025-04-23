---
title: Zusammenführen und Aufteilen von Zellen
description: Aspose.Cells ist eine .NET Bibliothek zum Arbeiten mit Tabellendateien, die das Zusammenführen und Trennen von Zellen unterstützt. Dieser Artikel zeigt, wie Sie Zellen mit der Aspose.Cells Bibliothek zusammenführen und trennen können, sowie die Anpassung des Zellen Zusammenführungsstils.
keywords: Aspose.Cells, NET Bibliothek, Tabelle, Zellen zusammenführen, Zellen trennen, Stileinstellungen, benutzerdefinierte Stile
type: docs
weight: 190
url: /de/net/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells unterstützt diese Funktion und kann auch Zellen in einem Arbeitsblatt zusammenführen. Sie können auch Zellen trennen oder aufteilen. Der Zellenbezug einer zusammengeführten Zelle ist der Bezug der links oben Zelle im ursprünglich ausgewählten Bereich.

{{% /alert %}} 
## **Einführung**
Nicht immer benötigen Sie dieselbe Anzahl von Zellen in jeder Zeile oder Spalte. Zum Beispiel möchten Sie möglicherweise einen Titel in einer Zelle haben, die mehrere Spalten umspannt. Oder wenn Sie eine Rechnung erstellen, möchten Sie weniger Spalten für die Gesamtsumme haben. Um eine Zelle aus zwei oder mehr Zellen zu machen, führen Sie sie zusammen. Microsoft Excel ermöglicht es Benutzern, Zellen auszuwählen und zu verschmelzen, um die Tabelle nach ihren Wünschen zu strukturieren.

{{% alert color="primary" %}} 

Beachten Sie, dass beim Zusammenführen von Zellen nur die Daten in den links oben Zellen erhalten bleiben. Wenn Daten in den anderen Zellen im Bereich vorhanden sind, werden diese gelöscht.
Ebenso basiert die Formatierung auf der Bezugszelle, sodass beim Zusammenführen von Zellen die Formatierungseinstellungen der links oben Zelle im Bereich auf die zusammengeführte Zelle angewendet werden. Wenn die Zelle getrennt ist, behalten die neuen Zellen ihre ursprünglichen Formatierungseinstellungen bei.

{{% /alert %}} 
## **Zellen in einem Arbeitsblatt zusammenführen**
### **Zusammenführen von Zellen in Microsoft Excel**
Die folgenden Schritte beschreiben, wie Sie Zellen im Arbeitsblatt mit MS Excel zusammenführen können.

1. Kopieren Sie die Daten, die Sie in die oberste linke Zelle innerhalb des Bereichs einfügen möchten.
1. Wählen Sie die Zellen aus, die Sie zusammenführen möchten.
1. Um Zellen in einer Zeile oder Spalte zusammenzuführen und den Zellinhalt zu zentrieren, klicken Sie auf das Icon **Zusammenführen und Zentrieren** in der **Formatierung**-Symbolleiste.
### **Zellen zusammenführen mit Aspose.Cells**
Die Aspose.Cells.Cells-Klasse verfügt über einige nützliche Methoden für diese Aufgabe. So führt z.B. die Methode Merge() die Zellen in eine einzelne Zelle innerhalb eines angegebenen Bereichs zusammen.

Das folgende Beispiel zeigt, wie Zellen (C6:E7) in einem Arbeitsblatt zusammengeführt werden.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}
## **Aufsplitten (Teilen) von zusammengeführten Zellen**
### **Verwendung von Microsoft Excel**
Die folgenden Schritte beschreiben, wie Sie zusammengeführte Zellen mit Microsoft Excel aufspalten können.

1. Wählen Sie die zusammengeführte Zelle aus.
   Wenn Zellen kombiniert wurden, ist **Zusammenführen und Zentrieren** in der **Formatierung**-Symbolleiste ausgewählt.
1. Klicken Sie auf **Zusammenführen und Zentrieren** in der **Formatierung**-Symbolleiste.
### **Verwendung von Aspose.Cells**
Die Klasse Aspose.Cells.Cells hat eine Methode namens UnMerge(), die die Zellen in ihren ursprünglichen Zustand aufteilt. Die Methode entpackt die Zellen mithilfe des Verweises der Zelle im Bereich der zusammengeführten Zelle.

Das folgende Beispiel zeigt, wie die zusammengeführten Zellen (C6) aufgeteilt werden. Das Beispiel verwendet die Datei, die im vorherigen Beispiel erstellt wurde, und teilt die zusammengeführten Zellen auf.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-UnMergingtheMergedCells-1.cs" >}}


## **Erweiterte Themen**
- [Erkennen von zusammengeführten Zellen in einem Arbeitsblatt](/cells/de/net/detect-merged-cells-in-a-worksheet/)
{{< app/cells/assistant language="csharp" >}}
