---
title: Conversion de la feuille de travail en image en utilisant les options ImageOrPrint avec C++
linktitle: Conversion de la feuille de travail en image
type: docs
weight: 90
url: /fr/cpp/converting-worksheet-to-image-using-imageorprint-options/
description: Apprenez comment convertir une feuille de travail en fichier image et appliquer différentes options d image et d impression en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Ce document est conçu pour fournir une compréhension détaillée de la façon de convertir une feuille de travail en fichier image et d'appliquer différentes options d'image et d'impression pour l'image, telles que la résolution, la compression TIFF, le format d'image, et la qualité de la page.

{{% /alert %}}

## **Enregistrement de feuilles de calcul en images - différentes approches**

Parfois, vous devrez peut-être présenter vos feuilles de calcul sous forme de représentation picturale. Vous pouvez avoir besoin de présenter les images des feuilles de calcul dans vos applications ou pages Web, les insérer dans un document Word, un fichier PDF, une présentation PowerPoint, ou les utiliser dans un autre scénario. En résumé, vous souhaitez qu'une feuille de calcul soit rendue sous forme d'image afin de pouvoir l'utiliser ailleurs. Aspose.Cells prend en charge la conversion des feuilles de calcul dans des fichiers Excel en images. De plus, Aspose.Cells supporte la configuration de différentes options telles que le format d'image, la résolution (verticale et horizontale), la qualité de l’image, et d'autres options d'image et d'impression.

Vous pouvez envisager l'automatisation de la suite bureautique, mais cela présente ses propres inconvénients. Plusieurs raisons et problèmes sont impliqués, tels que la sécurité, la stabilité, la scalabilité, la vitesse, le prix, et les fonctionnalités. En bref, il y a beaucoup de raisons, la principale étant que Microsoft lui-même recommande fortement de ne pas utiliser l'automatisation de la suite bureautique à partir de solutions logicielles.

Cet article montre comment créer une application console dans Visual Studio, effectuer la conversion d'une feuille de calcul en image en utilisant différentes options d'image et d'impression avec quelques lignes de code simples grâce à l'API Aspose.Cells.

Vous devez inclure l'espace de noms [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) dans votre programme/projet. Il contient plusieurs classes précieuses, par exemple, [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/), etc.

La classe [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) représente une feuille de calcul pour rendre des images de la feuille. Elle possède une méthode surcharge [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/) qui peut convertir directement une feuille de calcul en(s) fichier(s) image spécifié(s) avec vos attributs ou options désirés. Elle peut renvoyer un objet bitmap, et vous pouvez enregistrer un fichier image sur le disque/flux. Plusieurs formats d'image sont supportés, tels que BMP, PNG, GIF, JPEG, TIFF, EMF, etc.

## **Utilisation d'Aspose.Cells pour convertir une feuille en image en utilisant les options ImageOrPrint**

### **Création d'un classeur modèle dans Microsoft Excel**

J'ai créé un nouveau classeur dans MS Excel et ajouté quelques données dans la première feuille. Maintenant, je vais convertir la feuille "Sheet1" du fichier modèle en une image "SheetImage.tiff" et appliquer différentes options d’image comme la résolution horizontale et verticale, la compression Tiff, etc.

### **Téléchargez et installez Aspose.Cells**

Tout d'abord, vous devez [télécharger](https://downloads.aspose.com/cells/cpp) Aspose.Cells for C++. L'installer sur votre ordinateur de développement. Tous les composants [Aspose](http://www.aspose.com/) lorsqu'ils sont installés, fonctionnent en mode d’évaluation. Le mode d’évaluation n'a pas de limite de temps et insère uniquement des filigranes dans les documents produits.

### **Créer un projet**

Démarrez Visual Studio et créez une nouvelle application console. Cet exemple montrera une application console en C++.

### **Ajouter des références**

Ce projet utilisera Aspose.Cells. Vous devez donc ajouter une référence au composant Aspose.Cells dans votre projet. Par exemple, ajoutez une référence à `...\Program Files\Aspose\Aspose.Cells for C++\Bin\Aspose.Cells.lib`.

### **Convertir une feuille en fichier image**

```c++
#include <iostream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleWorksheetToAnImage.xlsx");

    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(300);
    options.SetVerticalResolution(300);
    options.SetTiffCompression(TiffCompression::CompressionLZW);
    options.SetImageType(ImageType::Tiff);
    options.SetPrintingPage(PrintingPageType::Default);

    SheetRender sr(sheet, options);

    int pageIndex = 3;
    int pageNumber = pageIndex + 1;
    std::wstring pageStr = std::to_wstring(pageNumber);
    U16String pageNumberStr(reinterpret_cast<const char16_t*>(pageStr.c_str()));
    U16String outputPath = outDir + U16String(u"outputWorksheetToAnImage_") + pageNumberStr + U16String(u".tiff");
    sr.ToImage(pageIndex, outputPath);

    std::cout << "Worksheet converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Options de conversion**

Il est possible d'enregistrer des pages spécifiques en tant qu'image. Le code suivant convertit les première et deuxième feuilles d'un classeur en images JPG.

```c++
#include <iostream>
#include <fstream>
#include <sstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputPath = srcDir + u"sampleSpecificPagesToImages.xlsx";
    Workbook workbook(inputPath);

    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(Aspose::Cells::Drawing::ImageType::Jpeg);

    SheetRender sr(worksheet, imgOptions);

    int32_t pageIndex = 3;

    Vector<uint8_t> imageData = sr.ToImage(pageIndex);

    std::wstringstream ws;
    ws << (pageIndex + 1);
    U16String pageNumStr(reinterpret_cast<const char16_t*>(ws.str().c_str()));

    U16String outputPath = outDir + u"outputSpecificPagesToImage_" + pageNumStr + u".jpg";
    std::ofstream outputFile(outputPath.ToUtf8(), std::ios::binary);
    outputFile.write(reinterpret_cast<const char*>(imageData.GetData()), imageData.GetLength());
    outputFile.close();

    std::cout << "Page rendered successfully to: " << outputPath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Conversion d’image utilisant WorkbookRender**

Une image TIFF peut contenir plus d’un cadre. Vous pouvez enregistrer tout le classeur dans une seule image TIFF avec plusieurs cadres ou pages :

```cpp
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

    // Load the workbook
    Workbook wb(srcDir + u"sampleUseWorkbookRenderForImageConversion.xlsx");

    // Set image options
    ImageOrPrintOptions opts;
    opts.SetImageType(ImageType::Tiff);

    // Render workbook to image
    WorkbookRender wr(wb, opts);
    wr.ToImage(outDir + u"outputUseWorkbookRenderForImageConversion.tiff");

    std::cout << "Workbook rendered to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
