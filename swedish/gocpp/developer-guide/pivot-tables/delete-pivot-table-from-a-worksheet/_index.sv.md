---
title: Ta bort pivottabellen från ett arbetsblad med Golang via C++
linktitle: Ta bort PivotTabell
type: docs
weight: 60
url: /sv/go-cpp/delete-pivot-table-from-a-worksheet/
description: C++ kod för att ta bort PivotTabell för Excel Ark
keywords: c++ ta bort pivot tabell från kalkylblad, c++ ta bort pivot tabell från excel, hur man raderar pivot tabell med c++, ta bort pivot tabell med c++, ta bort pivot tabell från excel med c++, c++ radera pivot tabell, c++ ta bort pivot tabell, ta bort pivot tabell, radera pivot tabell, hur man tar bort pivot tabell
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller en funktion för att radera eller ta bort pivottabell från ett arbetsblad. Du kan ta bort pivottabellen med hjälp av pivottabellobjektet eller pivottabellens position. Använd [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/go-cpp/pivottablecollection/remove_pivottable/) -metoden för att ta bort pivottabellen med hjälp av pivottabellobjektet och [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/) metoden för att ta bort pivottabellen med hjälp av dess position i pivottabellssamlingen.

{{% /alert %}}

Följande kod tar bort två pivot-tabeller från kalkylbladet. Först tas pivot-tabellen bort med [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/go-cpp/pivottablecollection/remove_pivottable/)-metoden och sedan tas en till bort med [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/)-metoden.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeletePivotTableFromAWorksheet.go" >}}
