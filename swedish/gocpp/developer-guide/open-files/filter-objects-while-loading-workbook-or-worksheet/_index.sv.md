---
title: Filtrera objekt vid inläsning av arbetsbok eller kalkylblad med Golang via C++
linktitle: Filtrera objekt när du laddar arbetsbok eller kalkylblad
type: docs
weight: 330
url: /sv/go-cpp/filter-objects-while-loading-workbook-or-worksheet/
description: Lär dig hur du filtrerar objekt som diagram, former och villkorlig formatering medan du laddar arbetsboken eller kalkylblad med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**
Använd gärna [LoadOptions.GetLoadFilter()](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/) egenskapen vid filtrering av data från arbetsboken. Men om du vill filtrera data från enskilda kalkylblad måste du överskrida metoden [LoadFilter.StartSheet](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/startsheet/). Ange ett lämpligt värde från [LoadDataFilterOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) -upptäckten när du skapar eller arbetar med [LoadFilter](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/).

[LoadDataFilterOptions](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/) -upptäckten har följande möjliga värden.

- Alla
- Bokinställningar
- CellTom
- CellBool
- CellData
- CellFel
- CellNumeriskt
- CellSträng
- CellVärde
- Chart
- VillkorligFormatering
- DataValidering
- DefinieradeNamn
- Dokumentegenskaper
- Formel
- Hyperlänkar
- SammanslagnaOmråde
- PivotTabell
- Inställningar
- Form
- ArkData
- Arkinställningar
- Struktur
- Stil
- Tabell
- VBA
- XmlKarta

## **Filtrera objekt när du laddar arbetsbok**
Följande exempelkod illustrerar hur du filtrerar diagram från arbetsboken. Kontrollera den [exempel-Excel-filen](5115258.xlsx) som används i denna kod och den [utdata PDF](5115257.pdf) som genererats av den. Som du kan se i utdata PDF:en har alla diagram filtrerats bort från arbetsboken.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet.go" >}}
## **Filtrera objekt när du laddar kalkylblad**
Följande exempelkod laddar den [ursprungliga excel-filen](5115255.xlsx) och filtrerar följande data från dess kalkylblad med en anpassad filter.

- Det filtrerar diagram från kalkylbladet som heter NoCharts.
- Det filtrerar former från kalkylbladet som heter NoShapes.
- Det filtrerar villkorlig formatering från kalkylbladet som heter NoConditionalFormatting.

När den laddar [ursprungliga excel-filen](5115255.xlsx) med en anpassad filter tar den bilderna av alla kalkylblad en efter en. Här är utdata bilderna för din referens. Som du kan se har den första bilden inga diagram, den andra bilden har inga former och den tredje bilden har ingen villkorlig formatering.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet-1.go" >}}
Så här använder du klassen CustomLoadFilter enligt kalkylbladsnamn.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet-2.go" >}}
