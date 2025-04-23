---
title: Använd Microsoft Excels avancerade filter för att visa poster som uppfyller komplexa kriterier med C++
linktitle: Tillämpa avancerad filter av Microsoft Excel för att visa poster som uppfyller komplexa kriterier
type: docs
weight: 280
url: /sv/cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Lär dig hur man tillämpar avancerat filter i Microsoft Excel för att visa poster som uppfyller komplexa kriterier genom att använda API et Aspose.Cells for C++.
keywords: Tillämpa avancerat filter, Inställa avancerat filter, Lägg till avancerat filter, Skapa avancerat filter, Hur man lägger till avancerat filter till en serie
---

## **Möjliga användningsscenario**

Microsoft Excel tillåter att du tillämpar *Advanced Filter* på arbetsbladets data för att visa poster som möter komplexa kriterier. Du kan tillämpa avancerad filter med Microsoft Excel via dess *Data > Advanced* kommando som visas i denna skärmskärm.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells tillåter också att du använder det avancerade filtret med hjälp av [**GetAdvancedFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getadvancedfilter/)-metoden. Precis som i Microsoft Excel accepterar den följande parametrar.

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

Följande kodexempel använder det avancerade filtret på [Exempelfilen Excel](48496692.xlsx) och genererar [Utdata Excel-fil](48496691.xlsx). Skärmbilden visar båda filerna för jämförelse. Som du kan se i skärmbilden, har data filtrerats i utdata Excel-filen enligt komplexa kriterier.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **Exempelkod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Load your source workbook
    Workbook workbook(sourceDir + u"sampleAdvancedFilter.xlsx");

    // Access first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Apply advanced filter on range A5:D19 and criteria range is A1:D2
    // Besides, we want to filter in place
    // And, we want all filtered records not just unique records
    ws.Advanced_Filter(true, u"A5:D19", u"A1:D2", u"", false);

    // Save the workbook in xlsx format
    workbook.Save(outputDir + u"outputAdvancedFilter.xlsx", SaveFormat::Xlsx);

    std::cout << "Advanced filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
