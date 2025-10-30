---
title: Hinzufügen benutzerdefinierter Eigenschaften, die im Dokumentinformationen Panel sichtbar sind, mit C++
linktitle: Hinzufügen von benutzerdefinierten Eigenschaften, die im Dokumentinformationsfeld sichtbar sind
type: docs
weight: 300
url: /de/cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Erfahren Sie, wie Sie mit Aspose.Cells und C++ benutzerdefinierte Eigenschaften hinzufügen, die im Dokumentinformationen Panel sichtbar sind.
---

## **Hinzufügen von benutzerdefinierten Eigenschaften, die im Dokumentinformationsfeld sichtbar sind**

Aspose.Cells kann verwendet werden, um benutzerdefinierte Eigenschaften im Arbeitsmappenobjekt hinzuzufügen, die im Dokumentinformationsfeld sichtbar sind. Sie können das Dokumentinformationsfeld in Microsoft Excel über die Befehle Datei > Informationen > Eigenschaften > Dokumentinformationsfeld anzeigen öffnen.

Bitte verwenden Sie die [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/)-Methode, um eine benutzerdefinierte Eigenschaft hinzuzufügen, die im Dokumentinformationsbereich sichtbar ist.

Der folgende Beispielcode fügt zwei benutzerdefinierte Eigenschaften hinzu. Die erste Eigenschaft hat keinen Typ, die zweite Eigenschaft hat den Typ DateTime. Sobald Sie die Ausgabedatei im Excel öffnen, die mit diesem Code generiert wurde, sehen Sie diese beiden Eigenschaften im Dokumentinformationsbereich.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object with specified format
    Workbook workbook(FileFormatType::Xlsx);

    // Add simple property without any type
    workbook.GetContentTypeProperties().Add(u"MK31", u"Simple Data");

    // Add date time property with type
    workbook.GetContentTypeProperties().Add(u"MK32", u"04-Mar-2015", u"DateTime");

    // Save the workbook
    workbook.Save(srcDir + u"AddingCustomPropertiesVisible_out.xlsx");

    std::cout << "Custom properties added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Verwandter Artikel**

{{% alert color="primary" %}}

- [Verwendung von benutzerdefinierten XML-Teilen in Aspose.Cells](/cells/de/cpp/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
