---
title: C++でワークシートにアイコンを追加
linktitle: アイコンを管理する
type: docs
weight: 100
url: /ja/cpp/insert-svg-to-excel/
description: Aspose.Cellsを使用してC++でExcelワークシートにアイコンを追加する方法を学びます。
---

## Aspose.Cells でワークシートにアイコンを追加

Excel ファイルに 'アイコン' を追加する必要がある場合は、このドキュメントが役立ちます。[Aspose.Cells](https://products.aspose.com/cells/) を使用して、Excel ファイルにアイコンを追加する方法について説明します。

挿入アイコン操作に対応する Excel インターフェースは次のとおりです。

![](1.png)

- ワークシートに挿入するアイコンの位置を選択します
- *挿入*->*アイコン* を左クリックします
- 開いたウィンドウで、上図の赤い四角内のアイコンを選択します
- 左クリックで*挿入*を選択すると、Excelファイルに挿入されます。

効果は以下のようになります。

![](2.png)

ここでは、[Aspose.Cells](https://products.aspose.com/cells/)を使ったアイコン挿入を支援するための*サンプルコード*を用意しています。また、必要な[サンプルファイル](sample.xlsx)とアイコン[リソースファイル](icon.zip)もあります。Excelのインターフェースを使用して、[リソースファイル](icon.zip)と同じ表示効果のアイコンを[サンプルファイル](sample.xlsx)に挿入しました。

### C++

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    U16String fileName = u"icon.svg";
    std::ifstream fsSource(fileName.ToUtf8(), std::ios::binary);
    if (!fsSource) {
        std::cerr << "Failed to open file: " << fileName.ToUtf8() << std::endl;
        return -1;
    }

    fsSource.seekg(0, std::ios::end);
    size_t fileSize = fsSource.tellg();
    fsSource.seekg(0, std::ios::beg);

    std::vector<uint8_t> bytes(fileSize);
    fsSource.read(reinterpret_cast<char*>(bytes.data()), fileSize);
    fsSource.close();

    Aspose::Cells::Vector<uint8_t> asposeBytes(bytes.size());
    if (!bytes.empty()) {
        memcpy(asposeBytes.GetData(), bytes.data(), bytes.size());
    }

    Workbook workbook(u"sample.xlsx");
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    sheet.GetShapes().AddIcons(3, 0, 7, 0, 100, 100, asposeBytes, Aspose::Cells::Vector<uint8_t>());

    Cell c = sheet.GetCells().Get(8, 7);
    c.PutValue(u"Insert via Aspose.Cells");
    Style s = c.GetStyle();
    s.GetFont().SetColor(Color::Blue());
    c.SetStyle(s);

    workbook.Save(u"sample2.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```

プロジェクトで上記のコードを実行すると、次の結果が得られます。

![](3.png)
