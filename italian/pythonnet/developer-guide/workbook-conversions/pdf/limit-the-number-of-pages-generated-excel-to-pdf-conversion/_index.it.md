---
title: Limita il numero di pagine generate - Conversione Excel a PDF
type: docs
weight: 180
url: /it/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Scopri come limitare il numero di pagine generate durante il rendering di Excel a PDF con Aspose.Cells for Python via .NET API.
keywords: Python Limit the Number of Pages Generated while Rendering Excel to PDF, Limit the Number of Pages Generated while saving Excel to PDF using Python, Python Set the Number of Pages Generated while converting Excel to PDF, Control the Number of Pages Generated for Excel to PDF in python
---
{{% alert color="primary" %}}

volte, desideri stampare un intervallo di pagine su un file di output PDF. Aspose.Cells for Python via .NET ha la possibilità di impostare un limite al numero di pagine generate quando si converte un foglio di calcolo Excel nel formato file PDF.

{{% /alert %}}

##  **Limitazione del numero di pagine generate**

L'esempio seguente mostra come eseguire il rendering di un intervallo di pagine (3 e 4) in un file Excel Microsoft in PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-LimitNumberOfPagesGenerated-1.py" >}}

{{% alert color="primary" %}}

 Se il foglio di calcolo contiene formule, è meglio chiamare[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) metodo appena prima di renderizzarlo in PDF. In questo modo si garantisce che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati nel file di output.

{{% /alert %}}
