---
title: Rendere una pagina PDF per foglio di lavoro di Excel  Conversione di Excel in PDF
type: docs
weight: 40
url: /it/java/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

Quando si lavora con grandi file Microsoft Excel (ad esempio un workbook che ha molti fogli, ciascuno con 50 colonne e 300 o più righe di dati), potresti desiderare che l'output PDF mostri una pagina per foglio, indipendentemente dalla dimensione del foglio di lavoro. Ciò significherebbe che ogni pagina avrà probabilmente una dimensione di pagina radicalmente diversa. Questo può essere realizzato usando Aspose.Cells for Java.

{{% /alert %}}

Si prega di vedere il seguente codice di esempio che converte un file di Excel con più fogli di lavoro in PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExceltoPDF-ExceltoPDF.java" >}}

{{% alert color="primary" %}}

Se l'opzione [**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OnePagePerSheet) è impostata su **true**, tutto il contenuto del foglio è reso in una sola pagina PDF. La dimensione carta impostata da [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) è non valida, ma le altre impostazioni impostate con [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) avranno comunque effetto.

{{% /alert %}} {{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare il metodo [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) subito prima di rendere il foglio di calcolo in PDF. Questo assicura che i valori dipendenti dalle formule vengano ricalcolati e che i valori corretti vengano resi nel PDF.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
