---
title: Copia Sparkline specificando intervallo dati e posizione del gruppo di Sparkline
type: docs
weight: 120
url: /it/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

Copia Sparkline specificando intervallo dati e posizione del gruppo di Sparkline in MS Excel

Microsoft Excel consente di copiare una Sparkline specificando l'intervallo dati e la posizione del gruppo di Sparkline. Segui questi passaggi per copiare la tua Sparkline su altre celle.

- Seleziona la cella contenente la tua Sparkline.
- Seleziona **Modifica dati** dalla sezione **Sparkline** all'interno della scheda **Design**
- Scegli **Modifica Posizione Gruppo & Dati...**
- Specifica l'intervallo dei dati e la posizione e fai clic su OK.

## Esempio

Aspose.Cells fornisce il metodo [**SparklineCollection.add(dataRange, row, column)**](https://reference.aspose.com/cells/java/com.aspose.cells/SparklineCollection) per specificare l'intervallo dei dati e la posizione del gruppo di Sparkline.

### Schermate dei file sorgente e di output

La seguente schermata mostra il file Excel sorgente utilizzato nel codice. L'area evidenziata in rosso mostra l'opzione "**Modifica Posizione Gruppo & Dati...**" per specificare l'intervallo dati e la posizione del gruppo di sparkline. La cella P4 mostra la sparkline che verrà copiata nelle altre quattro celle riempite di colore giallo utilizzando Aspose.Cells.

![todo:image_alt_text](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_1.png)

La seguente schermata mostra il file Excel di output generato dal codice di esempio. Come puoi vedere, la sparkline nella cella P4 è stata copiata nelle quattro celle successive nella colonna P ciascuna con un intervallo dati diverso.

![todo:image_alt_text](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_2.png)

### Codice Java per copiare la sparkline specificando l'intervallo dati e la posizione del gruppo di sparkline

Il seguente codice di esempio carica il file Excel sorgente come mostrato nella schermata sopra, quindi accede al primo gruppo di sparkline e aggiunge intervalli di dati e posizioni all'interno del gruppo di sparkline. Infine, scrive il file Excel di output su disco che è anche mostrato nella schermata sopra.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopySparkline-CopySparkline.java" >}}
{{< app/cells/assistant language="java" >}}
