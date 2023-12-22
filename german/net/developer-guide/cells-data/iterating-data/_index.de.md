---
title: Wie und wo Enumeratoren verwendet werden
linktitle: Daten iterieren
type: docs
weight: 55
url: /de/net/how-and-where-to-use-enumerators/
description: Erfahren Sie unter Aspose.Cells for .NET API, wie und wo Sie Enumeratoren verwenden.
keywords: How to use Enumerators, Cells Enumerator, Rows Enumerator, Columns Enumerator
---
{{% alert color="primary" %}}

Ein Enumerator ist ein Objekt, das die Möglichkeit bietet, einen Container oder eine Sammlung zu durchlaufen. Enumeratoren können zum Lesen der Daten in der Sammlung verwendet werden, sie können jedoch nicht zum Ändern der zugrunde liegenden Sammlung verwendet werden, wohingegen IEnumerable eine Schnittstelle ist, die eine Methode GetEnumerator definiert, die eine IEnumerator-Schnittstelle zurückgibt, die wiederum schreibgeschützten Zugriff ermöglicht eine Sammlung.

Aspose.Cells APIs bieten eine Reihe von Enumeratoren. In diesem Artikel werden jedoch hauptsächlich die drei unten aufgeführten Typen erläutert.

1. Cells Zähler
1. Zeilen-Enumerator
1. Spalten-Enumerator

{{% /alert %}}

##  **So verwenden Sie Enumeratoren**

###  **Cells Zähler**

Es gibt verschiedene Möglichkeiten, auf den Enumerator Cells zuzugreifen, und je nach Anwendungsanforderungen kann jede dieser Methoden verwendet werden. Hier sind die Methoden, die den Zellenenumerator zurückgeben.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

Alle oben genannten Methoden geben den Enumerator zurück, der das Durchlaufen der Sammlung initialisierter Zellen ermöglicht.

{{% alert color="primary" %}}

Beim Durchlaufen der Zellen sollte die Sammlung nicht geändert werden (Vorgänge, die dazu führen, dass eine neue Cell instanziiert oder eine vorhandene Cell gelöscht wird). Andernfalls kann der Enumerator möglicherweise nicht alle Zellen korrekt durchlaufen (einige Elemente werden möglicherweise wiederholt durchlaufen oder übersprungen).

{{% /alert %}}

Das folgende Codebeispiel veranschaulicht die Implementierung der IEnumerator-Schnittstelle für eine Cells-Sammlung.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

###  **Zeilen-Enumerator**

 Auf den Zeilenenumerator kann bei Verwendung von zugegriffen werden[**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator) Methode. Das folgende Codebeispiel demonstriert die Implementierung der IEnumerator-Schnittstelle für[**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

###  **Spalten-Enumerator**

 Auf den Spaltenenumerator kann bei Verwendung von zugegriffen werden[**ColumnCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/columncollection) Methode. Das folgende Codebeispiel demonstriert die Implementierung der IEnumerator-Schnittstelle für[**ColumnCollection**](https://reference.aspose.com/cells/net/aspose.cells/columncollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

##  **Wo man Enumeratoren verwendet**

Um die Vorteile der Verwendung von Enumeratoren zu diskutieren, nehmen wir ein Echtzeitbeispiel.

**Szenario**

 Eine Anwendungsanforderung besteht darin, alle Zellen in einem bestimmten Bereich zu durchlaufen[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)ihre Werte zu lesen. Zur Umsetzung dieses Ziels kann es mehrere Möglichkeiten geben. Nachfolgend werden einige davon demonstriert.

###  **Verwenden des Anzeigebereichs**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

###  **Verwenden von MaxDataRow und MaxDataColumn**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

Wie Sie sehen können, verwenden beide oben genannten Ansätze eine mehr oder weniger ähnliche Logik, das heißt; Durchlaufen Sie alle Zellen in der Sammlung, um die Zellwerte zu lesen. Dies könnte aus mehreren Gründen problematisch sein, wie unten erläutert.

1.  APIs wie[**MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow), [**MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow), [**MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn), [**MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) & [**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)erfordern zusätzliche Zeit, um die entsprechenden Statistiken zu sammeln. Falls die Datenmatrix (Zeilen x Spalten) groß ist, kann die Verwendung dieser APIs zu Leistungseinbußen führen.
1. In den meisten Fällen werden nicht alle Zellen in einem bestimmten Bereich instanziiert. In solchen Situationen ist die Überprüfung jeder Zelle in der Matrix nicht so effizient wie die Überprüfung nur der initialisierten Zellen.
1. Der Zugriff auf eine Zelle in einer Schleife als Cells Zeile, Spalte führt dazu, dass alle Zellobjekte in einem Bereich instanziiert werden, was schließlich zu einer OutOfMemoryException führen kann.

##  **Abschluss**

Basierend auf den oben genannten Fakten sind die folgenden möglichen Szenarien, in denen Enumeratoren verwendet werden sollten.

1. Es ist ein schreibgeschützter Zugriff auf die Zellsammlung erforderlich, d. h. Die Anforderung besteht darin, nur die Zellen zu untersuchen.
1. Eine große Anzahl von Zellen soll durchquert werden.
1. Nur initialisierte Zellen/Zeilen/Spalten werden durchlaufen.
