---
title: Lavorare con i formati di visualizzazione dei dati di DataField nella Pivot Table con C++
linktitle: Lavorare con i formati di visualizzazione dei dati di DataField nella Pivot Table
type: docs
weight: 140
url: /it/cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
description: Impara come lavorare con i formati di visualizzazione dei dati di DataField nella Pivot Table usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells supporta tutti i formati di visualizzazione dei dati del DataField.

{{% /alert %}}

## **Opzione di visualizzazione "Classifica dal più piccolo al più grande" e "Classifica dal più grande al più piccolo"**

Aspose.Cells consente di impostare l'opzione di formato di visualizzazione per i campi pivot. Per questo, l'API fornisce la proprietà [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotshowvaluessetting/getcalculationtype/). Per ordinare dal più grande al più piccolo, puoi impostare la proprietà [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotshowvaluessetting/getcalculationtype/) su [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfielddatadisplayformat/). Il seguente frammento di codice mostra come impostare le opzioni di formato di visualizzazione.

Il file di origine e i file di output di esempio possono essere scaricati da qui per testare il codice di esempio.

[File Excel di origine](101089332.xlsx)

[File Excel di output](101089333.xlsx)

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
