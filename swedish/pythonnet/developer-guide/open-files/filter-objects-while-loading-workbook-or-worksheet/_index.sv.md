---
title: Filtrera objekt när du laddar arbetsbok eller kalkylblad
type: docs
weight: 330
url: /sv/python-net/filter-objects-while-loading-workbook-or-worksheet/
---

## **Möjliga användningsscenario**
Använd egenskapen [LoadOptions.load_filter](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter) för att filtrera data från arbetsboken. Men om du vill filtrera data från enskilda arbetsblad måste du överrida metoden [LoadFilter.start_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter/start_sheet). Ange ett lämpligt värde från [LoadDataFilterOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions) när du skapar eller arbetar med [LoadFilter](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter).

Enumerationen [LoadDataFilterOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions) har följande möjliga värden.

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilteringObjectsAtLoadTime-FilteringObjects.py" >}}

