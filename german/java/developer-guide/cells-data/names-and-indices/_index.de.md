---
title: Umwandlung zwischen Zellnamen und Zeile/Spaltenindex
linktitle: Zellname und Indexumwandlung
type: docs
weight: 5
url: /de/java/names-and-indices/
description: Erfahren Sie, wie Sie das Umwandlungsergebnis zwischen Zellnamen und Zeilen/Spaltenindex mit Aspose.Cells for Java APIs erhalten.
keywords: Java Zellenindex in Namen umwandeln, Zellennamen in Zeilen/Spaltenindex mit Java APIs umwandeln, Wie man Zellnamen aus Zeilen und Spaltenindizes mit Java erhält, Java  Wie man Zeilen und Spaltenindizes aus Zellnamen erhält.
---

## **So erhalten Sie Zellnamen aus Zeilen- und Spaltenindizes**
Es ist möglich, den Namen einer Zelle anhand des Zeilen- und Spaltenindex zu finden. Dieser Artikel erläutert, wie.

Aspose.Cells stellt die Methode [CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) zur Verfügung, mit der Entwickler den Namen einer Zelle erhalten, wenn sie den Zeilen- und Spaltenindex angeben.

{{% alert color="primary" %}} 

Im Gegensatz zu Microsoft Excel, wo die Zeilen- und Spaltenindizes bei 1 beginnen, zählt Aspose.Cells die Zeilen- und Spaltenindizes ab 0.

{{% /alert %}} 

Der folgende Beispielcode veranschaulicht, wie [CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) verwendet wird, um den Zellnamen bei bekanntem Zeilen- und Spaltenindex abzurufen. Der Code generiert die folgende Ausgabe:



Zellname bei [0, 0]: A1

Zellname bei [4, 0]: A5

Zellname bei [0, 4]: E1

Zellname bei [2, 2]: C3

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
## **So erhalten Sie Zeilen- und Spaltenindizes aus dem Zellnamen**
Es ist möglich, den Zeilen- und Spaltenindex der Zelle anhand ihres Namens zu finden. Dieser Artikel erläutert, wie.

Aspose.Cells stellt die Methode [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) zur Verfügung, mit der Entwickler den Zeilen- und Spaltenindex aus dem Zellnamen erhalten.

{{% alert color="primary" %}} 

Im Gegensatz zu Microsoft Excel, wo die Zeilen- und Spaltenindizes bei 1 beginnen, zählt Aspose.Cells die Zeilen- und Spaltenindizes ab 0.

{{% /alert %}} 

Der folgende Beispielcode veranschaulicht, wie [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) verwendet wird, um den Zeilen- und Spaltenindex aus dem Zellnamen zu erhalten. Der Code generiert die folgende Ausgabe:



Zeilenindex der Zelle C6: 5

Spaltenindex der Zelle C6: 2

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
## **So erstellen Sie sichere Blattnamen**
Manchmal besteht die Notwendigkeit, den Tabellennamen zur Laufzeit zuzuweisen. In diesem Szenario können Tabellennamen zusätzliche Zeichen wie <>+(?”. enthalten. Es ist erforderlich, jedes solche Zeichen, das nicht als Tabellenname erlaubt ist, durch ein vom Benutzer bereitgestelltes voreingestelltes Zeichen zu ersetzen. Ebenso kann die Länge auf mehr als 31 Zeichen ansteigen, was abgeschnitten werden muss. Apache POI bietet bestimmte Funktionen zur Erstellung sicherer Namen, daher bietet Aspose.Cells eine ähnliche Funktion, um all diese Probleme zu behandeln. Der folgende Beispielcode zeigt diese Funktion:



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**Konsolenausgabe**

das ist der erste Name, der erstellt wurde

{{< highlight java >}}

` `<> + (adj.Private _ " Private"

{{< /highlight >}}
