---
title: C++を使用してセルのリッチテキスト部分のアクセスと更新
linktitle: リッチフォーマットテキスト
type: docs
weight: 40
url: /ja/cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Aspose.Cells for C++ APIを使ったセルのリッチテキスト部分のアクセスと更新の方法を学習します。
keywords: セルのリッチテキストへのアクセスおよび更新、セルのリッチテキストの取得、セルのリッチテキストの編集、セルのリッチテキストへのアクセス、セルのリッチテキストの更新、セルのリッチテキストの変更
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すると、セルのリッチテキストの部分にアクセスして更新することができます。このために、[**Cell->GetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcharacters/)および[**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/)メソッドを使用することができます。これらのメソッドは、フォント名、フォント色、太字などのフォントのさまざまなプロパティにアクセスおよび更新するために使用できる[**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/)オブジェクトの配列を返し、受け入れます。

{{% /alert %}}

## **セルのリッチテキストの部分にアクセスして更新**

以下のコードは、[ソースExcelファイル](5112369.xlsx)を使用した[**Cell->GetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcharacters/)および[**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/)メソッドの使用例を示しています。ソースExcelファイルのセルA1には3つの部分に分かれたリッチテキストがあり、それぞれ異なるフォントが設定されています。このコードはこれらの部分にアクセスし、最初の部分のフォントを**"Arial"**に更新します。修正したブックは[出力Excelファイル](5112366.xlsx)として保存されます。

### リッチテキスト部分にアクセスし更新するC++コード

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputPath = srcDir + u"Sample.xlsx";
    U16String outputPath = outDir + u"Output.out.xlsx";

    Workbook workbook(inputPath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Cell cell = worksheet.GetCells().Get(U16String(u"A1"));

    std::cout << "Before updating the font settings...." << std::endl;

    Vector<FontSetting> fnts = cell.GetCharacters();

    for (int i = 0; i < fnts.GetLength(); ++i)
    {
        FontSetting& fs = fnts[i];
        std::cout << fs.GetFont().GetName().ToUtf8() << std::endl;
    }

    if (fnts.GetLength() > 0)
    {
        FontSetting& fs = fnts[0];
        fs.GetFont().SetName(u"Arial");
        cell.SetCharacters(fnts);
    }

    std::cout << std::endl << "After updating the font settings...." << std::endl;

    fnts = cell.GetCharacters();

    for (int i = 0; i < fnts.GetLength(); ++i)
    {
        FontSetting& fs = fnts[i];
        std::cout << fs.GetFont().GetName().ToUtf8() << std::endl;
    }

    workbook.Save(outputPath);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### サンプルコードによって生成されたコンソール出力

こちらは[ソースExcelファイル](5112369.xlsx)を使用したときのコンソール出力例です:

{{< highlight java >}}

Before updating the font settings....
Century
Courier New
Verdana

After updating the font settings....
Arial
Courier New
Verdana

{{< /highlight >}}
