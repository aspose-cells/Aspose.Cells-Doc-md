---
title: Salva ciascun foglio di calcolo in un file PDF separato
type: docs
weight: 130
url: /it/net/save-each-worksheet-to-a-different-pdf-file/
---

{{% alert color="primary" %}} 

Aspose.Cells supporta la conversione dei file XLS (che contengono immagini, grafici, ecc.) in documenti PDF. Aspose.Cells for .NET può lavorare in modo indipendente per convertire un foglio di calcolo in PDF e non è necessario utilizzare Aspose.PDF per .NET per la conversione. La conversione non richiede al software di creare o utilizzare file temporanei in quanto l'intero processo può essere eseguito in memoria.

{{% /alert %}} 
## **Salva ciascun foglio di calcolo in un file PDF separato**
Se è necessario salvare ciascun foglio di lavoro nel file di modello Excel per generare file PDF diversi, è possibile farlo facilmente. È possibile provare a impostare un indice di foglio alla volta sull'opzione [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) per renderlo in PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SaveEachWorksheetToDifferentPDF-1.cs" >}}

{{% alert color="primary" %}} 

Se il foglio di calcolo contiene formule, è meglio chiamare [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) proprio prima di rendere il foglio di calcolo in formato PDF. In questo modo si garantisce il ricalcolo dei valori dipendenti dalle formule e la visualizzazione dei valori corretti nel PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
