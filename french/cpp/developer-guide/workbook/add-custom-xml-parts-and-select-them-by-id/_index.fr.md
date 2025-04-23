---
title: Ajouter des parties XML personnalisées et les sélectionner par ID avec C++
linktitle: Ajouter des parties XML personnalisées et les sélectionner par ID
type: docs
weight: 70
url: /fr/cpp/add-custom-xml-parts-and-select-them-by-id/
description: Apprenez à ajouter et à sélectionner des parties XML personnalisées dans des fichiers Excel en utilisant Aspose.Cells avec C++.
---

## **Scénarios d'utilisation possibles**

Les parties XML personnalisées sont des données XML stockées à l'intérieur des documents Microsoft Excel et sont utilisées par des applications qui interagissent avec elles. Il n'existe actuellement aucun moyen direct de les ajouter via l'UI de Microsoft Excel. Cependant, vous pouvez les ajouter de manière programmatique de plusieurs façons, comme en utilisant VSTO ou Aspose.Cells. Utilisez la méthode [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/add/) pour ajouter une partie XML personnalisée via l'API Aspose.Cells. Vous pouvez également définir son ID en utilisant la propriété [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/). De même, si vous souhaitez sélectionner une partie XML personnalisée par ID, vous pouvez utiliser la méthode [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/).

## **Ajouter des parties XML personnalisées et les sélectionner par ID**

Le code exemple suivant ajoute d'abord quatre parties XML personnalisées en utilisant la méthode [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/add/). Ensuite, il définit leurs IDs en utilisant la propriété [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/). Enfin, il trouve ou sélectionne l'une des parties XML ajoutées en utilisant la méthode [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/). Veuillez également consulter la sortie de la console ci-dessous pour référence.

## **Code d'exemple**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Markup;

int main()
{
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Some data in the form of byte array
    // Please use correct XML and Schema instead
    Vector<uint8_t> btsData = { 1, 2, 3 };
    Vector<uint8_t> btsSchema = { 1, 2, 3 };

    // Create four custom xml parts
    wb.GetCustomXmlParts().Add(btsData, btsSchema);
    wb.GetCustomXmlParts().Add(btsData, btsSchema);
    wb.GetCustomXmlParts().Add(btsData, btsSchema);
    wb.GetCustomXmlParts().Add(btsData, btsSchema);

    // Assign ids to custom xml parts
    wb.GetCustomXmlParts().Get(0).SetID(u"Fruit");
    wb.GetCustomXmlParts().Get(1).SetID(u"Color");
    wb.GetCustomXmlParts().Get(2).SetID(u"Sport");
    wb.GetCustomXmlParts().Get(3).SetID(u"Shape");

    // Specify search custom xml part id
    U16String srchID = u"Fruit";
    srchID = u"Color";
    srchID = u"Sport";

    // Search custom xml part by the search id
    CustomXmlPart cxp = wb.GetCustomXmlParts().SelectByID(srchID);

    // Print the found or not found message on console
    if (cxp.IsNull())
    {
        std::cout << "Not Found: CustomXmlPart ID " << srchID.ToUtf8() << std::endl;
    }
    else
    {
        std::cout << "Found: CustomXmlPart ID " << srchID.ToUtf8() << std::endl;
    }

    std::cout << "AddCustomXMLPartsAndSelectThemByID executed successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sortie console**

{{< highlight java >}}
Found: CustomXmlPart ID Sport
{{< /highlight >}}
