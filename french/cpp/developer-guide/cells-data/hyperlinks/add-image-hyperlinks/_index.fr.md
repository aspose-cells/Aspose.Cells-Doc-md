---
title: Ajouter des liens hypertexte d images avec C++
linktitle: Ajouter des hyperliens d image
type: docs
weight: 140
url: /fr/cpp/add-image-hyperlinks/
description: Apprenez à ajouter des liens hypertexte d images via l API Aspose.Cells for C++.
keywords: Ajouter des hyperliens d image, Insérer des hyperliens d image
---

{{% alert color="primary" %}} 

Les hyperliens sont utiles pour accéder à des informations sur d'autres feuilles de calcul ou sur des sites Web. Microsoft Excel permet aux utilisateurs d'ajouter des hyperliens sur le texte dans les cellules, ainsi que sur les images. Les hyperliens d'image peuvent faciliter la navigation dans une feuille de calcul, par exemple, en tant que boutons suivant et précédent, ou des logos qui renvoient à des sites particuliers. Ce document explique comment insérer des hyperliens d'image dans une feuille de calcul à l'aide d'Aspose.Cells.

{{% /alert %}} 

Aspose.Cells vous permet d'ajouter des hyperliens aux images dans les feuilles de calcul à l'exécution. Il est possible de définir et de modifier l'info-bulle et l'adresse du lien. Le code d'exemple suivant illustre comment ajouter un hyperlien d'image dans une feuille de calcul.

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

    // Instantiate a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a string value to a cell
    worksheet.GetCells().Get(u"C2").PutValue(u"Image Hyperlink");

    // Set the 4th row height
    worksheet.GetCells().SetRowHeight(3, 100);

    // Set the C column width
    worksheet.GetCells().SetColumnWidth(2, 21);

    // Add a picture to the C4 cell
    int index = worksheet.GetPictures().Add(3, 2, 4, 3, srcDir + u"aspose-logo.jpg");

    // Get the picture object
    Picture pic = worksheet.GetPictures().Get(index);

    // Set the placement type
    pic.SetPlacement(PlacementType::FreeFloating);

    // Add an image hyperlink
    Hyperlink hlink = pic.AddHyperlink(u"http://www.aspose.com/");

    // Specify the screen tip
    hlink.SetScreenTip(u"Click to go to Aspose site");

    // Save the Excel file
    workbook.Save(outDir + u"ImageHyperlink_out.xls");

    std::cout << "Image hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
