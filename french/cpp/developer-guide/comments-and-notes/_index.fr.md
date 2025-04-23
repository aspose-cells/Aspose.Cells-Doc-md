---
title: Gérer les commentaires et notes avec C++
linktitle: Commentaires et notes
type: docs
weight: 128
url: /fr/cpp/comments-and-notes/
description: Insérer et gérer des commentaires ou notes avec Aspose.Cells for C++.
keywords: insérer des commentaires, insérer des notes
---

## **Introduction**

Les commentaires sont utilisés pour ajouter des informations supplémentaires aux cellules. Aspose.Cells propose deux méthodes pour ajouter des commentaires aux cellules. La première consiste à créer des commentaires dans un fichier du concepteur manuellement. Ces commentaires sont ensuite importés en utilisant Aspose.Cells. La seconde consiste à ajouter des commentaires en utilisant l'API Aspose.Cells à l'exécution. Ce sujet traite de l'ajout de commentaires aux cellules en utilisant l'API Aspose.Cells. La mise en forme des commentaires sera également expliquée.

## **Ajouter un commentaire**

Ajoutez un commentaire à une cellule en appelant la méthode [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/add/) de la collection [**Comments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/) (encapsulée dans l'objet [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)). Le nouvel objet [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/) peut être accédé à partir de la collection [**Comments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/) en passant l'indice du commentaire. Après avoir accédé à l'objet [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/), personnalisez la note du commentaire en utilisant la propriété [**GetNote()**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/getnote/) de l'objet [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/).

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

## **Mise en forme des commentaires**

Il est également possible de formater l'apparence des commentaires en configurant leur hauteur, leur largeur et leurs paramètres de police.

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

## **Ajouter une image au commentaire**

Avec Microsoft Excel 2007, il est également possible d'avoir une image en arrière-plan d'un commentaire de cellule. Dans Excel 2007, cela se fait en suivant les étapes suivantes. (Ils supposent que vous avez déjà ajouté un commentaire de cellule.)

1. Faites un clic droit sur la cellule qui contient le commentaire.
1. Sélectionnez **Afficher/masquer les commentaires**, et effacez tout texte du commentaire.
1. Cliquez sur le bord du commentaire pour le sélectionner.
1. Sélectionnez **Format**, puis **Commentaire**.
1. Sur l'onglet **Couleurs et traits**, développez la liste **Couleur**.
1. Cliquez sur **Remplissage**.
1. Sur l'onglet **Image**, cliquez sur **Sélectionner une image**.
1. Localisez et sélectionnez l'image.
1. Cliquez sur **OK** jusqu'à ce que tous les dialogues se ferment.

Aspose.Cells propose également cette fonctionnalité. Ci-dessous se trouve un exemple de code qui crée un fichier XLSX à partir de zéro, en ajoutant un commentaire à la cellule "A1" avec une image définie comme arrière-plan.

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

## **Sujets avancés**
- [Modifier la direction du texte du commentaire](/cells/fr/cpp/change-text-direction-of-the-comment/)
- [Comment changer la couleur de police du commentaire](/cells/fr/cpp/how-to-change-the-comment-font-color/)
- [Comment définir l'arrière-plan du commentaire](/cells/fr/cpp/how-to-set-comment-background/)
- [Commentaires en fil](/cells/fr/cpp/threaded-comments/)
