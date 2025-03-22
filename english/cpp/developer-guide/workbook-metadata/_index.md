---
title: Using WorkbookMetadata with C++
linktitle: Workbook Metadata
type: docs
weight: 320
url: /cpp/using-workbookmetadata/
description: Learn how to use WorkbookMetadata to edit custom document properties of a workbook in C++ with Aspose.Cells.
---

{{% alert color="primary" %}}

Aspose.Cells allows you to load a light-weight version of a workbook into memory to edit its metadata information. Please use the [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/) class to load the workbook.

{{% /alert %}}

The following sample code uses the [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/) class to edit custom document properties of a workbook. Once you open the workbook using the [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class, you will be able to read the document properties. Here is a sample code using the [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/) class.

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