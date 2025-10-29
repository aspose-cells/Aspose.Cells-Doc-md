---
title: Comment changer la couleur de la police du commentaire avec C++
linktitle: Comment changer la couleur de la police du commentaire
type: docs
weight: 180
url: /fr/cpp/how-to-change-the-comment-font-color/
description: Apprenez comment personnaliser la couleur de la police du commentaire dans Excel en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}} 

Microsoft Excel permet aux utilisateurs d'ajouter des commentaires aux cellules pour ajouter des informations supplémentaires et mettre en évidence des données. Les développeurs peuvent avoir besoin de personnaliser le commentaire pour spécifier les paramètres d'alignement, de direction du texte, de couleur de police, etc. Aspose.Cells fournit des APIs pour accomplir la tâche.

{{% /alert %}} 

Aspose.Cells fournit une propriété [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/) pour définir la couleur de la police du commentaire. Le code d'exemple ci-dessous démontre l'utilisation de la propriété [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/) pour définir la direction du texte d'un commentaire.

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

Le [fichier de sortie](102662195.xlsx) généré par le code ci-dessus est joint à titre de référence.
{{< app/cells/assistant language="cpp" >}}
