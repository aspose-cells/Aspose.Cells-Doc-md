---
title: Limita il numero di pagine generate - Conversione da Excel a PDF
type: docs
weight: 60
url: /it/java/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

A volte, si desidera stampare un intervallo di pagine su un file PDF di output. Aspose.Cells ha la possibilità di impostare un limite al numero di pagine generate durante la conversione di un foglio di calcolo Excel in PDF.

{{% /alert %}}

## **Limitazione del numero di pagine generate**

L'esempio seguente mostra come eseguire il rendering di un intervallo di pagine (3 e 4) in un file Microsoft Excel in PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LimitNumberofPagesGenerated-LimitNumberofPagesGenerated.java" >}}

{{% alert color="primary" %}}

 Se il foglio di calcolo contiene formule, è meglio chiamare[**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) appena prima di renderla in formato PDF. In questo modo si garantisce che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati nel file di output.

{{% /alert %}}
