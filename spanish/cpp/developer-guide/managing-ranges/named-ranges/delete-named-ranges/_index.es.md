---
title: Eliminar Rangos con Nombre con C++
linktitle: Eliminar rangos con nombres
type: docs
weight: 90
url: /es/cpp/delete-named-ranges/
description: Aprenda cómo eliminar nombres definidos o rangos con nombre de archivos de Excel o OpenOffice usando Aspose.Cells for C++.
---

## **Introducción**
Si hay demasiados nombres definidos o rangos con nombre en los archivos de Excel, debemos eliminar algunos para que no se vuelvan a hacer referencia.

## **Eliminar rango con nombre en MS Excel**

Para eliminar un rango con nombre en Excel, siga estos pasos:
1. Abra Microsoft Excel y abra el libro que contiene el rango con nombre.
2. Vaya a la pestaña "Fórmulas" en la cinta de Excel.
3. Haga clic en el botón "Administrador de nombres" en el grupo "Nombres definidos". Esto abrirá la ventana de diálogo del Administrador de nombres.
4. En la ventana de diálogo del Administrador de nombres, seleccione el rango con nombre que desea eliminar.
5. Haga clic en el botón "Eliminar". Confirme la eliminación cuando se lo soliciten.
6. Haz clic en el botón "Cerrar" para cerrar el cuadro de diálogo del Administrador de nombres.
7. Guarda el libro para guardar los cambios.

## **Elimina Rango con Nombre usando Aspose.Cells for C++**
Con Aspose.Cells for C++, puede eliminar rangos con nombre o nombres definidos por [texto](https://reference.aspose.com/cells/cpp/aspose.cells/namecollection/remove/) o [índice](https://reference.aspose.com/cells/cpp/aspose.cells/namecollection/removeat/) en la lista.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Book2.xlsx";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Delete a named range by text
    worksheets.GetNames().Remove(u"NamedRange");

    // Delete a defined name by index
    worksheets.GetNames().RemoveAt(0);

    // Save the workbook to retain the changes
    workbook.Save(outputFilePath);

    std::cout << "Named ranges removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Nota: si el nombre definido es referido por fórmulas, no se puede eliminar. Solo se puede eliminar la fórmula del nombre definido.

## **Eliminar algunos rangos con nombre**
Cuando eliminamos un nombre definido, debemos verificar si está referido por todas las fórmulas en el archivo.
Para mejorar el rendimiento de la eliminación de rangos con nombre, podemos eliminar algunos juntos.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Book2.xlsx";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Delete some defined names
    Vector<U16String> namesToRemove = { u"NamedRange1", u"NamedRange2" };
    worksheets.GetNames().Remove(namesToRemove);

    // Save the workbook to retain the changes
    workbook.Save(outputFilePath);

    std::cout << "Named ranges removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Eliminar nombres definidos duplicados**
Algunos archivos de Excel se corrompen porque algunos nombres definidos están duplicados. Por lo tanto, podemos eliminar estos nombres duplicados para reparar el archivo.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Book2.xlsx";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Delete some defined names
    worksheets.GetNames().RemoveDuplicateNames();

    // Save the workbook to retain the changes
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully after removing duplicate names!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
