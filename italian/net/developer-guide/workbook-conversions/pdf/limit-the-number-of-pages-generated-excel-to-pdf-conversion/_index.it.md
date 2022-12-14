---
title: Limita il numero di pagine generate - Conversione da Excel a PDF
type: docs
weight: 180
url: /it/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

A volte, si desidera stampare un intervallo di pagine su un file PDF di output. Aspose.Cells ha la possibilità di impostare un limite al numero di pagine generate durante la conversione di un foglio di calcolo Excel nel formato di file PDF.

{{% /alert %}}

## **Limitazione del numero di pagine generate**

L'esempio seguente mostra come eseguire il rendering di un intervallo di pagine (3 e 4) in un file Excel Microsoft in PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LimitNumberOfPagesGenerated-1.cs" >}}

{{% alert color="primary" %}}

 Se il foglio di calcolo contiene formule, è meglio chiamare[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) appena prima di renderla in PDF. Questa operazione garantisce che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati nel file di output.

{{% /alert %}}
