---
title: 他の言語で小計や総計ラベルを実装する（C++使用)
linktitle: 他の言語で小計または合計ラベルを実装する
type: docs
weight: 50
url: /ja/cpp/implement-subtotal-or-grand-total-labels-in-other-languages/
description: Aspose.Cells for C++を使用して、英語以外の言語で小計および合計ラベルを実装する方法を学びます。
---

## **可能な使用シナリオ**

中国語、日本語、アラビア語、ヒンディー語などの非英語言語で小計と合計のラベルを表示したい場合があります。Aspose.Cellsは、[**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/)クラスと[**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getglobalizationsettings/)プロパティを使用してこれを可能にします。[**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/)クラスの利用方法についてはこちらの記事を参照してください：

- [ピーグラフのカスタムサブトータルラベルおよびその他のラベル用のGlobalizationSettingsクラスの使用](/cells/ja/cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **他の言語で小計または合計ラベルを実装する**

以下のサンプルコードは、[サンプルExcelファイル](5115151.xlsx)を読み込み、中国語で小計と合計の名前を実装しています。このコードで生成された[出力Excelファイル](5115152.xlsx)を参考にしてください。まず[**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/)クラスを作成し、それをコードで使用します。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class GlobalizationSettingsImp : public GlobalizationSettings
{
public:
    U16String GetTotalName(ConsolidationFunction functionType) override
    {
        return u"Chinese Total - \u53EF\u80FD\u7684\u7528\u6CD5";
    }

    U16String GetGrandTotalName(ConsolidationFunction functionType) override
    {
        return u"Chinese Grand Total - \u53EF\u80FD\u7684\u7528\u6CD5";
    }
};
```

次に、以下のように上記で作成したクラスをコード内で使用します：

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

class GlobalizationSettingsImp : public GlobalizationSettings {
public:
    virtual U16String GetTotalName(ConsolidationFunction functionType) override {
        return u"Custom Total";
    }

    virtual U16String GetGrandTotalName(ConsolidationFunction functionType) override {
        return u"Custom Grand Total";
    }
};

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(srcDir + u"sample.xlsx");

    GlobalizationSettingsImp gsi;
    wb.GetSettings().SetGlobalizationSettings(&gsi);

    Worksheet ws = wb.GetWorksheets().Get(0);

    CellArea ca = CellArea::CreateCellArea(u"A1", u"B10");
    ws.GetCells().Subtotal(ca, 0, ConsolidationFunction::Sum, {2, 3, 4});

    ws.GetCells().SetColumnWidth(0, 40);

    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "Subtotal applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
