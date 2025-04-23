---
title: Utilizzando WorkbookMetadata con C++
linktitle: Metadati del foglio di lavoro
type: docs
weight: 320
url: /it/cpp/using-workbookmetadata/
description: Impara come usare WorkbookMetadata per modificare le proprietà personalizzate di un documento in C++ con Aspose.Cells.
---

{{% alert color="primary" %}}

Aspose.Cells permette di caricare una versione leggera di una cartella di lavoro in memoria per modificare le sue informazioni metadata. Si prega di usare la classe [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/) per caricare la cartella di lavoro.

{{% /alert %}}

Il seguente esempio di codice usa la classe [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/) per modificare le proprietà personalizzate di un documento. Una volta aperta la cartella di lavoro usando la classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), sarai in grado di leggere le proprietà del documento. Ecco un esempio di codice usando la classe [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/).

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
