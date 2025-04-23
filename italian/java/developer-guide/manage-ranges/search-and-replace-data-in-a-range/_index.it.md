---
title: Cerca e Sostituisci Dati in un Intervallo
type: docs
weight: 60
url: /it/java/search-and-replace-data-in-a-range/
description: Questo articolo mostra come cercare e sostituire dati in un intervallo in Excel utilizzando il codice Java.
keywords: java cerca e sostituisci dati in excel, java cerca dati in excel, java cerca e sostituisci dati in un intervallo, java cerca dati in un intervallo, ricerca dati in un intervallo in java, ricerca dati in un intervallo in java, ricerca dati in excel in java, java cerca dati in un intervallo, cerca e sostituisci dati in excel con java, cerca e sostituisci dati in un intervallo con java, cerca e sostituisci dati in un intervallo con java
---

{{% alert color="primary" %}}

A volte è necessario cercare e sostituire dati specifici in un intervallo, ignorando i valori delle celle al di fuori dell'intervallo desiderato. Aspose.Cells permette di limitare una ricerca a un intervallo specifico. Questo articolo spiega come.

{{% /alert %}}

Aspose.Cells fornisce il metodo [**FindOptions.setRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#setRange-com.aspose.cells.CellArea-) per specificare un intervallo durante la ricerca di dati.

Supponiamo di voler cercare la stringa **"cerca"** e sostituirla con **"sostituisci"** nell'intervallo **E3:H6**. Nella schermata sottostante, la stringa "cerca" può essere vista in diverse celle ma vogliamo sostituirla solo in un dato intervallo, qui evidenziato in giallo.

**File di input**

![todo:image_alt_text](search-and-replace-data-in-a-range_1.png)

Dopo l'esecuzione del codice, il file di output appare come di seguito. Tutte le stringhe "cerca" all'interno dell'intervallo sono state sostituite con "sostituisci".

**File di output**

![todo:image_alt_text](search-and-replace-data-in-a-range_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchReplaceDataInRange-SearchReplaceDataInRange.java" >}}

## Articoli correlati

- [Trova o cerca dati](/cells/it/java/find-or-search-data/)
{{< app/cells/assistant language="java" >}}
