---
title: Charger une image Web depuis une URL dans une feuille Excel avec C++
linktitle: Charger une image web à partir d une URL dans une feuille de calcul Excel
type: docs
weight: 30
url: /fr/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/
description: Apprenez comment convertir une image depuis une URL en image intégrée dans Excel en utilisant C++ et l API Aspose.Cells for C++.
keywords: excel afficher une image depuis une URL, excel URL vers image, afficher une image dans excel depuis une URL, excel insérer une image depuis une URL, convertir une URL en image dans excel, image excel depuis une URL, charger une image depuis une URL dans excel, C++, Excel
---

## Charger une image à partir d'une URL dans une feuille de calcul Excel

L'API Aspose.Cells for C++ offre une méthode simple pour charger des images depuis des URLs dans les feuilles Excel. Cet article explique comment télécharger des données d'image dans un courant mémoire et l'insérer dans la feuille à l'aide d'Aspose.Cells. L'image devient intégrée dans le fichier Excel et ne nécessite pas de téléchargements externes lors de l'ouverture.

## Code d'exemple

```c++
#include <iostream>
#include <Aspose.Cells.h>
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    try
    {
        // Create a new workbook
        Workbook wb;

        // Get the first worksheet
        WorksheetCollection worksheets = wb.GetWorksheets();
        Worksheet sheet = worksheets.Get(0);

        // Get the pictures collection
        PictureCollection pictures = sheet.GetPictures();

        // Insert the picture from local file to B2 cell (row 1, column 1)
        // Note: Image file should be pre-downloaded to source directory
        U16String imagePath = srcDir + u"aspose-logo.jpg";
        pictures.Add(1, 1, imagePath);

        // Save the Excel file
        wb.Save(outDir + u"webimagebook.out.xlsx");
        std::cout << "Image added successfully." << std::endl;
    }
    catch (const std::exception& ex)
    {
        std::cerr << "Error: " << ex.what() << std::endl;
        return 1;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Pour les scénarios nécessitant des images toujours à jour à partir d'une URL, utilisez la méthode décrite dans [Insérer une Image Liée depuis une Adresse Web](/cells/fr/cpp/insert-a-linked-picture-from-web-address/). Cette approche charge l'image depuis l'URL à chaque ouverture de la feuille de calcul.

{{% /alert %}}
