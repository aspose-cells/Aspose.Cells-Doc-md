---
title: Converti Excel in PDF
type: docs
weight: 50
url: /it/python-java/convert-excel-to-pdf/
description: Come convertire Excel in PDF con Python. Questo articolo mostra come convertire i file di Excel in PDF utilizzando Python e l API semplice da utilizzare Aspose.Cells per Python via Java.
keywords: excel to pdf python, python convert excel to pdf, python excel to pdf, convert excel to pdf python, convert excel to pdf in python, convert excel to pdf using python, excel to pdf in python, excel to pdf using python, aspose excel to pdf, aspose convert excel to pdf
---

## **Converti Excel in PDF**

I documenti PDF sono ampiamente utilizzati come formato standard per lo scambio di documenti tra organizzazioni, settori governativi e individui. Spesso agli sviluppatori software viene chiesto di trovare un modo per convertire facilmente i file di Microsoft Excel in documenti PDF. L'API Aspose.Cells per Python via Java fornisce la possibilità di convertire i file di Excel in documenti PDF (incluso PDF/A). Aspose.Cells converte i fogli di calcolo in PDF con un alto grado di precisione e fedeltà.

### **Conversione Diretta**

Per salvare direttamente un file Excel in PDF, è possibile utilizzare il metodo [**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) e passare [**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) come secondo parametro.

Il seguente frammento di codice dimostra l'uso di [**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) e del metodo [**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) per convertire Excel nel formato PDF.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToPDFFiles.py" >}}

### **Conversione Avanzata**

Per avere maggior controllo sulla conversione in PDF, l'API fornisce la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions). La classe [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions) può essere utilizzata per impostare attributi diversi per la conversione. Impostando diverse proprietà della classe [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions), avrai il controllo sulle impostazioni di Stampa, Carattere, Sicurezza e Compressione del file PDF risultante. La proprietà più nota è il [**Compliance**](https://reference.aspose.com/cells/python/asposecells.api/pdfsaveoptions#Compliance) che ti consente di salvare i file Excel in file PDF/A conformi.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-AdvancedConversiontoPdf.py" >}}

{{% alert color="primary" %}}

Se il tuo foglio di calcolo contiene formule, chiama il metodo [**Workbook.calculateFormula**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#calculateFormula()) giusto prima di rendere il foglio di calcolo in PDF. Questo assicura che i valori dipendenti dalle formule vengano ricalcolati e che i valori corretti vengano visualizzati nel PDF.

{{% /alert %}}
