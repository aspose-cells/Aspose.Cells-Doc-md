---
title: C++でワークシートにテキストボックスを追加/挿入する方法
linktitle: ワークシートにテキストボックスを追加
type: docs
weight: 10
url: /ja/cpp/add-text-box-to-worksheet-in-aspose-cells/
description: Aspose.Cellsを使ったC++でのワークシートへのテキストボックスの追加/挿入方法。
keywords: Excel Aspose への追加/挿入テキストボックス ワークシート
---

Excel でワークシートにテキストボックスを追加

Excelプログラム（バージョン07以降）では、テキストボックスを挿入できる場所が2つあります。一つは『挿入-図形』、もう一つは『挿入』のトップメニューの右側です。

### 方法一：

![1](1.png)

### 方法二：

![2](2.png)

## 作成方法

水平または垂直のテキストボックスを作成できます。

- 対応するオプション（横向きまたは縦向き）を選択してください
- ページ上で左クリックします。
- 左ボタンを押したまま、ページ上で距離をドラッグします。
- 左ボタンを離します。

これでテキストボックスができます。

Aspose.Cells でワークシートにテキストボックスを追加

ワークシートに一括でテキストボックスを挿入する必要がある場合、手動での挿入方法は明らかに失敗です。これに不満がある場合、このドキュメントが役立つでしょう。 [Aspose.Cells](https://products.aspose.com/cells/)は、あなたのコードで簡単に一括挿入を行うAPIを提供します。

次のサンプルコードはテキストボックスを作成します。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create an object of the Workbook class
    Workbook workbook;

    // Access first worksheet from the collection
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add the TextBox to the worksheet
    sheet.GetTextBoxes().Add(6, 10, 100, 200);

    // Save the workbook with the text box
    workbook.Save(outDir + u"result.xlsx", SaveFormat::Xlsx);

    std::cout << "Text box added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

結果ファイル（result.xlsx）と類似したファイルを取得します。その中に次のものが見られます：

![](52449.png)
