---
title: Einfügen und Löschen von Zeilen und Spalten
type: docs
weight: 60
url: /de/java/inserting-and-deleting-rows-and-columns/
description: Erfahren Sie, wie Sie Zeilen und Spalten über die APIs Aspose.Cells for Java einfügen und löschen.
keywords: How to Insert and Delete Rows and Columns in Java, Insert Rows and Columns using Java, Java Delete Rows and Columns, Insert Rows or Columns with Java, Delete Rows or Columns via Java.
---
##  **Einführung**
Unabhängig davon, ob wir ein neues Arbeitsblatt von Grund auf erstellen oder an einem vorhandenen Arbeitsblatt arbeiten, müssen wir möglicherweise zusätzliche Zeilen oder Spalten hinzufügen, um mehr Daten aufzunehmen. Umgekehrt müssen wir möglicherweise auch Zeilen oder Spalten an bestimmten Positionen im Arbeitsblatt löschen.

Um diese Anforderungen zu erfüllen, stellt Aspose.Cells einen sehr einfachen Satz von Klassen und Methoden bereit, die unten erläutert werden.
##  **So verwalten Sie Zeilen/Spalten**
 Aspose.Cells bietet a[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse, die eine Microsoft Excel-Datei darstellt. Der[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält a[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) Dies ermöglicht den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse. Der[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse bietet a[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)Sammlung, die alle Zellen im Arbeitsblatt darstellt.

 Der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)Die Sammlung bietet verschiedene Methoden zum Verwalten von Zeilen und Spalten in einem Arbeitsblatt. Einige davon werden im Folgenden besprochen.

{{% alert color="primary" %}} 

Wenn Zeilen oder Spalten hinzugefügt werden, wird der Inhalt im Arbeitsblatt nach unten oder rechts verschoben, wenn jedoch Zeilen oder Spalten entfernt werden, wird der Inhalt nach oben oder links verschoben.

{{% /alert %}} 
##  **So fügen Sie eine Zeile ein**
 Fügen Sie an einer beliebigen Stelle eine Zeile ein, indem Sie die aufrufen[insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) ) Methode der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung. Der[insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)Die Methode verwendet den Index der Zeile, in die die neue Zeile eingefügt wird, als erstes Argument und die Anzahl der einzufügenden Zeilen als zweites Argument.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
##  **So fügen Sie mehrere Zeilen ein**
 Um mehrere Zeilen in das Arbeitsblatt einzufügen, rufen Sie auf[insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) ) Methode der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung. Der[insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\))-Methode benötigt zwei Parameter:

- Zeilenindex: der Index der Zeile, ab der die neuen Zeilen eingefügt werden.
- Anzahl der Zeilen: Die Gesamtzahl der Zeilen, die eingefügt werden müssen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
##  **So fügen Sie eine Zeile mit Formatierung ein**
Um eine Zeile mit Formatierungsoptionen einzufügen, verwenden Sie die[insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int,%20com.aspose.cells.InsertOptions\)Überlastung, die dauert[InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)als Parameter. Stellen Sie die ein[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType)Eigentum von[InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)Klasse mit[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)Aufzählung. Der[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)Die Aufzählung hat drei Mitglieder, wie unten aufgeführt.

- [SAME_AS_ABOVE](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_ABOVE): Formatiert die Zeile genauso wie die obige Zeile.
- [SAME_AS_BELOW](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_BELOW): Formatiert die Zeile genauso wie die folgende Zeile.
- [CLEAR](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR): Löscht die Formatierung.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
##  **So löschen Sie eine Zeile**
 Um eine Zeile an einer beliebigen Stelle zu löschen, rufen Sie die auf[deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) Methode der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung. Der[deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\))-Methode benötigt zwei Parameter:

- Zeilenindex: der Index der Zeile, aus der die Zeilen gelöscht werden.
- Anzahl der Zeilen: Die Gesamtzahl der Zeilen, die gelöscht werden müssen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
##  **So löschen Sie mehrere Zeilen**
 Um mehrere Zeilen aus einem Arbeitsblatt zu löschen, rufen Sie auf[deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) Methode der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung. Der[deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\))-Methode benötigt zwei Parameter:

- Zeilenindex: der Index der Zeile, aus der die Zeilen gelöscht werden.
- Anzahl der Zeilen: Die Gesamtzahl der Zeilen, die gelöscht werden müssen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
##  **So fügen Sie eine oder mehrere Spalten ein**
 Entwickler können auch an einer beliebigen Stelle eine Spalte in das Arbeitsblatt einfügen, indem sie die aufrufen[insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\) ) Methode der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Sammlung. Der[insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\))-Methode benötigt zwei Parameter:

- Spaltenindex, der Index der Spalte, ab der die Spalte eingefügt wird
- Anzahl der Spalten, die Gesamtzahl der Spalten, die eingefügt werden müssen

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
##  **So löschen Sie eine Spalte**
 Um an einer beliebigen Stelle eine Spalte aus dem Arbeitsblatt zu löschen, rufen Sie auf[deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\) ) Methode der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung. Der[deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\))-Methode akzeptiert die folgenden Parameter:

- Spaltenindex: der Index der Spalte, aus der die Spalte gelöscht wird.
- Anzahl der Spalten: Die Gesamtzahl der Spalten, die gelöscht werden müssen.
- Referenz aktualisieren: Boolescher Parameter, der angibt, ob Referenzen in anderen Arbeitsblättern aktualisiert werden sollen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

