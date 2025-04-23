---
title: C++ ile WorkbookMetadata kullanımıyla
linktitle: Çalışma Kitabı Meta Verisi
type: docs
weight: 320
url: /tr/cpp/using-workbookmetadata/
description: Aspose.Cells ile, WorkbookMetadata kullanarak çalışma kitabının özel belge özelliklerini düzenlemenin nasıl yapılacağını öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, metaveri bilgilerini düzenlemek için hafif bir çalışma kitabı sürümünü belleğe yüklemenize olanak tanır. Lütfen çalışma kitabını yüklemek için [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/) sınıfını kullanın.

{{% /alert %}}

Aşağıdaki örnek kod, bir çalışma kitabının özel belge özelliklerini düzenlemek için [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/) sınıfını kullanır. Çalışma kitabını [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı kullanarak açtıktan sonra belge özelliklerini okuyabilirsiniz. İşte [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/) sınıfını kullanarak örnek kod.

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
