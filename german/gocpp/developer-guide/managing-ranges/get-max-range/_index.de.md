---
title: Maximalbereich in einem Arbeitsblatt mit Golang via C++ ermitteln
linktitle: Holen Sie den maximalen Bereich in einem Arbeitsblatt ab
type: docs
weight: 360
url: /de/go-cpp/get-max-range-in-a-worksheet/
description: Dieser Artikel beschreibt, wie man den Maximalbereich, den Maximal Datenbereich und den Maximal Anzeige Bereich von Excel Dateien mit der Aspose.Cells for C++ Bibliothek ermittelt.
---

{{% alert color="primary" %}} 

Beim Lesen von Daten aus dem Arbeitsblatt müssen wir den maximalen Bereich kennen.

Beim Kopieren aller Daten aus einem Arbeitsblatt müssen wir den maximalen Bereich kennen.

Beim Exportieren eines bestimmten Bereichs nach HTML und PDF müssen wir den maximalen Bereich kennen.

Aspose.Cells for C++ bietet verschiedene Möglichkeiten, den Maximalbereich in einem Arbeitsblatt zu ermitteln. 

{{% /alert %}} 

## **Den Maximalbereich abrufen**
In Aspose.Cells werden, wenn die Objekte [**Row**](https://reference.aspose.com/cells/go-cpp/row/) und [**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/) initialisiert sind, diese Zeilen und Spalten zum maximalen Bereich gezählt, selbst wenn in leeren Zeilen oder Spalten keine Daten vorhanden sind.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetMaxRange.go" >}}
## **Maximalen Datenbereich abrufen**
In den meisten Fällen müssen wir nur alle Bereiche erhalten, die alle Daten enthalten, auch wenn die leeren Zellen außerhalb des Bereichs formatiert sind.
Und die Einstellungen zu Formen, Tabellen und Pivot-Tabellen werden ignoriert.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetMaxRange-1.go" >}}
## **Maximale Anzeigebereich erhalten**
Wenn wir alle Daten aus dem Arbeitsblatt in HTML, PDF oder Bildern exportieren, müssen wir einen Bereich erhalten, der alle sichtbaren Objekte enthält, einschließlich Daten, Styles, Grafiken, Tabellen und Pivot-Tabellen.
Die folgenden Codes zeigen, wie der maximale Anzeigebereich in HTML gerendert wird:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetMaxRange-2.go" >}}
Hier ist die [Quelldatei Excel](Book1.xlsx).
