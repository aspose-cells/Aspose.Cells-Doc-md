---
title: Gestion des images avec C++
linktitle: Gestion des images
type: docs
weight: 10
url: /fr/cpp/managing-pictures/
description: Ajoutez, positionnez et gérez des images dans des feuilles de calcul en utilisant l API Aspose.Cells for C++.
---

Aspose.Cells permet aux développeurs d'ajouter des images à des feuilles de calcul en cours d'exécution. De plus, le positionnement de ces images peut être contrôlé en cours d'exécution, ce qui est discuté plus en détail dans les sections suivantes.

Cet article explique comment ajouter des images et comment insérer une image qui montre le contenu de certaines cellules.

## **Ajout d'images**

Ajouter des images à une feuille de calcul est très facile. Il suffit de quelques lignes de code :
Appelez simplement la méthode [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/add/) de la classe [**PictureCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/) (encapsulée dans l'objet [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)). La méthode [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/add/) prend les paramètres suivants :

- **Index de la ligne supérieure gauche**, l'index de la ligne supérieure gauche.
- **Index de la colonne supérieure gauche**, l'index de la colonne supérieure gauche.
- **Nom du fichier image**, le nom du fichier image, complet avec le chemin.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Add worksheet and get reference
    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add image to worksheet at F6 (row 5, column 5)
    U16String imagePath = srcDir + u"logo.jpg";
    worksheet.GetPictures().Add(5, 5, imagePath);

    // Save workbook
    U16String outputPath = outDir + u"output.xls";
    workbook.Save(outputPath);

    std::cout << "Worksheet with image created successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Positionnement des images**

Il existe deux façons possibles de contrôler le positionnement des images à l'aide d'Aspose.Cells :

- Positionnement proportionnel: définir une position proportionnelle à la hauteur et à la largeur de la ligne.
- Positionnement absolu : définissez la position exacte sur la page où l'image sera insérée, par exemple, 40 pixels à gauche et 20 pixels en dessous du bord de la cellule.

### **Positionnement proportionnel**

Les développeurs peuvent positionner les images en proportion de la hauteur des lignes et de la largeur des colonnes en utilisant les propriétés [**UpperDeltaX**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getupperdeltax/) et [**UpperDeltaY**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getupperdeltay/) du objet [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/). Un objet [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) peut être obtenu à partir de [**PictureCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/) en passant son index d'image. Cet exemple place une image dans la cellule F6.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook workbook;

    // Add new worksheet and get reference
    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add picture to worksheet at (5,5) position
    U16String imagePath = outDir + u"logo.jpg";
    int pictureIndex = worksheet.GetPictures().Add(5, 5, imagePath);

    // Access added picture and set positioning
    Drawing::Picture picture = worksheet.GetPictures().Get(pictureIndex);
    picture.SetUpperDeltaX(200);
    picture.SetUpperDeltaY(200);

    // Save modified workbook
    U16String outputPath = outDir + u"book1.out.xls";
    workbook.Save(outputPath);

    std::cout << "Picture added and positioned successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Positionnement Absolu**

Les développeurs peuvent également positionner les images absolument en utilisant les propriétés [**Left**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getleft/) et [**Top**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettop/) de l'objet [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/). Cet exemple place une image dans la cellule F6, à 60 pixels de la gauche et à 10 pixels du haut de la cellule.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Access worksheet collection and add new sheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    int sheetIndex = worksheets.Add();

    // Get reference to newly added worksheet
    Worksheet worksheet = worksheets.Get(sheetIndex);

    // Add picture to worksheet at row 5, column 5 (cell F6)
    PictureCollection pictures = worksheet.GetPictures();
    int pictureIndex = pictures.Add(5, 5, srcDir + u"logo.jpg");

    // Access added picture and set position
    Picture picture = pictures.Get(pictureIndex);
    picture.SetLeft(60);
    picture.SetTop(10);

    // Save modified workbook
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Workbook with inserted picture saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Insérer une image basée sur la référence de cellule**

Aspose.Cells vous permet d'afficher le contenu d'une cellule de feuille de calcul dans une forme d'image. Vous pouvez lier l'image à la cellule qui contient les données que vous souhaitez afficher. Étant donné que la cellule ou la plage de cellules est liée à l'objet graphique, les modifications apportées aux données dans cette cellule ou plage de cellules apparaissent automatiquement dans l'objet graphique.

Ajoutez une image à la feuille de calcul en appelant la méthode [**AddPicture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpicture/) de la classe [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) (encapsulée dans l'objet [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)). Spécifiez la plage de la cellule en utilisant l'attribut [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) de l'objet [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Access first worksheet and cells collection
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);
    Cells cells = worksheet.GetCells();

    // Set cell values
    cells.Get(u"A1").PutValue(U16String(u"A1"));
    cells.Get(u"C10").PutValue(U16String(u"C10"));

    // Add picture to worksheet
    auto shapes = worksheet.GetShapes();
    Picture pic = shapes.AddPicture(0, 3, 10, 6, Vector<uint8_t>());

    // Set picture formula and update values
    pic.SetFormula(u"A1:C10");
    shapes.UpdateSelectedValue();

    // Save workbook
    U16String outputPath = outDir + u"output.out.xls";
    workbook.Save(outputPath);

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**
- [Ajouter un ensemble d'icônes conditionnelles avec le texte de la cellule](/cells/fr/cpp/add-conditional-icons-set-with-the-cell-text/)
- [Insérer une image liée à partir d'une adresse web](/cells/fr/cpp/insert-a-linked-picture-from-web-address/)
- [Insérer une image en fonction de la référence de la cellule](/cells/fr/cpp/insert-a-picture-based-on-cell-reference/)
- [Charger une image Web à partir d'une URL dans une feuille de calcul Excel](/cells/fr/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
{{< app/cells/assistant language="cpp" >}}
