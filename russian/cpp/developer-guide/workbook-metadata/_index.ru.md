---
title: Использование WorkbookMetadata с C++
linktitle: Метаданные книги
type: docs
weight: 320
url: /ru/cpp/using-workbookmetadata/
description: Узнайте, как использовать WorkbookMetadata для редактирования пользовательских свойств документа книги в C++ с Aspose.Cells.
---

{{% alert color="primary" %}}

Aspose.Cells позволяет загружать легкую версию книги в память для редактирования метаданных. Пожалуйста, используйте класс [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/) для загрузки книги.

{{% /alert %}}

Следующий пример кода использует класс [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/) для редактирования пользовательских свойств документа книги. После открытия книги с помощью класса [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), вы сможете читать свойства документа. Вот пример использования класса [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/).

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
