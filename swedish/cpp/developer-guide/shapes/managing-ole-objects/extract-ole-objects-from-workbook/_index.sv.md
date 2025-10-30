---
title: Extrahera OLE objekt från arbetsbok med C++
linktitle: Extrahera OLE objekt från arbetsboken
type: docs
weight: 110
url: /sv/cpp/extract-ole-objects-from-workbook/
description: Lär dig hur man extraherar OLE objekt från en arbetsbok med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Ibland behöver du extrahera OLE-objekt från en arbetsbok. Aspose.Cells stöder att extrahera och spara dessa OLE-objekt.

Denna artikel visar hur man skapar en konsolapplikation i Visual Studio och extraherar olika OLE-objekt från en arbetsbok med några enkla kodrader.

{{% /alert %}}

## **Extrahera OLE-objekt från en arbetsbok**

### **Skapa en mallarbok**

1. Skapa en arbetsbok i Microsoft Excel.
1. Lägg till ett Microsoft Word-dokument, en Excel-arbetsbok och ett PDF-dokument som OLE-objekt på det första arbetsbladet.

|**Mall-dokument med OLE-objekt (OleFile.xls)**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

Nästa steg, extrahera OLE-objekten och spara dem på hårddisken med respektive filtyper.

### **Ladda ner och installera Aspose.Cells**

1. [Ladda ner Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp).
1. Installera det på din utvecklingsdator.

Alla Aspose-komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och det injicerar endast vattenstämplar i producerade dokument.

### **Skapa ett projekt**

Starta **Visual Studio** och skapa en ny konsolapplikation. Detta exempel visar en C++-konsolapplikation.

1. Lägg till referenser
   1. Lägg till en referens till Aspose.Cells-komponenten i ditt projekt, till exempel, lägg till en referens till ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll.

### **Extrahera OLE-objekt**

Koden nedan utför det faktiska arbetet med att hitta och extrahera OLE-objekt. OLE-objekten (DOC, XLS och PDF-filer) sparas på disken.

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
{{< app/cells/assistant language="cpp" >}}
