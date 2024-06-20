---
title: Salva ciascun foglio di calcolo in un file PDF separato
type: docs
weight: 130
url: /it/python-net/save-each-worksheet-to-a-different-pdf-file/
description: Scopri come Salvare Ciascun Foglio di Lavoro in un File PDF Diverso con Aspose.Cells for Python via .NET API.
keywords: Python Salva Ciascun Foglio di Lavoro in un File PDF Diverso
---

{{% alert color="primary" %}} 

Aspose.Cells for Python via .NET supporta la conversione di file XLS (che contengono immagini, grafici, ecc.) in documenti PDF. Aspose.Cells for Python via .NET può lavorare indipendentemente per convertire un foglio di calcolo in PDF e non è necessario utilizzare Aspose.PDF for .NET per la conversione. La conversione non richiede al software di creare o utilizzare file temporanei poiché l'intero processo può essere eseguito in memoria.

{{% /alert %}} 
## **Salva ciascun foglio di calcolo in un file PDF separato**
Se è necessario salvare ciascun foglio di lavoro nel file di modello Excel per generare file PDF diversi, è possibile farlo facilmente. È possibile provare a impostare un indice di foglio alla volta sull'opzione [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/) per renderlo in PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SaveEachWorksheetToDifferentPDF-1.py" >}}

{{% alert color="primary" %}} 

Se il foglio di calcolo contiene formule, è meglio chiamare [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) proprio prima di rendere il foglio di calcolo in formato PDF. In questo modo si garantisce il ricalcolo dei valori dipendenti dalle formule e la visualizzazione dei valori corretti nel PDF.

{{% /alert %}}
