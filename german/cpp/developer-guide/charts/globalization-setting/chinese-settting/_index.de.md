---
title: Diagramm in Bild umwandeln für chinesisches Gebiet mit C++
linktitle: Chinesische Region festlegen
description: Erfahren Sie, wie Sie Aspose.Cells for C++ verwenden, um die chinesische Konfiguration für Diagramme einzustellen. Unser Leitfaden zeigt, wie man Diagramme so konfiguriert, dass sie chinesische Zeichen und Formate unterstützen, einschließlich Schriftarten, Größen, Textausrichtungen und mehr.
keywords: Aspose.Cells for C++, Diagramme, Chinesische Konfiguration, Schriftarten, Schriftgrößen, Textausrichtung, Unterstützung.
type: docs
weight: 9
url: /de/cpp/convert-chart-to-image-for-chinese-region/
alias: [/cpp/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

In diesem Thema zeigen wir Ihnen, wie Sie eine chinesische Region für ein Diagramm festlegen können.

{{% /alert %}}

## **Definiert eine Vererbungsklasse**

Der erste Schritt besteht darin, eine Klasse "ChartChineseSetttings" zu definieren, die von [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/) erbt. 
Anschließend können Sie durch Überschreiben der zugehörigen Funktionen den Text der Diagrammelemente in Ihrer eigenen Sprache einstellen.

Codebeispiel:
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

Dann können Sie den Effekt im Ausgabebild sehen, die Elemente im Diagramm werden gemäß Ihren Einstellungen gerendert.

## **Fazit**

In diesem Beispiel, wenn Sie keine chinesische Region für ein Diagramm festlegen, werden die folgenden Diagrammelemente möglicherweise in der Standardsprache, wie Englisch, gerendert.
Nach der oben genannten Operation können wir ein Ausgabediagrammbild mit chinesischer Region erhalten.

|**Unterstützte Elemente**|**Wert in diesem Beispiel**|**Standardwert in der englischen Umgebung**|
| :- | :- | :- |
|Axis Title Name|坐标轴标题|Achsentitel|
|Achsenbezeichnung|百,千...|Hunderte, Tausende...|
|Chart Title Name|图表标题|Diagrammtitel|
|Legend Increase Name|增加|Zunahme|
|Legend Decrease Name|减少|Rückgang|
|Legend Total Name|汇总|Gesamt|
|Other Name|其他|Sonstige|
|Series Name|系列|Serie|
{{< app/cells/assistant language="cpp" >}}
