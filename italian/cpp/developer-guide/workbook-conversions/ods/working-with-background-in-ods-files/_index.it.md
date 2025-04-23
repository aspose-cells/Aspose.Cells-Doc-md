---
title: Lavorare con lo sfondo nei file ODS con C++
linktitle: Lavorare con lo sfondo nei file ODS
type: docs
weight: 150
url: /it/cpp/working-with-background-in-ods-files/
description: Impara come gestire sfondi colorati e grafici nei file ODS usando Aspose.Cells con C++.
---

## **Sfondo nei file ODS**

Lo sfondo può essere aggiunto ai fogli dei file ODS. Lo sfondo può essere di colore o grafico. Lo sfondo non è visibile quando il file è aperto ma se il file viene stampato come PDF, lo sfondo è visibile nel PDF generato. Lo sfondo è anche visibile nella visualizzazione anteprima di stampa.

Aspose.Cells fornisce la capacità di leggere le informazioni di sfondo e aggiungere lo sfondo nei file ODS.

## **Leggi informazioni di sfondo dal file ODS**

Aspose.Cells fornisce la classe [**OdsPageBackground**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/odspagebackground/) per gestire lo sfondo nei file ODS. Il seguente esempio di codice mostra l'uso della classe [**OdsPageBackground**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/odspagebackground/) caricando il file [source ODS](90112030.ods) e leggendo le informazioni sullo sfondo. Consulta l'output della console generato dal codice come riferimento.

### **Codice di Esempio**

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

### **Output della console**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **Aggiungere uno sfondo colorato al file ODS**

Aspose.Cells fornisce la classe [**OdsPageBackground**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/odspagebackground/) per gestire lo sfondo nei file ODS. Il seguente esempio di codice dimostra l'uso della proprietà [**OdsPageBackground.Color**](https://reference.aspose.com/cells/cpp/aspose.cells/color/) per aggiungere uno sfondo colorato al file ODS. Consulta il file [output ODS](90112031.ods) generato dal codice come riferimento.

### **Codice di Esempio**

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

## **Aggiungere uno sfondo grafico al file ODS**

Aspose.Cells fornisce la classe [**OdsPageBackground**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/odspagebackground/) per gestire lo sfondo nei file ODS. Il seguente esempio di codice dimostra l'uso della proprietà [**OdsPageBackground.GetGraphicData()**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/odspagebackground/getgraphicdata/) per aggiungere uno sfondo grafico al file ODS. Consulta il file [output ODS](90112030.ods) generato dal codice come riferimento.

### **Codice di Esempio**

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
