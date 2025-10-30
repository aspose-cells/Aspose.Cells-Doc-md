---
title: Limita il numero di pagine generate  Conversione di Excel in PDF
type: docs
weight: 180
url: /it/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Scopri come limitare il numero di pagine generate durante la rappresentazione di Excel in PDF con Aspose.Cells per l API Python via .NET.
keywords: Limitare il numero di pagine generate durante il rendering di Excel in PDF, Limitare il numero di pagine generate durante il salvataggio di Excel in PDF usando Python, Impostare il numero di pagine generate durante la conversione di Excel in PDF, Controllare il numero di pagine generate per Excel in PDF in python
---

{{% alert color="primary" %}}

A volte desideri stampare un intervallo di pagine in un file PDF di output. Aspose.Cells for Python via .NET ha la capacità di impostare un limite su quante pagine sono generate durante la conversione di un foglio di calcolo Excel nel formato di file PDF.

{{% /alert %}}

## **Limitazione del numero di pagine generate**

L'esempio seguente mostra come rendere un intervallo di pagine (3 e 4) in un file Microsoft Excel in PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-LimitNumberOfPagesGenerated-1.py" >}}

{{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare il metodo [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) appena prima di renderizzarlo in PDF. Farlo assicura che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano renderizzati nel file di output.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
