---
title: Konvertera diagram till bild för kinesisk region med C++
linktitle: Ställ in kinesisk region
description: Lär dig hur du använder Aspose.Cells for C++ för att ställa in kinesisk konfiguration för diagram. Vår guide visar hur du konfigurerar diagram för att stödja kinesiska tecken och format, inklusive teckensnitt, storlekar, texts riktningar och mer.
keywords: Aspose.Cells for C++, diagram, kinesisk konfiguration, teckensnitt, teckenstorlek, textriktning, stöd.
type: docs
weight: 9
url: /sv/cpp/convert-chart-to-image-for-chinese-region/
alias: [/cpp/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

I det här ämnet kommer vi att visa dig hur du ställer in kinesisk region för ett diagram.

{{% /alert %}}

## **Definierar en arvs klass**

 Första steget, du måste definiera en klass "ChartChineseSetttings" som ärver från [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/). 
 Sedan, genom att överskrida relaterade funktioner, kan du ställa in texten på diagrammets element på ditt eget språk.

Kodexempel:
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

Sedan kan du se effekten i utdata bilden, elementen i diagrammet kommer att renderas enligt dina inställningar.

## **Slutsats**

I det här exemplet, om du inte ställer in kinesisk region för ett diagram, kan följande diagramelement renderas på det vanliga språket, såsom engelska.
Efter ovanstående åtgärd kan vi få en utmatningsdiagrambild med kinesisk region.

|**Stödda element**|**Värde i detta exempel**|**Standardvärde i den engelska miljön**|
| :- | :- | :- |
|Axel Titel Namn|坐标轴标题|Axis Title|
|axelenhetsnamn|百,千...|Hundratals, Tusentals...|
|Diagram Titel Namn|图表标题|Chart Title|
|Legend Öka Namn|增加|Increase|
|Legend Minska Namn|减少|Decrease|
|Legend Total Namn|汇总|Total|
|Annat Namn|其他|Other|
|Serienamn|系列|Series|
{{< app/cells/assistant language="cpp" >}}
