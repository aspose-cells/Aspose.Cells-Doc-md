---
title: Cambia la direzione del testo del commento con C++
linktitle: Cambia la Direzione del Testo del Commento
type: docs
weight: 10
url: /it/cpp/change-text-direction-of-the-comment/
description: Impara come cambiare la direzione del testo dei commenti in Excel utilizzando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Microsoft Excel consente agli utenti di aggiungere commenti alle celle per aggiungere informazioni aggiuntive e evidenziare dati. Gli sviluppatori potrebbero aver bisogno di personalizzare il commento per specificare le impostazioni di allineamento e la direzione del testo. Aspose.Cells fornisce API per completare il compito.

{{% /alert %}}

Aspose.Cells fornisce una proprietà [**Shape.GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextdirection/) per impostare la direzione del testo di un commento. Il seguente esempio di codice dimostra l'uso della proprietà [**Shape.GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextdirection/) per impostare la direzione del testo di un commento.

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
