---
title: Rendere una pagina PDF per foglio di lavoro di Excel  Conversione di Excel in PDF
type: docs
weight: 100
url: /it/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Scopri come rendere una pagina PDF per foglio di lavoro di Excel durante la conversione di Excel in PDF con l API Aspose.Cells for Python via .NET.
keywords: Python renderizza una pagina PDF per foglio di lavoro Excel durante il salvataggio del file in PDF, Una pagina PDF per foglio di lavoro Excel durante il salvataggio di Excel in PDF usando Python, Python mostra una pagina per foglio di lavoro durante la conversione di Excel in PDF
---

{{% alert color="primary" %}} 

Quando si lavora con grandi file di Microsoft Excel (ad esempio un file di lavoro che ha molti fogli, ognuno con 50 colonne e 300 o più righe di dati), potresti voler che l'output in PDF mostri una pagina per foglio di lavoro, indipendentemente dalle dimensioni del foglio di lavoro. Ciò significherebbe che ogni pagina avrà probabilmente una dimensione di pagina radicalmente diversa. Questo può essere realizzato utilizzando l'API Aspose.Cells for Python via .NET.

{{% /alert %}} 

Si prega di vedere il seguente codice di esempio che converte un file di Excel con più fogli di lavoro in PDF.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderOnePdfPagePerExcelWorksheet-1.py" >}}

{{% alert color="primary" %}} 

Se l'opzione [PdfSaveOptions.one_page_per_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/one_page_per_sheet/) è impostata su **true**, tutto il contenuto del foglio sarà reso in una pagina PDF.

{{% /alert %}} {{% alert color="primary" %}} 

Se il tuo foglio di calcolo contiene formule, è meglio chiamare il metodo [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) proprio prima di renderizzare il foglio di calcolo in PDF. Questo garantisce che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano resi nel PDF.

{{% /alert %}}
