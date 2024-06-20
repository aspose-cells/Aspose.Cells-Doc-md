---
title: Tillämpa avancerad filter av Microsoft Excel för att visa poster som uppfyller komplexa kriterier
type: docs
weight: 280
url: /sv/python-net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Lär dig hur du tillämpar avancerad filter av Microsoft Excel för att visa poster som uppfyller komplexa kriterier med hjälp av Aspose.Cells för Python via .NET API.
keywords: Python Excel bibliotek, Python Tillämpa avancerat filter, Python Ställa in avancerat filter, Python Lägga till avancerat filter, Python Skapa avancerat filter, Hur man lägger till avancerat filter till ett intervall med hjälp av Python.
---

## **Möjliga användningsscenario**

Microsoft Excel tillåter dig att tillämpa *Avancerat filter* på kalkylbladsdata för att visa poster som uppfyller komplexa kriterier. Du kan tillämpa Avancerat filter i Microsoft Excel via dess *Data > Avancerat* kommando som visas i denna skärmbild.

![todo:image_alt_text](1.png)

Aspose.Cells för Python via .NET tillåter dig också att tillämpa det avancerade filtret med metoden [**Worksheet.advancedFilter()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/advanced_filter/#bool-str-str-str-bool). Precis som Microsoft Excel accepterar det följande parametrar.

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

![todo:image_alt_text](2.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ApplyAdvancedFilterOfMicrosoftExcel.py" >}}
