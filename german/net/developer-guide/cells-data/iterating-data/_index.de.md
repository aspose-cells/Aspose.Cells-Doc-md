---
title: Wie und wo Verwenden von Enumeratoren
linktitle: Daten durchlaufen
type: docs
weight: 55
url: /de/net/how-and-where-to-use-enumerators/
description: Erfahren Sie, wie und wo Verwenden von Enumeratoren durch die Aspose.Cells for .NET API
keywords: Wie man Enumeratoren verwendet, Zellen Enumerator, Zeilen Enumerator, Spalten Enumerator
---

{{% alert color="primary" %}}

Ein Enumerator ist ein Objekt, das die Möglichkeit bietet, einen Container oder eine Sammlung zu durchlaufen. Enumeratoren können zum Lesen der Daten in der Sammlung verwendet werden, dürfen jedoch nicht zur Änderung der zugrunde liegenden Sammlung verwendet werden, während IEnumerable ein Interface ist, das eine Methode GetEnumerator definiert, die ein IEnumerator-Interface zurückgibt, das wiederum einen schreibgeschützten Zugriff auf eine Sammlung ermöglicht.

Aspose.Cells APIs bieten eine Reihe von Enumeratoren, in diesem Artikel werden jedoch hauptsächlich die drei unten aufgeführten Typen diskutiert.

1. Zellen-Enumerator
1. Zeilen Enumerator
1. Spalten Enumerator

{{% /alert %}}

## **Wie man Enumerators verwendet**

### **Zellen Enumerator**

Es gibt verschiedene Möglichkeiten, auf den Zellen Enumerator zuzugreifen, und man kann eine dieser Methoden basierend auf den Anforderungen der Anwendung verwenden. Hier sind die Methoden, die den Zellen Enumerator zurückgeben.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

Alle oben genannten Methoden geben den Enumerator zurück, der das Durchlaufen der Sammlung von Zellen ermöglicht, die initialisiert wurden.

{{% alert color="primary" %}}

Beim Durchlaufen der Zellen sollte die Sammlung nicht geändert werden (Operationen, die dazu führen, dass eine neue Zelle instanziiert oder eine vorhandene Zelle gelöscht wird). Andernfalls kann der Enumerator möglicherweise nicht in der Lage sein, alle Zellen korrekt zu durchlaufen (einige Elemente können wiederholt durchlaufen oder übersprungen werden).

{{% /alert %}}

Das folgende Codebeispiel demonstriert die Implementierung des IEnumerator-Interface für eine Zellen-Sammlung.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

### **Zeilen Enumerator**

Der Zeilen Enumerator kann beim Verwenden der [**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator)-Methode abgerufen werden. Das folgende Codebeispiel demonstriert die Implementierung des IEnumerator-Interface für [**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

### **Spalten Enumerator**

Der Spalten Enumerator kann beim Verwenden der [**ColumnCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/columncollection)-Methode abgerufen werden. Das folgende Codebeispiel demonstriert die Implementierung des IEnumerator-Interface für [**ColumnCollection**](https://reference.aspose.com/cells/net/aspose.cells/columncollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

## **Wo man Enumerators verwenden sollte**

Um die Vorteile der Verwendung von Enumerators zu diskutieren, lassen Sie uns ein Echtzeitbeispiel betrachten.

**Szenario**

Eine Anforderung der Anwendung besteht darin, alle Zellen in einem gegebenen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) zu durchlaufen, um ihre Werte zu lesen. Es könnten mehrere Möglichkeiten geben, dieses Ziel zu implementieren. Einige sind unten dargestellt.

### **Die Anzeigebereich verwenden**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

### **Verwenden von MaxDataRow & MaxDataColumn**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

Wie Sie beobachten können, verwenden beide oben genannten Ansätze mehr oder weniger ähnliche Logik, nämlich das Durchlaufen aller Zellen in der Sammlung, um die Zellwerte zu lesen. Dies könnte aus einer Reihe von Gründen problematisch sein, wie unten diskutiert.

1. APIs wie [**MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow), [**MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow), [**MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn), [**MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) & [**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) benötigen zusätzliche Zeit, um die entsprechenden Statistiken zu sammeln. Wenn die Datenmatrix (Zeilen x Spalten) groß ist, könnte die Verwendung dieser APIs eine Leistungseinbuße bedeuten.
1. In den meisten Fällen sind nicht alle Zellen in einem bestimmten Bereich instanziiert. In solchen Situationen ist es nicht so effizient, jede Zelle in der Matrix zu überprüfen, im Vergleich dazu nur die initialisierten Zellen zu überprüfen.
1. Das Zugreifen auf eine Zelle in einer Schleife als Cells row, column wird alle Zellenobjekte in einem Bereich instanziieren, was letztendlich zu einem OutOfMemoryException führen könnte.

## **Fazit**

Basierend auf den oben genannten Fakten sind die folgenden möglichen Szenarien, in denen Enumeratoren verwendet werden sollten.

1. Nur Lesezugriff auf die Zellsammlung erforderlich ist, d.h. die Anforderung besteht darin, nur die Zellen zu inspizieren.
1. Eine große Anzahl von Zellen muss durchlaufen werden.
1. Nur initialisierte Zellen/Zeilen/Spalten müssen durchlaufen werden.
