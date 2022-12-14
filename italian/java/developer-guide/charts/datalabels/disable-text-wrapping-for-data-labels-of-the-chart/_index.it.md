---
title: Disabilita la disposizione del testo per le etichette dati del grafico
type: docs
weight: 60
url: /it/java/disable-text-wrapping-for-data-labels-of-the-chart/
---
{{% alert color="primary" %}}

Microsoft Excel 2013 consente agli utenti di disporre o separare il testo all'interno delle etichette dei dati di un grafico. Per impostazione predefinita, il testo dell'etichetta dati è a capo.

{{% /alert %}}

Aspose.Cells fornisce il[**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped) metodo. Impostato**Vero** o**Falso** rispettivamente per abilitare o disabilitare la disposizione del testo sulle etichette dei dati.

 Allo stesso modo, usa il[**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)metodo per scoprire se un'etichetta dati è già racchiusa.

Questa schermata mostra un file Excel Microsoft di esempio contenente un grafico in cui è racchiuso il testo delle etichette dei dati. Come puoi vedere, puoi controllare o cancellare il file**Avvolgi il testo in forma** opzione nella sezione ALLINEAMENTO del pannello Formato etichette dati in Microsoft Excel 2013.

**Avvolgere etichette dati**

![cose da fare:immagine_alt_testo](disable-text-wrapping-for-data-labels-of-the-chart_1.png)

 Il codice di esempio che segue carica il file Excel Microsoft di esempio utilizzando Aspose.Cells e disabilita il ritorno a capo del testo dell'etichetta dati utilizzando il[**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)metodo. Quando il codice viene eseguito, il grafico ha questo aspetto. Il testo precedentemente inserito viene ora scartato.

**Visualizzazione delle etichette dei dati su una sola riga**

![cose da fare:immagine_alt_testo](disable-text-wrapping-for-data-labels-of-the-chart_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableTextWrapping-DisableTextWrapping.java" >}}
