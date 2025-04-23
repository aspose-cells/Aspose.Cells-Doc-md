---
title: Fügen Sie benutzerdefinierte XML Parts hinzu und wählen Sie sie nach ID mit C++ aus
linktitle: Benutzerdefinierte XML Teile hinzufügen und nach ID auswählen
type: docs
weight: 70
url: /de/cpp/add-custom-xml-parts-and-select-them-by-id/
description: Lernen Sie, wie Sie benutzerdefinierte XML Parts in Excel Dateien mit Aspose.Cells in C++ hinzufügen und auswählen.
---

## **Mögliche Verwendungsszenarien**

Benutzerdefinierte XML-Parts sind XML-Daten, die in Microsoft Excel-Dokumenten gespeichert werden und von Anwendungen genutzt werden, die mit ihnen interagieren. Derzeit gibt es keine direkte Möglichkeit, sie mit der Microsoft Excel-Benutzeroberfläche hinzuzufügen. Sie können sie jedoch programmatisch auf verschiedene Weisen hinzufügen, z.B. mit VSTO oder Aspose.Cells. Verwenden Sie die [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/add/)-Methode, um einen benutzerdefinierten XML-Teil mit der API von Aspose.Cells hinzuzufügen. Sie können auch seine ID mit der [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/)-Eigenschaft festlegen. Wenn Sie einen benutzerdefinierten XML-Teil nach ID auswählen möchten, können Sie die [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/)-Methode verwenden.

## **Benutzerdefinierte XML-Teile hinzufügen und nach ID auswählen**

Der folgende Beispielcode fügt zunächst vier benutzerdefinierte XML-Parts mit der [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/add/)-Methode hinzu. Dann setzt er ihre IDs mit der [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/)-Eigenschaft. Schließlich findet oder wählt er einen der hinzugefügten benutzerdefinierten XML-Parts mit der [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/)-Methode. Bitte sehen Sie sich auch die Konsolenausgabe des unten angegebenen Codes zur Referenz an.

## **Beispielcode**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Markup;

int main()
{
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Some data in the form of byte array
    // Please use correct XML and Schema instead
    Vector<uint8_t> btsData = { 1, 2, 3 };
    Vector<uint8_t> btsSchema = { 1, 2, 3 };

    // Create four custom xml parts
    wb.GetCustomXmlParts().Add(btsData, btsSchema);
    wb.GetCustomXmlParts().Add(btsData, btsSchema);
    wb.GetCustomXmlParts().Add(btsData, btsSchema);
    wb.GetCustomXmlParts().Add(btsData, btsSchema);

    // Assign ids to custom xml parts
    wb.GetCustomXmlParts().Get(0).SetID(u"Fruit");
    wb.GetCustomXmlParts().Get(1).SetID(u"Color");
    wb.GetCustomXmlParts().Get(2).SetID(u"Sport");
    wb.GetCustomXmlParts().Get(3).SetID(u"Shape");

    // Specify search custom xml part id
    U16String srchID = u"Fruit";
    srchID = u"Color";
    srchID = u"Sport";

    // Search custom xml part by the search id
    CustomXmlPart cxp = wb.GetCustomXmlParts().SelectByID(srchID);

    // Print the found or not found message on console
    if (cxp.IsNull())
    {
        std::cout << "Not Found: CustomXmlPart ID " << srchID.ToUtf8() << std::endl;
    }
    else
    {
        std::cout << "Found: CustomXmlPart ID " << srchID.ToUtf8() << std::endl;
    }

    std::cout << "AddCustomXMLPartsAndSelectThemByID executed successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Konsolenausgabe**

{{< highlight java >}}
Found: CustomXmlPart ID Sport
{{< /highlight >}}
