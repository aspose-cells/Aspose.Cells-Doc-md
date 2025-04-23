---
title: Ajouter un filigrane Word Art au graphique
type: docs
weight: 10
url: /fr/java/add-word-art-watermark-to-chart/
---

## **Aspose.Cells - Ajouter un filigrane Word Art au graphique**
Vous pouvez utiliser WordArt pour ajouter des effets de texte spéciaux aux feuilles de calcul. Par exemple, étirer un titre, décorer du texte, ajuster un texte à une forme prédéfinie ou appliquer le texte affecté à la zone de traçage d'un graphique en tant que filigrane. Le WordArt devient un objet que vous pouvez déplacer ou positionner dans vos feuilles de calcul pour ajouter une décoration.

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
## **Télécharger le code en cours d'exécution**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AddWordArtWatermarkToChart.java)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Ajouter un filigrane WordArt au graphique](/cells/fr/java/add-wordart-watermark-to-chart).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
