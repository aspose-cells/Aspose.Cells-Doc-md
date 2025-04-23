---
title: Daten sortieren
type: docs
weight: 90
url: /de/java/sort-data-of-excel/
---

{{% alert color="primary" %}}

Das Sortieren von Daten ist eine der vielen nützlichen Funktionen von Microsoft Excel. Es ermöglicht Benutzern, Daten zu ordnen, um deren Überprüfung zu erleichtern.

Aspose.Cells ermöglicht es Ihnen, Arbeitsblattdaten alphabetisch oder numerisch zu sortieren. Es funktioniert genauso wie Microsoft Excel, um Daten zu sortieren.

{{% /alert %}}

## **Daten sortieren in Microsoft Excel**

Um Daten in Microsoft Excel zu sortieren:

1. Wählen Sie **Daten** im **Sortieren**-Menü aus.
   Der Sortierdialog wird angezeigt.
1. Wählen Sie eine Sortieroption aus.

Im Allgemeinen wird das Sortieren auf einer Liste durchgeführt - definiert als eine zusammenhängende Gruppe von Daten, bei der die Daten in Spalten angezeigt werden.

**Der Sortierdialog in Microsoft Excel**

![todo:image_alt_text](data-sorting_1.png)

## **Daten mit Aspose.Cells sortieren**

Aspose.Cells bietet die [**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter)-Klasse zum Sortieren von Daten in aufsteigender oder absteigender Reihenfolge an. Die Klasse hat wichtige Elemente wie z.B. Methoden wie [**setKey1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key1)...[**setKey2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key2) und [**setOrder1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order1)...[**setOrder2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order2). Diese Elemente werden verwendet, um sortierte Schlüssel zu definieren und die Schlüsselsortierreihenfolge anzugeben.

Sie müssen Schlüssel definieren und die Sortierreihenfolge festlegen, bevor Sie das Daten sortieren implementieren. Die Klasse bietet die [**sort**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort--)-Methode, die verwendet wird, um Daten nach den Zelldaten in einem Arbeitsblatt zu sortieren.

Die [**sort**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort--)-Methode akzeptiert die folgenden Parameter:

- [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), die Zellen des Arbeitsblatts.
- [**CellArea**](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea), der Bereich von Zellen. Definieren Sie den Zellenbereich, bevor Sie das Daten sortieren anwenden.

Dieses Beispiel zeigt, wie man Daten mit der Aspose.Cells API sortiert. Das Beispiel verwendet eine Vorlagendatei "Book1.xls" und sortiert Daten für den Datenbereich (A1:B14) im ersten Arbeitsblatt:

Dieses Beispiel verwendet die Vorlagendatei "Book1.xls", die in Microsoft Excel erstellt wurde.

**Vorlagen-Excel-Datei komplett mit Daten**

![todo:image_alt_text](data-sorting_2.png)

Nach Ausführen des folgenden Codes werden die Daten entsprechend sortiert, wie Sie es in der Ausgabedatei Excel sehen können.

**Ausgabedatei Excel nach Sortieren der Daten**

![todo:image_alt_text](data-sorting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DataSorting-DataSorting.java" >}}

{{% alert color="primary" %}}

Um *VonLinksNachRechts* zu sortieren, verwenden Sie das [**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortLeftToRight)-Attribut.

{{% /alert %}}

## **Daten mit Hintergrundfarbe sortieren**

Excel bietet die Möglichkeit, Daten basierend auf der Hintergrundfarbe zu sortieren. Die gleiche Funktion wird mit Aspose.Cells unter Verwendung von [**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) bereitgestellt, wobei [**SortOnType.CELL_COLOR**](https://reference.aspose.com/cells/java/com.aspose.cells/sortontype#CELL-COLOR) in [**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey-int-int-) verwendet wird, um Daten basierend auf der Hintergrundfarbe zu sortieren. Alle Zellen, die die festgelegte Farbe im [**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey-int-int-) enthalten, werden je nach Sortierreihenfolge-Einstellung an die Spitze oder an den Boden verschoben, und die Reihenfolge der übrigen Zellen bleibt unverändert.

Hier sind die Beispiel Dateien, die heruntergeladen werden können, um diese Funktion zu testen:

[sampleBackGroundFile.xlsx](sampleBackGroundFile.xlsx)

[outputsampleBackGroundFile.xlsx](outputsampleBackGroundFile.xlsx)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

## **Erweiterte Themen**
- [Daten in Spalte mit benutzerdefinierter Sortierliste sortieren](/cells/de/java/sort-data-in-column-with-custom-sort-list/)
- [Spezifizieren von Sortierwarnungen beim Sortieren von Daten](/cells/de/java/specifying-sort-warning-while-sorting-data/)

{{< app/cells/assistant language="java" >}}
