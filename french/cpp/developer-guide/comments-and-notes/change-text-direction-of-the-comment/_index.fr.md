---
title: Changer la direction du texte du commentaire avec C++
linktitle: Changer la direction du texte du commentaire
type: docs
weight: 10
url: /fr/cpp/change-text-direction-of-the-comment/
description: Apprenez comment changer la direction du texte des commentaires dans Excel à l aide de Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Microsoft Excel permet aux utilisateurs d'ajouter des commentaires aux cellules pour ajouter des informations supplémentaires et mettre en évidence des données. Les développeurs peuvent avoir besoin de personnaliser le commentaire pour spécifier les paramètres d'alignement et la direction du texte. Aspose.Cells fournit des APIs pour accomplir la tâche.

{{% /alert %}}

Aspose.Cells fournit une propriété [**Shape.GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextdirection/) pour définir la direction du texte d'un commentaire. Le code d'exemple ci-dessous démontre l'utilisation de la propriété [**Shape.GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextdirection/) pour définir la direction du texte d'un commentaire.

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
