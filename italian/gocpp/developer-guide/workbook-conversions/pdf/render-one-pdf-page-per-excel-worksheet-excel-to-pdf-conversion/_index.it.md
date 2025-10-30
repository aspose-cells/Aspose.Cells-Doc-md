---
title: Renderizza una pagina PDF per ogni foglio di lavoro di Excel  Conversione Excel in PDF con Golang tramite C++
type: docs
weight: 100
url: /it/go-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Converte i fogli di lavoro di Excel in formato PDF con una pagina per ogni foglio di lavoro usando Aspose.Cells con Golang tramite C++.
---

{{% alert color="primary" %}} 

Quando si lavora con file Microsoft Excel di grandi dimensioni (ad esempio una cartella di lavoro con molti fogli, ciascuno con 50 colonne e 300 o più righe di dati), potresti voler che l'output PDF mostri una pagina per ogni foglio, indipendentemente dalle dimensioni del foglio. Ciò significa che ogni pagina avrà probabilmente una dimensione molto diversa. Questo può essere ottenuto usando Aspose.Cells for C++.

{{% /alert %}} 

Si prega di vedere il seguente codice di esempio che converte un file di Excel con più fogli di lavoro in PDF.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RenderOnePdfPagePerExcelWorksheetExcelToPdfConversion.go" >}}
{{% alert color="primary" %}} 

Se l'opzione [PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) è impostata su **true**, tutto il contenuto del foglio verrà renderizzato su una singola pagina PDF.

{{% /alert %}} {{% alert color="primary" %}} 

Se il tuo foglio di calcolo contiene formule, è meglio chiamare [Workbook::CalculateFormula()](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) immediatamente prima di renderizzare il foglio in PDF. Questo garantisce che i valori dipendenti dalle formule vengano ricalcolati e che i valori corretti vengano rappresentati nel PDF.

{{% /alert %}}
