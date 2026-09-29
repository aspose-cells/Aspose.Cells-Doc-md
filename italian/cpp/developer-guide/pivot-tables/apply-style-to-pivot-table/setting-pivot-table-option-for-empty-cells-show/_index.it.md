---
title: Impostare opzione tabella pivot  Per mostrare nelle celle vuote con C++
linktitle: Impostazione dell opzione tabella pivot  Per le celle vuote mostra
type: docs
weight: 40
url: /it/cpp/setting-pivot-table-option-for-empty-cells-show/
description: Impara come impostare l opzione "Per mostrare nelle celle vuote" nelle tabelle pivot usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

È possibile impostare diverse opzioni per le tabelle pivot utilizzando Aspose.Cells. Una di queste opzioni è "Mostra per celle vuote". Impostando questa opzione, tutte le celle vuote in una tabella pivot vengono visualizzate come una stringa specificata.

{{% /alert %}}

## **Impostazione dell'opzione della tabella pivot in Microsoft Excel**

Per trovare e impostare questa opzione in Microsoft Excel:

1. Seleziona una tabella pivot e fai clic con il pulsante destro del mouse.
1. Seleziona **Opzioni tabella pivot**.
1. Seleziona la scheda **Layout e Formato**.
1. Seleziona l'opzione **Per le celle vuote mostra** e specifica una stringa.

## **Impostare l'opzione della tabella pivot utilizzando Aspose.Cells**

Aspose.Cells fornisce le proprietà [**PivotTable.GetDisplayNullString()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getdisplaynullstring/) e [**PivotTable.GetNullString()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getnullstring/) per impostare l'opzione della tabella pivot "Per le celle vuote mostrare".

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"input.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Get the first worksheet
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Get the first pivot table
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    PivotTable pt = pivotTables.Get(0);

    // Indicating if or not display the empty cell value
    pt.SetDisplayNullString(true);

    // Indicating the null string
    pt.SetNullString(u"null");

    // Calculate pivot table data
    pt.CalculateData();

    // Set refresh data on opening file to false
    pt.SetRefreshDataOnOpeningFile(false);

    // Save the workbook
    wb.Save(outputFilePath);

    std::cout << "Pivot table settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Articoli correlati

- [Formattazione tabella pivot](/cells/it/cpp/formatting-pivot-table/)
{{< app/cells/assistant language="cpp" >}}
