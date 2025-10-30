---
title: Zusammenführen und Aufteilen von Zellen
description: Aspose.Cells ist eine Python Bibliothek zum Arbeiten mit Tabellenkalkulationsdateien, die das Zusammenführen und Trennen von Zellen unterstützt. Dieser Artikel führt ein, wie man Zellen mit der Aspose.Cells für Python via .NET Bibliothek zusammenführt und trennt sowie die Stilgestaltung für zusammengeführte Zellen anpasst.
keywords: Aspose.Cells für Python via .NET, NET Bibliothek, Tabellenkalkulation, Zellen zusammenführen, Trennen, Stil Einstellungen, benutzerdefinierte Stile
type: docs
weight: 190
url: /de/python-net/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells für Python via .NET unterstützt diese Funktion und kann auch Zellen in einem Arbeitsblatt zusammenführen. Sie können die Zellen auch wieder trennen oder aufteilen. Der Zellbezug einer zusammengeführten Zelle ist der Verweis auf die obere linke Zelle im ursprünglichen ausgewählten Bereich.

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

### **Zellen mit Aspose.Cells für Python via .NET zusammenführen**
Die Aspose.Cells.Cells-Klasse verfügt über einige nützliche Methoden für diese Aufgabe. So führt z.B. die Methode Merge() die Zellen in eine einzelne Zelle innerhalb eines angegebenen Bereichs zusammen.

Das folgende Beispiel zeigt, wie Zellen (C6:E7) in einem Arbeitsblatt zusammengeführt werden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-MergingCellsInWorksheet.-1.py" >}}

## **Aufsplitten (Teilen) von zusammengeführten Zellen**
### **Verwendung von Microsoft Excel**
Die folgenden Schritte beschreiben, wie Sie zusammengeführte Zellen mit Microsoft Excel aufspalten können.

1. Wählen Sie die zusammengelegte Zelle aus. Wenn Zellen zusammengeführt wurden, ist **Zellen verbinden und zentrieren** in der **Formatierung**-Symbolleiste ausgewählt.
1. Klicken Sie auf **Zusammenführen und Zentrieren** in der **Formatierung**-Symbolleiste.

### **Mit Aspose.Cells für Python via .NET**
Die Klasse Aspose.Cells.Cells hat eine Methode namens UnMerge(), die die Zellen in ihren ursprünglichen Zustand aufteilt. Die Methode entpackt die Zellen mithilfe des Verweises der Zelle im Bereich der zusammengeführten Zelle.

Das folgende Beispiel zeigt, wie die zusammengeführten Zellen (C6) aufgeteilt werden. Das Beispiel verwendet die Datei, die im vorherigen Beispiel erstellt wurde, und teilt die zusammengeführten Zellen auf.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UnMergingtheMergedCells-1.py" >}}


## **Erweiterte Themen**
- [Erkennen von zusammengeführten Zellen in einem Arbeitsblatt](/cells/de/python-net/detect-merged-cells-in-a-worksheet/)

{{< app/cells/assistant language="python-net" >}}
