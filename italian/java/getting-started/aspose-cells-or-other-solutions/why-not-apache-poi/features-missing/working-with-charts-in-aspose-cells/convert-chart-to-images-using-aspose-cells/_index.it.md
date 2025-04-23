---
title: Converti il grafico in immagini usando Aspose.Cells
type: docs
weight: 30
url: /it/java/convert-chart-to-images-using-aspose-cells/
---

## **Aspose.Cells - Converti grafico in immagini**
I grafici sono visualmente accattivanti e rendono facile per gli utenti vedere confronti, modelli e tendenze nei dati.
Il metodo toImage della classe Chart converte il grafico in un file immagine, che può essere salvato su disco o in uno stream.

**Java**

{{< highlight java >}}

 //Get the Chart image

ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();

imgOpts.setImageFormat(ImageFormat.getPng());

//Save the chart image file.

chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage.png"), imgOpts);

{{< /highlight >}}
## **Scarica il codice in esecuzione**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposeChartToImage.java)

{{% alert color="primary" %}} 

Per ulteriori dettagli, visita [Conversione del grafico in un'immagine](/java/converting-chart-to-image).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
