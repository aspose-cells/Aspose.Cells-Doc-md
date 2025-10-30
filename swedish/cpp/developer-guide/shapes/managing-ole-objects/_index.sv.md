---
title: Hantera OLE objekt med C++
linktitle: Hantera OLE objekt
type: docs
weight: 50
url: /sv/cpp/managing-ole-objects/
description: Lär dig hur du lägger till, extraherar och manipulerar OLE objekt i blad med Aspose.Cells med C++.
---

## **Introduktion**

OLE (Object Linking and Embedding) är Microsofts ramverk för en sammanfogande dokumentteknik. Kort sagt är en sammanfogande dokument något som en visnings- skrivbord som kan innehålla visuella och informationsobjekt av alla slag: text, kalendrar, animationer, ljud, rörlig video, 3D, löpande uppdaterade nyheter, kontroller och så vidare. Varje skrivbordsobjekt är en oberoende programenhet som kan interagera med en användare och också kommunicera med andra objekt på skrivbordet.

OLE (Object Linking and Embedding) stöds av många olika program och används för att göra innehåll skapat i ett program tillgängligt i ett annat. Till exempel kan du infoga ett Microsoft Word-dokument i Microsoft Excel. För att se vilka typer av innehåll du kan infoga, klicka på **Object** i **Infoga**-menyn. Endast program som är installerade på datorn och som stöder OLE-objekt visas i rutan **Objekttyp**.

### **Infoga OLE-objekt i arbetsbladet**

Aspose.Cells stöder tillägg, extrahering och manipulation av OLE-objekt i kalkylblad. Av denna anledning har Aspose.Cells klassen [**OleObjectCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobjectcollection/), som används för att lägga till ett nytt OLE-objekt till listan. En annan klass, [**OleObject**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/), representerar ett OLE-objekt. Den har några viktiga medlemmar:

- Egenskapen [**ImageData**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getimagedata/) specificerar bild (ikonen) data av typ byte-array. Bilden kommer att visas för att visa OLE-objektet i kalkbladet.
- Egenskapen [**ObjectData**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/) specificerar objektets data i form av en byte-array. Denna data kommer att visas i det relaterade programmet när du dubbelklickar på OLE-objektets ikon.

Följande exempel visar hur man lägger till en OLE-objekt/-objekt i ett arbetsblad.

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

### **Extrahera OLE-objekt i arbetsboken**

Följande exempel visar hur man extraherar OLE-objekt i en arbetsbok. Exemplet hämtar olika OLE-objekt från en befintlig XLS-fil och sparar olika filer (DOC, XLS, PPT, PDF etc.) baserat på OLE-objektets filformatstyp.

Efter att ha kört koden kan vi spara olika filer baserat på deras respektive OLE-objektets format.

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

### **Extrahera inbäddad MOL-fil**

Aspose.Cells stöder att extrahera objekt av ovanliga typer som MOL (Molekylär datfil som innehåller information om atomer och bindningar). Följande kodutdrag demonstrerar att extrahera en inbäddad MOL-fil och spara den på disken med hjälp av denna [exempel Excel-fil](94896196.xlsx).

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

## **Avancerade ämnen**
- [Åtkomst och ändring av visningsmärket för det länkade OLE-objektet](/cells/sv/cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Automatisk uppdatering av OLE-objekt via Microsoft Excel med Aspose.Cells](/cells/sv/cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Extrahera OLE-objekt från arbetsboken](/cells/sv/cpp/extract-ole-objects-from-workbook/)
- [Hämta eller ange klassidentifieraren för det inbäddade OLE-objektet](/cells/sv/cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Infoga en WAV-fil som ett Ole-objekt](/cells/sv/cpp/inserting-a-wav-file-as-an-ole-object/)
{{< app/cells/assistant language="cpp" >}}
