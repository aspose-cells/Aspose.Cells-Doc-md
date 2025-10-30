---
title: Wie und Wo Enumeratoren mit Golang über C++ verwenden
linktitle: Daten durchlaufen
type: docs
weight: 55
url: /de/go-cpp/how-and-where-to-use-enumerators/
description: Lernen Sie, wie man How and Where to Use Enumerators durch die API Aspose.Cells for C++ verwendet.
keywords: Wie man Enumeratoren verwendet, Zellen Enumerator, Zeilen Enumerator, Spalten Enumerator
---

{{% alert color="primary" %}}

Ein Enumerator ist ein Objekt, das die Fähigkeit bietet, einen Container oder eine Sammlung zu durchlaufen. Enumerator können verwendet werden, um die Daten in der Sammlung zu lesen, aber sie können nicht verwendet werden, um die zugrunde liegende Sammlung zu modifizieren, während IEnumerable eine Schnittstelle ist, die eine Methode GetEnumerator definiert, die ein IEnumerator Interface zurückgibt, was wiederum lese-aktuellen Zugriff auf eine Sammlung ermöglicht.

Aspose.Cells APIs bieten eine Reihe von Enumeratoren, in diesem Artikel werden jedoch hauptsächlich die drei unten aufgeführten Typen diskutiert.

1. Zellen-Enumerator
1. Zeilen Enumerator
1. Spalten Enumerator

{{% /alert %}}

## **Wie man Enumerators verwendet**

### **Zellen Enumerator**

Es gibt verschiedene Möglichkeiten, auf den Zellen Enumerator zuzugreifen, und man kann eine dieser Methoden basierend auf den Anforderungen der Anwendung verwenden. Hier sind die Methoden, die den Zellen Enumerator zurückgeben.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/cells/getenumerator/)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/row/getenumerator/)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/range/getenumerator/)

Alle oben genannten Methoden geben den Enumerator zurück, der das Durchlaufen der Sammlung von Zellen ermöglicht, die initialisiert wurden.

{{% alert color="primary" %}}

Beim Durchlaufen der Zellen sollte die Sammlung nicht geändert werden (Operationen, die dazu führen, dass eine neue Zelle instanziiert oder eine vorhandene Zelle gelöscht wird). Andernfalls kann der Enumerator möglicherweise nicht in der Lage sein, alle Zellen korrekt zu durchlaufen (einige Elemente können wiederholt durchlaufen oder übersprungen werden).

{{% /alert %}}

Das folgende Codebeispiel demonstriert die Implementierung des IEnumerator-Interface für eine Zellen-Sammlung.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData.go" >}}
### **Zeilen Enumerator**

Der Zeilen-Enumerator kann beim Verwenden der [**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/rowcollection/getenumerator/)-Methode aufgerufen werden. Das folgende Codebeispiel demonstriert die Implementierung des IEnumerator-Interfaces für [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-1.go" >}}
### **Zeilen Get**

Die Spalten können beim Verwenden der [**ColumnCollection.Get**](https://reference.aspose.com/cells/go-cpp/columncollection/get/)-Methode aufgerufen werden. Das folgende Codebeispiel demonstriert die Implementierung der Get-Methode für [**ColumnCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/columncollection/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-2.go" >}}
## **Wo man Enumerators verwenden sollte**

Um die Vorteile der Verwendung von Enumerators zu diskutieren, lassen Sie uns ein Echtzeitbeispiel betrachten.

**Szenario**

Ein Anwendungsziel ist es, alle Zellen in einem gegebenen [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) zu durchlaufen, um ihre Werte zu lesen. Es gibt mehrere Möglichkeiten, dieses Ziel zu erreichen. Einige werden unten demonstriert.

### **Die Anzeigebereich verwenden**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-3.go" >}}
### **Verwenden von MaxDataRow & MaxDataColumn**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-4.go" >}}
Wie Sie beobachten können, verwenden beide oben genannten Ansätze mehr oder weniger ähnliche Logik, nämlich das Durchlaufen aller Zellen in der Sammlung, um die Zellwerte zu lesen. Dies könnte aus einer Reihe von Gründen problematisch sein, wie unten diskutiert.

1. APIs wie [**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/cells/getmaxrow/), [**GetMaxDataRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/), [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxcolumn/), [**GetMaxDataColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) & [**GetMaxDisplayRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) benötigen zusätzliche Zeit, um die entsprechenden Statistiken zu sammeln. Falls die Datenmatrix (Zeilen x Spalten) groß ist, könnte die Verwendung dieser APIs eine Leistungsverzögerung verursachen.
1. In den meisten Fällen sind nicht alle Zellen in einem bestimmten Bereich instanziiert. In solchen Situationen ist es nicht so effizient, jede Zelle in der Matrix zu überprüfen, im Vergleich dazu nur die initialisierten Zellen zu überprüfen.
1. Das Zugreifen auf eine Zelle in einer Schleife als Cells row, column wird alle Zellenobjekte in einem Bereich instanziieren, was letztendlich zu einem OutOfMemoryException führen könnte.

## **Fazit**

Basierend auf den oben genannten Fakten sind die folgenden möglichen Szenarien, in denen Enumeratoren verwendet werden sollten.

1. Nur Lesezugriff auf die Zellsammlung erforderlich ist, d.h. die Anforderung besteht darin, nur die Zellen zu inspizieren.
1. Eine große Anzahl von Zellen muss durchlaufen werden.
1. Nur initialisierte Zellen/Zeilen/Spalten müssen durchlaufen werden.
