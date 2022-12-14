---
title: Använd avancerat filter i Microsoft Excel för att visa poster som uppfyller komplexa kriterier
type: docs
weight: 190
url: /sv/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
---
## **Möjliga användningsscenarier**
 Microsoft Excel låter dig ansöka*Avancerat filter* på kalkylbladsdata för att visa poster som uppfyller komplexa kriterier. Du kan använda Advanced Filter med Microsoft Excel via dess*Data > Avancerat*kommandot som visas i den här skärmdumpen.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells låter dig också tillämpa det avancerade filtret med hjälp av[Worksheet.advancedFilter()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#advancedFilter\(boolean,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20boolean\)metod. Precis som Microsoft Excel accepterar den följande parametrar.

**isFilter**

Anger om filtrering av listan på plats.

**listRange**

Listomfånget.

**kriterierOmfång**

Kriterierna varierar.

**kopia till**

Området dit kopiering av data till.

**Endast unikaRecord**

Visar eller kopierar endast unika rader.
## **Använd avancerat filter i Microsoft Excel för att visa poster som uppfyller komplexa kriterier**
Följande exempelkod tillämpar det avancerade filtret på[Exempel på Excel-fil](48496702.xlsx) och genererar[Utdata Excel-fil](48496705.xlsx). Skärmdumpen visar båda filerna för jämförelse. Som du kan se inuti skärmdumpen har data filtrerats in i Excel-utdatafilen enligt komplexa kriterier.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ApplyAdvancedFilterOfMicrosoftExcel.java" >}}
