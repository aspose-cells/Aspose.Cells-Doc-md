---
title: Använd WorkbookMetadata med C++
linktitle: Arbetsboksmetadata 
type: docs
weight: 320
url: /sv/cpp/using-workbookmetadata/
description: Lär dig hur du använder WorkbookMetadata för att redigera anpassade dokumentegenskaper för ett arbetsdokument i C++ med Aspose.Cells.
---

{{% alert color="primary" %}}

Aspose.Cells låter dig ladda en lättviktig version av en arbetsbok i minnet för att redigera dess metadata. Använd [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/) klassen för att ladda arbetsboken.

{{% /alert %}}

Följande exempel använder [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/) klassen för att redigera anpassade dokumentegenskaper i en arbetsbok. När du har öppnat arbetsboken med [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)-klassen kan du läsa dokumentegenskaperna. Här är ett exempel på kod med [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/)-klassen.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Metadata;
using namespace Aspose::Cells::Properties;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    MetadataOptions options(MetadataType::Document_Properties);
    WorkbookMetadata meta(srcDir + u"Sample1.xlsx", options);

    meta.GetCustomDocumentProperties().Add(u"test", u"test");

    meta.Save(srcDir + u"Sample2.out.xlsx");

    Workbook w(srcDir + u"Sample2.out.xlsx");

    std::cout << w.GetCustomDocumentProperties().Get(u"test").ToString().ToUtf8() << std::endl;

    std::cout << "Press any key to continue..." << std::endl;
    std::cin.get();

    Aspose::Cells::Cleanup();
}
```
