---
title: 使用WorkbookMetadata与C++
linktitle: 工作簿元数据
type: docs
weight: 320
url: /zh/cpp/using-workbookmetadata/
description: 了解如何使用WorkbookMetadata在C++中编辑工作簿的自定义文档属性。
---

{{% alert color="primary" %}}

Aspose.Cells 允许你加载工作簿的轻量级版本以编辑其元数据信息。请使用 [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/) 类加载工作簿。

{{% /alert %}}

以下示例代码使用 [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/) 类编辑工作簿的自定义文档属性。打开工作簿后，便可读取文档属性。以下为使用 [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/) 类的示例代码。

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
