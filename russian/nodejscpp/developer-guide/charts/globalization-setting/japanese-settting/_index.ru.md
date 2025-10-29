---  
title: Конвертация диаграммы в изображение для японского региона с Node.js через C++  
description: Узнайте, как использовать Aspose.Cells for Node.js via C++ для настройки японской конфигурации диаграммы. Наш гид демонстрирует, как настроить диаграммы для поддержки японских символов и форматирования, включая шрифты, размер, направление текста и другое.  
keywords: Aspose.Cells for Node.js via C++, диаграммы, японская настройка, шрифт, размер шрифта, направление текста, поддержка.  
linktitle: Установить японский регион  
type: docs  
weight: 10  
url: /ru/nodejs-cpp/convert-chart-to-image-for-japanese-region/  
alias: [/nodejs-cpp/set-japanese-configuration-for-chart/]  
---  

{{% alert color="primary" %}}  
В этой теме мы покажем вам, как установить японский регион для диаграммы.  
{{% /alert %}}  

## **Определяет класс наследования**  

Первый шаг — определить класс "ChartJapaneseSettings", наследующий от [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/).  
Затем, переписав соответствующие функции, вы можете установить текст элементов диаграммы на своем собственном языке.  
Пример кода:  
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

## **Настройка японских настроек для диаграммы**  

На этом этапе вы используете класс "ChartJapaneseSettings", определённый на предыдущем шаге.  
Пример кода:  

```javascript  
const { Workbook } = require('aspose.cells');

let wb = new Workbook("Japanese.xls");
wb.settings.globalizationSettings.chartSettings = new ChartJapaneseSettings();
let chart0 = wb.worksheets[0].charts[0];
chart0.toImage("Output.png");
```

Затем вы можете увидеть эффект на выходном изображении, элементы на диаграмме будут отображаться в соответствии с вашими настройками.  

## **Заключение**  

В этом примере, если вы не установите японскую регион для диаграммы, следующие элементы диаграммы могут быть отображены на языке по умолчанию, таком как английский.  
После вышеуказанных операций мы можем получить выходное изображение диаграммы с японским регионом.  

|**Поддерживаемые элементы**|**Значение в этом примере**|**значение по умолчанию в английской среде**|  
| :- | :- | :- |  
|Название оси|軸タイトル|Название оси|  
|Единица оси|百,千...|Сотни, тысячи...|  
|Название диаграммы|グラフ タイトル|Название диаграммы|  
|Название легенды увеличения|ぞうか|Увеличение|  
|Название легенды уменьшения|削減|Уменьшение|  
|Название общего легенды|すべての|Всего|  
|Прочие название|その他|Другое|  
|Название серии|シリーズ|Серии|  

{{< app/cells/assistant language="nodejs-cpp" >}}
