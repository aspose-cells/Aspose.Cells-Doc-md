---
title: Rendering di una pagina PDF per foglio di lavoro Excel - Conversione da Excel a PDF
type: docs
weight: 100
url: /it/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---
{{% alert color="primary" %}} 

Quando si lavora con file Excel Microsoft di grandi dimensioni (ad esempio una cartella di lavoro con molti fogli, ciascuno con 50 colonne e 300 o più righe di dati), è possibile che l'output PDF mostri una pagina per foglio di lavoro, indipendentemente dalle dimensioni del foglio di lavoro . Ciò significherebbe che è probabile che ogni pagina abbia una dimensione di pagina radicalmente diversa. Ciò può essere ottenuto utilizzando Aspose.Cells for .NET.

{{% /alert %}} 

Vedere il seguente codice di esempio che converte un file Excel con più fogli di lavoro in PDF.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderOnePdfPagePerExcelWorksheet-1.cs" >}}

{{% alert color="primary" %}} 

 Se la[Una pagina per foglio](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/onepagepersheet) l'opzione è impostata su**VERO**, tutto il contenuto del foglio verrà visualizzato in una pagina PDF.

{{% /alert %}} {{% alert color="primary" %}} 

Se il tuo foglio di calcolo contiene formule, è meglio chiamare[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)appena prima di eseguire il rendering del foglio di calcolo in PDF. Ciò garantisce che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati in PDF.

{{% /alert %}}
