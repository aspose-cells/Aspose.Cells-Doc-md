---
title: Cómo cambiar el color de la fuente del comentario con C++
linktitle: Cómo cambiar el color de fuente del comentario
type: docs
weight: 180
url: /es/cpp/how-to-change-the-comment-font-color/
description: Aprenda cómo personalizar el color de la fuente en los comentarios de Excel usando Aspose.Cells con C++.
---

{{% alert color="primary" %}} 

Microsoft Excel permite a los usuarios agregar comentarios a las celdas para proporcionar información adicional y resaltar datos. Los desarrolladores pueden necesitar personalizar el comentario para especificar la configuración de alineación, dirección del texto, color de fuente, etc. Aspose.Cells proporciona API para lograr esta tarea.

{{% /alert %}} 

Aspose.Cells proporciona una propiedad [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/) para establecer el color de la fuente del comentario. El siguiente código de ejemplo demuestra el uso de la propiedad [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/) para configurar la dirección del texto de un comentario.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add some text in cell A1
    worksheet.GetCells().Get(u"A1").PutValue(u"Here");

    // Add a comment to A1 cell
    int commentIndex = worksheet.GetComments().Add(u"A1");
    Comment comment = worksheet.GetComments().Get(commentIndex);

    // Set its vertical alignment setting
    comment.GetCommentShape().SetTextVerticalAlignment(TextAlignmentType::Center);

    // Set the Comment note
    comment.SetNote(u"This is my Comment Text. This is Test.");

    // Get the comment shape
    Shape shape = comment.GetCommentShape();

    // Set the fill color of the shape to black
    shape.GetFill().GetSolidFill().SetColor(Color::Black());

    // Get the font of the shape
    Font font = shape.GetFont();

    // Set the font color to white
    font.SetColor(Color::White());

    // Create a StyleFlag to apply font color changes
    StyleFlag styleFlag;
    styleFlag.SetFontColor(true);

    // Apply the font color changes to the shape's text
    shape.GetTextBody().Format(0, shape.GetText().GetLength(), font, styleFlag);

    // Save the Excel file
    workbook.Save(outDir + u"outputChangeCommentFontColor.xlsx");

    Aspose::Cells::Cleanup();
}
```

El [archivo de salida](102662195.xlsx) generado por el código anterior se adjunta para su referencia.
