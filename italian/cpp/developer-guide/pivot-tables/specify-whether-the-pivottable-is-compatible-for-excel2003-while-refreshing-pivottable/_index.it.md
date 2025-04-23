---
title: Specificare se la PivotTable è compatibile con Excel2003 durante l aggiornamento della PivotTable con C++
linktitle: Specificare la compatibilità con Excel2003 nella PivotTable
type: docs
weight: 80
url: /it/cpp/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: Impara come specificare la compatibilità della PivotTable con Excel2003 usando Aspose.Cells for C++ durante l aggiornamento della PivotTable.
---

{{% alert color="primary" %}}

Aspose.Cells fornisce la proprietà [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/isexcel2003compatible/) che puoi utilizzare per specificare se la tabella pivot è compatibile per Excel 2003 durante l'aggiornamento della tabella pivot. Se è vero, una stringa deve essere inferiore o uguale a 255 caratteri, quindi se la stringa è maggiore di 255 caratteri, verrà troncata. Se è falso, una stringa non avrà la restrizione menzionata. Il valore predefinito è vero.

{{% /alert %}}

## **Specificare se la tabella pivot è compatibile per Excel2003 durante l'aggiornamento della tabella pivot**

Il codice di esempio seguente spiega l'uso della proprietà [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/isexcel2003compatible/). La stringa originale è lunga 383 caratteri. Ma quando la proprietà [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/isexcel2003compatible/) è impostata su **true** e la tabella pivot viene aggiornata, i dati della cella B5 della tabella pivot vengono troncati e diventano lunghi 255 caratteri. Tuttavia, quando la proprietà [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/isexcel2003compatible/) è impostata su **false** e la tabella pivot viene di nuovo aggiornata, i dati della cella B5 della tabella pivot non vengono troncati e rimangono lunghi 383 caratteri. Si prega di leggere i commenti all'interno del codice per una migliore comprensione di questa proprietà.

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

    // Load source excel file containing sample pivot table
    Workbook wb(srcDir + u"sample-pivot-table.xlsx");

    // Access first worksheet that contains pivot table data
    Worksheet dataSheet = wb.GetWorksheets().Get(0);

    // Access cell A3 and sets its data
    Cells cells = dataSheet.GetCells();
    Cell cell = cells.Get(u"A3");
    cell.PutValue(u"FooBar");

    // Access cell B3, sets its data. We set B3 a very long string which has more than 255 characters
    U16String longStr = u"Very long text 1. very long text 2. very long text 3. very long text 4. very long text 5. very long text 6. very long text 7. very long text 8. very long text 9. very long text 10. very long text 11. very long text 12. very long text 13. very long text 14. very long text 15. very long text 16. very long text 17. very long text 18. very long text 19. very long text 20. End of text.";
    cell = cells.Get(u"B3");
    cell.PutValue(longStr);

    // Print the length of cell B3 string
    std::cout << "Length of original data string: " << cell.GetStringValue().GetLength() << std::endl;

    // Access cell C3 and sets its data
    cell = cells.Get(u"C3");
    cell.PutValue(u"closed");

    // Access cell D3 and sets its data
    cell = cells.Get(u"D3");
    cell.PutValue(u"2016/07/21");

    // Access the second worksheet that contains pivot table
    Worksheet pivotSheet = wb.GetWorksheets().Get(1);

    // Access the pivot table
    PivotTable pivotTable = pivotSheet.GetPivotTables().Get(0);

    // IsExcel2003Compatible property tells if PivotTable is compatible for Excel2003 while refreshing PivotTable.
    // If it is true, a string must be less than or equal to 255 characters, so if the string is greater than 255 characters,
    // it will be truncated. If false, a string will not have the aforementioned restriction. The default value is true.
    pivotTable.SetIsExcel2003Compatible(true);
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Check the value of cell B5 of pivot sheet.
    // It will be 255 because we have set IsExcel2003Compatible property to true. All the data after 255 characters has been truncated
    Cell b5 = pivotSheet.GetCells().Get(u"B5");
    std::cout << "Length of cell B5 after setting IsExcel2003Compatible property to True: " << b5.GetStringValue().GetLength() << std::endl;

    // Now set IsExcel2003Compatible property to false and again refresh
    pivotTable.SetIsExcel2003Compatible(false);
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Now it will print 383 the original length of cell data. The data has not been truncated now.
    b5 = pivotSheet.GetCells().Get(u"B5");
    std::cout << "Length of cell B5 after setting IsExcel2003Compatible property to False: " << b5.GetStringValue().GetLength() << std::endl;

    // Set the row height and column width of cell B5 and also wrap its text
    pivotSheet.GetCells().SetRowHeight(b5.GetRow(), 100);
    pivotSheet.GetCells().SetColumnWidth(b5.GetColumn(), 65);
    Style st = b5.GetStyle();
    st.SetIsTextWrapped(true);
    b5.SetStyle(st);

    // Save workbook in xlsx format
    wb.Save(outDir + u"SpecifyCompatibility_out_.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
}
```
