---
title: Converte il grafico in immagine in xlsx4j
type: docs
weight: 10
url: /it/java/convert-chart-to-image-in-xlsx4j/
---

## **Aspose.Cells - Converte il grafico in un'immagine**
I grafici sono visualmente accattivanti e rendono facile per gli utenti vedere confronti, modelli e tendenze nei dati.
Il metodo toImage della classe Chart converte il grafico in un file immagine, che può essere salvato su disco o su stream.

**Java**

{{< highlight java >}}

 //Get the Chart image

ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();

imgOpts.setImageFormat(ImageFormat.getPng());

//Save the chart image file.

chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage_Out.png"), imgOpts);

{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Scarica il codice di esempio**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/charts/convertcharttoimage/AsposeChartToImage.java)

{{% alert color="primary" %}} 

Per ulteriori dettagli, visita [Conversione del grafico in un'immagine](/java/converting-chart-to-image).

{{% /alert %}}
