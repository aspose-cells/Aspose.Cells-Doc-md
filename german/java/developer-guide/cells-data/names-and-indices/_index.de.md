---
title: Konvertierung zwischen Zellenname und Zeilen-/Spaltenindex
linktitle: Cell Namens- und Indexkonvertierung
type: docs
weight: 5
url: /de/java/names-and-indices/
---
## **Rufen Sie den Namen Cell aus den Zeilen- und Spaltenindizes ab**
Es ist möglich, den Namen einer Zelle anhand des Zeilen- und Spaltenindex zu finden. Dieser Artikel erklärt, wie.

 Aspose.Cells bietet die[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\))-Methode, die es Entwicklern ermöglicht, den Namen einer Zelle zu erhalten, wenn sie den Zeilen- und Spaltenindex bereitstellen.

{{% alert color="primary" %}} 

Im Gegensatz zu Microsoft Excel, wo die Zeilen- und Spaltenindizes bei 1 beginnen, beginnt Aspose.Cells mit dem Zählen der Zeilen- und Spaltenindizes bei 0.

{{% /alert %}} 

 Der folgende Beispielcode veranschaulicht die Verwendung[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)), um auf den Namen der Zelle zuzugreifen, der an einem bekannten Zeilen- und Spaltenindex angegeben ist. Der Code generiert die folgende Ausgabe.



Cell Name bei [0, 0]: A1

Cell Name bei [4, 0]: A5

Cell Name bei [0, 4]: E1

Cell Name bei [2, 2]: C3

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
## **Rufen Sie Zeilen- und Spaltenindizes von Cell Name ab**
Es ist möglich, einen Zeilen- und Spaltenindex der Zelle anhand ihres Namens zu finden. Dieser Artikel erklärt, wie.

 Aspose.Cells bietet die[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\))-Methode, mit der Entwickler einen Zeilen- und Spaltenindex aus dem Namen der Zelle erhalten können.

{{% alert color="primary" %}} 

Im Gegensatz zu Microsoft Excel, wo die Zeilen- und Spaltenindizes bei 1 beginnen, beginnt Aspose.Cells mit dem Zählen der Zeilen- und Spaltenindizes bei 0.

{{% /alert %}} 

 Der folgende Beispielcode veranschaulicht die Verwendung[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)), um den Zeilen- und Spaltenindex aus dem Namen der Zelle abzurufen. Der Code generiert die folgende Ausgabe.



Zeilenindex von Cell C6: 5

Spaltenindex von Cell C6: 2

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
## **Erstellen Sie sichere Blattnamen**
Manchmal muss der Blattname zur Laufzeit zugewiesen werden. In diesem Szenario kann es Blattnamen geben, die einige zusätzliche Zeichen enthalten können, wie z<>+(?". Es ist notwendig, solche Zeichen, die als Blattname nicht zulässig sind, durch ein vom Benutzer bereitgestelltes voreingestelltes Zeichen zu ersetzen. Ebenso kann die Länge auf mehr als 31 Zeichen ansteigen, die abgeschnitten werden müssen. Apache POI bietet bestimmte Funktionen zum Erstellen sicherer Namen, daher wird eine ähnliche Funktion von Aspose.Cells bereitgestellt, um all diese Probleme zu behandeln. Der folgende Beispielcode demonstriert diese Funktion:



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**Konsolenausgabe**

Dies ist der Vorname, der cre ist

` `<> + (Adj. Privat _ "Privat"
