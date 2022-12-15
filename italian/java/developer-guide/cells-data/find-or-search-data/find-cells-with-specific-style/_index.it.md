---
title: Trova le celle con uno stile specifico
type: docs
weight: 80
url: /it/java/find-cells-with-specific-style/
description: Questo articolo mostra come trovare celle con uno stile specifico utilizzando MS Excel e l'API Aspose.Cells for Java.
keywords: find cells with specific style, find cells with specific style excel, find cells with specific style excel java, search cells with specific style, search cells with specific style excel, search cells with specific style excel java, how to find cells with specific style, how to find cells with specific style excel, how to find cells with specific style excel java
---
{{% alert color="primary" %}}

A volte, devi trovare le celle con uno stile particolare. In questo articolo viene illustrato come ottenere ciò utilizzando Microsoft Excel e l'API Aspose.Cells for Java.

{{% /alert %}}

## Utilizzo di Microsoft Excel

Questi sono i passaggi necessari per cercare celle con stili specifici in MS Excel.

1.  Selezionare**Trova e seleziona** nel**Scheda Casa**.
1.  Selezionare**Trova**.
1.  Clic**Opzioni** se le opzioni avanzate non sono visibili.
1.  Selezionare**Scegli Formato Da Cell...** dal**Formato** cadere in picchiata.
1. Seleziona la cella con lo stile in cui vuoi cercare.
1.  Clic**Trova tutto** per trovare tutte le celle con uno stile simile alla cella selezionata.

## Utilizzando Aspose.Cells for Java

 Aspose.Cells for Java fornisce la funzione per trovare le celle nel foglio di lavoro con uno stile specifico. Per questo, l'API fornisce[**FindOptions.setStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#Style) proprietà.

### Codice di esempio

 Il seguente frammento di codice trova tutte le celle che hanno lo stesso stile di cell**A1** e cambia il testo all'interno di quelle celle. Si prega di vedere lo screenshot dei file di origine e di output per analizzare l'output del codice di esempio.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindCellsWithSpecificStyle-FindCellsWithSpecificStyle.java" >}}

Dopo l'esecuzione del codice, tutte le celle che hanno lo stesso stile della cella A1 avranno un testo "Trovato".

### Screenshot

![cose da fare:immagine_alt_testo](find-cells-with-specific-style_1.png)

**Figura:** File di origine con celle con stili

 Ecco il file di output generato dal seguente codice. Puoi vedere tutte le celle che hanno lo stesso stile di cell**A1** ha un testo "Trovato"

![cose da fare:immagine_alt_testo](find-cells-with-specific-style_2.png)

**Figura:** File di output con le celle trovate dopo la ricerca per**A1** stile
