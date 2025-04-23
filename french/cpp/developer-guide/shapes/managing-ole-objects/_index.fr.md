---
title: Gestion des objets OLE avec C++
linktitle: Gestion des objets OLE
type: docs
weight: 50
url: /fr/cpp/managing-ole-objects/
description: Apprenez comment ajouter, extraire et manipuler des objets OLE dans des feuilles de calcul à l aide d Aspose.Cells avec C++.
---

## **Introduction**

OLE (Object Linking and Embedding) est le cadre de Microsoft pour une technologie de document composé. En bref, un document composé est quelque chose comme un bureau d'affichage qui peut contenir des objets visuels et d'information de toutes sortes : texte, calendriers, animations, son, vidéo en mouvement, 3D, actualités continuellement mises à jour, contrôles, etc. Chaque objet de bureau est une entité de programme indépendante qui peut interagir avec un utilisateur et communiquer avec d'autres objets sur le bureau.

OLE (Object Linking and Embedding) est pris en charge par de nombreux programmes différents et est utilisé pour rendre le contenu créé dans un programme disponible dans un autre. Par exemple, vous pouvez insérer un document Microsoft Word dans Microsoft Excel. Pour voir quels types de contenus vous pouvez insérer, cliquez sur **Objet** dans le menu **Insérer**. Seuls les programmes installés sur l'ordinateur et prenant en charge les objets OLE apparaissent dans la zone **Type d'objet**.

### **Insertion d'objets OLE dans la feuille de calcul**

Aspose.Cells prend en charge l'ajout, l'extraction et la manipulation d'objets OLE dans les feuilles de calcul. Pour cette raison, Aspose.Cells possède la classe [**OleObjectCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobjectcollection/), utilisée pour ajouter un nouvel Objet OLE à la liste de collection. Une autre classe, [**OleObject**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/), représente un objet OLE. Elle possède quelques membres importants :

- La propriété [**ImageData**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getimagedata/) spécifie les données d'image (icône) de type tableau d'octets. L'image sera affichée pour montrer l'objet OLE dans la feuille de calcul.
- La propriété [**ObjectData**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/) spécifie les données de l'objet sous forme de tableau d'octets. Ces données seront affichées dans leur programme associé lors d'un double-clic sur l'icône de l'objet OLE.

L'exemple suivant montre comment ajouter un ou des objets OLE dans une feuille de calcul.

```c++
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

std::vector<uint8_t> ReadFileToVector(const U16String& filePath) {
    std::ifstream file(filePath.ToUtf8(), std::ios::binary | std::ios::ate);
    if (!file) return {};
    std::streamsize size = file.tellg();
    file.seekg(0, std::ios::beg);
    std::vector<uint8_t> buffer(size);
    if (size > 0)
        file.read(reinterpret_cast<char*>(buffer.data()), size);
    return buffer;
}

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    U16String imagePath = srcDir + u"logo.jpg";
    std::vector<uint8_t> imageData = ReadFileToVector(imagePath);

    U16String objectPath = srcDir + u"book1.xls";
    std::vector<uint8_t> objectData = ReadFileToVector(objectPath);
    Vector<uint8_t> data(objectData.data(), static_cast<int32_t>(objectData.size()));
    sheet.GetOleObjects().Add(14, 3, 200, 220, data);
    if (sheet.GetOleObjects().GetCount() > 0) {
        sheet.GetOleObjects().Get(0).SetObjectData(data);
    }

    workbook.Save(outDir + u"output.out.xls");
    std::cout << "OLE object added successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Extraction d'objets OLE dans le classeur**

L'exemple suivant montre comment extraire des objets OLE dans un classeur. L'exemple récupère différents objets OLE à partir d'un fichier XLS existant et enregistre différents fichiers (DOC, XLS, PPT, PDF, etc.) en fonction du type de format de fichier de l'objet OLE.

Après l'exécution du code, nous pouvons enregistrer différents fichiers en fonction de leurs types de format respectifs des objets OLE.

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the template file
    Workbook workbook(srcDir + u"book1.xls");

    // Get the OleObject Collection in the first worksheet
    OleObjectCollection oles = workbook.GetWorksheets().Get(0).GetOleObjects();

    // Loop through all the oleobjects and extract each object
    for (int32_t i = 0; i < oles.GetCount(); i++)
    {
        OleObject ole = oles.Get(i);

        // Specify the output filename
        U16String fileName = srcDir + u"ole_" + U16String(std::to_string(i).c_str()) + u".";

        // Specify each file format based on the oleobject format type
        switch (ole.GetFileFormatType())
        {
        case FileFormatType::Doc:
            fileName += u"doc";
            break;
        case FileFormatType::Xlsx:
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
            Workbook oleBook(objectData);
            oleBook.GetSettings().SetIsHidden(false);
            oleBook.Save(srcDir + u"Excel_File" + U16String(std::to_string(i).c_str()) + u".out.xlsx");
        }
        else
        {
            // Create the files based on the oleobject format types
            std::ofstream fs(fileName.ToUtf8().c_str(), std::ios::binary);
            Vector<uint8_t> objectData = ole.GetObjectData();
            fs.write(reinterpret_cast<const char*>(objectData.GetData()), objectData.GetLength());
            fs.close();
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Extraction des fichiers MOL intégrés**

Aspose.Cells permet d'extraire des objets de types peu courants comme MOL (fichier de données moléculaires contenant des informations sur les atomes et les liaisons). Le code suivant montre comment extraire un fichier MOL incorporé et le sauvegarder sur le disque en utilisant ce [fichier Excel d'exemple](94896196.xlsx).

```c++
#include <iostream>
#include <fstream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"EmbeddedMolSample.xlsx");

    int index = 1;

    WorksheetCollection sheets = workbook.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); i++)
    {
        Worksheet sheet = sheets.Get(i);
        OleObjectCollection oles = sheet.GetOleObjects();

        for (int j = 0; j < oles.GetCount(); j++)
        {
            OleObject ole = oles.Get(j);

            std::wstring indexWStr = std::to_wstring(index);
            U16String fileName = outDir + u"OleObject" + U16String(reinterpret_cast<const char16_t*>(indexWStr.c_str())) + u".mol";

            std::ofstream fs(fileName.ToUtf8(), std::ios::binary);
            if (fs.is_open())
            {
                Vector<uint8_t> objectData = ole.GetObjectData();
                fs.write(reinterpret_cast<const char*>(objectData.GetData()), objectData.GetLength());
                fs.close();
                index++;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sujets avancés**
- [Accéder et modifier l'étiquette d'affichage de l'objet Ole lié](/cells/fr/cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Rafraîchir automatiquement un objet OLE via Microsoft Excel en utilisant Aspose.Cells](/cells/fr/cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Extraire des objets OLE du classeur](/cells/fr/cpp/extract-ole-objects-from-workbook/)
- [Obtenir ou définir l'identifiant de classe de l'objet OLE incorporé](/cells/fr/cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Insérer un fichier WAV en tant qu'objet Ole](/cells/fr/cpp/inserting-a-wav-file-as-an-ole-object/)
