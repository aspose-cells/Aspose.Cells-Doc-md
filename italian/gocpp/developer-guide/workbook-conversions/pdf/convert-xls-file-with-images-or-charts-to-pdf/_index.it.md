---
title: Converti file XLS con immagini o grafici in PDF con Golang tramite C++
linktitle: Converti il file XLS con immagini o grafici nel formato PDF
type: docs
weight: 50
url: /it/go-cpp/convert-xls-file-with-images-or-charts-to-pdf/
description: Converti file XLS contenenti immagini o grafici in documenti PDF usando Aspose.Cells con Golang tramite C++.
---

{{% alert color="primary" %}} 

Aspose.Cells supporta la conversione di file XLS contenenti immagini e grafici in documenti PDF. Aspose.Cells for C++ può funzionare indipendentemente per convertire un foglio di calcolo in PDF: non è necessario Aspose.PDF per C++ per la conversione. Il processo può essere eseguito in memoria poiché non dipende da file XML temporanei o intermedi. Ciò significa che grandi file Excel, ad esempio quelli che contengono immagini, grafici e altri oggetti di disegno, possono essere convertiti rapidamente ed efficacemente.

{{% /alert %}} 
## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertXlsFileWithImagesOrChartsToPdf.go" >}}
{{% alert color="primary" %}} 

Se il foglio contiene formule, è meglio chiamare il metodo [Calculate(CalculationData data)](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/calculate/) appena prima di esportare in PDF. Questo assicura che i valori dipendenti dalla formula siano ricalcolati e che i valori corretti siano visualizzati nel PDF.

{{% /alert %}}
