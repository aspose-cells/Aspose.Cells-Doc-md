---
title: Arbeta med datavisningsformat för DataField i pivottabell med C++
linktitle: Arbeta med datavisningsformat för DataField i pivottabell
type: docs
weight: 140
url: /sv/cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
description: Lär dig hur du arbetar med datavisningsformat för DataField i pivottabell med hjälp av Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells stöder alla dataradens dataformat.

{{% /alert %}}

## **"Rank Smallest to Largest" och "Rank Largest to Smallest" displayformatalternativ**

Aspose.Cells ger möjlighet att ställa in displayformatalternativ för pivottfälten. För detta tillhandahåller API:n egenskapen [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotshowvaluessetting/getcalculationtype/). För att ranka störst till minst kan du ställa in egenskapen [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotshowvaluessetting/getcalculationtype/) till [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfielddatadisplayformat/). Följande kodavsnitt visar hur du ställer in displayformatalternativen.

Provfil och utdatafiler kan laddas ner här för att testa provkoden:

[Käll-Excel-fil](101089332.xlsx)

[Utdata Excel-fil](101089333.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load a template file
    Workbook workbook(srcDir + u"PivotTableSample.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    int pivotIndex = 0;

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // Accessing the data fields
    PivotFieldCollection pivotFields = pivotTable.GetDataFields();

    // Accessing the first data field in the data fields
    PivotField pivotField = pivotFields.Get(0);

    // Setting data display format
    pivotField.GetShowValuesSetting().SetCalculationType(PivotFieldDataDisplayFormat::RankLargestToSmallest);

    // Calculate data
    pivotTable.CalculateData();

    // Saving the Excel file
    workbook.Save(outDir + u"PivotTableDataDisplayFormatRanking_out.xlsx");

    std::cout << "PivotTable data display format ranking applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
