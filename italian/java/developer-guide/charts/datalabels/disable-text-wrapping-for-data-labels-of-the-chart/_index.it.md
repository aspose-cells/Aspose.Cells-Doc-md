---
title: Disabilita il rientro del testo per le etichette dei dati del grafico
type: docs
weight: 60
url: /it/java/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013 consente agli utenti di andare a capo o non andare a capo il testo all'interno delle etichette dati di un grafico. In genere, il testo dell'etichetta dati è andato a capo.

{{% /alert %}}

Aspose.Cells fornisce il metodo [**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped). Imposta su **True** o **False** per abilitare o disabilitare il testo a capo sulle etichette dati rispettivamente.

Allo stesso modo, utilizza il metodo [**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped) per verificare se un'etichetta dati è già andata a capo.

Questa schermata mostra un campione di file Microsoft Excel contenente un grafico in cui il testo delle etichette dati è andato a capo. Come puoi vedere, puoi selezionare o deselezionare l'opzione **Andamento testo nella forma** nella sezione ALLINEAMENTO del pannello Formato etichette dati in Microsoft Excel 2013.

**Andamento etichette dati**

![todo:image_alt_text](disable-text-wrapping-for-data-labels-of-the-chart_1.png)

Il codice di esempio che segue carica il file di esempio di Microsoft Excel utilizzando Aspose.Cells e disabilita il testo a capo delle etichette dati utilizzando il metodo [**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped). Quando il codice viene eseguito, il grafico appare così. Il testo precedentemente andato a capo ora non è più andato a capo.

**Visualizzazione di etichette dati su una sola riga**

![todo:image_alt_text](disable-text-wrapping-for-data-labels-of-the-chart_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableTextWrapping-DisableTextWrapping.java" >}}
{{< app/cells/assistant language="java" >}}
