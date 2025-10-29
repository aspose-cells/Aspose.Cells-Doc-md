---  
title: Конвертация диаграммы в изображение для китайского региона с Node.js через C++  
description: Узнайте, как использовать Aspose.Cells for Node.js via C++ для настройки диаграмм для китайских символов и форматов, включая шрифты, размеры, направления текста и многое другое.  
keywords: Aspose.Cells для Node.js, диаграммы, настройка для Китая, шрифты, размер шрифта, направление текста, поддержка.  
linktitle: Установить китайский регион  
type: docs  
weight: 9  
url: /ru/nodejs-cpp/convert-chart-to-image-for-chinese-region/  
alias: [/nodejs-cpp/set-chinese-configuration-for-chart/]  
---  

{{% alert color="primary" %}}  
В этой теме мы покажем вам, как установить китайский регион для графика.  
{{% /alert %}}  

## **Определяет класс наследования**  

Первый шаг — определить класс "ChartChineseSetttings", который наследуется от [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/).  
Затем, переписав соответствующие функции, вы можете установить текст элементов диаграммы на своем собственном языке.  
Пример кода:  
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

## **Настройте китайские настройки для графика**  

На этом этапе вы будете использовать класс "ChartChineseSetttings", который вы определили на предыдущем этапе.  
Пример кода:  

```javascript  
const Workbook = require('aspose.cells');  
const wb = new Workbook("Chinese.xls");  
wb.settings.globalizationSettings.chartSettings = new ChartChineseSetttings();  
const chart0 = wb.worksheets[0].charts[0];  
chart0.toImage("Output.png");  
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

{{< app/cells/assistant language="nodejs-cpp" >}}
