---
title: Conversion de feuille en image et conversion de feuille en image par page avec C++
linktitle: Conversion de la feuille de calcul en image et de la feuille de calcul en image par page
type: docs
weight: 80
url: /fr/cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/
description: Apprenez comment convertir une feuille de calcul en fichier image et convertir une feuille avec plusieurs pages en un fichier image par page en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Ce document est conçu pour fournir aux développeurs une compréhension détaillée de la façon de convertir une feuille de calcul en fichier image et une feuille avec plusieurs pages en un fichier image par page.

Parfois, vous pourriez avoir besoin de présenter des feuilles de calcul en tant qu'images, par exemple, pour les utiliser dans des applications ou des pages web. Vous pourriez avoir besoin d'insérer les images dans un document Word, un fichier PDF, une présentation PowerPoint ou les utiliser dans un autre scénario. Fondamentalement, vous voulez afficher la feuille de calcul sous forme d'image. Aspose.Cells prend en charge la conversion des feuilles de calcul dans les fichiers Microsoft Excel en images. De plus, Aspose.Cells prend en charge la conversion d'un classeur en plusieurs fichiers image, un par page.

Vous pouvez utiliser l'automatisation Office pour réaliser cela, mais l'automatisation Office a ses propres inconvénients. Plusieurs raisons et problèmes sont impliqués : par exemple, la sécurité, la stabilité, l'évolutivité/vitesse, le prix et les fonctionnalités. En bref, il y a de nombreuses raisons, mais la principale est que Microsoft lui-même recommande vivement de ne pas utiliser l'automatisation Office.

{{% /alert %}}

## **Utilisation d'Aspose.Cells pour convertir une feuille de calcul en un fichier image**

Cet article montre comment créer une application console dans Visual Studio, convertir une feuille de calcul en une image et convertir une feuille de calcul en une image pour chaque feuille de calcul avec quelques lignes de code simples à l'aide de l'API Aspose.Cells.

Vous devez inclure l’espace de noms [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) dans votre programme/projet. Il possède plusieurs classes précieuses, telles que [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/), etc. La classe [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) représente une feuille de calcul pour rendre des images pour la feuille de calcul et possède une méthode [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/) surchargée qui peut convertir une feuille de calcul en fichiers d'image directement avec tous attributs ou options définis. Elle peut renvoyer un objet `System.Drawing.Bitmap`, et vous pouvez enregistrer un fichier image sur le disque/flux. Plusieurs formats d’image sont supportés, par exemple BMP, PNG, GIF, JPG, JPEG, TIFF, EMF, et autres.

Cet article explique comment :

- Convertir une feuille de calcul en une image
- Convertir chaque page d'une feuille de calcul en une image

Cette tâche montre comment utiliser Aspose.Cells pour convertir une feuille de calcul à partir d'un classeur modèle en un fichier image.

### **Configurer le projet**

1. Tout d'abord, [téléchargez Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp).
1. Installez-le sur votre ordinateur de développement. Tous les composants [Aspose](http://www.aspose.com/) une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et n'insère que des filigranes dans les documents produits. Maintenant, démarrez Visual Studio et créez une nouvelle application console. Cet exemple utilise une application console C++. Ajoutez une référence à Aspose.Cells dans le projet créé.

### **Convertir une feuille de calcul en un fichier image**

J'ai créé un nouveau classeur dans Microsoft Excel et ajouté des données dans la première feuille de calcul : **Testbook.xlsx** (1 feuille de calcul). Ensuite, convertissez la feuille de calcul du fichier modèle en un fichier image appelé SheetImage.jpg.

Voici le code utilisé par le composant pour accomplir la tâche. Il convertit la Feuille1 dans **Testbook.xlsx** en un fichier image pour expliquer à quel point cette conversion est facile.

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

std::string convert_u16_to_string(const U16String& u16str);

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheettoImageFile.xlsx");
    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions imgOptions;
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetImageType(ImageType::Jpeg);

    SheetRender sr(sheet, imgOptions);
    sr.ToImage(0, outDir + u"outputConvertWorksheettoImageFile.jpg");

    std::cout << "Worksheet converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Utilisation d'Aspose.Cells pour convertir une feuille de calcul en fichier image par page**

Cet exemple montre comment utiliser Aspose.Cells pour convertir une feuille de calcul d'un classeur modèle comportant plusieurs pages en un fichier image unique par page.

### **Convertir une feuille de calcul en image par page**

J'ai créé un nouveau classeur dans Microsoft Excel et ajouté des données dans la première feuille de calcul : **Testbook2.xlsx** (1 feuille de calcul).

Maintenant, convertissez la feuille de calcul du fichier modèle en fichiers image (un fichier par page). Comme j'ai déjà créé l'application console pour effectuer la tâche de copie, je vais ignorer ces étapes de création de l'application console et passer directement aux étapes de conversion de la feuille de calcul.

Voici le code utilisé par le composant pour accomplir la tâche. Il convertit Sheet1 dans Testbook2.xlsx en fichiers image par page.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

std::u16string intToU16String(int value) {
    std::u16string result;
    if (value == 0) {
        result.push_back(u'0');
        return result;
    }
    while (value > 0) {
        result.insert(result.begin(), static_cast<char16_t>(u'0' + (value % 10)));
        value /= 10;
    }
    return result;
}

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheetToImageByPage.xlsx");

    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);
    options.SetImageType(ImageType::Tiff);

    SheetRender sr(sheet, options);
    for (int j = 0; j < sr.GetPageCount(); j++)
    {
        std::u16string pageNum = intToU16String(j + 1);
        U16String fileName = outDir + U16String(u"outputConvertWorksheetToImageByPage_") + U16String(pageNum.c_str()) + U16String(u".tif");
        sr.ToImage(j, fileName);
    }

    std::cout << "Worksheet converted to images by page successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
