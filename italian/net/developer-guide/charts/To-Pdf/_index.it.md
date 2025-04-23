---
title: Grafico in PDF 
description: Scopri come utilizzare Aspose.Cells for .NET per convertire un grafico in un documento PDF. La nostra guida mostrerà come esportare un grafico da Microsoft Excel e salvarlo come PDF per distribuzione e archiviazione ulteriori.
keywords: Aspose.Cells for .NET, Grafico in PDF, Microsoft Excel, Conversione PDF, Esportazione, Distribuzione, Archiviazione.
type: docs
weight: 47
url: /it/net/chart-to-pdf/
---

## **Rendering del grafico in PDF**

Per renderizzare il grafico nel formato PDF, le API di Aspose.Cells hanno esposto il metodo [**Chart.ToPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index) con la capacità di memorizzare il PDF risultante su un percorso disco o su Stream.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToPDF.cs" >}}

## **Crea Grafico PDF con Dimensione Pagina Desiderata**
È possibile creare grafico Pdf con la dimensione di pagina desiderata utilizzando Aspose.Cells e specificare come si desidera allineare il grafico all'interno della pagina come in alto, in basso, nel centro, a sinistra, a destra, ecc. Inoltre, il grafico di output può essere creato in stream o su disco. Si prega di vedere il codice di esempio seguente che carica il [file Excel di esempio](64716906.xlsx), accede al primo grafico all'interno del foglio di lavoro e lo converte in [Pdf di output](64716907.pdf) con la dimensione di pagina desiderata. Lo screenshot seguente mostra che la dimensione di pagina nel Pdf di output è 7x7 come specificato all'interno del codice e il grafico è allineato al centro sia orizzontalmente che verticalmente. 

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-CreateChartPDFWithDesiredPageSize.cs" >}}

{{< app/cells/assistant language="csharp" >}}
