---
title: Tillämpa avancerad filter av Microsoft Excel för att visa poster som uppfyller komplexa kriterier
type: docs
weight: 190
url: /sv/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
---

## **Möjliga användningsscenario**
Microsoft Excel tillåter dig att tillämpa *Avancerat filter* på kalkylbladsdata för att visa poster som uppfyller komplexa kriterier. Du kan tillämpa Avancerat filter i Microsoft Excel via dess *Data > Avancerat* kommando som visas i denna skärmbild.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells tillåter också att du använder det avancerade filtret med hjälp av [Worksheet.advancedFilter()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#advancedFilter\(boolean,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20boolean\)) metoden. Precis som Microsoft Excel, godkänner den följande parametrar.

**isFilter**

Anger om filtreringen av listan på plats.

**listRange**

Listan intervall.

**criteriaRange**

Kriterieintervallet.

**copyTo**

Intervallet där data kopieras till.

**uniqueRecordOnly**

Endast visa eller kopiera unika rader.
## **Tillämpa Avancerat Filter i Microsoft Excel för att Visa Poster som Uppfyller Komplexa Kriterier**
Följande provkod tillämpar det avancerade filtret på [Prov Excel-fil](48496702.xlsx) och genererar [Utdata Excel-fil](48496705.xlsx). Skärmbilden visar båda filerna för jämförelse. Som du kan se inne i skärmdumpen har data filtrerats i utdata Excel-filen enligt komplexa kriterier.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ApplyAdvancedFilterOfMicrosoftExcel.java" >}}
