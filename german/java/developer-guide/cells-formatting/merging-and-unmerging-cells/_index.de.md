---
title: Zusammenführen und Aufteilen von Zellen
type: docs
weight: 140
url: /de/java/merging-and-unmerging-cells/
---

{{% alert color="primary" %}}

Sie möchten nicht immer die gleiche Anzahl von Zellen in jeder Zeile oder Spalte. Zum Beispiel möchten Sie einen Titel in einer Zelle platzieren, die mehrere Spalten umfasst. Oder, wenn Sie eine Rechnung erstellen, möchten Sie weniger Spalten für das Gesamtergebnis haben. Um aus zwei oder mehr Zellen eine Zelle zu machen, können Sie diese zusammenführen. Microsoft Excel ermöglicht es den Benutzern, Zellen auszuwählen und sie so zusammenzuführen, dass sie die Tabellenkalkulation nach ihren Wünschen strukturieren können.

**Das Ergebnis des Zusammenführens und Anschließenden Aufteilens eines Bereichs von Zellen, das wie die linken Zellen in Microsoft Excel formatiert ist** 

![todo:image_alt_text](merging-and-unmerging-cells_1.png)

Aspose.Cells unterstützt diese Funktion und kann auch Zellen in einem Arbeitsblatt zusammenführen. Sie können auch zusammengeführte Zellen trennen. Der Zellbezug einer zusammengeführten Zelle ist der Bezug der Zelle links oben im ursprünglich ausgewählten Bereich.

Beachten Sie, dass beim Zusammenführen von Zellen nur die Daten in der Zelle links oben beibehalten werden. Wenn sich Daten in den anderen Zellen im Bereich befinden, werden diese Daten gelöscht.

Auch die Formatierung basiert auf der Bezugszelle, sodass beim Zusammenführen von Zellen die Formatierungseinstellungen der Zelle oben links im Bereich auf die zusammengeführte Zelle angewendet werden. Wenn die Zelle aufgeteilt wird, behalten die neuen Zellen ihre Originalformatierungseinstellungen bei.

{{% /alert %}}

## **Zellen in einem Arbeitsblatt zusammenführen.**

### **Verwendung von Microsoft Excel**

Die folgenden Schritte beschreiben, wie man Zellen im Arbeitsblatt mit Microsoft Excel zusammenführen kann.

1. Kopieren Sie die Daten, die Sie in die oberste linke Zelle innerhalb des Bereichs einfügen möchten.
1. Wählen Sie die Zellen aus, die Sie zusammenführen möchten.
1. Um Zellen in einer Zeile oder Spalte zusammenzuführen und den Zellinhalt zu zentrieren, klicken Sie auf das Icon **Zusammenführen und Zentrieren** in der **Formatierung**-Symbolleiste.

### **Verwendung von Aspose.Cells**

Die Klasse [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) verfügt über einige nützliche Methoden für diese Aufgabe. Zum Beispiel führt die Methode [**merge()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)) die Zellen in eine einzige Zelle innerhalb eines festgelegten Bereichs von Zellen zusammen.

Die folgende Ausgabe wird nach Ausführung des untenstehenden Codes generiert.

**Die Zellen (C6:E7) wurden zusammengeführt** 

![todo:image_alt_text](merging-and-unmerging-cells_2.png)

#### **Codebeispiel**

Das folgende Beispiel zeigt, wie Zellen (C6:E7) in einem Arbeitsblatt zusammengeführt werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}

## **Aufsplitten (Teilen) von zusammengeführten Zellen**

### **Verwendung von Microsoft Excel**

Die folgenden Schritte beschreiben, wie Sie zusammengeführte Zellen mit Microsoft Excel aufspalten können.

1. Wählen Sie die zusammengeführte Zelle aus. 
   Wenn Zellen kombiniert wurden, ist **Zusammenführen und Zentrieren** in der **Formatierung**-Symbolleiste ausgewählt.
1. Klicken Sie auf **Zusammenführen und Zentrieren** in der **Formatierung**-Symbolleiste.

#### **Verwendung von Aspose.Cells**

Die Klasse [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) verfügt über eine Methode namens [**unMerge()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unMerge(int,%20int,%20int,%20int)), die Zellen in ihren ursprünglichen Zustand zurückversetzt. Die Methode hebt die Kombination der Zellen basierend auf dem Zellenverweis im Bereich der zusammengeführten Zelle auf.

#### **Codebeispiel**

Das folgende Beispiel zeigt, wie die zusammengeführten Zellen (C6) aufgeteilt werden. Das Beispiel verwendet die Datei, die im vorherigen Beispiel erstellt wurde, und teilt die zusammengeführten Zellen auf.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UnMergingCellsInWorksheet-UnMergingCellsInWorksheet.java" >}}

## **Verwandte Artikel**

- [Auffinden und Aufteilen von zusammengeführten Zellen](/cells/de/java/zusammengeführte-zellen-in-einem-arbeitsblatt-erkennen/).
- [Kombinieren und Aufteilen eines Zellenbereichs mit den Methoden Range.merge() und Range.unMerge()](/cells/de/java/zusammenführen-oder-aufteilen-eines-zellenbereichs/).

