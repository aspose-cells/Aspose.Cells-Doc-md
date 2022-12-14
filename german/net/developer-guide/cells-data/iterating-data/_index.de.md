---
title: Wie und wo Enumeratoren verwendet werden
linktitle: Daten iterieren
type: docs
weight: 55
url: /de/net/how-and-where-to-use-enumerators/
---
{{% alert color="primary" %}}

Ein Enumerator ist ein Objekt, das die Möglichkeit bietet, einen Container oder eine Sammlung zu durchlaufen. Enumeratoren können verwendet werden, um die Daten in der Sammlung zu lesen, aber sie können nicht verwendet werden, um die zugrunde liegende Sammlung zu ändern, während IEnumerable eine Schnittstelle ist, die eine Methode GetEnumerator definiert, die eine IEnumerator-Schnittstelle zurückgibt, die wiederum einen schreibgeschützten Zugriff auf ermöglicht eine Sammlung.

Aspose.Cells APIs bieten eine Reihe von Enumeratoren, dieser Artikel behandelt jedoch hauptsächlich die drei unten aufgeführten Typen.

1. Cells Zähler
1. Zeilen-Enumerator
1. Spalten-Enumerator

{{% /alert %}}

## **Verwendung von Enumeratoren**

### **Cells Zähler**

Es gibt verschiedene Möglichkeiten, auf den Cells-Enumerator zuzugreifen, und je nach Anwendungsanforderungen kann jede dieser Methoden verwendet werden. Hier sind die Methoden, die den Zellen-Enumerator zurückgeben.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

Alle oben genannten Methoden geben den Enumerator zurück, der das Durchlaufen der Sammlung von initialisierten Zellen ermöglicht.

{{% alert color="primary" %}}

Beim Durchlaufen der Zellen sollte die Sammlung nicht geändert werden (Operationen, die dazu führen, dass ein neuer Cell instanziiert oder ein bestehender Cell gelöscht wird). Andernfalls kann der Enumerator möglicherweise nicht alle Zellen korrekt durchlaufen (einige Elemente werden möglicherweise wiederholt durchlaufen oder übersprungen).

{{% /alert %}}

Das folgende Codebeispiel veranschaulicht die Implementierung der IEnumerator-Schnittstelle für eine Cells-Auflistung.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

### **Zeilen-Enumerator**

 Auf den Rows Enumerator kann zugegriffen werden, während Sie die verwenden[**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator) Methode. Das folgende Codebeispiel veranschaulicht die Implementierung der IEnumerator-Schnittstelle für[**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

### **Spalten-Enumerator**

 Auf den Columns Enumerator kann während der Verwendung von zugegriffen werden[**ColumnCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/columncollection) Methode. Das folgende Codebeispiel veranschaulicht die Implementierung der IEnumerator-Schnittstelle für[**ColumnCollection**](https://reference.aspose.com/cells/net/aspose.cells/columncollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

## **Wo Enumeratoren verwendet werden**

Um die Vorteile der Verwendung von Enumeratoren zu erörtern, nehmen wir ein Echtzeitbeispiel.

**Szenario**

 Eine Anwendungsanforderung besteht darin, alle Zellen in einem gegebenen zu durchlaufen[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)ihre Werte zu lesen. Es könnte mehrere Möglichkeiten geben, dieses Ziel umzusetzen. Einige werden unten demonstriert.

### **Anzeigebereich verwenden**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

### **Verwenden von MaxDataRow & MaxDataColumn**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

Wie Sie feststellen können, verwenden beide oben genannten Ansätze eine mehr oder weniger ähnliche Logik, das heißt; Schleife über alle Zellen in der Sammlung, um die Zellenwerte zu lesen. Dies könnte aus einer Reihe von Gründen problematisch sein, wie unten diskutiert wird.

1.  APIs wie z[**MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow), [**MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow), [**MaxSpalte**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn), [**MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) & [**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)erfordern zusätzliche Zeit, um die entsprechenden Statistiken zu sammeln. Falls die Datenmatrix (Zeilen x Spalten) groß ist, kann die Verwendung dieser APIs zu Leistungseinbußen führen.
1. In den meisten Fällen werden nicht alle Zellen in einem bestimmten Bereich instanziiert. In solchen Situationen ist es nicht so effizient, jede Zelle in der Matrix zu prüfen, als nur die initialisierten Zellen zu prüfen.
1. Der Zugriff auf eine Zelle in einer Schleife als Cells Zeile, Spalte führt dazu, dass alle Zellobjekte in einem Bereich instanziiert werden, was schließlich OutOfMemoryException verursachen kann.

## **Fazit**

Basierend auf den oben genannten Fakten sind die folgenden möglichen Szenarien, in denen Enumeratoren verwendet werden sollten.

1. Nur-Lese-Zugriff auf die Zellsammlung ist erforderlich, das heißt; Die Anforderung besteht darin, nur die Zellen zu inspizieren.
1. Eine große Anzahl von Zellen soll durchquert werden.
1. Nur initialisierte Zellen/Zeilen/Spalten werden durchlaufen.
