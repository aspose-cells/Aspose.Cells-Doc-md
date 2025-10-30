---
title: AutoFilterをリフレッシュした後のすべての非表示行のインデックスを取得（C++使用）
linktitle: オートフィルタを更新した後のすべての非表示行のインデックスを取得する
type: docs
weight: 320
url: /ja/cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: AutoFilterをリフレッシュした後のすべての非表示行のインデックスを取得する方法をAspose.Cells for C++ APIを使用して学びます。
keywords: Autofilterを更新後にすべての隠れた行のインデックスを取得する、Autofilterを更新後の隠れた行インデックスを取得する、Autofilterを更新後の隠れた行インデックスを取得する
---

## **可能な使用シナリオ**

ワークシートセルにオートフィルタを適用すると、一部の行が自動的に非表示になります。ただし、Excelエンドユーザーによって手動で非表示にされた行があり、それがオートフィルタによって非表示にされている行かどうかがわかりにくい場合があります。Aspose.Cellsはこの問題を解決するためにint[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/refresh/)を使用します。このメソッドはオートフィルタによって非表示にされた行の行インデックスを返し、Excelエンドユーザーによって手動で非表示にされた行の行インデックスではありません。

## **オートフィルタの更新後の非表示行インデックスの取得**

[サンプルExcelファイル](64716909.xlsx)を読み込み、Excelエンドユーザーによって手動で非表示にされた行の一部を示しています。コードはオートフィルタを適用し、int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/refresh/)メソッドを使用して自動フィルタによって非表示にされたすべての行の行インデックスを取得し、非表示にされた行のインデックスとセル名、値をコンソールに出力します。

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + U16String(u"sampleGetAllHiddenRowsIndicesAfterRefreshingAutoFilter.xlsx");
    Workbook workbook(inputFilePath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    AutoFilter autoFilter = worksheet.GetAutoFilter();
    autoFilter.AddFilter(0, u"Orange");

    Vector<int32_t> rowIndices = autoFilter.Refresh(true);

    std::cout << "Printing Rows Indices, Cell Names and Values Hidden By AutoFilter." << std::endl;
    std::cout << "--------------------------" << std::endl;

    for (int32_t i = 0; i < rowIndices.GetLength(); i++)
    {
        int32_t r = rowIndices[i];
        Cell cell = worksheet.GetCells().Get(r, 0);
        std::cout << r << "\t" << cell.GetName().ToUtf8() << "\t" << cell.GetStringValue().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **コンソール出力**

{{< highlight java >}}

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.

\--------------------------

1       A2      Apple

2       A3      Apple

3       A4      Apple

6       A7      Apple

7       A8      Apple

11      A12     Pear

12      A13     Pear

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
