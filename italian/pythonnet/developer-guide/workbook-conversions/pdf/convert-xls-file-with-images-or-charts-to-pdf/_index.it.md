---
title: Converti il file XLS con immagini o grafici nel formato PDF
type: docs
weight: 50
url: /it/python-net/convert-xls-file-with-images-or-charts-to-pdf/
description: Scopri come convertire il file XLS con immagini o grafici in PDF con Aspose.Cells for Python via .NET API.
keywords: Converti il file XLS con immagini o grafici in PDF con Python, Converti xls in pdf usando Python, File XLS Python con immagini in pdf, file xls con grafici in pdf in Python, Python xls in pdf
---

{{% alert color="primary" %}} 

Aspose.Cells for Python via .NET supporta la conversione dei file XLS che contengono immagini e grafici in documenti PDF. Aspose.Cells for Python via .NET API può funzionare in modo indipendente per convertire un foglio di calcolo in PDF: Aspose.PDF for .NET non è richiesto per la conversione. Il processo può essere eseguito in memoria in quanto non dipende da file XML temporanei o intermedi. Ciò significa che i file Excel di grandi dimensioni, ad esempio quelli contenenti immagini, grafici e altri oggetti disegnati, possono essere convertiti rapidamente ed efficientemente.

{{% /alert %}} 
## **Codice di Esempio**


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertXLSFileToPDF-1.py" >}}

{{% alert color="primary" %}} 

Se il foglio di calcolo contiene formule, è meglio chiamare il metodo [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) giusto prima del rendering in PDF. In questo modo si assicura che i valori dipendenti dalla formula vengano ricalcolati e i valori corretti vengano renderizzati nel PDF.

{{% /alert %}}
