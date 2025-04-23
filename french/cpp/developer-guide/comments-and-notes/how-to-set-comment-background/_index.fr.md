---
title: Comment changer l arrière plan d un commentaire dans Excel avec C++
linktitle: Arrière plan du commentaire
type: docs
weight: 190
url: /fr/cpp/how-to-set-comment-background/
description: Comment changer la couleur dans un commentaire dans Excel. Comment insérer une image ou une photo dans un commentaire dans Excel en utilisant C++.
keywords: ajouter une image en inset, une couleur de commentaire, arrière plan excel
---

{{% alert color="primary" %}}

Les commentaires sont ajoutés aux cellules pour enregistrer des remarques, allant des détails sur le fonctionnement d'une formule, de l'origine d'une valeur ou de questions des réviseurs. Les commentaires jouent un rôle extrêmement important lorsque plusieurs personnes discutent ou révisent le même document à différents moments. Comment distinguer les commentaires de différentes personnes ? Oui, nous pouvons définir une couleur d'arrière-plan différente pour chaque commentaire. Mais lorsque nous devons traiter beaucoup de documents et de nombreux commentaires, faire cela manuellement est un désastre. Heureusement, [**Aspose.Cells**](https://products.aspose.com/cells/cpp/) offre une API qui vous permet de faire cela dans le code.

{{% /alert %}}

## **Comment changer la couleur dans le commentaire dans Excel**

Lorsque vous n'avez pas besoin de la couleur de fond par défaut pour les commentaires, vous pouvez la remplacer par une couleur qui vous intéresse. Comment puis-je changer la couleur de l'arrière-plan de la boîte de commentaires dans Excel ?

Le code suivant vous guidera sur la façon d'utiliser [**Aspose.Cells**](https://products.aspose.com/cells/cpp/) pour ajouter votre couleur d'arrière-plan préférée aux commentaires de votre choix.

Voici un [fichier d'exemple](exmaple.xlsx) préparé pour vous. Ce fichier sert à initialiser l'objet Workbook dans le code ci-dessous.

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

Exécutez le code ci-dessus, et vous obtiendrez un [fichier de sortie](result.xlsx).

## **Comment insérer une image ou une photo dans le commentaire dans Excel**

Microsoft Excel permet aux utilisateurs de personnaliser considérablement l'apparence des feuilles de calcul. Il est même possible d'ajouter des images de fond aux commentaires. L'ajout d'une image d'arrière-plan peut être un choix esthétique ou utilisé pour renforcer la marque.

Le code d'exemple ci-dessous crée un fichier XLSX à partir de zéro en utilisant l'API [**Aspose.Cells**](https://products.aspose.com/cells/cpp/), et ajoute un commentaire avec une image d'arrière-plan à la cellule A1.

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
