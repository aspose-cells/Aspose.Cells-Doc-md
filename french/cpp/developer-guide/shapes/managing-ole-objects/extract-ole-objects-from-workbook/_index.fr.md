---
title: Extraire les objets OLE du classeur avec C++
linktitle: Extraire les objets OLE du classeur
type: docs
weight: 110
url: /fr/cpp/extract-ole-objects-from-workbook/
description: Apprenez comment extraire des objets OLE d un classeur en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Parfois, vous devez extraire des objets OLE d'un classeur. Aspose.Cells supporte l'extraction et la sauvegarde de ces objets OLE.

Cet article montre comment créer une application console dans Visual Studio et extraire différents objets OLE d'un classeur avec quelques lignes de code simples.

{{% /alert %}}

## **Extraire les objets OLE d'un classeur**

### **Création d'un classeur modèle**

1. Créez un classeur dans Microsoft Excel.
1. Ajoutez un document Microsoft Word, un classeur Excel et un document PDF en tant qu'objets OLE sur la première feuille.

|**Document de modèle avec des objets OLE (OleFile.xls)**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

Ensuite, extrayez les objets OLE et sauvegardez-les sur le disque dur avec leurs types de fichiers respectifs.

### **Téléchargez et installez Aspose.Cells**

1. [Télécharger Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp).
1. Installez-le sur votre ordinateur de développement.

Tous les composants Aspose, une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et n'injecte que des filigranes dans les documents produits.

### **Créer un projet**

Démarrez **Visual Studio** et créez une nouvelle application console. Cet exemple montrera une application console C++.

1. Ajouter des références
   1. Ajoutez une référence au composant Aspose.Cells dans votre projet, par exemple, ajoutez une référence à ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll.

### **Extraire des objets OLE**

Le code ci-dessous effectue le travail réel de recherche et d'extraction des objets OLE. Les objets OLE (fichiers DOC, XLS, et PDF) sont enregistrés sur le disque.

```cpp
#include <iostream>
#include <fstream>
#include <memory>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the template file
    Workbook workbook(srcDir + u"oleFile.xlsx");

    // Get the OleObject Collection in the first worksheet
    OleObjectCollection oles = workbook.GetWorksheets().Get(0).GetOleObjects();

    // Loop through all the oleobjects and extract each object in the worksheet
    for (int i = 0; i < oles.GetCount(); i++)
    {
        OleObject ole = oles.Get(i);

        // Specify the output filename
        U16String fileName = srcDir + u"outOle" + U16String(std::to_string(i).c_str()) + u".";

        // Specify each file format based on the oleobject format type
        switch (ole.GetFileFormatType())
        {
            case FileFormatType::Doc:
                fileName += u"doc";
                break;
            case FileFormatType::Excel97To2003:
                fileName += u"Xlsx";
                break;
            case FileFormatType::Ppt:
                fileName += u"Ppt";
                break;
            case FileFormatType::Pdf:
                fileName += u"Pdf";
                break;
            case FileFormatType::Unknown:
                fileName += u"Jpg";
                break;
            default:
                // Handle other formats if needed
                break;
        }

        // Save the oleobject as a new excel file if the object type is xls
        if (ole.GetFileFormatType() == FileFormatType::Xlsx)
        {
            Vector<uint8_t> objectData = ole.GetObjectData();
            if (objectData.GetLength() > 0)
            {
                Workbook oleBook(objectData);
                oleBook.GetSettings().SetIsHidden(false);
                oleBook.Save(srcDir + u"outOle" + U16String(std::to_string(i).c_str()) + u".out.xlsx");
            }
        }
        // Create the files based on the oleobject format types
        else
        {
            Vector<uint8_t> objectData = ole.GetObjectData();
            if (objectData.GetLength() > 0)
            {
                std::ofstream fs(fileName.ToUtf8().c_str(), std::ios::binary);
                fs.write(reinterpret_cast<const char*>(objectData.GetData()), objectData.GetLength());
                fs.close();
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
