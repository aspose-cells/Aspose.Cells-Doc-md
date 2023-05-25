---
title: Salva ogni foglio di lavoro in un file PDF diverso
type: docs
weight: 50
url: /it/java/save-each-worksheet-to-a-different-pdf-file/
---
{{% alert color="primary" %}}

Aspose.Cells supporta la conversione di file di fogli di calcolo (che contengono immagini, grafici, ecc.) in documenti PDF. Aspose.Cells for Java può funzionare in modo indipendente per convertire un foglio di calcolo in un documento PDF e non è più necessario utilizzare Aspose.PDF for Java per la conversione. La conversione non richiede di creare/utilizzare alcun file temporaneo, poiché l'intero processo può essere eseguito nella memoria.

{{% /alert %}}

Se è necessario salvare ogni foglio di lavoro nel file Excel modello per generare diversi file PDF. Questo può essere ottenuto facilmente. Puoi provare a impostare un indice del foglio su**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** opzione alla volta per eseguire il rendering a PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveEachWorksheettoDifferentPDF-SaveEachWorksheettoDifferentPDF.java" >}}

{{% alert color="primary" %}}

 Se il foglio di calcolo contiene formule, è meglio chiamare il file[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) appena prima di eseguire il rendering del foglio di calcolo in PDF. Ciò garantisce che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati nel file PDF.

{{% /alert %}}
