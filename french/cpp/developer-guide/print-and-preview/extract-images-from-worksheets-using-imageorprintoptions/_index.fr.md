---
title: Extraire des images des feuilles en utilisant ImageOrPrintOptions avec C++
linktitle: Extraire des images des feuilles de calcul
type: docs
weight: 140
url: /fr/cpp/extract-images-from-worksheets-using-imageorprintoptions/
description: Apprenez comment extraire des images des feuilles Excel et les enregistrer sur un lecteur local en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Les utilisateurs de Microsoft Excel peuvent ajouter des images aux feuilles de calcul. Avec Aspose.Cells, il est possible de lire des images à partir de fichiers Microsoft Excel et de les enregistrer sur un lecteur local. Cet article montre comment.

{{% /alert %}} 

Le code d'exemple ci-dessous montre comment extraire des images à partir d'un fichier Excel et les enregistrer.

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

    // Open a template Excel file
    Workbook workbook(srcDir + u"sampleExtractImagesFromWorksheets.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first Picture in the first worksheet
    Picture pic = worksheet.GetPictures().Get(0);

    // Define ImageOrPrintOptions
    ImageOrPrintOptions printoption;

    // Specify the image format
    printoption.SetImageType(ImageType::Jpeg);

    // Save the image
    pic.ToImage(outDir + u"outputExtractImagesFromWorksheets.jpg", printoption);

    std::cout << "Image extracted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
