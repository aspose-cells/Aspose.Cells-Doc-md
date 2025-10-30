---
title: Crear Rangos con nombre a nivel de Libro y Hoja de Trabajo con C++
linktitle: Rango con nombre
type: docs
weight: 40
url: /es/cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: Aprende a crear rangos con nombre a nivel de libro y hoja de trabajo con C++ usando Aspose.Cells.
---

{{% alert color="primary" %}} 

Microsoft Excel permite a los usuarios definir rangos con nombre con dos ámbitos diferentes: libro de trabajo (también conocido como ámbito global) y hoja de cálculo.

- Los rangos con nombre con ámbito de libro de trabajo se pueden acceder desde cualquier hoja de cálculo dentro de ese libro de trabajo simplemente utilizando su nombre.
- Los rangos con nombre de ámbito de hoja de cálculo se acceden con la referencia de la hoja de cálculo particular en la que se creó.

Aspose.Cells proporciona la misma funcionalidad que Microsoft Excel para agregar rangos con nombre a nivel de libro de trabajo y de hoja de cálculo. Al crear un rango con nombre de ámbito de hoja de cálculo, se debe utilizar la referencia de la hoja de cálculo en el rango con nombre para especificarlo como un rango con nombre de ámbito de hoja de cálculo.

{{% /alert %}} 

## **Agregar un Rango con Nombre de Alcance de Libro**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a new Workbook object
    Workbook workbook;

    // Get the first worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get worksheet's cells collection
    Cells cells = sheet.GetCells();

    // Create a range of Cells from Cell A1 to C10
    Range workbookScope = cells.CreateRange(u"A1", u"C10");

    // Assign the name to workbook scope named range
    workbookScope.SetName(u"workbookScope");

    // Save the workbook
    workbook.Save(srcDir + u"WorkbookScope.out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Agregar un Rango con Nombre de Alcance de Hoja de Cálculo**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a new Workbook object
    Workbook workbook;

    // Get the first worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get worksheet's cells collection
    Cells cells = sheet.GetCells();

    // Create a range of Cells
    Range localRange = cells.CreateRange(u"A1", u"C10");

    // Assign name to range with sheet reference
    localRange.SetName(u"Sheet1!local");

    // Save the workbook
    U16String outputFilePath = u"..\\Data\\02_OutputDirectory\\output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Temas avanzados**
- [Crear y Copiar Rangos con Nombre de Acceso](/cells/es/cpp/create-access-and-copy-named-ranges/)
- [Formato y Modificación de Rangos con Nombre](/cells/es/cpp/format-and-modify-named-ranges/)
- [Obtener Rango con Vínculos Externos](/cells/es/cpp/get-range-with-external-links/)
- [Implementación de Rangos No Secuenciales](/cells/es/cpp/implementing-non-sequential-ranges/)

{{< app/cells/assistant language="cpp" >}}
