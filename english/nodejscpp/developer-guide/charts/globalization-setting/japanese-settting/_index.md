---  
title: Convert Chart to Image for Japanese Region with Node.js via C++  
description: Learn how to use Aspose.Cells for Node.js via C++ to set the Japanese configuration for the chart. Our guide will demonstrate how to configure charts to support Japanese characters and formatting, including fonts, size, text direction, and more.  
keywords: Aspose.Cells for Node.js via C++, Charts, Japanese configuration, font, font size, text direction, support.  
linktitle: Set Japanese Region  
type: docs  
weight: 10  
url: /nodejs-cpp/convert-chart-to-image-for-japanese-region/  
alias: [/nodejs-cpp/set-japanese-configuration-for-chart/]  
---  

{{% alert color="primary" %}}  
In this topic, we will show you how to set Japanese Region for a chart.  
{{% /alert %}}  

## **Defines an inheritance class**  

First step, you need to define a class "ChartJapaneseSettings" that inherits from [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/).  
Then, by rewriting the related functions, you can set the text of the chart elements in your own language.  
Code example:  
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

## **Config Japanese Setting For Chart**  

In this step, you will use the class "ChartJapaneseSettings" you defined in the previous step.  
Code example:  

```javascript  
const { Workbook } = require('aspose.cells');

let wb = new Workbook("Japanese.xls");
wb.settings.globalizationSettings.chartSettings = new ChartJapaneseSettings();
let chart0 = wb.worksheets[0].charts[0];
chart0.toImage("Output.png");
```

Then you can see the effect in the output image, the elements in the chart will be rendered according to your settings.  

## **Conclusion**  

In this example, if you do not set Japanese Region for a chart, the following chart elements may be rendered in the default language, such as English.  
After the above operation, we can get an output chart picture with Japanese Region.  

|**Supported elements**|**Value in this example**|**default value in the English environment**|  
| :- | :- | :- |  
|Axis Title Name|軸タイトル|Axis Title|  
|Axis Unit Name|百,千...|Hundreds, Thousands...|  
|Chart Title Name|グラフ タイトル|Chart Title|  
|Legend Increase Name|ぞうか|Increase|  
|Legend Decrease Name|削減|Decrease|  
|Legend Total Name|すべての|Total|  
|Other Name|その他|Other|  
|Series Name|シリーズ|Series|  
  