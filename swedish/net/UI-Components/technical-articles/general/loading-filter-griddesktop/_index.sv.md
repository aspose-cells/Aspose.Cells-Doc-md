---
title: Filtrera objekt under inläsning av arbetsbok i GridDesktop
type: docs
weight: 1060
url: /sv/net/aspose-cells-griddesktop/loading-filter
description: Den här artikeln beskriver hur man använder laddningsfilter i GridDesktop.
keywords: GridDesktop,loading,loading filter,filter
---

## **Möjliga användningsscenario**
Använd [GridDesktop.LoadDataFilter](https://reference.aspose.com/cells/net/aspose.cells.griddesktop/griddesktop/properties/loaddatafilter)-egenskapen när du filtrerar data från arbetsboken.

Uppräkningen [GridLoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells.griddesktop.data/gridloaddatafilteroptions) har följande värden.
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
## **Filtrera data medan du laddar arbetsboken**
Följande exempelkodillustrerar hur man filtrerar ritningar från arbetsboken. Kolla på [exempelkalkylarket](5472489.xlsx). Som du kan se har alla diagram/former/bilder filtrerats bort från arbetsboken.
![arbetsbok utan bild](nodrawing.png)
### **Exempelkod**
{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "LoadingFilter.cs" >}}

