---
title: Salva ciascun foglio di calcolo in un file PDF separato
type: docs
weight: 50
url: /it/java/save-each-worksheet-to-a-different-pdf-file/
---

{{% alert color="primary" %}}

Aspose.Cells supporta la conversione di file di fogli elettronici (che contengono immagini, grafici, ecc.) in documenti PDF. Aspose.Cells for Java può lavorare in modo indipendente per convertire un foglio di calcolo in un documento PDF e non è più necessario utilizzare Aspose.PDF for Java per la conversione. La conversione non richiede di creare / utilizzare file temporanei in quanto l'intero processo può essere eseguito in memoria.

{{% /alert %}}

Se hai bisogno di salvare ogni foglio di lavoro nel tuo file di Excel modello per generare file PDF diversi. Ciò può essere facilmente raggiunto. Puoi provare a impostare un'opzione di indice del foglio a [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-) alla volta per renderla in PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveEachWorksheettoDifferentPDF-SaveEachWorksheettoDifferentPDF.java" >}}

{{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare il metodo [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) proprio prima di renderizzare il foglio di calcolo in PDF. Ciò garantisce che i valori dipendenti dalla formula vengano ricalcolati e i valori corretti vengano resi in PDF.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
