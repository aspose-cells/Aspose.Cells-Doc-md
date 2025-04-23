---
title: Administrar comentarios y notas con C++
linktitle: Comentarios y notas
type: docs
weight: 128
url: /es/cpp/comments-and-notes/
description: Insertar y administrar comentarios o notas con Aspose.Cells for C++.
keywords: insertar comentarios, insertar notas
---

## **Introducción**

Los comentarios se utilizan para agregar información adicional a las celdas. Aspose.Cells proporciona dos métodos para agregar comentarios a las celdas. El primero es crear comentarios en un archivo de diseño manualmente. Estos comentarios luego se importan utilizando Aspose.Cells. El segundo es agregar comentarios usando la API de Aspose.Cells en tiempo de ejecución. Este tema trata sobre cómo agregar comentarios a las celdas mediante la API de Aspose.Cells. También se explicará el formato de comentarios.

## **Agregar un comentario**

Agregar un comentario a una celda llamando al método [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/add/) de la colección [**Comments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/) (encapsulado en el objeto [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)). El nuevo objeto [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/) se puede acceder desde la colección [**Comments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/) pasando el índice del comentario. Después de acceder al objeto [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/), personalice la nota del comentario utilizando la propiedad [**GetNote()**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/getnote/) del objeto [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/).

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int32_t sheetIndex = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add a comment to cell "F5"
    int32_t commentIndex = worksheet.GetComments().Add(u"F5");

    // Access the newly added comment
    Comment comment = worksheet.GetComments().Get(commentIndex);

    // Set the comment note
    comment.SetNote(u"Hello Aspose!");

    // Save the Excel file
    U16String outputPath = outDir + u"book1.out.xls";
    workbook.Save(outputPath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Formato de comentario**

También es posible dar formato a la apariencia de los comentarios configurando su altura, ancho y ajustes de fuente.

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

    // Create workbook
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int32_t sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding a comment to "F5" cell
    int32_t commentIndex = worksheet.GetComments().Add(u"F5");

    // Accessing the newly added comment
    Comment comment = worksheet.GetComments().Get(commentIndex);

    // Setting the comment note
    comment.SetNote(u"Hello Aspose!");

    // Setting the font size of a comment to 14
    comment.GetFont().SetSize(14);

    // Setting the font of a comment to bold
    comment.GetFont().SetIsBold(true);

    // Setting the height of the font to 10
    comment.SetHeightCM(10);

    // Setting the width of the font to 2
    comment.SetWidthCM(2);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Agregar una imagen al comentario**

Con Microsoft Excel 2007, también es posible tener una imagen como fondo de un comentario de celda. En Excel 2007, esto se logra siguiendo los siguientes pasos. (Se supone que ya ha agregado un comentario de celda)

1. Haga clic con el botón derecho en la celda que contiene el comentario.
1. Seleccione **Mostrar/Ocultar comentarios**, y elimine cualquier texto del comentario.
1. Haga clic en el borde del comentario para seleccionarlo.
1. Seleccione **Formato**, luego **Comentario**.
1. En la pestaña **Colores y líneas**, expanda la lista de **Color**.
1. Haga clic en **Efectos de relleno**.
1. En la pestaña **Imagen**, haga clic en **Seleccionar imagen**.
1. Ubique y seleccione la imagen.
1. Haga clic en **Aceptar** hasta que se cierren todos los diálogos.

Aspose.Cells también proporciona esta función. A continuación se muestra un ejemplo de código que crea un archivo XLSX desde cero, agregando un comentario a la celda "A1" con una imagen como fondo.

```c++
#include <Aspose.Cells.h>
#include <fstream>
#include <vector>
#include <iostream>

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook workbook;
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);
    CommentCollection comments = sheet.GetComments();

    int32_t commentIndex = comments.Add(0, 0);
    Comment comment = comments.Get(commentIndex);
    comment.SetNote(u"First note.");

    Font commentFont = comment.GetFont();
    commentFont.SetName(u"Times New Roman");

    U16String imagePath = srcDir + u"logo.jpg";
    std::vector<uint8_t> imageData;
    std::ifstream file(imagePath.ToUtf8(), std::ios::binary | std::ios::ate);
    if (file)
    {
        std::streamsize size = file.tellg();
        file.seekg(0, std::ios::beg);
        imageData.resize(size);
        file.read(reinterpret_cast<char*>(imageData.data()), size);
    }
    Vector<uint8_t> data(imageData.data(), static_cast<int32_t>(imageData.size()));

    CommentShape shape = comment.GetCommentShape();
    shape.GetFill().SetImageData(data);

    U16String outputPath = outDir + u"book1.out.xlsx";
    workbook.Save(outputPath, SaveFormat::Xlsx);

    std::cout << "Workbook with image comment created successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Temas avanzados**
- [Cambiar la dirección del texto del comentario](/cells/es/cpp/change-text-direction-of-the-comment/)
- [Cómo cambiar el color de fuente del comentario](/cells/es/cpp/how-to-change-the-comment-font-color/)
- [Cómo configurar el fondo del comentario](/cells/es/cpp/how-to-set-comment-background/)
- [Comentarios enhebrados](/cells/es/cpp/threaded-comments/)
