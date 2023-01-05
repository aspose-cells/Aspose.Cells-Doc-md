---
title: Wie und wo man Iteratoren verwendet
linktitle: Daten iterieren
type: docs
weight: 640
url: /de/java/how-and-where-to-use-iterators/
---
{{% alert color="primary" %}} 

Ein Objekt einer Iteratorschnittstelle kann verwendet werden, um alle Elemente einer Sammlung zu durchlaufen. Iteratoren können verwendet werden, um die Daten in einer Sammlung zu untersuchen, aber sie können nicht verwendet werden, um die zugrunde liegende Sammlung zu ändern. Um einen Iterator zu verwenden, um den Inhalt einer Sammlung zu durchlaufen, müssen im Allgemeinen die folgenden Schritte ausgeführt werden:

1. Rufen Sie einen Iterator für den Beginn der Auflistung ab, indem Sie die Iteratormethode der Auflistung aufrufen.
1. Richten Sie eine Schleife ein, die die hasNext-Methode aufruft. Lassen Sie die Schleife durchlaufen, solange die hasNext-Methode true zurückgibt.
1. Rufen Sie innerhalb der Schleife jedes Element ab, indem Sie die nächste Methode aufrufen.

Aspose.Cells APIs bieten eine Reihe von Iteratoren, aber dieser Artikel behandelt hauptsächlich die drei unten aufgeführten Typen.

1. Cells Iterator
1. Zeilen-Iterator
1. Spalten-Iterator

{{% /alert %}} 
## **Verwendung von Iteratoren**
### **Cells Iterator**
Es gibt verschiedene Möglichkeiten, auf den Iterator der Zellen zuzugreifen, und je nach Anwendungsanforderungen kann jede dieser Methoden verwendet werden. Hier sind die Methoden, die den Iterator der Zellen zurückgeben.

1. Cells.iterator
1. Row.iterator
1. Range.iterator

Alle oben genannten Methoden geben den Iterator zurück, der es ermöglicht, die Sammlung von Zellen, die initialisiert wurden, zu durchlaufen.

{{% alert color="primary" %}} 

Beim Durchlaufen der Zellen sollte die Sammlung nicht geändert werden (Operationen, die dazu führen, dass ein neuer Cell instanziiert oder ein bestehender Cell gelöscht wird). Andernfalls ist der Iterator möglicherweise nicht in der Lage, alle Zellen korrekt zu durchlaufen (einige Elemente werden möglicherweise wiederholt durchlaufen oder übersprungen).

{{% /alert %}} 

Das folgende Codebeispiel veranschaulicht die Implementierung der Iterator-Klasse für eine Cells-Auflistung.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CellsIterator-CellsIterator.java" >}}




##### **Zeilen-Iterator**
Auf den Rows-Iterator kann zugegriffen werden, während die RowCollection.iterator-Methode verwendet wird. Das folgende Codebeispiel veranschaulicht die Implementierung der Iterator for RowCollection-Klasse.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RowsIterator-RowsIterator.java" >}}




##### **Spalten-Iterator**
Auf den Columns-Iterator kann mit der ColumnCollection.iterator-Methode zugegriffen werden. Das folgende Codebeispiel veranschaulicht die Implementierung der Iterator for ColumnCollection-Klasse.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ColumnsIterator-ColumnsIterator.java" >}}




#### **Wo man Iteratoren verwendet**
Um die Vorteile der Verwendung von Iteratoren zu erörtern, nehmen wir ein Echtzeitbeispiel.
##### **Szenario**
Eine Anwendungsanforderung besteht darin, alle Zellen in einem bestimmten Arbeitsblatt zu durchlaufen, um ihre Werte zu lesen. Es könnte mehrere Möglichkeiten geben, dieses Ziel umzusetzen. Einige werden unten demonstriert.
###### **Anzeigebereich verwenden**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDisplayRange-UsingDisplayRange.java" >}}




###### **Verwenden von MaxDataRow & MaxDataColumn**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingMaxDataRowAndMaxDataColumn-UsingMaxDataRowAndMaxDataColumn.java" >}}





Wie Sie feststellen können, verwenden beide oben genannten Ansätze eine mehr oder weniger ähnliche Logik, das heißt; Schleife über alle Zellen in der Sammlung, um die Zellenwerte zu lesen. Dies könnte aus einer Reihe von Gründen problematisch sein, wie unten diskutiert wird.

1. Die APIs wie MaxRow, MaxDataRow, MaxColumn, MaxDataColumn und MaxDisplayRange benötigen zusätzliche Zeit, um die entsprechenden Statistiken zu sammeln. Falls die Datenmatrix (Zeilen x Spalten) groß ist, kann die Verwendung dieser APIs zu Leistungseinbußen führen.
1. In den meisten Fällen werden nicht alle Zellen in einem bestimmten Bereich instanziiert. In solchen Situationen ist es nicht so effizient, jede Zelle in der Matrix zu prüfen, als nur die initialisierten Zellen zu prüfen.
1. Der Zugriff auf eine Zelle in einer Schleife als Cells.get(rowIndex, columnIndex) bewirkt, dass alle Zellobjekte in einem Bereich instanziiert werden, was schließlich zu OutOfMemoryError führen kann.
##### **Fazit**
Basierend auf den oben genannten Fakten sind im Folgenden die möglichen Szenarien aufgeführt, in denen Iteratoren verwendet werden sollten.

1. Nur-Lese-Zugriff auf die Zellsammlung ist erforderlich, das heißt; Voraussetzung ist, dass nur die Zellen inspiziert werden.
1. Eine große Anzahl von Zellen muss durchquert werden.
1. Es sollen nur initialisierte Zellen/Zeilen/Spalten durchlaufen werden.
