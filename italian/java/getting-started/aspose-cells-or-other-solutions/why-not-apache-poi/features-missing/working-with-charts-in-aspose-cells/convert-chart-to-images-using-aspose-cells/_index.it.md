---
title: Converti grafico in immagini utilizzando Aspose.Cells
type: docs
weight: 30
url: /it/java/convert-chart-to-images-using-aspose-cells/
---
## **Aspose.Cells - Converti grafico in immagini**
I grafici sono visivamente accattivanti e consentono agli utenti di vedere facilmente confronti, modelli e tendenze nei dati.
Il metodo toImage della classe Chart converte il grafico in un file immagine, che può essere salvato su disco o in streaming.

**Giava**

{{< highlight "java" >}}

 //Get the Chart image

ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();

imgOpts.setImageFormat(ImageFormat.getPng());

//Save the chart image file.

chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage.png"), imgOpts);

{{< /highlight >}}
## **Scarica il codice in esecuzione**

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposeChartToImage.java)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Conversione del grafico in immagine](/java/converting-chart-to-image).

{{% /alert %}}
