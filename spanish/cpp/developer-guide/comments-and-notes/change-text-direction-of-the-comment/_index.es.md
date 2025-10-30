---
title: Cambiar la dirección del texto del comentario con C++
linktitle: Cambiar la dirección del texto del comentario
type: docs
weight: 10
url: /es/cpp/change-text-direction-of-the-comment/
description: Aprenda cómo cambiar la dirección del texto de los comentarios en Excel usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Microsoft Excel permite a los usuarios agregar comentarios a las celdas para proporcionar información adicional y resaltar datos. Los desarrolladores pueden necesitar personalizar el comentario para especificar la configuración de alineación y la dirección del texto. Aspose.Cells proporciona API para lograr esta tarea.

{{% /alert %}}

Aspose.Cells proporciona una propiedad [**Shape.GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextdirection/) para establecer la dirección del texto de un comentario. El siguiente código de ejemplo demuestra el uso de la propiedad [**Shape.GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextdirection/) para configurar la dirección del texto de un comentario.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook wb;

    // Get the first worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Add a comment to A1 cell
    int commentIndex = sheet.GetComments().Add(u"A1");
    Comment comment = sheet.GetComments().Get(commentIndex);

    // Set its vertical alignment setting
    comment.GetCommentShape().SetTextVerticalAlignment(TextAlignmentType::Center);

    // Set its horizontal alignment setting
    comment.GetCommentShape().SetTextHorizontalAlignment(TextAlignmentType::Right);

    // Set the Text Direction - Right-to-Left
    comment.GetCommentShape().SetTextDirection(TextDirectionType::RightToLeft);

    // Set the Comment note
    comment.SetNote(u"This is my Comment Text. This is test");

    // Save the Excel file
    U16String outputPath = outDir + u"OutCommentShape.out.xlsx";
    wb.Save(outputPath);

    std::cout << "Comment shape created and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
