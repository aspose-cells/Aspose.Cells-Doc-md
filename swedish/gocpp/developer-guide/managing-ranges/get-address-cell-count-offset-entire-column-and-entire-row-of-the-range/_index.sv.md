---
title: Hämta adress, cellantal, offset, hela kolumnen och hela raden för området med Golang via C++
linktitle: Hämta adress, cellantal, offset, hela kolumnen och hela raden i intervallet
type: docs
weight: 330
url: /sv/go-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
description: Lär dig hur man får adress, cellantal, offset, hela kolumnen och hela raden för ett intervall med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**
Aspose.Cells tillhandahåller `Range`-objektet, som har olika hjälpfunktioner som underlättar arbetet med Excel-intervall. Denna artikel illustrerar användningen av följande metoder eller egenskaper för `Range`-objektet:

- **Adress**

  Hämtar intervalladressen.

- **Cellräkning**

  Hämtar det totala cellantalet i intervallet.

- **Offset**

  Hämtar ett intervall med offset.

- **Hela kolumnen**

  Hämtar ett `Range`-objekt som representerar hela kolumnen (eller kolumnerna) som innehåller det angivna intervallet.

- **Hela raden**

  Hämtar ett `Range`-objekt som representerar hela raden (eller rader) som innehåller det angivna intervallet.

## **Hämta adress, cellantal, offset, hela kolumnen och hela raden i intervallet**
Följande exempel kod förklarar användningen av de ovan nämnda metoderna och egenskaperna. Vänligen se konsolutmatningen av koden nedan som referens.

## **Exempelkod**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetAddressCellCountOffsetEntireColumnAndEntireRowOfTheRange.go" >}}
## **Konsoloutput**
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
