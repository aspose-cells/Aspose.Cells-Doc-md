---
title: Converti Grafico in Immagine per la Regione Giapponese
description: Impara come utilizzare Aspose.Cells for .NET imposta la configurazione giapponese per il grafico. La nostra guida mostrerà come configurare i grafici per supportare caratteri e formattazione giapponesi, inclusi caratteri, dimensioni, direzione del testo e altro.
keywords: Aspose.Cells for .NET, Grafici, configurazione giapponese, carattere, dimensione carattere, direzione del testo, supporto.
linktitle: Imposta Regione Giapponese
type: docs
weight: 10
url: /it/net/convert-chart-to-image-for-japanese-region/
alias: [/net/set-japanese-configuration-for-chart/]
---

{{% alert color="primary" %}}

In questo argomento, ti mostreremo come impostare la Regione Giapponese per un grafico.

{{% /alert %}}

## **Definisce una classe di ereditarietà**

Primo passo, è necessario definire una classe "ChartJapaneseSetttings" che eredita da [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
Poi, riscrivendo le funzioni correlate, è possibile impostare il testo degli elementi del grafico nella propria lingua.
Esempio di codice:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartJapaneseSetttings.cs" >}}

## **Configura Impostazione Giapponese per Grafico**

In questo passaggio, userai la classe "ChartJapaneseSetttings" che hai definito nel passaggio precedente.
Esempio di codice:

```
	Workbook wb = new Workbook("Japanese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartJapaneseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
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
