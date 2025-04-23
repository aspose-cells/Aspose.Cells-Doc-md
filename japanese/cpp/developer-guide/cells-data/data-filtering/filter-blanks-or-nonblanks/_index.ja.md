---
title: C++を使用して空白または空白でないセルをフィルタリングする方法
linktitle: 空白または非空白をフィルタリングする方法
type: docs
weight: 85
url: /ja/cpp/how-to-filter-blanks-and-non-blanks/
description: Aspose.Cells for C++ APIを使用して空白セルと非空白セルをフィルタリングする方法を学びます。
keywords: 空白をフィルタリングし、非空白をフィルタリングし、ワークシート内の空白をフィルタリングし、ワークシート内の非空白をフィルタリングし、Excel内の空白をフィルタリングし、Excel内の非空白をフィルタリングし、Excel内の空白および非空白をフィルタリングする
---

## **可能な使用シナリオ**
Excelでのデータのフィルタリングは、ユーザーが基準に基づいて特定のデータサブセットに焦点を当てることを可能にし、全体的なデータの操作および解釈プロセスをより効率的かつ効果的にします。

## **Excelで空白または非空白をフィルタリングする方法**
Excelでは、フィルタリングオプションを使用して簡単に空白または非空白をフィルタリングすることができます。以下にその方法を示します。

### **Excelで空白をフィルタリングする方法**
1. 範囲を選択する: 列ヘッダーの文字をクリックして列全体を選択するか、空白をフィルタリングしたい範囲を選択します。
1. フィルタメニューを開く: リボンの"データ"タブに移動します。
<br>
<image src="1.png" width="70%" />
1. フィルタオプション: "フィルタ"ボタンをクリックします。これにより、選択した範囲にフィルタ矢印が追加されます。
1. 空白をフィルタリング: 空白をフィルタリングしたい列のフィルタ矢印をクリックします。"空白"以外のすべてのオプションを選択解除し、OKをクリックします。これにより、その列の空白のセルのみが表示されます。
<br>
<image src="2.png" width="70%" />
1. 結果は次のとおりです:
<br>
<image src="3.png" width="70%" />

### **Excelで非空白をフィルタリングする方法**
1. 範囲を選択する: 列ヘッダーの文字をクリックして列全体を選択するか、非空白をフィルタリングしたい範囲を選択します。
1. フィルタメニューを開く: リボンの"データ"タブに移動します。
<br>
<image src="1.png" width="70%" />
1. フィルタオプション: "フィルタ"ボタンをクリックします。これにより、選択した範囲にフィルタ矢印が追加されます。
1. ブランク以外をフィルタする: フィルタ矢印をクリックし、非ブランクをフィルタしたい列を選択します。"非ブランク"または"カスタム"以外のすべてのオプションを選択解除または条件を設定し、「OK」をクリックします。これにより、その列のブランクでないセルのみが表示されます。
<br>
<image src="4.png" width="70%" />
1. 結果は次のとおりです:
<br>
<image src="5.png" width="70%" />

## **Aspose.Cellsを使用してブランクをフィルタする方法**
列にテキストが含まれており、その一部のセルが空白の場合、その行だけを選択する必要がある場合、[AutoFilter.MatchBlanks(int fieldIndex)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/matchblanks/) および [AutoFilter.AddFilter(int fieldIndex, string criteria)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/addfilter/) 関数を以下のように使用できます。 

[サンプルExcelファイル](sample.xlsx)を読み込み、ダミーデータを含むコード例をご覧ください。サンプルコードでは、ブランクをフィルタリングするための3つの方法を使用し、その後ブックを[output Excel file](FilteredBlanks.xlsx)として保存します。 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Open the Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Method 1: Call MatchBlanks function to apply the filter
    // worksheet.GetAutoFilter().MatchBlanks(1);

    // Method 2: Call AddFilter function and set criteria to ""
    // worksheet.GetAutoFilter().AddFilter(1, u"");

    // Method 3: Call AddFilter function and set criteria to nullptr
    worksheet.GetAutoFilter().AddFilter(1, nullptr);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(u"FilteredBlanks.xlsx");

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Aspose.Cellsを使用して非ブランクをフィルタする方法**

サンプルコードは、ダミーデータを含む [サンプルExcelファイル](sample.xlsx) を読み込み、[空白以外のデータをフィルタリング](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/matchnonblanks/) し、その後ワークブックを [出力Excelファイル](FilteredNonBlanks.xlsx) として保存します。 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook by opening an existing Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet in the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call MatchNonBlanks function to apply the filter on the second column (index 1)
    worksheet.GetAutoFilter().MatchNonBlanks(1);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(u"FilteredNonBlanks.xlsx");

    std::cout << "Filtered non-blanks saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```


