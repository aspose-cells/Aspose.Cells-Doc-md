---
title: Crea tabella utilizzando le linee di confine per un intervallo
type: docs
weight: 50
url: /it/java/create-table-by-using-border-lines-for-a-range/
description: Come creare una tabella con intervallo utilizzando le linee di confine. Aspose.Cells for Java fornisce un API semplice da usare che può essere utilizzato per aggiungere bordi a un intervallo.
keywords: create table, range to table, range to table excel, excel range to table, range to table with borders, how to create table from range, convert range to table, excel convert range to table, excel create table, range to table java 
---
{{% alert color="primary" %}}

 A volte, vuoi creare una tabella aggiungendo linee di confine per a**Allineare**/**CellArea** in base all'indirizzo delle celle che hai. Puoi usare[**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange(int,%20int,%20boolean) ) per creare un intervallo di celle. Il[**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange(int,%20int,%20boolean) ) metodo restituisce a[**Allineare**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) oggetto. Puoi creare un[**Stile**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) oggetto e specificare le opzioni dei bordi (superiore, sinistro, inferiore, destro) di conseguenza. Successivamente, potresti ottenere le cellule del[**Allineare**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)e applica la formattazione desiderata alle celle.

{{% /alert %}}

 L'esempio seguente mostra come creare un file[**Allineare**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)e specificare i limiti per le celle dell'intervallo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateTableforRange-CreateTableforRange.java" >}}

Dopo aver eseguito il codice sopra, possiamo avere il file excel generato contenente la tabella formattata; ecco lo screenshot del file.

![cose da fare:immagine_alt_testo](create-table-by-using-border-lines-for-a-range_1.png)
