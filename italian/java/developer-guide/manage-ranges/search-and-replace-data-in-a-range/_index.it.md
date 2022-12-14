---
title: Cerca e sostituisci i dati in un intervallo
type: docs
weight: 60
url: /it/java/search-and-replace-data-in-a-range/
description: Questo articolo mostra come cercare e sostituire i dati in un intervallo in Excel utilizzando il codice Java.
keywords: java search and replace data in excel, java search data in excel, java search and replace data in a range, java search data in a range, java searching data in a range, java searching data in range, java searching data in excel, java search data in range, search and replace data in excel with java, search and replace data in a range with java, search and replace data in range with java
---
{{% alert color="primary" %}}

A volte, è necessario cercare e sostituire dati specifici in un intervallo, ignorando qualsiasi valore di cella al di fuori dell'intervallo desiderato. Aspose.Cells consente di limitare la ricerca ad un intervallo specifico. Questo articolo spiega come.

{{% /alert %}}

Aspose.Cells fornisce il[**FindOptions.setRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#setRange(com.aspose.cells.CellArea)) metodo per specificare un intervallo durante la ricerca di dati.

 Supponiamo di voler cercare la stringa**"ricerca"** e sostituirlo con**"sostituire"** nell'intervallo**E3:H6**. Nello screenshot qui sotto, la stringa "cerca" è visibile in più celle ma vogliamo sostituirla solo in un determinato intervallo, qui evidenziato in giallo.

**File di input**

![cose da fare:immagine_alt_testo](search-and-replace-data-in-a-range_1.png)

Dopo l'esecuzione del codice, il file di output è simile al seguente. Tutte le stringhe "search" all'interno dell'intervallo sono state sostituite con "replace".

**File di uscita**

![cose da fare:immagine_alt_testo](search-and-replace-data-in-a-range_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchReplaceDataInRange-SearchReplaceDataInRange.java" >}}

## articoli Correlati

- [Trova o cerca dati](/cells/it/java/find-or-search-data/)
