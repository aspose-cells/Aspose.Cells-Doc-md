---
title: Använd avancerat filter av Microsoft Excel för att visa poster som uppfyller komplexa kriterier
type: docs
weight: 280
url: /sv/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
---
## **Möjliga användningsscenarier**

 Microsoft Excel låter dig ansöka*Avancerat filter* på kalkylbladsdata för att visa poster som uppfyller komplexa kriterier. Du kan använda Advanced Filter med Microsoft Excel via dess*Data > Avancerat*kommandot som visas i den här skärmdumpen.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells låter dig också tillämpa det avancerade filtret med hjälp av[**Worksheet.AdvancedFilter()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/advancedfilter)metod. Precis som Microsoft Excel accepterar den följande parametrar.

**isFilter**

Anger om filtrering av listan på plats.

**listRange**

Listomfånget.

**kriterierOmfång**

Kriterierna varierar.

**kopiera till**

Området dit kopiering av data till.

**Endast unikaRecord**

Visar eller kopierar endast unika rader.

## **Använd avancerat filter av Microsoft Excel för att visa poster som uppfyller komplexa kriterier**

Följande exempelkod tillämpar det avancerade filtret på[Exempel på Excel-fil](48496692.xlsx) och genererar[Utdata Excel-fil](48496691.xlsx). Skärmdumpen visar båda filerna för jämförelse. Som du kan se inuti skärmdumpen har data filtrerats in i Excel-utdatafilen enligt komplexa kriterier.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-ApplyAdvancedFilterOfMicrosoftExcel.cs" >}}
