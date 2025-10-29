---  
title: 将图表转换为图像支持中国地区，使用 Node.js via C++  
description: 了解如何使用 Aspose.Cells for Node.js via C++ 配置支持中文字符和格式的图表，包括字体、大小、文本方向等。  
keywords: Aspose.Cells for Node.js，图表，中文配置，字体，字体大小，文本方向，支持。  
linktitle: 设置中国区域  
type: docs  
weight: 9  
url: /zh/nodejs-cpp/convert-chart-to-image-for-chinese-region/  
alias: [/nodejs-cpp/set-chinese-configuration-for-chart/]  
---  

{{% alert color="primary" %}}  
在本主题中，我们将向您展示如何为图表设置中国区域。  
{{% /alert %}}  

## **定义继承类**  

第一步，你需要定义一个继承自[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/)的类"ChartChineseSetttings"。  
然后，通过重写相关函数，您可以将图表元素的文本设置为您自己的语言。  
代码示例:  
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

## **为图表配置中文设置**  

在这一步，您将使用在前一步中定义的类 "ChartChineseSetttings"。  
代码示例:  

```javascript  
const Workbook = require('aspose.cells');  
const wb = new Workbook("Chinese.xls");  
wb.settings.globalizationSettings.chartSettings = new ChartChineseSetttings();  
const chart0 = wb.worksheets[0].charts[0];  
chart0.toImage("Output.png");  
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

{{< app/cells/assistant language="nodejs-cpp" >}}
