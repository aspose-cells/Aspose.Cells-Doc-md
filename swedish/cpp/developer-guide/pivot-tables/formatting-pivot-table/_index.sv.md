---
title: Formatera PivotTabell med C++
linktitle: Formatera Pivot tabell
type: docs
weight: 10
url: /sv/cpp/formatting-pivot-table/
description: Lär dig hur man anpassar utseendet på pivot tabeller med Aspose.Cells for C++.
---

## **Pivottabellens utseende**

Hur man skapar en pivottabell förklarar hur man skapar en enkel pivottabell. Den här artikeln beskriver hur man anpassar en pivottabells utseende genom att ställa in olika egenskaper:

- Pivottabellformatalternativ
- Alternativ för pivottabellfältformat
- Alternativ för datafältformat

### **Inställning av pivottabellformatalternativ**

Klassen [**PivotTable**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/) kontrollerar den övergripande pivottabellen och kan formateras på olika sätt.

#### **Inställning av autoformat typ**

Microsoft Excel erbjuder ett antal förinställda rapportformat. Aspose.Cells stöder också dessa formateringsalternativ. För att komma åt dem:

1. Ställ in [**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/isautoformat/) till **true**.
1. Tilldela ett formateringsalternativ från uppräkningen [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottableautoformattype/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Load a template file
    Workbook workbook(inputFilePath);

    int pivotindex = 0;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotindex);

    // Setting the PivotTable report is automatically formatted
    pivotTable.SetIsAutoFormat(true);

    // Setting the PivotTable autoformat type
    pivotTable.SetAutoFormatType(PivotTableAutoFormatType::Report5);

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "PivotTable formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Inställning av formatalternativ**

Följande kodexempel visar hur man formaterar pivot-tabellen för att visa grand totals för rader och kolumner, och hur man ställer in rapportens fältordning. Det visar också hur man ställer in en anpassad sträng för null-värden.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Load a template file
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    int pivotindex = 0;

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotindex);

    // Setting the PivotTable report shows grand totals for rows.
    pivotTable.SetShowRowGrandTotals(true);

    // Setting the PivotTable report shows grand totals for columns.
    pivotTable.SetShowColumnGrandTotals(true);

    // Setting the PivotTable report displays a custom string in cells that contain null values.
    pivotTable.SetDisplayNullString(true);
    pivotTable.SetNullString(u"null");

    // Setting the PivotTable report's layout
    pivotTable.SetPageFieldOrder(PrintOrderType::DownThenOver);

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "PivotTable settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Manuell formatering av utseende**

För att formatera hur pivot-tabellrapporten ser ut manuellt, istället för att använda förinställda rapportformat, använd [**PivotTable.Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/)-och [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/)-metoderna. Skapa ett stildokument för önskad formatering, till exempel:

```cpp
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
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Load a template file
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    auto pivot = worksheet.GetPivotTables().Get(0);

    // Set pivot table style
    pivot.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleDark1);

    // Create a new style
    Style style = workbook.CreateStyle();
    style.GetFont().SetName(u"Arial Black");
    style.SetForegroundColor(Color::Yellow());
    style.SetPattern(BackgroundType::Solid);

    // Apply style to pivot table
    pivot.FormatAll(style);

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Pivot table style applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Inställning av pivottabellfältformatalternativ**

Klassen [**PivotField**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/) representerar ett fält i en pivottabell och kan formateras på olika sätt. Kodprovet nedan visar hur man:

- Tillgång till radfält.
- Inställning av delsummer.
- Inställning av autosortering.
- Inställning av autoshow.

#### **Inställning av format för rad/kolumn/sidofältsformat**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load a template file
    Workbook workbook(srcDir + u"Book1.xls");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    int pivotindex = 0;

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotindex);

    // Setting the PivotTable report shows grand totals for rows.
    pivotTable.SetShowRowGrandTotals(true);

    // Accessing the row fields.
    PivotFieldCollection pivotFields = pivotTable.GetRowFields();

    // Accessing the first row field in the row fields.
    PivotField pivotField = pivotFields.Get(0);

    // Setting Subtotals.
    pivotField.SetSubtotals(PivotFieldSubtotalType::Sum, true);
    pivotField.SetSubtotals(PivotFieldSubtotalType::Count, true);

    // Setting autosort options.
    // Setting the field auto sort.
    pivotField.SetIsAutoSort(true);

    // Setting the field auto sort ascend.
    pivotField.SetIsAscendSort(true);

    // Setting the field auto sort using the field itself.
    pivotField.SetAutoSortField(-5);

    // Setting autoShow options.
    // Setting the field auto show.
    pivotField.SetIsAutoShow(true);

    // Setting the field auto show ascend.
    pivotField.SetIsAscendShow(false);

    // Setting the auto show using field(data field).
    pivotField.SetAutoShowField(0);

    // Saving the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "PivotTable settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Anger format för datafält**

Kodprovet nedan visar hur man ställer in visningsformat och nummerformat för datafält.

```cpp
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

    // Load a template file
    U16String inputFilePath = srcDir + u"Book1.xls";
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    int pivotindex = 0;

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotindex);

    // Accessing the data fields
    PivotFieldCollection pivotFields = pivotTable.GetDataFields();

    // Accessing the first data field in the data fields
    PivotField pivotField = pivotFields.Get(0);

    // Setting data display format
    pivotField.GetShowValuesSetting().SetCalculationType(PivotFieldDataDisplayFormat::PercentageOf);

    // Setting the base field
    pivotField.GetShowValuesSetting().SetBaseFieldIndex(1);

    // Setting the base item
    pivotField.GetShowValuesSetting().SetBaseItemPositionType(PivotItemPositionType::Next);

    // Setting number format
    pivotField.SetNumber(10);

    // Saving the Excel file
    U16String outputFilePath = outDir + u"output.xls";
    workbook.Save(outputFilePath);

    std::cout << "Pivot table settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Rensa pivottabellsfält**

Klassen [**PivotFieldCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfieldcollection/) har en metod som heter [**Clear()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfieldcollection/clear/) som låter dig rensa pivottabellsfält. Använd den när du vill rensa alla pivottabellfält i områdena, till exempel sida, kolumn, rad eller data.
Kodprovet nedan visar hur man rensar alla pivottabellfält i ett dataområde.

```cpp
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
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Load a template file
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the pivot tables in the sheet
    PivotTableCollection pivotTables = sheet.GetPivotTables();

    // Get the first PivotTable
    PivotTable pivotTable = pivotTables.Get(0);

    // Clear all the data fields
    pivotTable.GetDataFields().Clear();

    // Add new data field
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Betrag Netto FW");

    // Set the refresh data flag off
    pivotTable.SetRefreshDataFlag(false);

    // Refresh and calculate the pivot table data
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Pivot table updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
