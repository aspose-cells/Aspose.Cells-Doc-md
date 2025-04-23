---  
title: 将图表转换为支持日本地区的图像，使用 Node.js via C++  
description: 学习如何使用 Aspose.Cells for Node.js via C++ 设置支持日文字符和格式的图表。我们的指南将演示如何配置图表以支持日文字体、大小、文本方向等。  
keywords: Aspose.Cells for Node.js via C++，图表，日语配置，字体，字体大小，文本方向，支持。  
linktitle: 设置日本地区  
type: docs  
weight: 10  
url: /zh/nodejs-cpp/convert-chart-to-image-for-japanese-region/  
alias: [/nodejs-cpp/set-japanese-configuration-for-chart/]  
---  

{{% alert color="primary" %}}  
在本主题中，我们将向您展示如何为图表设置日本地区。  
{{% /alert %}}  

## **定义继承类**  

第一步，您需要定义一个继承自 [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/) 的 "ChartJapaneseSettings" 类。  
然后，通过重写相关函数，您可以将图表元素的文本设置为您自己的语言。  
代码示例:  
```javascript
const AsposeCells = require("aspose.cells.node");

class ChartJapaneseSettings extends AsposeCells.ChartGlobalizationSettings {
getAxisTitleName() {
return "軸タイトル";
}

getAxisUnitName(type) {
switch (type) {
case AsposeCells.DisplayUnitType.None:
return '';
case AsposeCells.DisplayUnitType.Hundreds:
return "百";
case AsposeCells.DisplayUnitType.Thousands:
return "千";
case AsposeCells.DisplayUnitType.TenThousands:
return "万";
case AsposeCells.DisplayUnitType.HundredThousands:
return "10万";
case AsposeCells.DisplayUnitType.Millions:
return "百万";
case AsposeCells.DisplayUnitType.TenMillions:
return "千万";
case AsposeCells.DisplayUnitType.HundredMillions:
return "億";
case AsposeCells.DisplayUnitType.Billions:
return "10億";
case AsposeCells.DisplayUnitType.Trillions:
return "兆";
default:
return '';
}
}

getChartTitleName() {
return "グラフ タイトル";
}

getLegendDecreaseName() {
return "削減";
}

getLegendIncreaseName() {
return "ぞうか";
}

getLegendTotalName() {
return "すべての";
}

getOtherName() {
return "その他";
}

getSeriesName() {
return "シリーズ";
}
}
```  

## **为图表配置日本设置**  

在此步骤中，您将使用上一节中定义的 "ChartJapaneseSettings" 类。  
代码示例:  

```javascript  
const { Workbook } = require('aspose.cells');

let wb = new Workbook("Japanese.xls");
wb.settings.globalizationSettings.chartSettings = new ChartJapaneseSettings();
let chart0 = wb.worksheets[0].charts[0];
chart0.toImage("Output.png");
```

然后，您可以在输出图像中看到效果，图表中的元素将根据您的设置进行渲染。  

## **结论**  

在此示例中，如果不为图表设置日本地区，则以下图表元素可能以默认语言（如英文）呈现。  
在上述操作后，我们可以获得一个具有日本区域的输出图表图片。  

|**支持的元素**|**本示例中的值**|**英文环境中的默认值**|  
| :- | :- | :- |  
|轴标题名称|軸タイトル|Axis Title|  
|轴单位名称|百,千...|Hundreds, Thousands...|  
|图表标题名称|グラフ タイトル|Chart Title|  
|图例增加名称|ぞうか|Increase|  
|图例减少名称|削減|Decrease|  
|图例总数名称|すべての|Total|  
|其它名称|その他|Other|  
|系列名称|シリーズ|Series|  

