---
title: Gestión de Imágenes con C++
linktitle: Gestión de imágenes
type: docs
weight: 10
url: /es/cpp/managing-pictures/
description: Agregar, posicionar y gestionar imágenes en hojas de cálculo usando la API Aspose.Cells for C++.
---

Aspose.Cells permite a los desarrolladores agregar imágenes a las hojas de cálculo en tiempo de ejecución. Además, la posición de estas imágenes se puede controlar en tiempo de ejecución, lo cual se discute con más detalle en las siguientes secciones.

Este artículo explica cómo agregar imágenes e insertar una imagen que muestre el contenido de ciertas celdas.

## **Añadir imágenes**

Agregar imágenes a una hoja de cálculo es muy fácil. Solo toma unas pocas líneas de código:
Simplemente llama al método [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/add/) del [**PictureCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/) (envuelto en el objeto [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)). El método [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/add/) requiere los siguientes parámetros:

- **Índice de fila superior izquierda**, el índice de la fila superior izquierda.
- **Índice de columna superior izquierda**, el índice de la columna superior izquierda.
- **Nombre del archivo de imagen**, el nombre del archivo de imagen, completo con la ruta.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Add worksheet and get reference
    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add image to worksheet at F6 (row 5, column 5)
    U16String imagePath = srcDir + u"logo.jpg";
    worksheet.GetPictures().Add(5, 5, imagePath);

    // Save workbook
    U16String outputPath = outDir + u"output.xls";
    workbook.Save(outputPath);

    std::cout << "Worksheet with image created successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Posicionamiento de imágenes**

Hay dos formas posibles de controlar el posicionamiento de las imágenes usando Aspose.Cells:

- Posicionamiento proporcional: define una posición proporcional a la altura y ancho de la fila.
- Posicionamiento absoluto: define la posición exacta en la página donde se insertará la imagen, por ejemplo, 40 píxeles a la izquierda y 20 píxeles por debajo del borde de la celda.

### **Posicionamiento proporcional**

Los desarrolladores pueden posicionar las imágenes proporcionalmente a la altura de fila y el ancho de columna usando las propiedades [**UpperDeltaX**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getupperdeltax/) y [**UpperDeltaY**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getupperdeltay/) del objeto [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/). Se puede obtener un objeto [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) pasando su índice de imagen al [**PictureCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/). Este ejemplo coloca una imagen en la celda F6.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook workbook;

    // Add new worksheet and get reference
    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add picture to worksheet at (5,5) position
    U16String imagePath = outDir + u"logo.jpg";
    int pictureIndex = worksheet.GetPictures().Add(5, 5, imagePath);

    // Access added picture and set positioning
    Drawing::Picture picture = worksheet.GetPictures().Get(pictureIndex);
    picture.SetUpperDeltaX(200);
    picture.SetUpperDeltaY(200);

    // Save modified workbook
    U16String outputPath = outDir + u"book1.out.xls";
    workbook.Save(outputPath);

    std::cout << "Picture added and positioned successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Posicionamiento absoluto**

Los desarrolladores también pueden posicionar las imágenes de forma absoluta utilizando las propiedades [**Left**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getleft/) y [**Top**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettop/) del objeto [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/). Este ejemplo coloca una imagen en la celda F6, a 60 píxeles a la izquierda y 10 píxeles arriba de la celda.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Access worksheet collection and add new sheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    int sheetIndex = worksheets.Add();

    // Get reference to newly added worksheet
    Worksheet worksheet = worksheets.Get(sheetIndex);

    // Add picture to worksheet at row 5, column 5 (cell F6)
    PictureCollection pictures = worksheet.GetPictures();
    int pictureIndex = pictures.Add(5, 5, srcDir + u"logo.jpg");

    // Access added picture and set position
    Picture picture = pictures.Get(pictureIndex);
    picture.SetLeft(60);
    picture.SetTop(10);

    // Save modified workbook
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Workbook with inserted picture saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Insertar una imagen basada en referencia de celda**

Aspose.Cells te permite mostrar el contenido de una celda de la hoja de cálculo en una forma de imagen. Puedes vincular la imagen a la celda que contiene los datos que deseas mostrar. Dado que la celda o el rango de celdas está vinculado al objeto gráfico, los cambios que realices en los datos de esa celda o rango de celdas aparecerán automáticamente en el objeto gráfico.

Agrega una imagen a la hoja de cálculo llamando al método [**AddPicture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpicture/) del [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) (envuelto en el objeto [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)). Especifica el rango de celdas usando el atributo [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) del objeto [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Access first worksheet and cells collection
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);
    Cells cells = worksheet.GetCells();

    // Set cell values
    cells.Get(u"A1").PutValue(U16String(u"A1"));
    cells.Get(u"C10").PutValue(U16String(u"C10"));

    // Add picture to worksheet
    auto shapes = worksheet.GetShapes();
    Picture pic = shapes.AddPicture(0, 3, 10, 6, Vector<uint8_t>());

    // Set picture formula and update values
    pic.SetFormula(u"A1:C10");
    shapes.UpdateSelectedValue();

    // Save workbook
    U16String outputPath = outDir + u"output.out.xls";
    workbook.Save(outputPath);

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Temas avanzados**
- [Agregar Iconos Condicionales Establecidos con el Texto de la Celda](/cells/es/cpp/add-conditional-icons-set-with-the-cell-text/)
- [Insertar una imagen vinculada desde una dirección web](/cells/es/cpp/insert-a-linked-picture-from-web-address/)
- [Insertar una imagen basada en la referencia de la celda](/cells/es/cpp/insert-a-picture-based-on-cell-reference/)
- [Cargar una imagen web desde una URL en una hoja de cálculo de Excel](/cells/es/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
{{< app/cells/assistant language="cpp" >}}
