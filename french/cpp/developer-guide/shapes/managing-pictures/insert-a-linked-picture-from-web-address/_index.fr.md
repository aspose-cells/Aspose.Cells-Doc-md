---
title: Insérer une image liée depuis une adresse Web avec C++
linktitle: Insérer une image liée à partir de l adresse Web
type: docs
weight: 450
url: /fr/cpp/insert-a-linked-picture-from-web-address/
description: Apprenez comment insérer une image liée depuis une adresse Web dans une feuille de calcul en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Parfois, vous devez insérer une image à partir du web (http://) dans une feuille de calcul. Pour ce faire, spécifiez l'URL de l'image et l'image sera téléchargée à chaque ouverture de la feuille de calcul dans Microsoft Excel. L'image n'est pas physiquement intégrée dans le document Excel, mais pointe vers une ressource web.

{{% /alert %}}

## **Utilisation de Microsoft Excel**

Dans Microsoft Excel (par exemple 2007) :

1. Cliquez sur le menu **Insérer** et sélectionnez **Image**.
1. Spécifiez l'adresse web de l'image dans la boîte de dialogue Insérer une image.

## **Utilisation de Aspose.Cells for C++**

Aspose.Cells for C++ supporte l'ajout d'une image liée en utilisant la méthode [**ShapeCollection::AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, System::String sourceFullName)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlinkedpicture/). La méthode retourne un objet [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/).

L'exemple suivant montre comment ajouter une image liée depuis une adresse web dans une feuille de calcul.

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

    // Instantiate a new Workbook
    Workbook workbook;

    // Insert a linked picture (from Web Address) to B2 Cell
    U16String imageUrl(u"http://www.aspose.com/Images/aspose-logo.jpg");
    Picture pic = workbook.GetWorksheets().Get(0).GetShapes().AddLinkedPicture(1, 1, 100, 100, imageUrl);

    // Set the height and width of the inserted image
    pic.SetHeightInch(1.04);
    pic.SetWidthInch(2.6);

    // Save the Excel file
    U16String outputPath = outDir + u"outLinkedPicture.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Linked picture inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
