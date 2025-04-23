---
title: Obtenir DrawObject et Bound lors du rendu vers PDF avec C++ en utilisant la classe DrawObjectEventHandler
linktitle: Obtenir DrawObject et Bound lors du rendu vers PDF
type: docs
weight: 70
url: /fr/cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
description: Apprenez à utiliser la classe DrawObjectEventHandler en C++ pour capturer DrawObject et Bound lors du rendu de fichiers Excel en PDF ou en images.
---

## **Scénarios d'utilisation possibles**

Aspose.Cells fournit une classe abstraite [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) qui a une méthode [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/). L'utilisateur peut implémenter [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) et utiliser la méthode [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/) pour obtenir [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) et Bound lors du rendu Excel au format PDF ou Image. Voici une brève description des paramètres de la méthode [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/).

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) sera initialisé et renvoyé lors du rendu

- x: Gauche de [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

- y: Haut de [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

- largeur: Largeur de [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

- hauteur: Hauteur de [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

Si vous rendez un fichier Excel en PDF, vous pouvez utiliser la classe [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) avec [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/). De même, si vous rendez un fichier Excel en image, vous pouvez utiliser la classe [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) avec [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/).

## **Obtenez DrawObject et Bound lors du rendu au format Pdf en utilisant la classe DrawObjectEventHandler**

Veuillez voir le code exemple ci-dessous. Il charge le [fichier Excel d’exemple](64716821.xlsx) et le sauvegarde en [PDF de sortie](64716822.pdf). Lors du rendu en PDF, il utilise la propriété [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) et capture le [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) et le Bound des cellules existantes et des objets, tels que les images, etc. Si le type [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) est Cell, il affiche son Bound et StringValue. Et si le type [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) est Image, il affiche son Bound et le nom de Shape. Veuillez consulter la sortie console du code exemple ci-dessous pour plus d’aide.

## **Code d'exemple**

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

class ClsDrawObjectEventHandler : public DrawObjectEventHandler
{
public:
    void Draw(DrawObject& drawObject, float x, float y, float width, float height) override
    {
        std::cout << std::endl;

        if (drawObject.GetType() == DrawObjectEnum::Cell)
        {
            std::cout << "[X]: " << x << " [Y]: " << y << " [Width]: " << width << " [Height]: " << height 
                      << " [Cell Value]: " << drawObject.GetCell().GetStringValue().ToUtf8() << std::endl;
        }

        if (drawObject.GetType() == DrawObjectEnum::Image)
        {
            std::cout << "[X]: " << x << " [Y]: " << y << " [Width]: " << width << " [Height]: " << height 
                      << " [Shape Name]: " << drawObject.GetShape().GetName().ToUtf8() << std::endl;
        }

        std::cout << "----------------------" << std::endl;
    }
};

void Run()
{
    Workbook wb(u"sampleGetDrawObjectAndBoundUsingDrawObjectEventHandler.xlsx");
    PdfSaveOptions opts;
    auto drawObjectEventHandler = std::make_shared<ClsDrawObjectEventHandler>();
    opts.SetDrawObjectEventHandler(drawObjectEventHandler.get());
    wb.Save(u"outputGetDrawObjectAndBoundUsingDrawObjectEventHandler.pdf", opts);
}

int main()
{
    Aspose::Cells::Startup();
    Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sortie console**

{{< highlight java >}}

[X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
