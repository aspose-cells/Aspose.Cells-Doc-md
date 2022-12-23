---
title: Converti Excel in PDF
type: docs
weight: 50
url: /it/python-java/convert-excel-to-pdf/
description: Come convertire Excel in PDF con Python. Questo articolo illustra la conversione di file Excel in PDF utilizzando Python e facile da usare Aspose.Cells for Python via Java API.
keywords: excel to pdf python, python convert excel to pdf, python excel to pdf, convert excel to pdf python, convert excel to pdf in python, convert excel to pdf using python, excel to pdf in python, excel to pdf using python, aspose excel to pdf, aspose convert excel to pdf
---
## **Converti Excel in PDF**

I documenti PDF sono ampiamente utilizzati come formato standard per lo scambio di documenti tra organizzazioni, settori governativi e individui. Agli sviluppatori di software viene spesso chiesto di escogitare un modo per convertire facilmente i file Excel Microsoft in documenti PDF. Aspose.Cells for Python via Java API offre la possibilità di convertire i file Excel in documenti PDF (incluso PDF/A). Aspose.Cell's converte i fogli di calcolo in PDF con un alto grado di accuratezza e fedeltà.

### **Conversione diretta**

Per salvare un file Excel direttamente su PDF, puoi utilizzare il formato[**Cartella di lavoro.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) metodo e passaggio[**SalvaFormato.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) come secondo parametro.

Il seguente frammento di codice illustra l'uso di[**SalvaFormato.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF)e il[**Cartella di lavoro.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) per convertire Excel nel formato PDF.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToPDFFiles.py" >}}

### **Conversione avanzata**

Per avere un maggiore controllo sulla conversione a PDF, API fornisce il[**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)classe. Il[**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)class può essere utilizzato per impostare diversi attributi per la conversione. Impostazione di diverse proprietà del file[**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)class ti darà il controllo sulle impostazioni di stampa, carattere, sicurezza e compressione per il file PDF risultante. La proprietà più notevole è la[**Conformità**](https://reference.aspose.com/cells/python/asposecells.api/pdfsaveoptions#Compliance)che consente di salvare i file Excel in file PDF compatibili con PDF/A.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-AdvancedConversiontoPdf.py" >}}

{{% alert color="primary" %}}

 se il tuo foglio di calcolo contiene formule, chiama il[**Workbook.calculateFormula**](https://reference.aspose.com/cells/python/asposecells.api/workbook#calculateFormula()) appena prima di eseguire il rendering del foglio di calcolo in PDF. Ciò garantisce che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati nel file PDF.

{{% /alert %}}
