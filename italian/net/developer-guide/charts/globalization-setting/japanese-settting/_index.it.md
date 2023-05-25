---
title: Converti grafico in immagine per la regione giapponese
linktitle: Impostare la regione giapponese
type: docs
weight: 10
url: /it/net/convert-chart-to-image-for-japanese-region/
alias: [/net/set-japanese-configuration-for-chart/]
---
{{% alert color="primary" %}}

In questo argomento, ti mostreremo come impostare la regione giapponese per un grafico.

{{% /alert %}}

##  **Definisce una classe di ereditarietà**

 Primo passaggio, è necessario definire una classe "ChartJapaneseSetttings" da cui ereditare[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
Poi, riscrivendo le relative funzioni, puoi impostare il testo degli elementi del grafico nella tua lingua.
Esempio di codice:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartJapaneseSetttings.cs" >}}

##  **Configurazione impostazione giapponese per grafico**

In questo passaggio, utilizzerai la classe "ChartJapaneseSetttings" definita nel passaggio precedente.
Esempio di codice:

```
	Workbook wb = new Workbook("Japanese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartJapaneseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

Quindi puoi vedere l'effetto nell'immagine di output, gli elementi nel grafico verranno renderizzati in base alle tue impostazioni.

##  **Conclusione**

In questo esempio, se non si imposta Japanese Region per un grafico, i seguenti elementi del grafico potrebbero essere visualizzati nella lingua predefinita, ad esempio l'inglese.
Dopo l'operazione di cui sopra, possiamo ottenere un'immagine del grafico di output con la regione giapponese.

|**Elementi supportati**|**Valore in questo esempio**|**valore predefinito nell'ambiente inglese**|
| :- | :- | :- |
|Nome del titolo dell'asse|軸タイトル|Titolo dell'asse|
|Nome unità asse|百,千...|Centinaia, migliaia...|
|Titolo del grafico Nome|グラフ タイトル|Titolo grafico|
|Legenda Aumenta nome|ぞうか|Aumento|
|Legenda Diminuisci nome|削減|Diminuire|
|Legenda Nome totale|すべての|Totale|
|Altro nome|その他|Altro|
|Nome della serie|シリーズ|Serie|
