---
title: Cómo cambiar el fondo en un comentario en Excel con C++
linktitle: Fondo del comentario
type: docs
weight: 190
url: /es/cpp/how-to-set-comment-background/
description: Cómo cambiar el color en un comentario en Excel. Cómo insertar una imagen o foto en un comentario en Excel usando C++.
keywords: agregar imagen insertada, color, comentario y fondo en Excel
---

{{% alert color="primary" %}}

Los comentarios se añaden a las celdas para registrar observaciones, que van desde detalles de cómo funciona una fórmula, de dónde proviene un valor o preguntas de los revisores. Los comentarios juegan un papel muy importante cuando varias personas discuten o revisan el mismo documento en diferentes momentos. ¿Cómo distinguir los comentarios de diferentes personas? Sí, podemos establecer un color de fondo diferente para cada comentario. Pero cuando necesitamos procesar muchos documentos y muchos comentarios, hacerlo manualmente es un desastre. Afortunadamente, [**Aspose.Cells**](https://products.aspose.com/cells/cpp/) proporciona una API que te permite hacer esto en código.

{{% /alert %}}

## **Cómo cambiar el color en el comentario en Excel**

Cuando no necesitas el color de fondo predeterminado para los comentarios, tal vez quieras reemplazarlo por un color de tu interés. ¿Cómo cambio el color de fondo del cuadro de Comentarios en Excel?

El siguiente código te guiará sobre cómo usar [**Aspose.Cells**](https://products.aspose.com/cells/cpp/) para agregar tu color de fondo favorito a los comentarios de tu elección.

Aquí hemos preparado un [archivo de ejemplo](exmaple.xlsx) para ti. Este archivo se usa para inicializar el objeto Workbook en el código a continuación.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputPath = srcDir + u"exmaple.xlsx";
    Workbook book(inputPath);

    Worksheet worksheet = book.GetWorksheets().Get(0);
    Comment comment = worksheet.GetComments().Get(0);

    CommentShape shape = comment.GetCommentShape();
    shape.GetFill().GetSolidFill().SetColor(Color::Red());

    U16String outputPath = outDir + u"result.xlsx";
    book.Save(outputPath);

    std::cout << "Comment color changed successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

Ejecuta el código anterior y obtendrás un [archivo de salida](result.xlsx).

## **Cómo insertar una imagen en el comentario en Excel**

Microsoft Excel permite a los usuarios personalizar el aspecto de las hojas de cálculo en gran medida. Incluso es posible agregar imágenes de fondo a los comentarios. Agregar una imagen de fondo puede ser una opción estética o usarse para reforzar la marca.

El código de ejemplo a continuación crea un archivo XLSX desde cero usando la API de [**Aspose.Cells**](https://products.aspose.com/cells/cpp/), y agrega un comentario con fondo de imagen en la celda A1.

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include <vector>
#include <cstdint>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a Workbook
    Workbook workbook;

    // Get a reference of comments collection with the first sheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);
    CommentCollection comments = worksheet.GetComments();

    // Add a comment to cell A1
    int32_t commentIndex = comments.Add(0, 0);
    Comment comment = comments.Get(commentIndex);
    comment.SetNote(u"First note.");
    Font font = comment.GetFont();
    font.SetName(u"Times New Roman");

    // Load an image into stream
    U16String imagePath = srcDir + u"image2.jpg";
    std::vector<uint8_t> imageData;
    // Assume image loading logic here
    // For simplicity, we assume imageData is populated with the image bytes

    // Set image data to the shape associated with the comment
    CommentShape commentShape = comment.GetCommentShape();
    commentShape.GetFill().SetImageData(Aspose::Cells::Vector<uint8_t>(imageData.data(), imageData.size()));

    // Save the workbook
    U16String outputPath = outDir + u"commentwithpicture1.out.xlsx";
    workbook.Save(outputPath, SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully with comment and image!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
