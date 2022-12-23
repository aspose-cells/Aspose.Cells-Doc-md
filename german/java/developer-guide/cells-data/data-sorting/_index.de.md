---
title: Datensortierung
type: docs
weight: 90
url: /de/java/sort-data-of-excel/
---
{{% alert color="primary" %}}

Die Datensortierung ist eine der vielen nützlichen Funktionen von Microsoft Excel. Es ermöglicht Benutzern, Daten zu bestellen, um das Scannen zu erleichtern.

Aspose.Cells ermöglicht es Ihnen, Arbeitsblattdaten alphabetisch oder numerisch zu sortieren. Es funktioniert genauso wie Microsoft Excel zum Sortieren von Daten.

{{% /alert %}}

## **Sortieren von Daten in Microsoft Excel**

So sortieren Sie Daten in Microsoft Excel:

1.  Wählen**Daten** von dem**Sortieren** Speisekarte.
 Der Dialog Sortieren wird angezeigt.
1. Wählen Sie eine Sortieroption aus.

Im Allgemeinen wird die Sortierung in einer Liste durchgeführt, die als zusammenhängende Gruppe von Daten definiert ist, in der die Daten in Spalten angezeigt werden.

**Das Dialogfeld „Sortieren“ in Microsoft Excel**

![todo: Bild_alt_Text](data-sorting_1.png)

## **Sortieren von Daten mit Aspose.Cells**

 Aspose.Cells bietet die[**Datensortierer**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) Klasse zum Sortieren von Daten in aufsteigender oder absteigender Reihenfolge. Die Klasse hat einige wichtige Mitglieder, zum Beispiel Methoden wie[**setKey1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key1) ... [**setKey2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key2) und[**setOrder1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order1) ... [**setOrder2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order2)Diese Member werden verwendet, um sortierte Schlüssel zu definieren und die Schlüsselsortierreihenfolge anzugeben.

 Sie müssen Schlüssel definieren und die Sortierreihenfolge festlegen, bevor Sie die Datensortierung implementieren. Die Klasse bietet die[**Sortieren**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort()) Methode zum Sortieren von Daten basierend auf den Zellendaten in einem Arbeitsblatt.

 Das[**Sortieren**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort()) akzeptiert die folgenden Parameter:

- [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), die Zellen des Arbeitsblatts.
- [**Zellbereich**](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea), der Bereich der Zellen. Definieren Sie den Zellenbereich, bevor Sie die Datensortierung anwenden.

Dieses Beispiel zeigt, wie Daten mit Aspose.Cells API sortiert werden. Das Beispiel verwendet eine Vorlagendatei „Book1.xls“ und sortiert Daten für den Datenbereich (A1:B14) im ersten Arbeitsblatt:

Dieses Beispiel verwendet die in Microsoft Excel erstellte Vorlagendatei „Book1.xls“.

**Vorlage Excel-Datei komplett mit Daten**

![todo: Bild_alt_Text](data-sorting_2.png)

Nachdem Sie den folgenden Code ausgeführt haben, werden die Daten entsprechend sortiert, wie Sie in der Excel-Ausgabedatei sehen können.

**Excel-Datei nach dem Sortieren der Daten ausgeben**

![todo: Bild_alt_Text](data-sorting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DataSorting-DataSorting.java" >}}

{{% alert color="primary" %}}

 Sortieren*Links nach rechts* , verwenden Sie die[**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortLeftToRight) Attribut.

{{% /alert %}}

## **Sortieren von Daten mit Hintergrundfarbe**

 Excel bietet die Funktion, Daten basierend auf der Hintergrundfarbe zu sortieren. Die gleiche Funktion wird mit Aspose.Cells bereitgestellt[**Datensortierer**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) wo[**SortOnType.CELL_COLOR**](https://reference.aspose.com/cells/java/com.aspose.cells/sortontype#CELL_COLOR) kann verwendet werden[**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int) ), um Daten basierend auf der Hintergrundfarbe zu sortieren. Alle Zellen, die eine bestimmte Farbe in enthalten[**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int)), Funktion werden entsprechend der Einstellung SortOrder oben oder unten platziert und die Reihenfolge der restlichen Zellen wird überhaupt nicht geändert.

Im Folgenden finden Sie die Beispieldateien, die zum Testen dieser Funktion heruntergeladen werden können:

[sampleBackGroundFile.xlsx](sampleBackGroundFile.xlsx)

[AusgabebeispielBackGroundFile.xlsx](outputsampleBackGroundFile.xlsx)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

## **Themen vorantreiben**
- [Daten in Spalte mit benutzerdefinierter Sortierliste sortieren](/cells/de/java/sort-data-in-column-with-custom-sort-list/)
- [Angeben einer Sortierwarnung beim Sortieren von Daten](/cells/de/java/specifying-sort-warning-while-sorting-data/)

