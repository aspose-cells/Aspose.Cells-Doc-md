---  
title: Diagramm in Bild für japanische Region mit Node.js über C++ konvertieren  
description: Erfahren Sie, wie Sie Aspose.Cells for Node.js via C++ verwenden, um die japanische Konfiguration für das Diagramm festzulegen. Unser Leitfaden demonstriert, wie Sie Diagramme konfigurieren, um japanische Zeichen und Formatierungen zu unterstützen, einschließlich Schriftarten, Größe, Textausrichtung und mehr.  
keywords: Aspose.Cells for Node.js via C++, Diagramme, Japanische Konfiguration, Schriftart, Schriftgröße, Textausrichtung, Unterstützung.  
linktitle: Japanische Region festlegen  
type: docs  
weight: 10  
url: /de/nodejs-cpp/convert-chart-to-image-for-japanese-region/  
alias: [/nodejs-cpp/set-japanese-configuration-for-chart/]  
---  

{{% alert color="primary" %}}  
In diesem Thema zeigen wir Ihnen, wie Sie die japanische Region für ein Diagramm festlegen können.  
{{% /alert %}}  

## **Definiert eine Vererbungsklasse**  

Der erste Schritt besteht darin, eine Klasse "ChartJapaneseSettings" zu definieren, die von [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/) erbt.  
Dann können Sie durch Neudefinition der entsprechenden Funktionen den Text der Diagrammelemente in Ihrer eigenen Sprache festlegen.  
Codebeispiel:  
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

## **Japanische Einstellung für Diagramm konfigurieren**  

In diesem Schritt verwenden Sie die Klasse "ChartJapaneseSettings", die Sie im vorherigen Schritt definiert haben.  
Codebeispiel:  

```javascript  
const { Workbook } = require('aspose.cells');

let wb = new Workbook("Japanese.xls");
wb.settings.globalizationSettings.chartSettings = new ChartJapaneseSettings();
let chart0 = wb.worksheets[0].charts[0];
chart0.toImage("Output.png");
```

Dann können Sie den Effekt im Ausgabebild sehen, die Elemente im Diagramm werden gemäß Ihren Einstellungen gerendert.  

## **Fazit**  

In diesem Beispiel, wenn Sie für ein Diagramm keine japanische Region festlegen, können die folgenden Diagrammelemente in der Standardsprache gerendert werden, wie zum Beispiel Englisch.  
Nach obiger Operation können wir ein Ausgabediagrammbild mit japanischer Region erhalten.  

|**Unterstützte Elemente**|**Wert in diesem Beispiel**|**Standardwert in der englischen Umgebung**|  
| :- | :- | :- |  
|Achsentitelname|軸タイトル|Achsentitel|  
|Achsenbezeichnung|百,千...|Hunderte, Tausende...|  
|Diagramm-Titelname|グラフ タイトル|Diagrammtitel|  
|Legende Anstiegsname|ぞうか|Erhöhen|  
|Legende Abnahmename|削減|Abnehmen|  
|Legende Gesamtname|すべての|Gesamt|  
|Andere Bezeichnung|その他|Andere|  
|Serienname|シリーズ|Serie|  

