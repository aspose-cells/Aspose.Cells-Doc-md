---
title: C++で日本地域向けにチャートを画像に変換
linktitle: 日本語地域の設定
type: docs
weight: 10
url: /ja/cpp/convert-chart-to-image-for-japanese-region/
alias: [/cpp/set-japanese-configuration-for-chart/]
description: Aspose.Cells for C++を使用してチャートの日本語設定方法を学びます。フォント、サイズ、テキスト方向など、日本語の文字とフォーマットをサポートするための設定方法を示すガイドです。
keywords: Aspose.Cells for C++、チャート、日本語設定、フォント、フォントサイズ、テキスト方向、サポート。
---

{{% alert color="primary" %}}

このトピックでは、チャートの日本語地域を設定する方法を説明します。

{{% /alert %}}

## **継承クラスを定義する**

最初のステップは、[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/)から継承した`ChartJapaneseSettings`クラスを定義する必要があります。 
次に、関連する関数をオーバーライドして、チャート要素のテキストを自分の言語に設定できます。
コード例:
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

class ChartJapaneseSetttings : public ChartGlobalizationSettings
{
public:
    ChartJapaneseSetttings() : ChartGlobalizationSettings() {}

    U16String GetAxisTitleName() override
    {
        return U16String(u"\u8EF8\u30BF\u30A4\u30C8\u30EB");
    }

    U16String GetAxisUnitName(DisplayUnitType type) override
    {
        switch (type)
        {
        case DisplayUnitType::None:
            return U16String(u"");
        case DisplayUnitType::Hundreds:
            return U16String(u"\u767E");
        case DisplayUnitType::Thousands:
            return U16String(u"\u5343");
        case DisplayUnitType::TenThousands:
            return U16String(u"\u4E07");
        case DisplayUnitType::HundredThousands:
            return U16String(u"\u0031\u0030\u4E07");
        case DisplayUnitType::Millions:
            return U16String(u"\u767E\u4E07");
        case DisplayUnitType::TenMillions:
            return U16String(u"\u5343\u4E07");
        case DisplayUnitType::HundredMillions:
            return U16String(u"\u5104");
        case DisplayUnitType::Billions:
            return U16String(u"\u0031\u0030\u5104");
        case DisplayUnitType::Trillions:
            return U16String(u"\u5146");
        default:
            return U16String(u"");
        }
    }

    U16String GetChartTitleName() override
    {
        return U16String(u"\u30B0\u30E9\u30D5\u0020\u30BF\u30A4\u30C8\u30EB");
    }

    U16String GetLegendDecreaseName() override
    {
        return U16String(u"\u524A\u6E1B");
    }

    U16String GetLegendIncreaseName() override
    {
        return U16String(u"\u305E\u3046\u304B");
    }

    U16String GetLegendTotalName() override
    {
        return U16String(u"\u3059\u3079\u3066\u306E");
    }

    U16String GetOtherName() override
    {
        return U16String(u"\u305D\u306E\u4ED6");
    }

    U16String GetSeriesName() override
    {
        return U16String(u"\u30B7\u30EA\u30FC\u30BA");
    }
};
```

## **チャートの日本語設定を構成する**

このステップでは、前のステップで定義した`ChartJapaneseSettings`クラスを使用します。
コード例:

```cpp
    Workbook wb("Japanese.xls");
    wb.GetSettings().GetGlobalizationSettings().SetChartSettings(new ChartJapaneseSettings());
    Chart chart0 = wb.GetWorksheets().Get(0).GetCharts().Get(0);
    chart0.ToImage("Output.png");
```

その後、出力イメージで効果を確認できます。チャートの要素は、設定に従ってレンダリングされます。

## **結論**

この例では、チャートに日本の地域を設定しないと、次のチャート要素がデフォルト言語(英語など)でレンダリングされる可能性があります。
上記の操作の後、日本の地域で出力されたチャート画像を取得できます。

|**サポートされる要素**|**この例の値**|**英語環境のデフォルト値**|
| :- | :- | :- |
|軸タイトル名|軸タイトル|Axis Title|
|軸単位名|百,千...|Hundreds, Thousands...|
|グラフタイトル名|グラフ タイトル|Chart Title|
|凡例増加名|ぞうか|Increase|
|凡例減少名|削減|Decrease|
|凡例全体名|すべての|Total|
|その他の名前|その他|Other|
|系列名|シリーズ|Series|
{{< app/cells/assistant language="cpp" >}}
