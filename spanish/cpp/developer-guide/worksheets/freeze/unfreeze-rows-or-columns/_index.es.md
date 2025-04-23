---
title: Descongelar filas o columnas de la hoja de cálculo de Excel con C++
linktitle: Descongelar paneles
type: docs
weight: 190
url: /es/cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: En este artículo, aprenderá cómo descongelar filas, columnas o paneles de hojas de cálculo de Excel programáticamente usando la API Aspose.Cells for C++.
keywords: Descongelar paneles, descongelar filas, descongelar columnas, descongelar ventana.
---

## **Introducción**

En este artículo, aprenderemos cómo descongelar filas, columnas y paneles en hojas de cálculo de Excel. Si las hojas en archivos de Excel están congeladas, a veces queremos descongelar la hoja o ajustar filas, columnas o paneles congelados.

## **En Excel**

1. Haga clic en la pestaña **Vista** > **Inmovilizar paneles** > **Inmovilizar paneles**.

**![descongelar paneles en Excel](Unfreeze-Panes.png)**

## **Descongelar filas, columnas o paneles con Aspose.Cells for C++**
Es simple descongelar paneles con Aspose.Cells for C++. Utilice el método [**Worksheet.UnFreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unfreezepanes/) para descongelar paneles.

1. Construya un objeto `Workbook` para abrir el archivo congelado.
2. Descongelar paneles usando el método `Worksheet.UnFreezePanes()`.
3. Guarda el archivo.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    U16String inputFilePath(u"Frozen.xlsx");
    Workbook workbook(inputFilePath);

    // Unfreeze panes in the first worksheet
    workbook.GetWorksheets().Get(0).UnFreezePanes();

    // Save the modified workbook
    U16String outputFilePath(u"Unfrozen.xlsx");
    workbook.Save(outputFilePath);

    std::cout << "Panes unfrozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Adjunto [archivo de Excel de origen de ejemplo](Frozen.xlsx).
