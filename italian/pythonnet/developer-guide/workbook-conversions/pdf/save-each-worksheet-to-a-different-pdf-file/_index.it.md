---
title: Salva ogni foglio di lavoro in un file PDF diverso
type: docs
weight: 130
url: /it/python-net/save-each-worksheet-to-a-different-pdf-file/
description: Scopri come salvare ciascun foglio di lavoro in un file PDF diverso con Aspose.Cells for Python via .NET API.
keywords: Python Save Each Worksheet to a Different PDF File
---
{{% alert color="primary" %}} 

Aspose.Cells for Python via .NET supporta la conversione di file XLS (che contengono immagini, grafici, ecc.) in documenti PDF. Aspose.Cells for Python via .NET può funzionare in modo indipendente per convertire un foglio di calcolo in PDF e non è necessario utilizzare Aspose.PDF for .NET per la conversione. La conversione non richiede che il software crei o utilizzi file temporanei poiché l'intero processo può essere eseguito in memoria.

{{% /alert %}} 
##  **Salva ogni foglio di lavoro in un file PDF diverso**
 Se è necessario salvare ciascun foglio di lavoro nel file Excel modello per generare diversi file PDF, è possibile farlo facilmente. Potresti provare a impostare l'indice di un foglio su**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** opzione alla volta per rendere al PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SaveEachWorksheetToDifferentPDF-1.py" >}}

{{% alert color="primary" %}} 

 Se il tuo foglio di calcolo contiene formule, è meglio chiamare[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) appena prima di convertire il foglio di calcolo nel formato PDF. In questo modo si garantirà che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati in PDF.

{{% /alert %}}
