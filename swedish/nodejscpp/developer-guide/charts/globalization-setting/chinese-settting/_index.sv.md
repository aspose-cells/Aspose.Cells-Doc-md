---  
title: Konvertera diagram till bild för kinesisk region med Node.js via C++  
description: Lär dig hur man använder Aspose.Cells for Node.js via C++ för att konfigurera diagram för kinesiska tecken och format, inklusive typsnitt, storlekar, texts riktningar och mer.  
keywords: Aspose.Cells för Node.js, Diagram, Kinesisk konfiguration, Typsnitt, Teckenstorlek, Textriktning, Stöd.  
linktitle: Ställ in kinesisk region  
type: docs  
weight: 9  
url: /sv/nodejs-cpp/convert-chart-to-image-for-chinese-region/  
alias: [/nodejs-cpp/set-chinese-configuration-for-chart/]  
---  

{{% alert color="primary" %}}  
I det här ämnet kommer vi att visa dig hur du ställer in kinesisk region för ett diagram.  
{{% /alert %}}  

## **Definierar en arvs klass**  

 Första steget, du måste definiera en klass "ChartChineseSetttings" som ärver från [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/).  
Sedan, genom att omdefiniera relaterade funktioner, kan du ange texten i diagramelementen på ditt eget sprak.  
Kodexempel:  
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

## **Konfigurera kinesiska inställningar för diagram**  

I det här steget kommer du att använda klassen "ChartChineseSetttings" du har definierat i det föregående steget.  
Kodexempel:  

```javascript  
const Workbook = require('aspose.cells');  
const wb = new Workbook("Chinese.xls");  
wb.settings.globalizationSettings.chartSettings = new ChartChineseSetttings();  
const chart0 = wb.worksheets[0].charts[0];  
chart0.toImage("Output.png");  
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

{{< app/cells/assistant language="nodejs-cpp" >}}
