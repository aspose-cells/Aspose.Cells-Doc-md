---
title: 将图表转换为图片以支持中国地区使用C++
linktitle: 设置中国区域
description: 学习如何使用Aspose.Cells for C++设置支持中文字符和格式的图表。我们的指南将演示如何配置图表以支持中文字符，包括字体、大小、文本方向等。
keywords: Aspose.Cells for C++，图表，中文配置，字体，字体大小，文本方向，支持。
type: docs
weight: 9
url: /zh/cpp/convert-chart-to-image-for-chinese-region/
alias: [/cpp/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

在本主题中，我们将向您展示如何为图表设置中国区域。

{{% /alert %}}

## **定义继承类**

第一步，你需要定义一个继承自[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/)的类"ChartChineseSetttings"。 
然后，通过重写相关函数，你可以用自己的语言设置图表元素的文本。

代码示例:
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

然后，您可以在输出图像中看到效果，图表中的元素将根据您的设置进行渲染。

## **结论**

在这个示例中，如果不为图表设置中国区域，则以下图表元素可能以默认语言（例如英语）渲染。
在上述操作之后，我们可以获得一个带有中国区域的输出图表图片。

|**支持的元素**|**本示例中的值**|**英文环境中的默认值**|
| :- | :- | :- |
|轴标题名称|坐标轴标题|Axis Title|
|轴单位名称|百,千...|Hundreds, Thousands...|
|图表标题|图表标题|
|增加|增加|
|减少|减少|
|汇总|汇总|
|其他|其他|
|系列|系列|
