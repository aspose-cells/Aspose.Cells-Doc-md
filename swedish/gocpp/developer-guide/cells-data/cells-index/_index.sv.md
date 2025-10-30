---
title: Hämta cellindex med Golang via C++
linktitle: Få cellerindex
type: docs
weight: 600
url: /sv/go-cpp/get-cells-index/
description: Lär dig hur du hämtar rad eller kolumnindex efter namnet på rad, kolumn eller celler. Konvertera cellens namn till rad och kolumnindex (0 baserat) med Aspose.Cells med Golang via C++.
keywords: Få radindex och kolumnindex efter namnet på cellen, Få kolumnindex efter namnet på kolumnen, Få radindex efter namnet på raden, Få index efter namnet på cellen.
---

{{% alert color="primary" %}}
Standardvyn i Excel är A1-stilreferens, där varje kolumn definieras som A, B, C.... och cellerna heter A1, B2, C3... och så vidare.
 Du kanske vill veta vilken rad och kolumn denna cell befinner sig i.

{{% /alert %}}

## **Möjliga användningsscenario**

 När du bara behöver manipulera specifika data på arket efter rad- och kolumnindex, behöver du känna till rad- och kolumnindex för den specifika cellen.
Aspose.Cells erbjuder denna funktion för att få rad- och kolumnindex efter namnet på raden, kolumnen och cellen.
Aspose.Cells tillhandahåller följande egenskaper och metoder för att hjälpa dig att uppnå dina mål:

- [**CellsHelper::CellNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/cellnametoindex/)
- [**CellsHelper::ColumnIndexToName**](https://reference.aspose.com/cells/go-cpp/cellshelper/columnindextoname/)
- [**CellsHelper::ColumnNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/columnnametoindex/)
- [**CellsHelper::RowIndexToName**](https://reference.aspose.com/cells/go-cpp/cellshelper/rowindextoname/)
- [**CellsHelper::RowNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/rownametoindex/)

Observera: Indexeringen är nollbaserad i Aspose.Cells for C++, men Row-ID är 1-baskat i MS Excel.

## **Få cellers index med hjälp av Aspose.Cells**

Detta exempel visar hur man:

1. Skapa en arbetsbok och lägg till lite data.
1. Hitta den specifika cellen i det första arbetsbladet.
1. Få radindex och kolumnindex efter namnet på cellen.
1. Få kolumnindex efter namnet på kolumnen.
1. Få radindex efter namnet på raden.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CellsIndex.go" >}}
