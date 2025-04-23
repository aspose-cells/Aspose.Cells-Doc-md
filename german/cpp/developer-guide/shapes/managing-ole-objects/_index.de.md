---
title: Verwalten von OLE Objekten mit C++
linktitle: Verwaltung von OLE Objekten
type: docs
weight: 50
url: /de/cpp/managing-ole-objects/
description: Lernen Sie, wie Sie OLE Objekte in Arbeitsblättern mithilfe von Aspose.Cells mit C++ hinzufügen, extrahieren und verwalten.
---

## **Einführung**

OLE (Object Linking and Embedding) ist Microsofts Rahmenwerk für eine Compound-Dokumententechnologie. Kurz gesagt ist ein Compound-Dokument etwas Ähnliches wie ein Anzeigebereich, der visuelle und Informationsobjekte aller Art enthalten kann: Text, Kalender, Animationen, Ton, Bewegtbilder, 3D, ständig aktualisierte Nachrichten, Steuerungen und so weiter. Jedes Anzeigebereichsobjekt ist eine unabhängige Programm-Entität, die mit einem Benutzer interagieren und auch mit anderen Objekten auf dem Anzeigebereich kommunizieren kann.

OLE (Object Linking and Embedding) wird von vielen verschiedenen Programmen unterstützt und dient dazu, Inhalte, die in einem Programm erstellt wurden, in einem anderen verfügbar zu machen. Sie können beispielsweise ein Microsoft Word-Dokument in Microsoft Excel einfügen. Um zu sehen, welche Arten von Inhalten Sie einfügen können, klicken Sie auf **Objekt** im **Einfügen**-Menü. Nur Programme, die auf dem Computer installiert sind und OLE-Objekte unterstützen, erscheinen im **Objekttyp**-Feld.

### **Einfügen von OLE-Objekten in das Arbeitsblatt**

Aspose.Cells unterstützt das Hinzufügen, Extrahieren und Verwalten von OLE-Objekten in Arbeitsblättern. Zu diesem Zweck enthält Aspose.Cells die [**OleObjectCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobjectcollection/)-Klasse, die verwendet wird, um ein neues OLE-Objekt zur Sammlungsliste hinzuzufügen. Eine andere Klasse, [**OleObject**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/), stellt ein OLE-Objekt dar. Sie besitzt einige wichtige Mitglieder:

- Die [**ImageData**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getimagedata/)-Eigenschaft gibt die Bild- (Symbol-) Daten vom Typ Byte-Array an. Das Bild wird angezeigt, um das OLE-Objekt im Arbeitsblatt zu zeigen.
- Die [**ObjectData**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/)-Eigenschaft gibt die Objekt-Daten in Form eines Byte-Arrays an. Diese Daten werden in ihrem zugehörigen Programm angezeigt, wenn Sie doppelt auf das OLE-Objekt-Icon klicken.

Das folgende Beispiel zeigt, wie man OLE-Objekte in ein Arbeitsblatt einfügt.

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

### **Extrahieren von OLE-Objekten in der Arbeitsmappe**

Das folgende Beispiel zeigt, wie man OLE-Objekte in einer Arbeitsmappe extrahiert. Das Beispiel erhält verschiedene OLE-Objekte aus einer vorhandenen XLS-Datei und speichert verschiedene Dateien (DOC, XLS, PPT, PDF usw.) basierend auf dem Dateiformattyp des OLE-Objekts.

Nachdem der Code ausgeführt wurde, können wir verschiedene Dateien basierend auf ihren jeweiligen OLE-Objektformattypen speichern.

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

### **Extrahieren eingebetteter MOL-Datei**

Aspose.Cells unterstützt das Extrahieren von Objekten ungewöhnlicher Typen wie MOL (Molekül-Daten-Datei, die Informationen über Atome und Bindungen enthält). Das folgende Codesnippet zeigt das Extrahieren einer eingebetteten MOL-Datei und das Speichern auf der Festplatte mit dieser [Beispiel-Excel-Datei](94896196.xlsx).

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

## **Fortgeschrittene Themen**
- [Auf das Anzeigen des verknüpften Ole-Objekts zugreifen und es ändern](/cells/de/cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [OLE-Objekt automatisch über Microsoft Excel aktualisieren mit Aspose.Cells](/cells/de/cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Extrahieren Sie OLE-Objekte aus der Arbeitsmappe](/cells/de/cpp/extract-ole-objects-from-workbook/)
- [Abrufen oder Festlegen des Klassenbezeichners des eingebetteten OLE-Objekts](/cells/de/cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Einfügen einer WAV-Datei als OLE-Objekt](/cells/de/cpp/inserting-a-wav-file-as-an-ole-object/)
