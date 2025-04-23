---
title: Tabla dinámica y datos de origen con C++
linktitle: Tabla dinámica y datos fuente
type: docs
weight: 30
url: /es/cpp/pivot-table-and-source-data/
description: Aprenda cómo cambiar de manera dinámica los datos de origen de una tabla dinámica usando Aspose.Cells con C++.
---

## **Datos fuente de la tabla dinámica**

Hay momentos en los que deseas crear informes de Microsoft Excel con tablas dinámicas que toman datos de diferentes fuentes de datos (como una base de datos) que no se conocen en el momento del diseño. Este artículo proporciona un enfoque para cambiar dinámicamente la fuente de datos de una tabla dinámica.

### **Cambio de la fuente de datos de una tabla dinámica**

1. Crear una nueva plantilla de diseño.
   1. Crea un nuevo archivo de plantilla de diseñador como se muestra en la captura de pantalla a continuación.
   1. Luego define un rango nombrado, **DataSource**, que se refiere a este rango de celdas.

      **Creando una plantilla de diseñador y definiendo un rango nombrado, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. Crear una tabla dinámica basada en este rango nombrado.
   1. En Microsoft Excel, elige **Datos**, luego **Tabla Dinámica** y **Informe de Tabla Dinámica**.
   1. Crear una tabla dinámica basada en el rango nombrado creado en el primer paso.

      **Creando una tabla dinámica basada en el rango nombrado, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)


   1. Arrastra el campo correspondiente a la fila y columna de la tabla dinámica, luego crea la tabla dinámica resultante como en la captura de pantalla a continuación.

   **Creando una tabla dinámica basada en un campo correspondiente** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)


1. Haz clic derecho en la tabla dinámica y selecciona **Opciones de Tabla**.
   1. Marca **Actualizar al abrir** en la configuración de **Opciones de Datos**.

      **Configuración de las opciones de la tabla dinámica** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


Ahora, puedes guardar este archivo como tu archivo de plantilla de diseñador.

1. Poblar nuevos datos y cambiar la fuente de datos de una tabla dinámica.
   1. Una vez que se haya creado la plantilla de diseñador, utiliza el siguiente código para cambiar la fuente de datos de la tabla dinámica.

La ejecución del código de ejemplo a continuación cambia los datos fuente de la tabla dinámica.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Populating new data to the worksheet cells
    worksheet.GetCells().Get(u"A9").PutValue(u"Golf");
    worksheet.GetCells().Get(u"B9").PutValue(u"Qtr4");
    worksheet.GetCells().Get(u"C9").PutValue(7000);

    // Changing named range "DataSource"
    Range range = worksheet.GetCells().CreateRange(0, 0, 9, 3);
    range.SetName(u"DataSource");

    // Saving the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    std::cout << "File saved successfully!" << std::endl;

    return 0;
}
```
