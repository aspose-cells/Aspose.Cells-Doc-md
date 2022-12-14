---
title: Zusammengeführte Cells in einem Arbeitsblatt erkennen
type: docs
weight: 3000
url: /de/java/detect-merged-cells-in-a-worksheet/
---
{{% alert color="primary" %}}

In Microsoft Excel können mehrere Zellen zu einer zusammengeführt werden. Dies wird häufig verwendet, um komplexe Tabellen zu erstellen oder um eine Zelle zu erstellen, die eine Überschrift enthält, die sich über mehrere Spalten erstreckt.

Aspose.Cells ermöglicht es Ihnen, verbundene Zellbereiche in einem Arbeitsblatt zu identifizieren. Sie können die Zusammenführung auch aufheben. Dieser Artikel enthält die einfachsten Codezeilen zum Ausführen der Aufgabe mit Aspose.Cells.

Dieser Artikel enthält kompakte Anweisungen, wie Sie verbundene Zellen in einem Arbeitsblatt finden und dann die Verbindung aufheben.

{{% /alert %}}

## **Demonstration**

 Dieses Beispiel verwendet eine Vorlage Microsoft Excel-Datei namens**MergeTrial**. Es hat einige zusammengeführte Zellbereiche in einem Blatt, das auch Merge Trial genannt wird.

**Die Vorlagendatei**

![todo: Bild_alt_Text](detect-merged-cells-in-a-worksheet_1.png)

 Aspose.Cells bietet die[**Cells.getMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MergedCells)Methode, die verwendet wird, um eine ArrayList von zusammengeführten Zellbereichen zu erhalten.

Wenn der folgende Code ausgeführt wird, löscht er den Inhalt des Blatts und hebt die Zusammenführung aller Zellbereiche auf, bevor die Datei erneut gespeichert wird.

**Die Ausgabedatei**

![todo: Bild_alt_Text](detect-merged-cells-in-a-worksheet_2.png)

## **Codebeispiel**

Bitte sehen Sie sich den folgenden Beispielcode an, um zu erfahren, wie Sie zusammengeführte Zellbereiche in einem Arbeitsblatt identifizieren und die Zusammenführung aufheben.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectMergedCells-DetectMergedCells.java" >}}

## **In Verbindung stehende Artikel**

- [Zellen verbinden und teilen](/cells/de/java/merging-and-unmerging-cells/).
