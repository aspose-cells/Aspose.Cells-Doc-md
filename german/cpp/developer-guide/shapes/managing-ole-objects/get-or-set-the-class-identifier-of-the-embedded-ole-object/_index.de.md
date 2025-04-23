---
title: Klassen Identifikator des eingebetteten OLE Objekts mit C++ abrufen oder festlegen
linktitle: Abrufen oder Festlegen des Klassenbezeichners des eingebetteten OLE Objekts
type: docs
weight: 200
url: /de/cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: Lernen Sie, wie Sie den Klassen Identifikator von eingebetteten OLE Objekten mit Aspose.Cells und C++ abrufen oder festlegen.
---

## **Mögliche Verwendungsszenarien**
Aspose.Cells bietet die Eigenschaft [OleObject.GetClassIdentifier()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getclassidentifier/), mit der Sie den Klassen-Identifikator des eingebetteten OLE-Objekts abrufen oder festlegen können. OLE-Objektklassen-Identifikatoren sind tatsächlich GUIDs, also Globally Unique Identifiers. GUIDs sind immer 16 Bytes lang, daher sind Klassen-Identifikatoren ebenfalls 16 Bytes lang. Sie werden häufig im Windows-Registrierungseditor gefunden und liefern Informationen an die Host-Anwendung, wie eingebettete OLE-Objekte geöffnet werden sollen, die verschiedene eingebettete Ressourcen enthalten.

## **Abrufen oder Festlegen des Klassenbezeichners des eingebetteten OLE-Objekts**
Der folgende Screenshot zeigt den Klassen-Identifikator des OLE-Objekts, also die GUID, die aus der [Beispiel-Excel-Datei](5115190.xls) mit dem eingebetteten PowerPoint-OLE-Objekt gelesen wurde.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **Beispielcode**
Bitte sehen Sie sich den folgenden Beispielcode an, der mit der [Beispiel-Excel-Datei](5115190.xls) ausgeführt wird, und die Konsolenausgabe, die den Klassen-Identifikator des OLE-Objekts, also die GUID, druckt. Die gedruckte GUID ist genau die gleiche wie im Screenshot gezeigt.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include <guiddef.h>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook wb(srcDir + u"sample.xls");
    Worksheet ws = wb.GetWorksheets().Get(0);
    OleObject oleObj = ws.GetOleObjects().Get(0);

    Vector<uint8_t> classIdentifier = oleObj.GetClassIdentifier();
    GUID guid;
    memcpy(&guid, classIdentifier.GetData(), sizeof(GUID));

    char guidStr[39];
    snprintf(guidStr, sizeof(guidStr), "{%08X-%04X-%04X-%02X%02X-%02X%02X%02X%02X}",
             guid.Data1, guid.Data2, guid.Data3,
             guid.Data4[0], guid.Data4[1], guid.Data4[2], guid.Data4[3],
             guid.Data4[4], guid.Data4[5], guid.Data4[6], guid.Data4[7]);

    std::cout << guidStr << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Konsolenausgabe**
Dies ist die Konsolenausgabe des obigen Beispielscodes, wenn er mit der [Beispiel-Excel-Datei](5115190.xls) ausgeführt wird.

{{< highlight java >}}
DC020317-E6E2-4A62-B9FA-B3EFE16626F4
{{< /highlight >}}
