---
title: Accéder et modifier le libellé d affichage de l objet Ole lié avec C++
linktitle: Accéder et modifier l étiquette d affichage de l objet Ole lié
type: docs
weight: 100
url: /fr/cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: Apprenez comment accéder et modifier le libellé d affichage des objets Ole liés dans les fichiers Excel en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Microsoft Excel vous permet de changer le libellé d'affichage de l'objet Ole comme montré dans la capture d'écran suivante. Vous pouvez également accéder ou modifier le libellé d'affichage de l'objet Ole en utilisant les API Aspose.Cells avec les méthodes [**GetLabel()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getlabel/) et [**SetLabel(const U16String\& value)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/setlabel/).

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **Accéder et modifier l'étiquette d'affichage de l'objet Ole lié**

Veuillez consulter le code d'exemple suivant, il charge le [fichier Excel d'exemple](64716810.xlsx) qui contient l'objet Ole. Le code accède à l'objet Ole et modifie son libellé de API d'exemple à Aspose API. Veuillez consulter la sortie de la console ci-dessous qui montre l'effet du code d'exemple sur le fichier Excel d'exemple pour référence.

## **Code d'exemple**

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample Excel file
    U16String inputFilePath = u"sampleAccessAndModifyLabelOfOleObject.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first Ole Object
    OleObject oleObject = ws.GetOleObjects().Get(0);

    // Display the Label of the Ole Object
    std::cout << "Ole Object Label - Before: " << oleObject.GetLabel().ToUtf8() << std::endl;

    // Modify the Label of the Ole Object
    oleObject.SetLabel(u"Aspose APIs");

    // Save workbook to memory stream
    auto ms = wb.SaveToStream();

    // Set the workbook reference to null
    wb = Workbook();

    // Load workbook from memory stream
    wb = Workbook(ms);

    // Access first worksheet
    ws = wb.GetWorksheets().Get(0);

    // Access first Ole Object
    oleObject = ws.GetOleObjects().Get(0);

    // Display the Label of the Ole Object that has been modified earlier
    std::cout << "Ole Object Label - After: " << oleObject.GetLabel().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sortie console**

{{< highlight java >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
