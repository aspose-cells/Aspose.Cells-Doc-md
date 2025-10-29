---
title: Spécifiez si le PivotTable est compatible pour Excel2003 lors du rafraîchissement du PivotTable avec C++
linktitle: Spécifier la compatibilité pour Excel2003 dans PivotTable
type: docs
weight: 80
url: /fr/cpp/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: Apprenez comment spécifier la compatibilité d un PivotTable pour Excel2003 à l aide de Aspose.Cells for C++ lors du rafraîchissement du PivotTable.
---

{{% alert color="primary" %}}

Aspose.Cells offre la propriété [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/isexcel2003compatible/) que vous pouvez utiliser pour spécifier si le tableau croisé dynamique est compatible avec Excel 2003 lors du rafraîchissement du tableau croisé dynamique. Si true, une chaîne doit être inférieure ou égale à 255 caractères, donc si la chaîne est supérieure à 255 caractères, elle sera tronquée. Si **false**, une chaîne n'aura pas la restriction mentionnée. La valeur par défaut est **true**.

{{% /alert %}}

## **Spécifiez si le PivotTable est compatible pour Excel2003 lors de l'actualisation du PivotTable**

Le code d'exemple suivant explique l'utilisation de la propriété [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/isexcel2003compatible/). La chaîne d'origine fait 383 caractères de long. Mais lorsque la propriété [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/isexcel2003compatible/) est définie sur **vrai** et que le tableau croisé dynamique est actualisé, les données de la cellule B5 du tableau croisé dynamique sont tronquées et deviennent 255 caractères de long. Cependant, lorsque la propriété [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/isexcel2003compatible/) est définie sur **faux** et que le tableau croisé dynamique est à nouveau actualisé, les données de la cellule B5 du tableau croisé dynamique ne sont pas tronquées et restent longues de 383 caractères. Veuillez lire les commentaires à l'intérieur du code pour une meilleure compréhension de cette propriété.

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
{{< app/cells/assistant language="cpp" >}}
