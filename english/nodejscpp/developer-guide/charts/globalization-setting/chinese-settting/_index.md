---  
title: Convert Chart to Image for Chinese Region with Node.js via C++  
description: Learn how to use Aspose.Cells for Node.js via C++ to configure charts for Chinese characters and formats, including fonts, sizes, text directions, and more.  
keywords: Aspose.Cells for Node.js, Charts, Chinese Configuration, Fonts, Font Size, Text Direction, Support.  
linktitle: Set Chinese Region  
type: docs  
weight: 9  
url: /nodejs-cpp/convert-chart-to-image-for-chinese-region/  
alias: [/nodejs-cpp/set-chinese-configuration-for-chart/]  
---  

{{% alert color="primary" %}}  
In this topic, we will show you how to set Chinese Region for a chart.  
{{% /alert %}}  

## **Defines an inheritance class**  

First step, you need to define a class "ChartChineseSetttings" that inherits from [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/).  
Then, by rewriting the related functions, you can set the text of the chart elements in your own language.  
Code example:  
```javascript
const AsposeCells = require("aspose.cells.node");

class ChartChineseSettings extends AsposeCells.ChartGlobalizationSettings {
getAxisTitleName() {
return "坐标轴标题";
}

getAxisUnitName(type) {
switch (type) {
case AsposeCells.DisplayUnitType.None:
return '';
case AsposeCells.DisplayUnitType.Hundreds:
return '百';
case AsposeCells.DisplayUnitType.Thousands:
return '千';
case AsposeCells.DisplayUnitType.TenThousands:
return '万';
case AsposeCells.DisplayUnitType.HundredThousands:
return '十万';
case AsposeCells.DisplayUnitType.Millions:
return '百万';
case AsposeCells.DisplayUnitType.TenMillions:
return '千万';
case AsposeCells.DisplayUnitType.HundredMillions:
return '亿';
case AsposeCells.DisplayUnitType.Billions:
return '十亿';
case AsposeCells.DisplayUnitType.Trillions:
return '兆';
default:
return '';
}
}

getChartTitleName() {
return "图表标题";
}

getLegendDecreaseName() {
return "减少";
}

getLegendIncreaseName() {
return "增加";
}

getLegendTotalName() {
return "汇总";
}

getOtherName() {
return "其他";
}

getSeriesName() {
return "系列";
}
}
```  

## **Config Chinese Setting For Chart**  

In this step, you will use the class "ChartChineseSetttings" you defined in the previous step.  
Code example:  

```javascript  
const Workbook = require('aspose.cells');  
const wb = new Workbook("Chinese.xls");  
wb.settings.globalizationSettings.chartSettings = new ChartChineseSetttings();  
const chart0 = wb.worksheets[0].charts[0];  
chart0.toImage("Output.png");  
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
  
{{< app/cells/assistant language="nodejs-cpp" >}}