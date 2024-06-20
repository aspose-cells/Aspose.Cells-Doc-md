---
title: Tillämpa avancerad filter av Microsoft Excel för att visa poster som uppfyller komplexa kriterier
type: docs
weight: 280
url: /sv/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Lär dig hur man tillämpar avancerat filter för Microsoft Excel för att visa poster som uppfyller komplexa kriterier med hjälp av API et Aspose.Cells for .NET.
keywords: Tillämpa avancerat filter, Inställa avancerat filter, Lägg till avancerat filter, Skapa avancerat filter, Hur man lägger till avancerat filter till en serie 
---

## **Möjliga användningsscenario**

Microsoft Excel tillåter dig att tillämpa *Avancerat filter* på kalkylbladsdata för att visa poster som uppfyller komplexa kriterier. Du kan tillämpa Avancerat filter i Microsoft Excel via dess *Data > Avancerat* kommando som visas i denna skärmbild.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells tillåter också att tillämpa avancerat filter med hjälp av [**Worksheet.AdvancedFilter()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/advancedfilter) metoden. Precis som Microsoft Excel godtar den följande parametrar.

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

Följande exempelkod tillämpar den avancerade filtreringen på [Sample Excel File](48496692.xlsx) och genererar [Output Excel File](48496691.xlsx). Skärmbilden visar båda filerna för jämförelse. Som du kan se på skärmbilden har data filtrerats i utdata-Excel-filen enligt komplexa kriterier.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-ApplyAdvancedFilterOfMicrosoftExcel.cs" >}}
