---
title: Converti grafico in immagine per la regione cinese
linktitle: Impostare la regione cinese
type: docs
weight: 9
url: /it/net/convert-chart-to-image-for-chinese-region/
alias: [/net/set-chinese-configuration-for-chart/]
---
{{% alert color="primary" %}}

In questo argomento, ti mostreremo come impostare la regione cinese per un grafico.

{{% /alert %}}

##  **Definisce una classe di ereditarietà**

Primo passaggio, è necessario definire una classe "ChartChineseSetttings" da cui ereditare[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
Poi, riscrivendo le relative funzioni, puoi impostare il testo degli elementi del grafico nella tua lingua.
Esempio di codice:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartChineseSetttings.cs" >}}

##  **Impostazione cinese di configurazione per il grafico**

In questo passaggio utilizzerai la classe "ChartChineseSetttings" definita nel passaggio precedente.
Esempio di codice:

```
	Workbook wb = new Workbook("Chinese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartChineseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

Quindi puoi vedere l'effetto nell'immagine di output, gli elementi nel grafico verranno renderizzati in base alle tue impostazioni.

##  **Conclusione**

In questo esempio, se non si imposta la regione cinese per un grafico, i seguenti elementi del grafico potrebbero essere visualizzati nella lingua predefinita, ad esempio l'inglese.
Dopo l'operazione di cui sopra, possiamo ottenere un'immagine del grafico di output con la regione cinese.

|**Elementi supportati**|**Valore in questo esempio**|**valore predefinito nell'ambiente inglese**|
| :- | :- | :- |
|Nome del titolo dell'asse|坐标轴标题|Titolo dell'asse|
|Nome unità asse|百,千...|Centinaia, migliaia...|
|Titolo del grafico Nome|图表标题|Titolo grafico|
|Legenda Aumenta nome|增加|Aumento|
|Legenda Diminuisci nome|减少|Diminuire|
|Legenda Nome totale|汇总|Totale|
|Altro nome|其他|Altro|
|Nome della serie|系列|Serie|
