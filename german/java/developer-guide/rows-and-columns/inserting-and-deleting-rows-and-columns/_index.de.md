---
title: Einfügen und Löschen von Zeilen und Spalten
type: docs
weight: 60
url: /de/java/inserting-and-deleting-rows-and-columns/
description: Erfahren Sie, wie Sie Zeilen und Spalten über die Aspose.Cells for Java APIs einfügen und löschen.
keywords: Wie man in Java Zeilen und Spalten einfügt und löscht, Zeilen und Spalten mit Java einfügt, Java Zeilen und Spalten löscht, Zeilen oder Spalten mit Java einfügt, Zeilen oder Spalten via Java löscht.
---

## **Einführung**
Beim Erstellen eines neuen Arbeitsblatts von Grund auf oder bei der Arbeit an einem vorhandenen Arbeitsblatt müssen möglicherweise zusätzliche Zeilen oder Spalten hinzugefügt werden, um mehr Daten aufzunehmen. Umgekehrt können auch Zeilen oder Spalten von bestimmten Positionen im Arbeitsblatt gelöscht werden.

Um diese Anforderungen zu erfüllen, bietet Aspose.Cells eine sehr einfache Reihe von Klassen und Methoden, die unten diskutiert werden.
## **Wie man Zeilen/Spalten verwaltet**
Aspose.Cells stellt eine [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-Klasse bereit, die eine Microsoft Excel-Datei darstellt. Die [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-Klasse enthält eine [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-Klasse dargestellt. Die [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-Klasse bietet eine [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)-Sammlung, die alle Zellen im Arbeitsblatt darstellt.

Die [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)-Sammlung bietet mehrere Methoden zur Verwaltung von Zeilen und Spalten in einem Arbeitsblatt. Einige davon werden unten diskutiert.

{{% alert color="primary" %}} 

Beim Hinzufügen von Zeilen oder Spalten verschiebt sich der Inhalt im Arbeitsblatt nach unten oder rechts, aber wenn Zeilen oder Spalten entfernt werden, verschiebt sich der Inhalt nach oben oder links.

{{% /alert %}} 
## **Wie man eine Zeile einfügt**
Fügen Sie an beliebiger Stelle eine Zeile ein, indem Sie die Methode [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) der [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung aufrufen. Die Methode [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) nimmt den Index der Zeile, in die die neue Zeile eingefügt werden soll, als erstes Argument und die Anzahl der Zeilen, die eingefügt werden sollen, als zweites Argument.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
## **Wie man mehrere Zeilen einfügt**
Um mehrere Zeilen in das Arbeitsblatt einzufügen, rufen Sie die Methode [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) der [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung auf. Die Methode [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) erfordert zwei Parameter:

- Zeilenindex: Der Index der Zeile, ab dem die neuen Zeilen eingefügt werden.
- Anzahl der Zeilen: Die Gesamtanzahl der einzufügenden Zeilen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
## **Wie man eine Zeile mit Formatierung einfügt**
Um eine Zeile mit Formatierungsoptionen einzufügen, verwenden Sie die Überladung [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-com.aspose.cells.InsertOptions-) mit einem [InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions) Parameter. Setzen Sie die Eigenschaft [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType) der Klasse [InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions) auf den Wert des Enumeration [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType). Das [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType) Enum besteht aus drei Mitgliedern, wie unten aufgelistet.

- [SAME_AS_ABOVE](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME-AS-ABOVE): Formatiert die Zeile genauso wie die oben liegende Zeile.
- [SAME_AS_BELOW](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME-AS-BELOW): Formatiert die Zeile genauso wie die unten liegende Zeile.
- [LÖSCHEN](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR): Löscht die Formatierung.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
## **Wie man eine Zeile löscht**
Um eine Zeile an beliebiger Stelle zu löschen, rufen Sie die Methode [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) der [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung auf. Die Methode [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) erfordert zwei Parameter:

- Zeilenindex: Der Index der Zeile, ab der die Zeilen gelöscht werden sollen.
- Anzahl der Zeilen: Die Gesamtanzahl der zu löschenden Zeilen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
## **Wie man mehrere Zeilen löscht**
Um mehrere Zeilen aus einem Arbeitsblatt zu löschen, rufen Sie die Methode [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) der [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung auf. Die Methode [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) erfordert zwei Parameter:

- Zeilenindex: Der Index der Zeile, ab der die Zeilen gelöscht werden sollen.
- Anzahl der Zeilen: Die Gesamtanzahl der zu löschenden Zeilen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
## **Wie man eine oder mehrere Spalten einfügt**
Entwickler können auch eine Spalte in das Arbeitsblatt an beliebiger Stelle einfügen, indem sie die Methode [insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns-int-int-) der [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung verwenden. Die Methode [insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns-int-int-) erfordert zwei Parameter:

- Spaltenindex, der Index der Spalte, von der die Spalte eingefügt werden soll.
- Anzahl der Spalten, die Gesamtanzahl der einzufügenden Spalten

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
## **Wie man eine Spalte löscht**
Um eine Spalte aus dem Arbeitsblatt an beliebiger Stelle zu löschen, rufen Sie die Methode [deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns-int-int-boolean-) der [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung auf. Die Methode [deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns-int-int-boolean-) erfordert die folgenden Parameter:

- Spaltenindex: Der Index der Spalte, aus der die Spalte gelöscht werden soll.
- Anzahl der Spalten: Die Gesamtanzahl der zu löschenden Spalten.
- Aktualisierung des Verweises: Boolescher Parameter, der angibt, ob Verweise in anderen Arbeitsblättern aktualisiert werden sollen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

{{< app/cells/assistant language="java" >}}
