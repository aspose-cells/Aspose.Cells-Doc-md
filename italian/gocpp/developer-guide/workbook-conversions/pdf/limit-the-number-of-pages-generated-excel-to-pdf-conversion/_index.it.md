---
title: Limita il Numero di Pagine Generate  Conversione Excel in PDF con Golang tramite C++
linktitle: Limitare il Numero di Pagine Generate
type: docs
weight: 180
url: /it/go-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Impara come limitare il numero di pagine generate durante la conversione di Excel in PDF usando Aspose.Cells con Golang tramite C++.
---

{{% alert color="primary" %}}

A volte si desidera stampare un intervallo di pagine in un file PDF di output. Aspose.Cells ha la capacità di impostare un limite su quante pagine vengono generate durante la conversione di un foglio di calcolo di Excel nel formato di file PDF.

{{% /alert %}}

## **Limitazione del numero di pagine generate**

L'esempio seguente mostra come rendere un intervallo di pagine (3 e 4) in un file Microsoft Excel in PDF.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LimitTheNumberOfPagesGeneratedExcelToPdfConversion.go" >}}
{{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) appena prima di renderlo in PDF. Questo assicura che i valori dipendenti dalle formule vengano ricalcolati e che i valori corretti vengano resi nel file di output.

{{% /alert %}}
