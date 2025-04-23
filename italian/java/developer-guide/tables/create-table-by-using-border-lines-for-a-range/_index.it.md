---
title: Crea Tabella Utilizzando Linee di Bordo per un Intervallo
type: docs
weight: 50
url: /it/java/create-table-by-using-border-lines-for-a-range/
description: Come creare una tabella con un intervallo utilizzando linee di bordo. Aspose.Cells for Java fornisce un API semplice da usare che può essere utilizzata per aggiungere bordi a un intervallo.
keywords: crea tabella, intervallo in tabella, intervallo in tabella excel, excel intervallo in tabella, intervallo in tabella con bordi, come creare tabella da intervallo, converti intervallo in tabella, excel converti intervallo in tabella, excel crea tabella, intervallo in tabella java 
---

{{% alert color="primary" %}}

A volte vuoi creare una tabella aggiungendo linee di bordo per un **Intervallo**/**AreaCelle** basato sull'indirizzo delle celle che hai. Puoi usare il metodo [**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-int-int-boolean-) per creare un intervallo di celle. Il metodo [**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-int-int-boolean-) restituisce un oggetto [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range). Puoi creare un oggetto [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) e specificare le opzioni dei bordi (superiore, sinistro, inferiore, destro) di conseguenza. In seguito, puoi ottenere le celle del [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) e applicare la formattazione desiderata alle celle.

{{% /alert %}}

L'esempio seguente mostra come creare un [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) e specificare le linee di confine per le celle dell'intervallo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateTableforRange-CreateTableforRange.java" >}}

Dopo aver eseguito il codice sopra, possiamo avere il file Excel generato contenente la tabella formattata; ecco lo screenshot del file.

![todo:image_alt_text](create-table-by-using-border-lines-for-a-range_1.png)
{{< app/cells/assistant language="java" >}}
