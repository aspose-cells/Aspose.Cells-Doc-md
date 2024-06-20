---
title: Erkennen von zusammengeführten Zellen in einem Arbeitsblatt
type: docs
weight: 3000
url: /de/java/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

In Microsoft Excel können mehrere Zellen zu einer zusammengeführt werden. Dies wird oft verwendet, um komplexe Tabellen zu erstellen oder um eine Zelle zu erstellen, die eine Überschrift umfasst, die mehrere Spalten umfasst.

Aspose.Cells ermöglicht es Ihnen, zusammengeführte Zellbereiche in einem Arbeitsblatt zu identifizieren. Sie können sie auch aufteilen. Dieser Artikel bietet die einfachsten Codezeilen zum Ausführen der Aufgabe mit Aspose.Cells.

Dieser Artikel bietet kompakte Anweisungen, wie man zusammengeführte Zellen in einem Arbeitsblatt findet und dann aufteilt.

{{% /alert %}}

## **Demonstration**

Dieses Beispiel verwendet eine Vorlagen-Microsoft Excel-Datei namens **MergeTrial**. Es hat einige zusammengeführte Zellbereiche auf einem Blatt, das auch Merge Trial genannt wird.

**Die Vorlagendatei**

![todo:image_alt_text](detect-merged-cells-in-a-worksheet_1.png)

Aspose.Cells liefert die [**Cells.getMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MergedCells) Methode, die verwendet wird, um ein Array-Liste von zusammengeführten Zellbereichen zu erhalten.

Wenn der folgende Code ausgeführt wird, löscht er den Inhalt des Blatts und hebt alle Zellbereiche wieder auf, bevor die Datei erneut gespeichert wird.

**Die Ausgabedatei**

![todo:image_alt_text](detect-merged-cells-in-a-worksheet_2.png)

## **Codebeispiel**

Bitte sehen Sie sich den folgenden Beispielcode an, um zu sehen, wie Sie zusammengeführte Zellbereiche in einem Arbeitsblatt identifizieren und aufteilen können.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectMergedCells-DetectMergedCells.java" >}}

## **Verwandte Artikel**

- [Zusammenführen und Aufteilen von Zellen](/cells/de/java/zusammenführen-und-aufteilen-von-zellen/).
