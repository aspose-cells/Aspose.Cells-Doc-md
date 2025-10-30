---
title: Come cambiare il colore del carattere del commento con C++
linktitle: Come cambiare il colore del carattere del commento
type: docs
weight: 180
url: /it/cpp/how-to-change-the-comment-font-color/
description: Impara come personalizzare il colore del carattere del commento in Excel usando Aspose.Cells con C++.
---

{{% alert color="primary" %}} 

Microsoft Excel consente agli utenti di aggiungere commenti alle celle per aggiungere informazioni aggiuntive e evidenziare i dati. Gli sviluppatori potrebbero aver bisogno di personalizzare il commento per specificare le impostazioni di allineamento, la direzione del testo, il colore del font, ecc. Aspose.Cells fornisce API per completare il compito.

{{% /alert %}} 

Aspose.Cells fornisce una proprietà [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/) per impostare il colore del carattere del commento. Il seguente esempio di codice dimostra l'uso della proprietà [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/) per impostare la direzione del testo di un commento.

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

Il file di output (102662195.xlsx) generato dal codice sopra è allegato per il tuo riferimento.
{{< app/cells/assistant language="cpp" >}}
