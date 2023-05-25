---
title:  Grafico a PDF
type: docs
weight: 47
url: /it/net/chart-to-pdf/
---
##  **Grafico di rendering a PDF**

 Per eseguire il rendering del grafico nel formato PDF, le API Aspose.Cells hanno esposto il[**Grafico.ToPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)metodo con la possibilità di memorizzare il risultante PDF sul percorso del disco o Stream.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToPDF.cs" >}}

##  **Crea grafico PDF con dimensione pagina desiderata**
 Puoi creare un grafico Pdf con la dimensione della pagina desiderata utilizzando Aspose.Cells e specificare come desideri allineare il grafico all'interno della pagina come in alto, in basso, al centro, a sinistra, a destra ecc. Inoltre, il grafico di output può essere creato in streaming o su disco. Vedere il seguente codice di esempio che carica il file[esempio di file Excel](64716906.xlsx) , accede al primo grafico all'interno del foglio di lavoro e quindi lo converte in[uscita Pdf](64716907.pdf)con la dimensione della pagina desiderata. Lo screenshot seguente mostra che la dimensione della pagina nel Pdf di output è 7x7 come specificato all'interno del codice e il grafico è allineato al centro sia orizzontalmente che verticalmente.

![cose da fare:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)
##  **Codice d'esempio**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-CreateChartPDFWithDesiredPageSize.cs" >}}

