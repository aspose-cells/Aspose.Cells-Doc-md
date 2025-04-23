---
title: Ordenar datos en columna con lista de ordenamiento personalizada con C++
linktitle: Ordenar datos en una columna con lista de orden personalizado
type: docs
weight: 290
url: /es/cpp/sort-data-in-column-with-custom-sort-list/
description: Aprende cómo ordenar datos en la columna usando una lista personalizada mediante la API Aspose.Cells for C++.
keywords: Ordenar datos en una columna con lista de ordenación personalizada, Ordenar datos por lista personalizada.
---

## **Escenarios de uso posibles**

Puedes ordenar datos en la columna usando una lista personalizada. Esto se puede hacer usando el método [**DataSorter::AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/). Sin embargo, este método solo funciona si los ítems en la lista personalizada no contienen comas. Si contienen comas como "EE.UU.,US", "China,CN" etc., entonces debes usar el método [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/). Aquí, el último parámetro no es una cadena, sino un arreglo de cadenas.

## **Ordenar datos en una columna con lista de orden personalizado**

El siguiente código de ejemplo explica cómo usar el método [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) para ordenar datos con una lista de ordenamiento personalizada. Por favor, vea el [archivo de Excel de muestra](50528327.xlsx) utilizado en este código y el [archivo Excel de salida](50528328.xlsx) generado por él. La siguiente captura de pantalla muestra el efecto del código en el archivo de Excel de muestra al ejecutarse.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Código de muestra**

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

    // Load the source Excel file
    Workbook wb(srcDir + u"sampleSortData_CustomSortList.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Specify cell area - sort from A1 to A40
    CellArea ca = CellArea::CreateCellArea(u"A1", u"A40");

    // Create Custom Sort list
    Vector<U16String> customSortList = { u"USA,US", u"Brazil,BR", u"China,CN", u"Russia,RU", u"Canada,CA" };

    // Add Key for Column A, Sort it in Ascending Order with Custom Sort List
    wb.GetDataSorter().AddKey(0, SortOrder::Ascending, customSortList);
    wb.GetDataSorter().Sort(ws.GetCells(), ca);

    // Save the output Excel file
    wb.Save(outDir + u"outputSortData_CustomSortList.xlsx");

    std::cout << "Data sorted successfully with custom sort list!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
