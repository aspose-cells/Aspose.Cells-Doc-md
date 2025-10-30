---
title: 外部リンクの範囲を取得する（C++編）
linktitle: 外部リンクを含む範囲を取得
type: docs
weight: 120
url: /ja/cpp/get-range-with-external-links/
description: Aspose.Cellsを用いてExcelファイル中の外部リンク付き範囲を取得する方法を学びます。
---

## **外部リンク付きの範囲を取得する**

多くの場合、Excelファイルは他のExcelファイルの外部リンクを通じてデータにアクセスしています。Aspose.Cellsは、[**Name.GetReferredAreas**](https://reference.aspose.com/cells/cpp/aspose.cells/name/getreferredareas/)メソッドを使ってこれらの外部リンクを取得できます。[**Name.GetReferredAreas**](https://reference.aspose.com/cells/cpp/aspose.cells/name/getreferredareas/)メソッドは[**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/)タイプの配列を返します。[**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/)クラスは外部ファイルの名前を返す[**GetExternalFileName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getexternalfilename/)プロパティを持ちます。[**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/)クラスは以下のメンバーを公開しています。

- [**GetEndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getendcolumn/): 範囲の終了列
- [**GetEndRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getendrow/): 範囲の終了行
- [**GetExternalFileName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getexternalfilename/): これが外部参照の場合、外部ファイル名を取得します
- [**IsArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/isarea/): これはエリアであるかどうかを示します
- [**IsExternalLink**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/isexternallink/): これは外部リンクであるかどうかを示します
- [**GetSheetName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getsheetname/): この参照が含まれるシートを示します
- [**GetStartColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getstartcolumn/): エリアの開始列
- [**GetStartRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getstartrow/): エリアの開始行

以下に示すサンプルコードは、外部リンクを含む範囲を取得するための[**Name.GetReferredAreas**](https://reference.aspose.com/cells/cpp/aspose.cells/name/getreferredareas/)メソッドの使用例です。

## **サンプルコード**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook workbook(srcDir + u"SampleExternalReferences.xlsx");

    WorksheetCollection sheets = workbook.GetWorksheets();
    NameCollection namedRanges = sheets.GetNames();

    for (int i = 0; i < namedRanges.GetCount(); ++i)
    {
        Name namedRange = namedRanges.Get(i);
        Vector<ReferredArea> referredAreas = namedRange.GetReferredAreas(true);

        if (!referredAreas.IsNull())
        {
            for (int j = 0; j < referredAreas.GetLength(); ++j)
            {
                ReferredArea referredArea = referredAreas[j];
                std::cout << "IsExternalLink: " << referredArea.IsExternalLink() << std::endl;
                std::cout << "IsArea: " << referredArea.IsArea() << std::endl;
                std::cout << "SheetName: " << referredArea.GetSheetName().ToUtf8() << std::endl;
                std::cout << "ExternalFileName: " << referredArea.GetExternalFileName().ToUtf8() << std::endl;
                std::cout << "StartColumn: " << referredArea.GetStartColumn() << std::endl;
                std::cout << "StartRow: " << referredArea.GetStartRow() << std::endl;
                std::cout << "EndColumn: " << referredArea.GetEndColumn() << std::endl;
                std::cout << "EndRow: " << referredArea.GetEndRow() << std::endl;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
