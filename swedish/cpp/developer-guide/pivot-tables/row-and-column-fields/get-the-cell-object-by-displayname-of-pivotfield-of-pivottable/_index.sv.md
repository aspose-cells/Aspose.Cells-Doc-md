---
title: Hämta cellobjektet genom visningsnamn för PivotField i PivotTable med C++
linktitle: Hämta cellobjektet genom visningsnamn för PivotField i PivotTable
type: docs
weight: 70
url: /sv/cpp/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: Lär dig hur du hämtar cellobjektet via visningsnamnet för ett pivotelement och tillämpar formatering med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller metoden [**PivotTable::GetCellByDisplayName()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getcellbydisplayname/), vilken du kan använda för att komma åt cellobjektet via visningsnamnet för ett pivotelement. Denna metod är användbar när du vill markera eller formatera din pivothuvud. Denna artikel förklarar hur man hämtar cellobjektet via visningsnamnet för ett datafält och sedan tillämpar formatering på det.

{{% /alert %}}

## **Hämta cellobjektet genom visningsnamn för PivotField i PivotTable**

Följande kod får den första pivot-tabellen i kalkbladet och hämtar sedan cellen genom visningsnamnet för det andra datafältets pivot-tabell. Den ändrar sedan fyllnadsfärgen och teckensnittsfärgen till ljusblå respektive svart. Nedan visas skärmbilder på hur pivot-tabellen ser ut före och efter kodens körning.

|**Pivot-tabel - Före**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"source.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    Cell cell = pivotTable.GetCellByDisplayName(pivotTable.GetDataFields().Get(0).GetDisplayName());

    Style style = cell.GetStyle();
    style.SetForegroundColor(Color::LightBlue());
    style.GetFont().SetColor(Color::Black());

    pivotTable.Format(cell.GetRow(), cell.GetColumn(), style);
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Pivot table formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

|**Pivot-tabel - Efter**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
{{< app/cells/assistant language="cpp" >}}
