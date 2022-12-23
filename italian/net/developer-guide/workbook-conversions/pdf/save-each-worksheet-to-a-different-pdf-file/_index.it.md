---
title: Salva ogni foglio di lavoro in un file PDF diverso
type: docs
weight: 130
url: /it/net/save-each-worksheet-to-a-different-pdf-file/
---
{{% alert color="primary" %}} 

Aspose.Cells supporta la conversione di file XLS (che contengono immagini, grafici, ecc.) in documenti PDF. Aspose.Cells for .NET può funzionare in modo indipendente per convertire un foglio di calcolo in PDF e non è necessario utilizzare Aspose.PDF for .NET per la conversione. La conversione non richiede al software di creare o utilizzare alcun file temporaneo poiché l'intero processo può essere eseguito in memoria.

{{% /alert %}} 
## **Salva ogni foglio di lavoro in un file PDF diverso**
Se è necessario salvare ogni foglio di lavoro nel file Excel del modello per generare diversi file PDF, è possibile farlo facilmente. Puoi provare a nascondere i fogli nel file e rendere visibile un foglio alla volta per eseguire il rendering su PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SaveEachWorksheetToDifferentPDF-1.cs" >}}

{{% alert color="primary" %}} 

Se il tuo foglio di calcolo contiene formule, è meglio chiamare[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)appena prima di eseguire il rendering del foglio di calcolo nel formato PDF. In questo modo si assicurerà che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati in PDF.

{{% /alert %}}
