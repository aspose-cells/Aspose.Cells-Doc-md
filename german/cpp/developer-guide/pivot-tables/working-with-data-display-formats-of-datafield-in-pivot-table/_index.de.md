---
title: Arbeiten mit Datenanzeigeformaten des DataField in Pivot Tabellen mit C++
linktitle: Arbeiten mit Datenanzeigeformaten des DataField in Pivot Tabellen
type: docs
weight: 140
url: /de/cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
description: Erfahren Sie, wie Sie mit Aspose.Cells for C++ Datenanzeigeformate des DataField in Pivot Tabellen bearbeiten.
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt alle Datenanzeigeformate von DataField.

{{% /alert %}}

## **"Rank Kleinste bis Größte" und "Rank Größte bis Kleinste" Anzeigeformatoption**

Aspose.Cells bietet die Möglichkeit, das Anzeigeformat für Pivot-Felder festzulegen. Hierfür stellt die API die [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotshowvaluessetting/getcalculationtype/)-Eigenschaft bereit. Um nach Größe zu ranken, können Sie die [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotshowvaluessetting/getcalculationtype/)-Eigenschaft auf [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfielddatadisplayformat/) setzen. Das folgende Code-Beispiel zeigt, wie die Anzeigeformatoptionen eingestellt werden.

Die Beispielsquell- und Ausgabedateien können hier für das Testen des Beispielcodes heruntergeladen werden:

[Quell-Excel-Datei](101089332.xlsx)

[Ausgabe-Excel-Datei](101089333.xlsx)

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
