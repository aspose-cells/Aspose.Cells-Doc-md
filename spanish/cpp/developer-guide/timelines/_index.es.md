---
title: Insertar Línea de Tiempo con C++
linktitle: Líneas de tiempo
type: docs
weight: 170
url: /es/cpp/create-timeline/
description: Aprende cómo crear una línea de tiempo con Aspose.Cells usando C++.
---

## **Escenarios de uso posibles**

En lugar de ajustar filtros para mostrar fechas, puedes usar una línea de tiempo de Tabla Dinámica —una opción de filtro dinámica que te permite filtrar fácilmente por fecha/hora y acercar el período que deseas con un control deslizante. Microsoft Excel te permite crear una línea de tiempo seleccionando una tabla dinámica y luego haciendo clic en *Insertar > Línea de tiempo*. Aspose.Cells también te permite crear una línea de tiempo usando el método [**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.timelines/timelinecollection/add/).

## **Crear una línea de tiempo para una Tabla Dinámica**

Por favor, consulta el siguiente código de muestra. Carga el [archivo Excel de muestra](input.xlsx) que contiene la tabla dinámica. Luego crea la línea de tiempo basada en el primer campo pivote base. Finalmente, guarda el libro de trabajo en formato [XLSX de salida](output.xlsx). La siguiente captura de pantalla muestra la línea de tiempo creada por Aspose.Cells en el archivo Excel de salida.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Código de muestra**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing pivot table
    U16String inputFilePath = u"input.xlsx";
    Workbook wb(inputFilePath);

    // Access second worksheet (index 1)
    Worksheet sheet = wb.GetWorksheets().Get(1);

    // Access first pivot table inside the worksheet
    PivotTable pivot = sheet.GetPivotTables().Get(0);

    // Add timeline relating to pivot table
    int index = sheet.GetTimelines().Add(pivot, 15, 1, u"Ship Date");

    // Access the newly added timeline from timeline collection
    Timeline timeline = sheet.GetTimelines().Get(index);

    // Save the modified workbook
    U16String outputFilePath = u"output.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Timeline added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
