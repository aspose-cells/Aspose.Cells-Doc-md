---  
title: Diagramm in Bild für chinesische Region mit Node.js über C++ konvertieren  
description: Erfahren Sie, wie Sie Aspose.Cells for Node.js via C++ verwenden, um Diagramme für chinesische Zeichen und Formate zu konfigurieren, einschließlich Schriftarten, Größen, Textausrichtung und mehr.  
keywords: Aspose.Cells für Node.js, Diagramme, Chinesische Konfiguration, Schriftarten, Schriftgröße, Textausrichtung, Unterstützung.  
linktitle: Chinesische Region festlegen  
type: docs  
weight: 9  
url: /de/nodejs-cpp/convert-chart-to-image-for-chinese-region/  
alias: [/nodejs-cpp/set-chinese-configuration-for-chart/]  
---  

{{% alert color="primary" %}}  
In diesem Thema zeigen wir Ihnen, wie Sie eine chinesische Region für ein Diagramm festlegen können.  
{{% /alert %}}  

## **Definiert eine Vererbungsklasse**  

Der erste Schritt besteht darin, eine Klasse "ChartChineseSetttings" zu definieren, die von [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/) erbt.  
Dann können Sie durch Neudefinition der entsprechenden Funktionen den Text der Diagrammelemente in Ihrer eigenen Sprache festlegen.  
Codebeispiel:  
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

## **Konfigurieren Sie die chinesischen Einstellungen für das Diagramm**  

In diesem Schritt verwenden Sie die Klasse "ChartChineseSetttings", die Sie im vorherigen Schritt definiert haben.  
Codebeispiel:  

```javascript  
const Workbook = require('aspose.cells');  
const wb = new Workbook("Chinese.xls");  
wb.settings.globalizationSettings.chartSettings = new ChartChineseSetttings();  
const chart0 = wb.worksheets[0].charts[0];  
chart0.toImage("Output.png");  
```  

Dann können Sie den Effekt im Ausgabebild sehen, die Elemente im Diagramm werden gemäß Ihren Einstellungen gerendert.  

## **Fazit**  

In diesem Beispiel, wenn Sie keine chinesische Region für ein Diagramm festlegen, werden die folgenden Diagrammelemente möglicherweise in der Standardsprache, wie Englisch, gerendert.  
Nach der oben genannten Operation können wir ein Ausgabediagrammbild mit chinesischer Region erhalten.  

|**Unterstützte Elemente**|**Wert in diesem Beispiel**|**Standardwert in der englischen Umgebung**|  
| :- | :- | :- |  
|Axis Title Name|坐标轴标题|Achsentitel|  
|Achsenbezeichnung|百,千...|Hunderte, Tausende...|  
|Chart Title Name|图表标题|Diagrammtitel|  
|Legend Increase Name|增加|Zunahme|  
|Legend Decrease Name|减少|Rückgang|  
|Legend Total Name|汇总|Gesamt|  
|Other Name|其他|Sonstige|  
|Series Name|系列|Serie|  

