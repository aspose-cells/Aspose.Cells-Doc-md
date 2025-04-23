---
title: Limita il numero di pagine generate  Conversione di Excel in PDF
type: docs
weight: 60
url: /it/java/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

A volte si desidera stampare un intervallo di pagine in un file PDF di output. Aspose.Cells ha la capacità di impostare un limite su quante pagine vengono generate durante la conversione di un foglio di calcolo Excel in PDF.

{{% /alert %}}

## **Limitazione del numero di pagine generate**

L'esempio seguente mostra come rendere un intervallo di pagine (3 e 4) in un file Microsoft Excel in PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LimitNumberofPagesGenerated-LimitNumberofPagesGenerated.java" >}}

{{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) appena prima di renderlo nel formato PDF. Così facendo si garantisce che i valori dipendenti dalle formule vengano ricalcolati e i valori corretti vengano visualizzati nel file di output.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
