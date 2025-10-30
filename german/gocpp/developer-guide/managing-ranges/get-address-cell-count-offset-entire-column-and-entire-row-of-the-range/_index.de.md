---
title: Adresse, Zellanzahl, Offset, gesamte Spalte und gesamte Zeile des Bereichs mit Golang via C++ abrufen
linktitle: Erhalten Sie Adresse, Zellanzahl, Offset, gesamte Spalte und gesamte Zeile des Bereichs
type: docs
weight: 330
url: /de/go-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
description: Erfahren Sie, wie Sie Adresse, Zellanzahl, Offset, gesamte Spalte und gesamte Zeile eines Bereichs mit Aspose.Cells for C++ ermitteln.
---

## **Mögliche Verwendungsszenarien**
Aspose.Cells stellt das `Range`-Objekt bereit, das verschiedene Hilfsmethoden bietet, die die Arbeit mit Excel-Bereichen erleichtern. Dieser Artikel zeigt die Nutzung der folgenden Methoden oder Eigenschaften des `Range`-Objekts:

- **Adresse**

  Ermittelt die Adresse des Bereichs.

- **Zellanzahl**

  Ermittelt die Gesamtzahl der Zellen im Bereich.

- **Versatz**

  Ermittelt einen Bereich anhand des Offsets.

- **Gesamte Spalte**

  Erzeugt ein `Range`-Objekt, das die gesamte Spalte (oder Spalten) repräsentiert, die den angegebenen Bereich enthält.

- **Gesamte Zeile**

  Erzeugt ein `Range`-Objekt, das die gesamte Zeile (oder Zeilen) repräsentiert, die den angegebenen Bereich enthält.

## **Adresse, Zellanzahl, Offset, gesamte Spalte und gesamte Zeile des Bereichs abrufen**
Der folgende Beispielcode erklärt die Verwendung der oben diskutierten Methoden und Eigenschaften. Bitte beachten Sie die Konsolenausgabe des unten angegebenen Codes zu Referenz.

## **Beispielcode**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetAddressCellCountOffsetEntireColumnAndEntireRowOfTheRange.go" >}}
## **Konsolenausgabe**
{{< highlight java >}}

Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
