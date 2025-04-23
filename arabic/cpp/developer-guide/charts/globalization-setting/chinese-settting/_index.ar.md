---
title: تحويل المخطط إلى صورة للمنطقة الصينية باستخدام ++C
linktitle: تحديد المنطقة الصينية
description: تعلم كيفية استخدام Aspose.Cells for C++ لضبط إعدادات اللغة الصينية للمخططات. سيظهر دليلنا كيفية تكوين المخططات لدعم الأحرف والتنسيقات الصينية، بما في ذلك الخطوط، الأحجام، اتجاه النص، والمزيد.
keywords: Aspose.Cells for C++، المخططات، الإعدادات الصينية، الخطوط، حجم الخط، اتجاه النص، الدعم.
type: docs
weight: 9
url: /ar/cpp/convert-chart-to-image-for-chinese-region/
alias: [/cpp/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

في هذا الموضوع، سنوضح لك كيفية تعيين المنطقة الصينية لرسم بياني.

{{% /alert %}}

## **تحديد فئة الإرث**

الخطوة الأولى، تحتاج إلى تعريف فئة "ChartChineseSetttings" الوريثة من [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/). 
 ثم، من خلال تجاوز الدالات ذات الصلة، يمكنك ضبط نص عناصر المخطط بلغتك الخاصة.

مثال على الكود:
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

ثم يمكنك رؤية التأثير في الصورة الناتجة، حيث سيتم تقديم عناصر الرسم البياني وفقًا لإعداداتك.

## **الاستنتاج**

في هذا المثال، إذا لم تقم بتحديد المنطقة الصينية لرسم بياني، فقد يتم عرض عناصر الرسم البياني التالية باللغة الافتراضية، مثل الإنجليزية.
بعد العملية المذكورة أعلاه، يمكننا الحصول على صورة رسم بياني إخراجية مع المنطقة الصينية.

| ** العناصر المدعومة ** | ** القيمة في هذا المثال ** | ** القيمة الافتراضية في بيئة اللغة الإنجليزية ** |
| :- | :- | :- |
|اسم عنوان المحور|坐标轴标题|عنوان المحور|
| اسم وحدة المحور | 百,千... | مئات ، آلاف ... |
|Chart Title Name|اسم عنوان الرسم البياني|اسم عنوان الرسم البياني|
|Legend Increase Name|زيادة|زيادة|
|Legend Decrease Name|انخفاض|انخفاض|
|Legend Total Name|الإجمالي|الإجمالي|
|Other Name|آخر|آخر|
|Series Name|سلسلة|سلسلة|
