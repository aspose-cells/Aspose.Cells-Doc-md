---  
title: Converti Grafico in Immagine per la Regione Giapponese con Node.js tramite C++  
description: Impara come usare Aspose.Cells for Node.js via C++ per impostare la configurazione giapponese per il grafico. La nostra guida dimostrerà come configurare i grafici per supportare caratteri e formattazioni giapponesi, inclusi font, dimensioni, direzione del testo e altro.  
keywords: Aspose.Cells for Node.js via C++, Grafici, configurazione giapponese, font, dimensione font, direzione del testo, supporto.  
linktitle: Imposta Regione Giapponese  
type: docs  
weight: 10  
url: /it/nodejs-cpp/convert-chart-to-image-for-japanese-region/  
alias: [/nodejs-cpp/set-japanese-configuration-for-chart/]  
---  

{{% alert color="primary" %}}  
In questo argomento, ti mostreremo come impostare la Regione Giapponese per un grafico.  
{{% /alert %}}  

## **Definisce una classe di ereditarietà**  

 Primo passo, devi definire una classe "ChartJapaneseSettings" che eredita da [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/).  
Poi, riscrivendo le funzioni correlate, è possibile impostare il testo degli elementi del grafico nella propria lingua.  
Esempio di codice:  
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

## **Configura Impostazione Giapponese per Grafico**  

 In questo passo, utilizzerai la classe "ChartJapaneseSettings" che hai definito nel passo precedente.  
Esempio di codice:  

```javascript  
const { Workbook } = require('aspose.cells');

let wb = new Workbook("Japanese.xls");
wb.settings.globalizationSettings.chartSettings = new ChartJapaneseSettings();
let chart0 = wb.worksheets[0].charts[0];
chart0.toImage("Output.png");
```

Poi puoi vedere l'effetto nell'immagine di output, gli elementi nel grafico saranno resi in base alle tue impostazioni.  

## **Conclusioni**  

In questo esempio, se non si imposta la Regione Giapponese per un grafico, gli elementi del grafico seguenti potrebbero essere resi nella lingua predefinita, come l'inglese.  
Dopo l'operazione sopra, possiamo ottenere un'immagine del grafico di output con la Regione Giapponese.  

|**Elementi supportati**|**Valore in questo esempio**|**valore predefinito nell'ambiente inglese**|  
| :- | :- | :- |  
|Nome del titolo dell'asse|軸タイトル|Titolo dell'asse|  
|Nome dell'unità dell'asse|百,千...|Centinaia, Migliaia...|  
|Nome del titolo del grafico|グラフ タイトル|Titolo del grafico|  
|Nome incremento legenda|ぞうか|Aumento|  
|Nome decremento legenda|削減|Decremento|  
|Nome totale legenda|すべての|Totale|  
|Altro nome|その他|Altro|  
|Nome serie|シリーズ|Serie|  

{{< app/cells/assistant language="nodejs-cpp" >}}
