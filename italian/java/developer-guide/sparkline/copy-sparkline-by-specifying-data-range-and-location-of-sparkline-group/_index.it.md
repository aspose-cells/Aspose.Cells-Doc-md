---
title: Copia sparkline specificando l'intervallo di dati e la posizione del gruppo sparkline
type: docs
weight: 120
url: /it/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---
Copia sparkline specificando l'intervallo di dati e la posizione del gruppo sparkline in MS Excel

Microsoft Excel consente di copiare uno sparkline specificando l'intervallo di dati e la posizione del gruppo sparkline. Segui questi passaggi per copiare il tuo Sparkline in altre celle.

- Seleziona la cella contenente il tuo Sparkline.
-  Selezionare**Modifica dati** dal**Scintilla** sezione all'interno del**Design** scheda
-  Scegliere**Modifica posizione e dati del gruppo...**
- Specificare l'intervallo di dati e la posizione e fare clic su OK.

## Esempio

 Aspose.Cells fornisce il[**SparklineCollection.add(dataRange, riga, colonna)**](https://reference.aspose.com/cells/java/com.aspose.cells/SparklineCollection) metodo per specificare l'intervallo di dati e la posizione del gruppo sparkline.

### Screenshot dei file di origine e di output

Lo screenshot seguente mostra il file Excel di origine utilizzato all'interno del codice. L'area evidenziata in rosso mostra "**Modifica posizione e dati del gruppo...**" opzione per specificare l'intervallo di dati e la posizione del gruppo sparkline. La cella P4 mostra la sparkline che verrà copiata nelle altre quattro celle riempite di colore giallo utilizzando Aspose.Cells.

![cose da fare:immagine_alt_testo](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_1.png)

Lo screenshot seguente mostra il file Excel di output generato dal codice di esempio. Come puoi vedere, la sparkline nella cella P4 è stata copiata nelle successive quattro celle nella colonna P ciascuna con un intervallo di dati diverso.

![cose da fare:immagine_alt_testo](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_2.png)

### Java codice per copiare il grafico sparkline specificando l'intervallo di dati e la posizione del gruppo sparkline

Il seguente codice di esempio carica il file Excel di origine come mostrato nello screenshot precedente, quindi accede al primo gruppo sparkline e aggiunge intervalli di dati e posizioni all'interno del gruppo sparkline. Infine, scrive il file Excel di output su disco, mostrato anche nello screenshot qui sopra.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopySparkline-CopySparkline.java" >}}
