---
title: Converti file XLS con immagini o grafici in PDF
type: docs
weight: 50
url: /it/net/convert-xls-file-with-images-or-charts-to-pdf/
---
{{% alert color="primary" %}} 

Aspose.Cells supporta la conversione di file XLS che contengono immagini e grafici in documenti PDF. Aspose.Cells for .NET può funzionare in modo indipendente per convertire un foglio di calcolo in PDF: Aspose.PDF for .NET non è richiesto per la conversione. Il processo può essere eseguito in memoria poiché il processo non dipende da file XML temporanei o intermedi. Ciò significa che i file Excel di grandi dimensioni, ad esempio quelli contenenti immagini, grafici e altri oggetti di disegno, possono essere convertiti in modo rapido ed efficiente.

{{% /alert %}} 
## **Codice d'esempio**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertXLSFileToPDF-1.cs" >}}

{{% alert color="primary" %}} 

 Se il foglio di calcolo contiene formule, è meglio chiamare il file[Workbook.CalculateFormula](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) appena prima del rendering in PDF. In questo modo si garantisce che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati in PDF.

{{% /alert %}}
