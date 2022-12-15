---
title: Aggiungi filigrana Word Art al grafico
type: docs
weight: 10
url: /it/java/add-word-art-watermark-to-chart/
---
## **Aspose.Cells - Aggiungi filigrana Word Art al grafico**
Puoi utilizzare WordArt per aggiungere effetti di testo speciali ai fogli di calcolo. Ad esempio, allungare un titolo, decorare il testo, adattare il testo a una forma preimpostata o applicare il testo interessato all'area del tracciato di un grafico come filigrana. La WordArt diventa un oggetto che puoi spostare o posizionare nei tuoi fogli di calcolo per aggiungere decorazioni.

**Giava**

{{< highlight "java" >}}

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

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AddWordArtWatermarkToChart.java)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Aggiungi filigrana WordArt al grafico](/cells/it/java/add-wordart-watermark-to-chart).

{{% /alert %}}
