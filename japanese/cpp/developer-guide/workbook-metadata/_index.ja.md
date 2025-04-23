---
title: WorkbookMetadataを使用してC++でカスタムドキュメントプロパティを編集
linktitle: ワークブックメタデータ
type: docs
weight: 320
url: /ja/cpp/using-workbookmetadata/
description: Aspose.Cellsを使用してC++でワークブックのカスタムドキュメントプロパティを編集する方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsは、メモリに軽量なワークブックのバージョンをロードして、そのメタデータ情報を編集することを可能にします。ワークブックをロードするには、[**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/)クラスを使用してください。

{{% /alert %}}

以下のサンプルコードは、[**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/)クラスを使用してワークブックのカスタムドキュメントプロパティを編集する例です。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスを使ってワークブックを開くと、ドキュメントのプロパティを読むことができます。こちらは、[**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/)クラスを使ったサンプルコードです。

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
