---  
title: Créer un classeur partagé avec Aspose.Cells en C++  
linktitle: Créer un classeur partagé avec Aspose.Cells  
type: docs  
weight: 40  
url: /fr/cpp/create-shared-workbook-with-aspose-cells/  
description: Apprenez comment créer un classeur partagé en utilisant Aspose.Cells avec C++.  
---  

## **Scénarios d'utilisation possibles**  

Microsoft Excel vous permet de partager le classeur comme montré dans la capture d'écran suivante. Lorsque vous partagez le classeur, plus d'un utilisateur peut éditer le classeur sur le réseau. Aspose.Cells vous permet de créer un classeur partagé avec la propriété [**Workbook.GetShared()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshared/).  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Créer un classeur partagé avec Aspose.Cells**  

Le code d'exemple suivant crée un classeur partagé en définissant la propriété [**Workbook.GetShared()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshared/) à **true**. Lorsque vous ouvrez le [fichier Excel de sortie](55541786.xlsx) dans Microsoft Excel, vous verrez **Shared** avec le nom du classeur de sortie comme montré dans cette capture d'écran.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **Code d'exemple**  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create Workbook object
    std::unique_ptr<Workbook> wb = std::make_unique<Workbook>();

    // Share the Workbook
    wb->GetSettings().SetShared(true);

    // Save the Shared Workbook
    wb->Save(u"outputSharedWorkbook.xlsx");

    std::cout << "Shared workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
