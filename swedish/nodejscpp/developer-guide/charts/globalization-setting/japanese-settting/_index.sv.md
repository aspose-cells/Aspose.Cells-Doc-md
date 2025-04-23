---  
title: Konvertera diagram till bild för japansk region med Node.js via C++  
description: Lär dig hur man använder Aspose.Cells for Node.js via C++ för att ställa in japansk konfiguration för diagrammet. Vår guide visar hur man konfigurerar diagram för att stödja japanska tecken och formatering, inklusive typsnitt, storlek, texts riktning och mer.  
keywords: Aspose.Cells for Node.js via C++, Diagram, Japansk konfiguration, typsnitt, teckenstorlek, texts riktning, stöd.  
linktitle: Ställ in japansk region  
type: docs  
weight: 10  
url: /sv/nodejs-cpp/convert-chart-to-image-for-japanese-region/  
alias: [/nodejs-cpp/set-japanese-configuration-for-chart/]  
---  

{{% alert color="primary" %}}  
I det här ämnet kommer vi att visa dig hur du ställer in japansk region för ett diagram.  
{{% /alert %}}  

## **Definierar en arvs klass**  

 Första steget, du behöver definiera en klass "ChartJapaneseSettings" som ärver från [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/).  
Sedan, genom att omdefiniera relaterade funktioner, kan du ange texten i diagramelementen på ditt eget sprak.  
Kodexempel:  
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

## **Konfigurera japanska inställningar för diagram**  

 I detta steg kommer du använda klassen "ChartJapaneseSettings" du definierade i föregående steg.  
Kodexempel:  

```javascript  
const { Workbook } = require('aspose.cells');

let wb = new Workbook("Japanese.xls");
wb.settings.globalizationSettings.chartSettings = new ChartJapaneseSettings();
let chart0 = wb.worksheets[0].charts[0];
chart0.toImage("Output.png");
```

Sedan kan du se effekten i utdata bilden, elementen i diagrammet kommer att renderas enligt dina inställningar.  

## **Slutsats**  

I det här exemplet, om du inte anger japansk region för ett diagram, kan följande diagramelement renderas på standardspråket, såsom engelska.  
Efter ovanstående operation kan vi få en utdata-diagrambild med japansk region.  

|**Stödda element**|**Värde i detta exempel**|**Standardvärde i den engelska miljön**|  
| :- | :- | :- |  
|axeltitelnamn|軸タイトル|Axeltitel|  
|axelenhetsnamn|百,千...|Hundratals, Tusentals...|  
|diagramtitelnamn|グラフ タイトル|Diagramtitel|  
|legend öka namn|ぞうか|Ökning|  
|legend minskning namn|削減|Minskning|  
|legend totalt namn|すべての|Totalt|  
|annat namn|その他|Övrigt|  
|Serienamn|シリーズ|Serie|  

