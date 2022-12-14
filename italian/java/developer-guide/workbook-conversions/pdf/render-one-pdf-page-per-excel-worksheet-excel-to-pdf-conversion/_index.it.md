---
title: Rendering di una pagina PDF per foglio di lavoro Excel - Conversione da Excel a PDF
type: docs
weight: 40
url: /it/java/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

Quando si lavora con file Excel di grandi dimensioni Microsoft (ad esempio una cartella di lavoro con molti fogli, ciascuno con 50 colonne e 300 o più righe di dati), è possibile che l'output PDF mostri una pagina per foglio di lavoro, indipendentemente dalle dimensioni del foglio di lavoro . Ciò significherebbe che è probabile che ogni pagina abbia una dimensione di pagina radicalmente diversa. Ciò può essere ottenuto utilizzando Aspose.Cells for Java.

{{% /alert %}}

Si prega di vedere il seguente codice di esempio che converte un file Excel con più fogli di lavoro in PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExceltoPDF-ExceltoPDF.java" >}}

{{% alert color="primary" %}}

 Se la[**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OnePagePerSheet) l'opzione è impostata su**VERO** , tutto il contenuto del foglio viene visualizzato in una pagina PDF. Il formato carta impostato da[**Impostazione della pagina**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) non è valido, ma le altre impostazioni impostate con[**Impostazione della pagina**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup)hanno ancora effetto.

{{% /alert %}} {{% alert color="primary" %}}

Se il tuo foglio di calcolo contiene formule, è meglio chiamare il file[**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) appena prima di eseguire il rendering del foglio di calcolo in PDF. Ciò garantisce che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati nel PDF.

{{% /alert %}}
