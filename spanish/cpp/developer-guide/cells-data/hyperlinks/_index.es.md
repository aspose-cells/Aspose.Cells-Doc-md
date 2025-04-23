---
title: Insertar Hipervínculos en Excel o OpenOffice con C++
linktitle: Gestión de hipervínculos
type: docs
weight: 45
url: /es/cpp/insert-hyperlinks-to-excel/
description: Cómo insertar hipervínculos en archivos de Excel con la biblioteca Aspose.Cells sin usar MS Excel usando C++.
keywords: Insertar hipervínculos en Excel, Agregar o insertar hipervínculos, Agregar o insertar enlace a una URL, Agregar o insertar un enlace a una celda, Agregar un enlace a un archivo externo
---

{{% alert color="primary" %}} 

Un hipervínculo se usa para crear un enlace entre dos entidades. Todos están familiarizados con el uso de hipervínculos, especialmente en sitios web.
Utilizando Aspose.Cells, los desarrolladores pueden crear diferentes tipos de hipervínculos en archivos de Microsoft Excel. Este tema discute qué tipos de hipervínculos son compatibles con Aspose.Cells y cómo se pueden usar en nuestros archivos de Excel.

{{% /alert %}} 

## **Añadiendo hipervínculos**
Aspose.Cells permite a los desarrolladores agregar hipervínculos a archivos de Excel usando la API o hojas de cálculo de diseño (hojas donde los hipervínculos se crean manualmente y Aspose.Cells se usa para importarlos en otras hojas).

Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite acceder a cada hoja en el archivo de Excel. Una hoja se representa por la clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) ofrece diferentes métodos para agregar distintos hipervínculos a archivos de Excel.

## **Añadir un enlace a una URL**
La clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) contiene una colección [GetHyperlinks()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/). Cada elemento en la colección [GetHyperlinks()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/) representa un [Hyperlink](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/). Añade hipervínculos a URLs llamando al método [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) de la colección [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/). El método [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) requiere los siguientes parámetros:

- Nombre de la celda, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas en este rango de hipervínculo.
- URL, la dirección de la URL.

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

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a hyperlink to cell "A1"
    worksheet.GetHyperlinks().Add(u"A1", 1, 1, u"http://www.aspose.com");

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

En el ejemplo anterior, se añade un hipervínculo a una URL en una celda vacía, **A1**. En tales casos, si una celda está vacía, entonces la dirección URL también se agrega a esa celda vacía como su valor. Si la celda no está vacía y se agrega un hipervínculo, el valor de la celda se ve como texto plano. Para que se vea como un hipervínculo, aplique la configuración de formato adecuada en esa celda.

{{% /alert %}} 

## **Añadir un enlace a una celda en el mismo archivo**
Es posible agregar hipervínculos a celdas en el mismo archivo de Excel llamando al método [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) de la colección [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/). El método [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) funciona tanto para hipervínculos internos como externos. Una versión del método sobrecargado requiere los siguientes parámetros:

- Nombre de la celda, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas en este rango de hipervínculo.
- URL, la dirección de la celda de destino.

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    workbook.GetWorksheets().Add();

    // Obtaining the reference of the first (default) worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in
    // The same Excel file
    worksheet.GetHyperlinks().Add(u"B3", 1, 1, u"Sheet2!B9");

    // Saving the Excel file
    workbook.Save(outDir + u"output.out.xls");

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Agregar un enlace a un archivo externo**
Es posible agregar hipervínculos a archivos externos de Excel llamando al método [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) de la colección [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/). El método [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) requiere los siguientes parámetros:

- Nombre de la celda, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas en este rango de hipervínculo.
- URL, la dirección del destino, archivo externo de Excel.

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Add an internal hyperlink to the "A5" cell of the other worksheet "Sheet2" in the same Excel file
    worksheet.GetHyperlinks().Add(U16String(u"A5"), 1, 1, srcDir + U16String(u"book1.xls"));

    // Save the Excel file
    workbook.Save(outDir + U16String(u"output.out.xls"));

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Temas avanzados**
- [Agregar hipervínculos de imagen](/cells/es/cpp/add-image-hyperlinks/)
- [Detectar tipo de hipervínculo](/cells/es/cpp/detect-hyperlink-type/)
- [Editando Hipervínculos de la Hoja de Cálculo](/cells/es/cpp/editing-hyperlinks-of-worksheet/)
- [Obtener Hipervínculos en Rango](/cells/es/cpp/get-hyperlinks-in-range/)
