---
title: OLE Objekte aus Arbeitsmappe mit C++ extrahieren
linktitle: OLE Objekte aus Arbeitsmappe extrahieren
type: docs
weight: 110
url: /de/cpp/extract-ole-objects-from-workbook/
description: Lernen Sie, wie Sie OLE Objekte aus einer Arbeitsmappe mit Aspose.Cells und C++ extrahieren.
---

{{% alert color="primary" %}}

Manchmal müssen Sie OLE-Objekte aus einer Arbeitsmappe extrahieren. Aspose.Cells unterstützt das Extrahieren und Speichern dieser OLE-Objekte.

Dieser Artikel zeigt, wie Sie eine Konsolenanwendung in Visual Studio erstellen und verschiedene OLE-Objekte aus einer Arbeitsmappe mit wenigen Codezeilen extrahieren.

{{% /alert %}}

## **OLE-Objekte aus einer Arbeitsmappe extrahieren**

### **Erstellen einer Vorlagearbeitsmappe**

1. Erstellen Sie ein Arbeitsbuch in Microsoft Excel.
1. Fügen Sie ein Microsoft Word-Dokument, ein Excel-Arbeitsbuch und ein PDF-Dokument als OLE-Objekte auf das erste Arbeitsblatt ein.

|**Vorlagendokument mit OLE-Objekten (OleFile.xls)**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

 Als nächstes extrahieren Sie die OLE-Objekte und speichern sie mit ihren jeweiligen Dateitypen auf der Festplatte.

### **Aspose.Cells herunterladen und installieren**

 1. [Laden Sie Aspose.Cells for C++ herunter](https://downloads.aspose.com/cells/cpp).
1. Installieren Sie es auf Ihrem Entwicklungscomputer.

Alle Aspose-Komponenten arbeiten im Evaluierungsmodus, wenn sie installiert sind. Der Evaluierungsmodus hat kein Zeitlimit und fügt nur Wasserzeichen in erstellte Dokumente ein.

### **Ein Projekt erstellen**

Starten Sie **Visual Studio** und erstellen Sie eine neue Konsolenanwendung. Dieses Beispiel zeigt eine C++-Konsolenanwendung.

1. Verweise hinzufügen
   1. Fügen Sie Ihrem Projekt eine Referenz zur Aspose.Cells-Komponente hinzu, z.B. fügen Sie eine Referenz zu ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll hinzu.

### **OLE-Objekte extrahieren**

Der unten stehende Code führt die eigentliche Arbeit beim Finden und Extrahieren von OLE-Objekten aus. Die OLE-Objekte (DOC, XLS und PDF Dateien) werden auf die Festplatte gespeichert.

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
