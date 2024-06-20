---
title: Wie und wo Iteratoren verwenden
linktitle: Daten durchlaufen
type: docs
weight: 640
url: /de/java/how-and-where-to-use-iterators/
---

{{% alert color="primary" %}} 

Ein Objekt einer Iterator-Schnittstelle kann verwendet werden, um alle Elemente einer Sammlung zu durchlaufen. Iteratoren können verwendet werden, um die Daten in einer Sammlung zu inspizieren, aber sie können nicht verwendet werden, um die zugrunde liegende Sammlung zu ändern. Im Allgemeinen müssen folgende Schritte unternommen werden, um einen Iterator zum Durchlaufen des Inhalts einer Sammlung zu verwenden:

1. Einen Iterator am Anfang der Sammlung erhalten, indem die Iterator-Methode der Sammlung aufgerufen wird.
1. Eine Schleife einrichten, die die hasNext-Methode aufruft. Die Schleife iteriert, solange die hasNext-Methode true zurückgibt.
1. Innerhalb der Schleife jedes Element erhalten, indem die next-Methode aufgerufen wird.

Aspose.Cells-APIs bieten eine Vielzahl von Iteratoren, jedoch behandelt dieser Artikel hauptsächlich die unten aufgeführten drei Arten.

1. Cells-Iterator
1. Rows-Iterator
1. Columns-Iterator

{{% /alert %}} 
## **Wie man Iteratoren verwendet**
### **Cells-Iterator**
Es gibt verschiedene Möglichkeiten, auf den Zellen-Iterator zuzugreifen, und man kann je nach den Anforderungen der Anwendung eine dieser Methoden verwenden. Hier sind die Methoden, die den Zellen-Iterator zurückgeben.

1. Cells.iterator
1. Row.iterator
1. Range.iterator

Alle oben genannten Methoden geben den Iterator zurück, der es ermöglicht, die Sammlung von Zellen zu durchlaufen, die initialisiert wurden.

{{% alert color="primary" %}} 

Beim Durchlaufen der Zellen sollte die Sammlung nicht verändert werden (Operationen, die dazu führen, dass eine neue Zelle instantiiert oder eine vorhandene Zelle gelöscht wird). Andernfalls kann der Iterator nicht in der Lage sein, alle Zellen korrekt zu durchlaufen (einige Elemente können wiederholt oder übersprungen durchlaufen werden).

{{% /alert %}} 

Das folgende Codebeispiel demonstriert die Implementierung der Iterator-Klasse für eine Zellensammlung.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CellsIterator-CellsIterator.java" >}}




##### **Reihen Iterator**
Der Reihen-Iterator kann beim Verwenden der RowCollection.iterator-Methode aufgerufen werden. Das folgende Codebeispiel demonstriert die Implementierung des Iterators für die RowCollection-Klasse.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RowsIterator-RowsIterator.java" >}}




##### **Spalten Iterator**
Der Spalten-Iterator kann beim Verwenden der ColumnCollection.iterator-Methode aufgerufen werden. Das folgende Codebeispiel demonstriert die Implementierung des Iterators für die ColumnCollection-Klasse.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ColumnsIterator-ColumnsIterator.java" >}}




#### **Wo Iteratoren verwendet werden sollen**
Um die Vorteile der Verwendung von Iteratoren zu diskutieren, betrachten wir ein reales Beispiel.
##### **Szenario**
Eine Anwendungsanforderung besteht darin, alle Zellen in einem gegebenen Arbeitsblatt zu durchlaufen, um ihre Werte zu lesen. Es könnte mehrere Möglichkeiten geben, dieses Ziel zu erreichen. Einige sind unten dargestellt.
###### **Die Anzeigebereich verwenden**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDisplayRange-UsingDisplayRange.java" >}}




###### **Verwenden von MaxDataRow & MaxDataColumn**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingMaxDataRowAndMaxDataColumn-UsingMaxDataRowAndMaxDataColumn.java" >}}





Wie Sie beobachten können, verwenden beide oben genannten Ansätze mehr oder weniger ähnliche Logik, nämlich; Schleife über alle Zellen in der Sammlung, um die Zellwerte zu lesen. Dies könnte aus verschiedenen Gründen problematisch sein, wie unten diskutiert.

1. Die APIs wie MaxRow, MaxDataRow, MaxColumn, MaxDataColumn & MaxDisplayRange benötigen zusätzliche Zeit, um die entsprechenden Statistiken zu sammeln. Wenn die Datenmatrix (Zeilen x Spalten) groß ist, könnte die Verwendung dieser APIs eine Leistungsstrafe verhängen.
1. In den meisten Fällen sind nicht alle Zellen in einem bestimmten Bereich instanziiert. In solchen Situationen ist es nicht so effizient, jede Zelle in der Matrix zu überprüfen, im Vergleich dazu nur die initialisierten Zellen zu überprüfen.
1. Der Zugriff auf eine Zelle in einer Schleife wie Cells.get(rowIndex, columnIndex) führt dazu, dass alle Zellenobjekte in einem Bereich instanziiert werden, was letztendlich zu einem OutOfMemoryError führen kann.
##### **Fazit**
Basierend auf den oben genannten Fakten sind folgende mögliche Szenarien, in denen Iteratoren verwendet werden sollten.

1. Schreibgeschützter Zugriff auf die Zellsammlung ist erforderlich, d.h. es ist nur erforderlich, die Zellen zu inspizieren.
1. Eine große Anzahl von Zellen muss durchlaufen werden.
1. Es sollen nur initialisierte Zellen/Zeilen/Spalten durchlaufen werden.
