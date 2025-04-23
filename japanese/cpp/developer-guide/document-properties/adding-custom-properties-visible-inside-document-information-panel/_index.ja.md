---
title: C++を使用したドキュメント情報パネル内に表示されるカスタムプロパティの追加方法
linktitle: 文書情報パネル内で表示されるカスタムプロパティを追加する
type: docs
weight: 300
url: /ja/cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Aspose.CellsとC++を使用して、ドキュメント情報パネルに表示されるカスタムプロパティを追加する方法を学びます。
---

## **ドキュメント情報パネルで表示されるカスタムプロパティの追加**

Aspose.Cellsを使用すると、ワークブックオブジェクト内に文書情報パネルで表示されるカスタムプロパティを追加できます。Microsoft Excelで文書情報パネルを開くには、ファイル > 情報 > プロパティ > ドキュメントパネルを選択します。

[**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/)メソッドを使用して、ドキュメント情報パネルに表示されるカスタムプロパティを追加してください。

次のサンプルコードは、2つのカスタムプロパティを追加します。最初のプロパティにはタイプがなく、2つ目のプロパティにはDateTimeタイプがあります。このコードで生成されたExcelファイルを開くと、これらの2つのプロパティがドキュメント情報パネル内に表示されます。

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

### **関連記事**

{{% alert color="primary" %}}

- [Aspose.CellsでカスタムXMLパーツを使用する](/cells/ja/cpp/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
