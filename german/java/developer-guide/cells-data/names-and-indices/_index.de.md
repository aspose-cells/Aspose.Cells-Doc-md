---
title: Konvertierung zwischen Zellenname und Zeilen-/Spaltenindex
linktitle: Cell Namens- und Indexkonvertierung
type: docs
weight: 5
url: /de/java/names-and-indices/
description: Erfahren Sie, wie Sie mit den APIs Aspose.Cells for Java Konvertierungsergebnisse zwischen Zellennamen und Zeilen-/Spaltenindex erhalten.
keywords: Java Convert cell index to name, Convert cell name to row/column index using java apis, How to Get Cell Name from Row and Column Indices with java, Java How to Get Row and Column Indices from Cell Name.
---
##  **So erhalten Sie den Namen Cell aus Zeilen- und Spaltenindizes**
Es ist möglich, den Namen einer Zelle anhand des Zeilen- und Spaltenindex zu finden. In diesem Artikel wird erklärt, wie.

 Aspose.Cells bietet die[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\))-Methode, die es Entwicklern ermöglicht, den Namen einer Zelle abzurufen, wenn sie den Zeilen- und Spaltenindex angeben.

{{% alert color="primary" %}} 

Im Gegensatz zu Microsoft Excel, wo die Zeilen- und Spaltenindizes bei 1 beginnen, beginnt Aspose.Cells mit der Zählung der Zeilen- und Spaltenindizes bei 0.

{{% /alert %}} 

 Der folgende Beispielcode veranschaulicht die Verwendung[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)), um auf den Namen der Zelle zuzugreifen, der bei einem bekannten Zeilen- und Spaltenindex angegeben ist. Der Code generiert die folgende Ausgabe.



Cell Name bei [0, 0]: A1

Cell Name bei [4, 0]: A5

Cell Name bei [0, 4]: E1

Cell Name bei [2, 2]: C3

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
##  **So erhalten Sie Zeilen- und Spaltenindizes vom Namen Cell**
Es ist möglich, anhand des Namens einen Zeilen- und Spaltenindex der Zelle zu ermitteln. In diesem Artikel wird erklärt, wie.

 Aspose.Cells bietet die[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\))-Methode, die es Entwicklern ermöglicht, einen Zeilen- und Spaltenindex aus dem Namen der Zelle abzurufen.

{{% alert color="primary" %}} 

Im Gegensatz zu Microsoft Excel, wo die Zeilen- und Spaltenindizes bei 1 beginnen, beginnt Aspose.Cells mit der Zählung der Zeilen- und Spaltenindizes bei 0.

{{% /alert %}} 

 Der folgende Beispielcode veranschaulicht die Verwendung[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)), um den Zeilen- und Spaltenindex aus dem Namen der Zelle abzurufen. Der Code generiert die folgende Ausgabe.



Zeilenindex von Cell C6: 5

Spaltenindex von Cell C6: 2

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
##  **So erstellen Sie sichere Blattnamen**
 Manchmal ist es erforderlich, den Blattnamen zur Laufzeit zuzuweisen. In diesem Szenario kann es Blattnamen geben, die einige zusätzliche Zeichen enthalten, z<>+(?“. Es besteht die Notwendigkeit, solche Zeichen, die nicht als Blattname zulässig sind, durch einige vom Benutzer bereitgestellte voreingestellte Zeichen zu ersetzen. Ebenso kann die Länge auf mehr als 31 Zeichen ansteigen, die gekürzt werden müssen. Apache POI bietet bestimmte Funktionen zum Erstellen sicherer Namen. Daher bietet Aspose.Cells eine ähnliche Funktion zur Lösung all dieser Probleme. Der folgende Beispielcode demonstriert diese Funktion:



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**Konsolenausgabe**

Dies ist der Vorname, der cre ist

` `<> + (adj.Private _ „Privat“
