---
title: Grafico in PDF 
description: Impara come usare Aspose.Cells per Python via .NET per convertire un grafico in un documento PDF. La nostra guida dimostrerà come esportare un grafico da Microsoft Excel e salvarlo come PDF per distribuzione e archiviazione.
keywords: Aspose.Cells per Python via .NET, Grafico in PDF, Microsoft Excel, Conversione PDF, Esportazione, Distribuzione, Archiviazione.
type: docs
weight: 47
url: /it/python-net/chart-to-pdf/
---

## **Rendering del grafico in PDF**

Per rendere il grafico in formato PDF, le API di Aspose.Cells per Python via .NET hanno esposto il metodo [**Chart.to_pdf**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_pdf) con la possibilità di memorizzare il PDF risultante su percorso disco o Stream.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChartRenderingChartToPDF.py" >}}

## **Crea Grafico PDF con Dimensione Pagina Desiderata**
Puoi creare un PDF del grafico con la dimensione di pagina desiderata usando Aspose.Cells per Python via .NET e specificare come vuoi allineare il grafico all'interno della pagina, come alto, basso, centro, sinistra, destra, ecc. Inoltre, il grafico di uscita può essere creato in stream o su disco. Consulta il seguente esempio di codice che carica il [file Excel di esempio](64716906.xlsx), accede al primo grafico all'interno del foglio di lavoro e lo converte in [output PDF](64716907.pdf) con la dimensione di pagina desiderata. Lo screenshot seguente mostra che la dimensione della pagina nel PDF di output è 7x7 come specificato nel codice e che il grafico è allineato al centro sia orizzontalmente che verticalmente. 

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateChartPDFWithDesiredPageSize.py" >}}

