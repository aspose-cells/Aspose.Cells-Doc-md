---
title: Einfügen einer WAV Datei als Ole Objekt mit C++
linktitle: Einbinden einer WAV Datei als Ole Objekt
type: docs
weight: 70
url: /de/cpp/inserting-a-wav-file-as-an-ole-object/
description: Lernen Sie, wie Sie eine WAV Datei als OLE Objekt in Excel Tabellen mit Aspose.Cells und C++ einfügen.
---

{{% alert color="primary" %}} 

Aspose.Cells bietet die Funktionalität, verschiedene Arten von OLE-Objekten zu Excel-Tabellen hinzuzufügen. Wir werden in den folgenden Codebeispielen sehen, wie man eine WAV-Datei als OLE-Objekt mit den einfachen APIs von Aspose.Cells hinzufügt. 

{{% /alert %}} 

```c++
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String imageUrl = srcDir + u"image2.jpg";

    std::ifstream imageStream(imageUrl.ToUtf8(), std::ios::binary);
    if (!imageStream.is_open()) {
        std::cerr << "Failed to open image file." << std::endl;
        return -1;
    }

    imageStream.seekg(0, std::ios::end);
    std::vector<uint8_t> imageData(imageStream.tellg());
    imageStream.seekg(0, std::ios::beg);
    imageStream.read(reinterpret_cast<char*>(imageData.data()), imageData.size());
    imageStream.close();

    Aspose::Cells::Vector<uint8_t> aspImageData(imageData.data(), imageData.size());

    U16String path = srcDir + u"chord.wav";

    std::ifstream wavStream(path.ToUtf8(), std::ios::binary);
    if (!wavStream.is_open()) {
        std::cerr << "Failed to open WAV file." << std::endl;
        return -1;
    }

    wavStream.seekg(0, std::ios::end);
    std::vector<uint8_t> objectData(wavStream.tellg());
    wavStream.seekg(0, std::ios::beg);
    wavStream.read(reinterpret_cast<char*>(objectData.data()), objectData.size());
    wavStream.close();

    Aspose::Cells::Vector<uint8_t> aspObjectData(objectData.data(), objectData.size());

    int intIndex = 0;

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    sheet.GetOleObjects().Add(14, 3, 200.0, 220.0, aspImageData);
    workbook.GetWorksheets().Get(0).GetOleObjects().Get(intIndex).SetFileFormatType(FileFormatType::Unknown);
    workbook.GetWorksheets().Get(0).GetOleObjects().Get(intIndex).SetObjectData(aspObjectData);
    workbook.GetWorksheets().Get(0).GetOleObjects().Get(intIndex).SetObjectSourceFullName(path);

    workbook.Save(outDir + u"testWAV.out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
