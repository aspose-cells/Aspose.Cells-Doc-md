---
title: Aggiungi una filigrana con Word Art al grafico
type: docs
weight: 10
url: /it/java/add-word-art-watermark-to-chart/
---

## **Aspose.Cells - Aggiungi una filigrana con Word Art al grafico**
Puoi usare WordArt per aggiungere effetti speciali al testo nei fogli di calcolo. Ad esempio, distende un titolo, decora il testo, fa adattare il testo a una forma preimpostata o applica il testo interessato all'area di trama di un grafico come un watermark. Il WordArt diventa un oggetto che puoi spostare o posizionare nei fogli di calcolo per aggiungere decorazioni.

**Java**

{{< highlight java >}}

 //Instantiate a new workbook.

//Open the existing excel file.

Workbook workbook = new Workbook(dataDir + "AsposeChart.xls");

//Get the chart in the first worksheet.

com.aspose.cells.Chart chart = workbook.getWorksheets().get(0).getCharts().get(0);

//Add a WordArt watermark (shape) to the chart's plot area.

com.aspose.cells.Shape wordart = chart.getShapes().addTextEffectInChart(MsoPresetTextEffect.TEXT_EFFECT_2,

"CONFIDENTIAL", "Arial Black", 66, false, false, 1200, 500, 2000, 3000);

//Get the shape's fill format.

FillFormat wordArtFormat = wordart.getFill();

//Set the transparency.

wordArtFormat.setTransparency(0.9);

//Make the line invisible.

wordart.setHasLine(false);

//Save the excel file.

workbook.save(dataDir + "AsposeChartWatermarked_Out.xls", SaveFormat.EXCEL_97_TO_2003);

{{< /highlight >}}
## **Scarica il codice in esecuzione**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AddWordArtWatermarkToChart.java)

{{% alert color="primary" %}} 

Per ulteriori dettagli, visita [Aggiungi una filigrana con WordArt al grafico](/cells/it/java/add-wordart-watermark-to-chart).

{{% /alert %}}
