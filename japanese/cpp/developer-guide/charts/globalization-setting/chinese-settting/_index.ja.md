---
title: C++でチャートを画像に変換（中国地域向け）
linktitle: 中国地域を設定する
description: Aspose.Cells for C++を使用して中国向けのチャート設定を行う方法を学びます。フォント、サイズ、テキスト方向などを設定し、中国文字やフォーマットのサポートを行います。
keywords: Aspose.Cells for C++、チャート、中国設定、フォント、フォントサイズ、テキスト方向、サポート。
type: docs
weight: 9
url: /ja/cpp/convert-chart-to-image-for-chinese-region/
alias: [/cpp/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

このトピックでは、チャートの中国地域を設定する方法を示します。

{{% /alert %}}

## **継承クラスを定義する**

最初のステップでは、[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/)から継承する"ChartChineseSetttings"クラスを定義する必要があります。 
次に、関連する関数をオーバーライドして、チャート要素のテキストを自分の言語に設定できます。

コード例:
```c++
#include <iostream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

class ChartChineseSettings : public ChartGlobalizationSettings
{
public:
	ChartChineseSettings() {}
	virtual ~ChartChineseSettings() {}

	virtual U16String GetAxisTitleName()
	{
		return U16String(u"\u5750\u6807\u8F74\u6807\u9898");
	}

	virtual U16String GetAxisUnitName(DisplayUnitType type)
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
			return U16String(u"\u5341\u4E07");
		case DisplayUnitType::Millions:
			return U16String(u"\u767E\u4E07");
		case DisplayUnitType::TenMillions:
			return U16String(u"\u5343\u4E07");
		case DisplayUnitType::HundredMillions:
			return U16String(u"\u4EBF");
		case DisplayUnitType::Billions:
			return U16String(u"\u5341\u4EBF");
		case DisplayUnitType::Trillions:
			return U16String(u"\u5146");
		default:
			return U16String(u"");
		}
	}

	virtual U16String GetChartTitleName()
	{
		return U16String(u"\u56FE\u8868\u6807\u9898");
	}

	virtual U16String GetLegendDecreaseName()
	{
		return U16String(u"\u51CF\u5C11");
	}

	virtual U16String GetLegendIncreaseName()
	{
		return U16String(u"\u589E\u52A0");
	}

	virtual U16String GetLegendTotalName()
	{
		return U16String(u"\u6C47\u603B");
	}

	virtual U16String GetOtherName()
	{
		return U16String(u"\u5176\u4ED6");
	}

	virtual U16String GetSeriesName()
	{
		return U16String(u"\u7CFB\u5217");
	}
};

//Config Chinese Setting For Chart
//In this step, you will use the class "ChartChineseSetttings" you defined in the previous step.
int main()
{
	Workbook wb("Chinese.xls");
	ChartChineseSettings* chartChineseSettings = new ChartChineseSettings();
	wb.GetSettings().GetGlobalizationSettings()->SetChartSettings(chartChineseSettings);
	Chart chart0 = wb.GetWorksheets().Get(0).GetCharts().Get(0);
	chart0.ToImage("Output.png");
	delete chartChineseSettings;
	return 0;
}

```

その後、出力イメージで効果を確認できます。チャートの要素は、設定に従ってレンダリングされます。

## **結論**

この例では、チャートに日本語の地域を設定しない場合、次のチャート要素はデフォルトの言語（英語など）でレンダリングされる場合があります。
上記の操作を行った後、日本語の地域を設定した出力チャート画像を取得できます。

|**サポートされる要素**|**この例の値**|**英語環境のデフォルト値**|
| :- | :- | :- |
| 軸タイトル名 | 坐標軸タイトル | 軸タイトル |
|軸単位名|百,千...|Hundreds, Thousands...|
| チャートタイトル名 | グラフタイトル | Chart Title |
| 凡例の増加名 | 増加 | Increase |
| 凡例の減少名 | 減少 | Decrease |
| 凡例の合計名 | 汇总 | Total |
| その他の名前 | その他 | Other |
| 系列名 | 系列 | Series |
{{< app/cells/assistant language="cpp" >}}
