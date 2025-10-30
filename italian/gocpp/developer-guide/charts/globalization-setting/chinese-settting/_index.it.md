---
title: Converti il grafico in immagine per la regione cinese con Golang via C++
linktitle: Imposta la regione cinese
description: Impara come usare Aspose.Cells for C++ per impostare la configurazione cinese per i grafici. La nostra guida dimostrerà come configurare i grafici per supportare i caratteri e i formati cinesi, inclusi font, dimensioni, direzioni del testo e altro.
keywords: Aspose.Cells for C++, Grafici, Configurazione cinese, Font, Dimensione font, Direzione del testo, Supporto.
type: docs
weight: 9
url: /it/go-cpp/convert-chart-to-image-for-chinese-region/
alias: [/cpp/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

In questo argomento, ti mostreremo come impostare la regione cinese per un grafico.

{{% /alert %}}

## **Definisce una classe di ereditarietà**

 Primo passo, devi definire una classe "ChartChineseSetttings" che eredita da [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/). 
Quindi, sovrascrivendo le funzioni correlate, puoi impostare il testo degli elementi del grafico nella tua lingua.

Esempio di codice:
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChineseSettting.go" >}}
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
