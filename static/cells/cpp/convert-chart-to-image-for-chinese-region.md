##Convert Chart to Image for Chinese Region with C++
Learn how to use Aspose.Cells for C++ to set Chinese configuration for charts. Our guide will demonstrate how to configure charts to support Chinese characters and formats, including fonts, sizes, text directions, and more.
In this topic, we will show you how to set Chinese Region for a chart.
## **Defines an inheritance class**
First step, you need to define a class "ChartChineseSetttings" that inherits from [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/).
Then, by overriding the related functions, you can set the text of the chart elements in your own language.
Code example:
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
Then you can see the effect in the output image, the elements in the chart will be rendered according to your settings.
## **Conclusion**
In this example, if you do not set Chinese Region for a chart, the following chart elements may be rendered in the default language, such as English.
After the above operation, we can get an output chart picture with Chinese Region.
|**Supported elements**|**Value in this example**|**default value in the English environment**|
| :- | :- | :- |
|Axis Title Name|坐标轴标题|Axis Title|
|Axis Unit Name|百,千...|Hundreds, Thousands...|
|Chart Title Name|图表标题|Chart Title|
|Legend Increase Name|增加|Increase|
|Legend Decrease Name|减少|Decrease|
|Legend Total Name|汇总|Total|
|Other Name|其他|Other|
|Series Name|系列|Series|
