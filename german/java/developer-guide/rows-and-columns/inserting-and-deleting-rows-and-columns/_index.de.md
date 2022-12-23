---
title: Einfügen und Löschen von Zeilen und Spalten
type: docs
weight: 60
url: /de/java/inserting-and-deleting-rows-and-columns/
---
## **Einführung**
Unabhängig davon, ob Sie ein neues Arbeitsblatt von Grund auf neu erstellen oder an einem vorhandenen Arbeitsblatt arbeiten, müssen wir möglicherweise zusätzliche Zeilen oder Spalten hinzufügen, um mehr Daten aufzunehmen. Umgekehrt müssen wir möglicherweise auch Zeilen oder Spalten von bestimmten Positionen im Arbeitsblatt löschen.

Um diese Anforderungen zu erfüllen, stellt Aspose.Cells einen sehr einfachsten Satz von Klassen und Methoden bereit, die unten besprochen werden.
## **Zeilen/Spalten verwalten**
 Aspose.Cells bietet eine[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse, die eine Microsoft Excel-Datei darstellt. Das[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält a[Arbeitsblattsammlung](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse. Das[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse bietet a[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)Auflistung, die alle Zellen im Arbeitsblatt darstellt.

 Das[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)-Sammlung bietet mehrere Methoden zum Verwalten von Zeilen und Spalten in einem Arbeitsblatt. Einige davon werden unten besprochen.

{{% alert color="primary" %}} 

Wenn Zeilen oder Spalten hinzugefügt werden, wird der Inhalt im Arbeitsblatt nach unten oder rechts verschoben, aber wenn Zeilen oder Spalten entfernt werden, wird der Inhalt nach oben oder links verschoben.

{{% /alert %}} 
## **Einfügen einer Zeile**
 Fügen Sie an beliebiger Stelle eine Zeile ein, indem Sie die aufrufen[Zeilen einfügen](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) ) Methode der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung. Das[Zeilen einfügen](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\))-Methode nimmt den Index der Zeile, in die die neue Zeile eingefügt wird, als erstes Argument und die Anzahl der einzufügenden Zeilen als zweites Argument.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
## **Mehrere Zeilen einfügen**
 Um mehrere Zeilen in das Arbeitsblatt einzufügen, rufen Sie die auf[Zeilen einfügen](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) ) Methode der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung. Das[Zeilen einfügen](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) Methode nimmt zwei Parameter:

- Zeilenindex: Der Index der Zeile, ab der die neuen Zeilen eingefügt werden.
- Anzahl der Zeilen: Die Gesamtzahl der Zeilen, die eingefügt werden müssen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
## **Zeile mit Formatierung einfügen**
Um eine Zeile mit Formatierungsoptionen einzufügen, verwenden Sie die[Zeilen einfügen](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int,%20com.aspose.cells.InsertOptions\)) Überlastung, die dauert[Einfügeoptionen](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)als Parameter. Stellen Sie die ein[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType)Eigentum von[Einfügeoptionen](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)Klasse mit[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)Aufzählung. Das[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)Die Aufzählung hat drei Mitglieder, wie unten aufgeführt.

- [GLEICH_ALS_OBEN](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_ABOVE)Formatiert die Zeile genauso wie die obige Zeile.
- [GLEICH_ALS_UNTER](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_BELOW): Formatiert die Zeile genauso wie die untere Zeile.
- [KLAR](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR): Löscht die Formatierung.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
## **Löschen einer Zeile**
 Um eine Zeile an einer beliebigen Stelle zu löschen, rufen Sie die auf[Zeilen löschen](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) Methode der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung. Das[Zeilen löschen](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) Methode nimmt zwei Parameter:

- Zeilenindex: Der Index der Zeile, aus der die Zeilen gelöscht werden.
- Anzahl der Zeilen: Die Gesamtzahl der Zeilen, die gelöscht werden müssen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
## **Löschen mehrerer Zeilen**
Um mehrere Zeilen aus einem Arbeitsblatt zu löschen, rufen Sie die auf[Zeilen löschen](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) Methode der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung. Das[Zeilen löschen](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) Methode nimmt zwei Parameter:

- Zeilenindex: Der Index der Zeile, aus der die Zeilen gelöscht werden.
- Anzahl der Zeilen: Die Gesamtzahl der Zeilen, die gelöscht werden müssen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
## **Einfügen einer oder mehrerer Spalten**
 Entwickler können auch an beliebiger Stelle eine Spalte in das Arbeitsblatt einfügen, indem sie die aufrufen[Spalten einfügen](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\) ) Methode der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Sammlung. Das[Spalten einfügen](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\)) Methode nimmt zwei Parameter:

- Spaltenindex, der Index der Spalte, aus der die Spalte eingefügt wird
- Anzahl der Spalten, die Gesamtzahl der Spalten, die eingefügt werden müssen

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
## **Löschen einer Spalte**
 Um eine Spalte an einer beliebigen Stelle aus dem Arbeitsblatt zu löschen, rufen Sie die auf[Spalten löschen](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\) ) Methode der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung. Das[Spalten löschen](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\))-Methode nimmt die folgenden Parameter an:

- Spaltenindex: Der Index der Spalte, aus der die Spalte gelöscht wird.
- Spaltenanzahl: Die Gesamtzahl der zu löschenden Spalten.
- Referenz aktualisieren: Boolescher Parameter, der angibt, ob Referenzen in anderen Arbeitsblättern aktualisiert werden sollen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

