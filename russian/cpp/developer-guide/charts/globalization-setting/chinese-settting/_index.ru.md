---
title: Конвертация графика в изображение для региона Китая с помощью C++
linktitle: Установить китайский регион
description: Узнайте, как использовать Aspose.Cells for C++ для настройки китайской конфигурации графиков. Наше руководство покажет, как настроить графики для поддержки китайских символов и форматов, включая шрифты, размеры, направление текста и многое другое.
keywords: Aspose.Cells for C++, графики, настройка для Китая, шрифты, размер шрифта, направление текста, поддержка.
type: docs
weight: 9
url: /ru/cpp/convert-chart-to-image-for-chinese-region/
alias: [/cpp/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

В этой теме мы покажем вам, как установить китайский регион для графика.

{{% /alert %}}

## **Определяет класс наследования**

Первый шаг — определить класс "ChartChineseSetttings", который наследуется от [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/). 
Далее, переопределяя соответствующие функции, вы можете задавать текст элементов графика на вашем языке.

Пример кода:
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

Затем вы можете увидеть эффект на выходном изображении, элементы на диаграмме будут отображаться в соответствии с вашими настройками.

## **Заключение**

В этом примере, если вы не установите китайский регион для диаграммы, следующие элементы диаграммы могут отображаться на языке по умолчанию, например, на английском.
После вышеуказанных действий мы получим выходное изображение диаграммы с китайским регионом.

|**Поддерживаемые элементы**|**Значение в этом примере**|**значение по умолчанию в английской среде**|
| :- | :- | :- |
|Имя заголовка оси|坐标轴标题|Название оси|
|Единица оси|百,千...|Сотни, тысячи...|
|Название заголовка диаграммы|图表标题|Название диаграммы|
|Имя увеличения легенды|增加|Увеличение|
|Имя уменьшения легенды|减少|Уменьшение|
|Имя общей легенды|汇总|Общее|
|Другое имя|其他|Другое|
|Имя серии|系列|Серия|
{{< app/cells/assistant language="cpp" >}}
