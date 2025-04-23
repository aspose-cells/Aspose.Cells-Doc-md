--- 
title: Cómo verificar el estado de congelación sin Excel con C++ 
linktitle: Estado congelado 
type: docs 
weight: 190 
url: /es/cpp/how-to-check-frozen-state-of-excel-worksheet 
description: En este artículo, aprenderá cómo verificar el estado congelado de una hoja de cálculo de Excel programáticamente usando C++ con la API Aspose.Cells. 
--- 

## **Introducción** 

En este artículo, aprenderemos cómo comprobar el estado congelado de una hoja de cálculo de Excel programáticamente. Podemos simplemente descubrir si la hoja está congelada o dividida en MS Excel. Pero, ¿existe alguna forma de saber si está congelada o dividida con C++? Podemos hacerlo con Aspose.Cells for C++. 

## **¿Están congelados los paneles de la ventana?** 
Con Aspose.Cells for C++, podemos verificar si la ventana está congelada y cuántas filas y columnas están bloqueadas. 

Utilice la propiedad [**GetPaneState()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getpanestate/) para verificar el estado de los paneles de ventana y obtener filas y columnas bloqueadas con el método [**Worksheet::GetFreezedPanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getfreezedpanes/). 
1. Construir un libro de trabajo para abrir el archivo. 
2. Verificar si la hoja de cálculo está congelada. 
3. Obtener filas y columnas bloqueadas. 

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create the workbook from the specified file
    Workbook workbook(u"Frozen.xlsx");

    // Get the first worksheet from the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Check whether the worksheet is frozen
    if (sheet.GetPaneState() == PaneStateType::Frozen || sheet.GetPaneState() == PaneStateType::FrozenSplit)
    {
        int32_t row = 0, column = 0;
        int32_t rows = 0, columns = 0;

        // Get the locked rows and columns
        sheet.GetFreezedPanes(row, column, rows, columns);

        // Output the details if needed (just for demonstration)
        std::cout << "Frozen panes at Row: " << row << ", Column: " << column << ", Total Frozen Rows: " 
                  << rows << ", Total Frozen Columns: " << columns << std::endl;
    }

    Aspose::Cells::Cleanup();
}
``` 

