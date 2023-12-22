---
title: Visualizza una pagina PDF per foglio di lavoro Excel - Conversione da Excel a PDF
type: docs
weight: 100
url: /it/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Scopri come eseguire il rendering di una pagina per foglio di lavoro Excel PDF durante la conversione di Excel in PDF con Aspose.Cells for Python via .NET API.
keywords: Python Render One PDF Page Per Excel Worksheet while saving file to PDF, One PDF Page Per Excel Worksheet while saving Excel to PDF using Python, Python show one page per worksheet when converting Excel to PDF
---
{{% alert color="primary" %}} 

Quando si lavora con file Excel Microsoft di grandi dimensioni (ad esempio una cartella di lavoro con molti fogli, ciascuno con 50 colonne e 300 o più righe di dati), è possibile che l'output PDF mostri una pagina per foglio di lavoro, indipendentemente dalle dimensioni del foglio di lavoro . Ciò significherebbe che è probabile che ciascuna pagina abbia dimensioni di pagina radicalmente diverse. Ciò può essere ottenuto utilizzando Aspose.Cells for Python via .NET API.

{{% /alert %}} 

Consulta il seguente codice di esempio che converte un file Excel con più fogli di lavoro in PDF.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderOnePdfPagePerExcelWorksheet-1.py" >}}

{{% alert color="primary" %}} 

 Se la[PdfSaveOptions.one_page_per_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/one_page_per_sheet/)è impostata su *true**, tutto il contenuto del foglio verrà visualizzato in una pagina PDF.

{{% /alert %}} {{% alert color="primary" %}} 

 Se il tuo foglio di calcolo contiene formule, è meglio chiamare[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) subito prima di eseguire il rendering del foglio di calcolo su PDF. Ciò garantisce che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati in PDF.

{{% /alert %}}
