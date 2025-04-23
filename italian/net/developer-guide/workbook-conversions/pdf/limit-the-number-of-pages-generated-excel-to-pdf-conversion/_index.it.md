---
title: Limita il numero di pagine generate  Conversione di Excel in PDF
type: docs
weight: 180
url: /it/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

A volte si desidera stampare un intervallo di pagine in un file PDF di output. Aspose.Cells ha la capacità di impostare un limite su quante pagine vengono generate durante la conversione di un foglio di calcolo di Excel nel formato di file PDF.

{{% /alert %}}

## **Limitazione del numero di pagine generate**

L'esempio seguente mostra come rendere un intervallo di pagine (3 e 4) in un file Microsoft Excel in PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LimitNumberOfPagesGenerated-1.cs" >}}

{{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) appena prima di renderlo in PDF. Questo assicura che i valori dipendenti dalle formule vengano ricalcolati e che i valori corretti vengano resi nel file di output.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
