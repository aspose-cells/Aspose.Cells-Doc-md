---
title: Cómo controlar la barra de pestañas de la hoja con C++
linktitle: Cómo Controlar la Barra de Pestañas de la Hoja
type: docs
weight: 600
url: /es/cpp/how-to-control-sheet-tab-bar/
description: Aprende cómo controlar la barra de pestañas de la hoja a través de la API Aspose.Cells for C++.
keywords: Cómo Controlar la Barra de Pestañas de la Hoja, Operar la Barra de Pestañas de la Hoja, Configurar la Barra de Pestañas de la Hoja, Controlar la Barra de Pestañas de la Hoja. 
---

## **Escenarios de uso posibles**
Cuando necesitas ajustar la visualización de la barra de hojas de Excel, necesitas saber cómo controlar la barra de pestañas de la hoja, como ocultar o mostrar la barra de pestañas, cambiar el ancho de la barra de pestañas, especificar la primera pestaña visible, y más. Aspose.Cells soporta estas funciones. Aspose.Cells proporciona las siguientes propiedades y métodos para ayudarte a lograr tus objetivos.

- [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/)
- [**WorkbookSettings.GetSheetTabBarWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getsheettabbarwidth/)
- [**WorkbookSettings.GetFirstVisibleTab()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getfirstvisibletab/)

## **Cómo controlar la barra de pestañas de la hoja usando Aspose.Cells for C++**
Este ejemplo muestra cómo:

1. Crear un libro de trabajo.
1. Agregar datos a las celdas en la primera hoja de cálculo.
1. Mostrar la pestaña de la hoja y configurar el ancho de la barra de pestañas.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook object
    Workbook workbook;

    // Obtain the reference to the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");
    cell = cells.Get(u"C1");
    cell.PutValue(u"Price");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");

    // Display the sheet tab and set the width of the tab bar
    workbook.GetSettings().SetShowTabs(true);
    workbook.GetSettings().SetSheetTabBarWidth(150);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Vista previa del archivo resultante:
<br>
<image src="result.png" width="70%" />

