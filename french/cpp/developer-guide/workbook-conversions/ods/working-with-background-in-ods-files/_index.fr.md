---
title: Travailler avec l arrière plan dans les fichiers ODS avec C++
linktitle: Travailler avec l arrière plan dans les fichiers ODS
type: docs
weight: 150
url: /fr/cpp/working-with-background-in-ods-files/
description: Apprenez comment gérer les arrière plans colorés et graphiques dans les fichiers ODS en utilisant Aspose.Cells avec C++.
---

## **Arrière-plan dans les fichiers ODS**

Un arrière-plan peut être ajouté aux feuilles dans les fichiers ODS. L'arrière-plan peut être soit un arrière-plan coloré, soit un arrière-plan graphique. L'arrière-plan n'est pas visible lorsque le fichier est ouvert, mais s'il est imprimé en PDF, l'arrière-plan est visible dans le PDF généré. L'arrière-plan est également visible dans la boîte de dialogue d'aperçu avant impression.

Aspose.Cells permet de lire les informations d'arrière-plan et d'ajouter l'arrière-plan dans les fichiers ODS.

## **Lire les informations d'arrière-plan à partir du fichier ODS**

Aspose.Cells fournit la classe [**OdsPageBackground**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/odspagebackground/) pour gérer l'arrière-plan dans les fichiers ODS. L'exemple de code suivant montre l'utilisation de la classe [**OdsPageBackground**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/odspagebackground/) en chargeant le fichier [source ODS](90112030.ods) et en lisant les informations d'arrière-plan. Veuillez consulter la sortie Console générée par le code en référence.

### **Code d'exemple**

```c++
#include <iostream>
#include <fstream>
#include <codecvt>
#include <locale>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook workbook(srcDir + u"GraphicBackground.ods");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    OdsPageBackground background = worksheet.GetPageSetup().GetODSPageBackground();

    std::cout << "Background Type: " << static_cast<int>(background.GetType()) << std::endl;
    std::cout << "Background Position: " << static_cast<int>(background.GetGraphicPositionType()) << std::endl;

    Vector<uint8_t> graphicData = background.GetGraphicData();
    std::string filePath = (outDir + u"background.jpg").ToUtf8();
    std::ofstream fout(filePath, std::ios::binary);
    fout.write(reinterpret_cast<const char*>(graphicData.GetData()), graphicData.GetLength());
    fout.close();

    std::cout << "Background image saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Sortie console**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **Ajouter un arrière-plan coloré au fichier ODS**

Aspose.Cells fournit la classe [**OdsPageBackground**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/odspagebackground/) pour gérer l'arrière-plan dans les fichiers ODS. L'exemple de code suivant montre l'utilisation de la propriété [**OdsPageBackground.Color**](https://reference.aspose.com/cells/cpp/aspose.cells/color/) pour ajouter un arrière-plan coloré au fichier ODS. Veuillez consulter le fichier [output ODS](90112031.ods) généré par le code en référence.

### **Code d'exemple**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set cell values
    worksheet.GetCells().Get(0, 0).SetValue(1);
    worksheet.GetCells().Get(1, 0).SetValue(2);
    worksheet.GetCells().Get(2, 0).SetValue(3);
    worksheet.GetCells().Get(3, 0).SetValue(4);
    worksheet.GetCells().Get(4, 0).SetValue(5);
    worksheet.GetCells().Get(5, 0).SetValue(6);
    worksheet.GetCells().Get(0, 1).SetValue(7);
    worksheet.GetCells().Get(1, 1).SetValue(8);
    worksheet.GetCells().Get(2, 1).SetValue(9);
    worksheet.GetCells().Get(3, 1).SetValue(10);
    worksheet.GetCells().Get(4, 1).SetValue(11);
    worksheet.GetCells().Get(5, 1).SetValue(12);

    // Access the ODS page background
    OdsPageBackground background = worksheet.GetPageSetup().GetODSPageBackground();

    // Set background color and type
    background.SetColor(Color::Azure());
    background.SetType(OdsPageBackgroundType::Color);

    // Save the workbook
    workbook.Save(outDir + u"ColoredBackground.ods", SaveFormat::Ods);

    std::cout << "Workbook saved successfully with colored background!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Ajouter un arrière-plan graphique au fichier ODS**

Aspose.Cells fournit la classe [**OdsPageBackground**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/odspagebackground/) pour gérer l'arrière-plan dans les fichiers ODS. L'exemple de code suivant montre l'utilisation de la propriété [**OdsPageBackground.GetGraphicData()**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/odspagebackground/getgraphicdata/) pour ajouter un arrière-plan graphique au fichier ODS. Veuillez consulter le fichier [output ODS](90112030.ods) généré par le code en référence.

### **Code d'exemple**

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

Vector<uint8_t> GetDataFromFile(const U16String& file)
{
    std::string f = file.ToUtf8();
    // open a file 
    std::ifstream fileStream(f, std::ios::binary);

    if (!fileStream.is_open()) {
        std::cerr << "Failed to open the file." << std::endl;
        return 1;
    }

    // Get file size
    fileStream.seekg(0, std::ios::end);
    std::streampos fileSize = fileStream.tellg();
    fileStream.seekg(0, std::ios::beg);

    // Read file contents into uint8_t array
    uint8_t* buffer = new uint8_t[fileSize];
    fileStream.read(reinterpret_cast<char*>(buffer), fileSize);
    fileStream.close();

    Vector<uint8_t>data(buffer, fileSize);
    delete[] buffer;

    return data;
}


int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set values in cells
    worksheet.GetCells().Get(0, 0).SetValue(1);
    worksheet.GetCells().Get(1, 0).SetValue(2);
    worksheet.GetCells().Get(2, 0).SetValue(3);
    worksheet.GetCells().Get(3, 0).SetValue(4);
    worksheet.GetCells().Get(4, 0).SetValue(5);
    worksheet.GetCells().Get(5, 0).SetValue(6);
    worksheet.GetCells().Get(0, 1).SetValue(7);
    worksheet.GetCells().Get(1, 1).SetValue(8);
    worksheet.GetCells().Get(2, 1).SetValue(9);
    worksheet.GetCells().Get(3, 1).SetValue(10);
    worksheet.GetCells().Get(4, 1).SetValue(11);
    worksheet.GetCells().Get(5, 1).SetValue(12);

    // Get the ODS page background
    OdsPageBackground background = worksheet.GetPageSetup().GetODSPageBackground();

    // Set background type to graphic
    background.SetType(OdsPageBackgroundType::Graphic);

    // Read the background image file
    Vector<uint8_t> graphicData = GetDataFromFile(U16String(srcDir + u"background.jpg"));

    // Set graphic data and type
    background.SetGraphicData(graphicData);
    background.SetGraphicType(OdsPageBackgroundGraphicType::Area);

    // Save the workbook
    workbook.Save(outDir + u"GraphicBackground.ods", SaveFormat::Ods);

    std::cout << "Graphic background applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
