---  
title: Converti Grafico in Immagine per la Regione Cinese con Node.js tramite C++  
description: Impara come usare Aspose.Cells for Node.js via C++ per configurare grafici per caratteri cinesi e formati, inclusi font, dimensioni, direzioni del testo e altro.  
keywords: Aspose.Cells per Node.js, Grafici, Configurazione Cinese, Font, Dimensione Font, Direzione del Testo, Supporto.  
linktitle: Imposta la regione cinese  
type: docs  
weight: 9  
url: /it/nodejs-cpp/convert-chart-to-image-for-chinese-region/  
alias: [/nodejs-cpp/set-chinese-configuration-for-chart/]  
---  

{{% alert color="primary" %}}  
In questo argomento, ti mostreremo come impostare la regione cinese per un grafico.  
{{% /alert %}}  

## **Definisce una classe di ereditarietà**  

 Primo passo, devi definire una classe "ChartChineseSetttings" che eredita da [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/).  
Poi, riscrivendo le funzioni correlate, è possibile impostare il testo degli elementi del grafico nella propria lingua.  
Esempio di codice:  
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

## **Configurare Impostazione Cinese Per Grafico**  

In questo passaggio, utilizzerai la classe "ChartChineseSetttings" che hai definito nel passaggio precedente.  
Esempio di codice:  

```javascript  
const Workbook = require('aspose.cells');  
const wb = new Workbook("Chinese.xls");  
wb.settings.globalizationSettings.chartSettings = new ChartChineseSetttings();  
const chart0 = wb.worksheets[0].charts[0];  
chart0.toImage("Output.png");  
```  

Poi puoi vedere l'effetto nell'immagine di output, gli elementi nel grafico saranno resi in base alle tue impostazioni.  

## **Conclusioni**  

In questo esempio, se non imposti la regione cinese per un grafico, determinati elementi del grafico potrebbero essere renderizzati nella lingua predefinita, come l'inglese.  
Dopo l'operazione precedente, possiamo ottenere un'immagine del grafico in uscita con la regione cinese.  

|**Elementi supportati**|**Valore in questo esempio**|**valore predefinito nell'ambiente inglese**|  
| :- | :- | :- |  
|Nome titolo asse|坐标轴标题|Titolo asse|  
|Nome dell'unità dell'asse|百,千...|Centinaia, Migliaia...|  
|Nome titolo grafico|图表标题|Titolo grafico|  
|Nome leggenda aumento|增加|Aumento|  
|Nome della Riduzione Leggenda|减少|Ridurre|  
|Nome della Somma Totale Leggenda|汇总|Totale|  
|Altro Nome|其他|Altro|  
|Nome della Serie Leggenda|系列|Serie|  

{{< app/cells/assistant language="nodejs-cpp" >}}
