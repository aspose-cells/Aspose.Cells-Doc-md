---
title: Convertire il grafico in un immagine per la regione cinese
description: Scopri come utilizzare Aspose.Cells for .NET impostazioni di configurazione cinese per i grafici. La nostra guida mostrerà come configurare i grafici per supportare caratteri e formati cinesi, inclusi font, dimensioni, direzioni del testo e altro ancora.
keywords: Aspose.Cells for .NET, Grafici, Configurazione cinese, Caratteri, Dimensioni del font, Direzione del testo, Supporto.
linktitle: Imposta la regione cinese
type: docs
weight: 9
url: /it/net/convert-chart-to-image-for-chinese-region/
alias: [/net/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

In questo argomento, ti mostreremo come impostare la regione cinese per un grafico.

{{% /alert %}}

## **Definisce una classe di ereditarietà**

Primo passo, devi definire una classe "ChartChineseSetttings" che eredita da [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
Poi, riscrivendo le funzioni correlate, è possibile impostare il testo degli elementi del grafico nella propria lingua.
Esempio di codice:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartChineseSetttings.cs" >}}

## **Configurare Impostazione Cinese Per Grafico**

In questo passaggio, utilizzerai la classe "ChartChineseSetttings" che hai definito nel passaggio precedente.
Esempio di codice:

```
	Workbook wb = new Workbook("Chinese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartChineseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
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
