---
title: Lägga till anpassade egenskaper som är synliga i Dokumentinformation panelen med C++
linktitle: Lägga till anpassade egenskaper som är synliga i dokumentinformationspanelen
type: docs
weight: 300
url: /sv/cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Lär dig att lägga till anpassade egenskaper som syns i Dokumentinformation panelen med Aspose.Cells och C++.
---

## **Lägga till anpassade egenskaper synliga inuti dokumentinformationspanelen**

Aspose.Cells kan användas för att lägga till anpassade egenskaper i arbetsboksobjektet som är synliga i dokumentinformationspanelen. Du kan öppna dokumentinformationspanelen i Microsoft Excel med hjälp av menyn Fil > Information > Egenskaper > Visa dokumentpanelkommandon.

Använd [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/)-metoden för att lägga till en anpassad egenskap som syns i Dokumentinformation-panelen.

Följande exempel kod lägger till två anpassade egenskaper. Den första egenskapen saknar typ och den andra är av typen DateTime. När du öppnar den genererade Excel-filen kommer du att se dessa två egenskaper i Dokumentinformation-panelen.

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

### **Relaterad artikel**

{{% alert color="primary" %}}

- [Använd anpassade XML-delsar i Aspose.Cells](/cells/sv/cpp/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
