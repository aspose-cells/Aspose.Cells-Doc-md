---
title: Converti il file XLS con immagini o grafici nel formato PDF
type: docs
weight: 50
url: /it/net/convert-xls-file-with-images-or-charts-to-pdf/
---

{{% alert color="primary" %}} 

Aspose.Cells supporta la conversione dei file XLS che contengono immagini e grafici in documenti PDF. Aspose.Cells for .NET può funzionare in modo indipendente per convertire un foglio di calcolo in PDF: non è richiesto Aspose.PDF for .NET per la conversione. Il processo può essere eseguito in memoria in quanto non dipende da file XML temporanei o intermediari. Questo significa che grandi file Excel, ad esempio quelli contenenti immagini, grafici e altri oggetti di disegno, possono essere convertiti rapidamente ed efficientemente.

{{% /alert %}} 
## **Codice di Esempio**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertXLSFileToPDF-1.cs" >}}

{{% alert color="primary" %}} 

Se il foglio di calcolo contiene formule, è meglio chiamare il metodo [Workbook.CalculateFormula](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) appena prima del rendering in PDF. In questo modo si garantisce che i valori dipendenti dalla formula siano ricalcolati e i valori corretti vengano resi in PDF.

{{% /alert %}}
