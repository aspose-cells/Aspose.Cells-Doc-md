---
title: Converti grafico in immagine per la regione cinese
description: Scopri come utilizzare Aspose.Cells for .NET imposta la configurazione cinese per i grafici. La nostra guida mostrerà come configurare i grafici per supportare caratteri e formati cinesi, inclusi caratteri, dimensioni, indicazioni del testo e altro ancora.
keywords: Aspose.Cells for .NET, Charts, Chinese Configuration, Fonts, Font Size, Text Direction, Support.
linktitle: Imposta la regione cinese
type: docs
weight: 9
url: /it/net/convert-chart-to-image-for-chinese-region/
alias: [/net/set-chinese-configuration-for-chart/]
---
{{% alert color="primary" %}}

In questo argomento ti mostreremo come impostare la regione cinese per un grafico.

{{% /alert %}}

##  **Definisce una classe di ereditarietà**

 Primo passo, è necessario definire una classe "ChartChineseSetttings" da cui ereditare[**GraficoGlobalizzazioneImpostazioni**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
Successivamente, riscrivendo le relative funzioni, potrai impostare il testo degli elementi del grafico nella tua lingua.
Esempio di codice:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartChineseSetttings.cs" >}}

##  **Impostazione cinese di configurazione per il grafico**

In questo passaggio utilizzerai la classe "ChartChineseSetttings" che hai definito nel passaggio precedente.
Esempio di codice:

```
	Workbook wb = new Workbook("Chinese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartChineseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

Quindi puoi vedere l'effetto nell'immagine di output, gli elementi nel grafico verranno renderizzati in base alle tue impostazioni.

##  **Conclusione**

In questo esempio, se non imposti la regione cinese per un grafico, i seguenti elementi del grafico potrebbero essere visualizzati nella lingua predefinita, ad esempio l'inglese.
Dopo l'operazione di cui sopra, possiamo ottenere un'immagine del grafico di output con la regione cinese.

|**Elementi supportati**|**Valore in questo esempio**|**valore predefinito nell'ambiente inglese**|
| :- | :- | :- |
|Nome del titolo dell'asse|坐标轴标题|Titolo dell'Asse|
|Nome dell'unità dell'asse|百,千...|Centinaia, migliaia...|
|Nome del titolo del grafico|图表标题|Titolo del grafico|
|Legenda Aumenta nome|增加|Aumento|
|Legenda Riduci nome|减少|Diminuire|
|Nome totale della legenda|汇总|Totale|
|Altro nome|其他|Altro|
|Nome della serie|系列|Serie|
