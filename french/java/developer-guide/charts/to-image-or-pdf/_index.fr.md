---
title: Rendu du graphique
linktitle: En image ou en PDF
type: docs
weight: 40
url: /fr/java/chart-rendering/
---

## **Création de graphiques**

Les API Aspose.Cells prennent en charge la création d'une variété de graphiques Excel comme détaillé dans le sujet [Création et personnalisation de graphiques Excel](/cells/fr/java/creating-and-customizing-charts/). Afin de démontrer l'utilisation des API Aspose.Cells pour rendre les graphiques au format image et PDF, nous créerons un graphique de type Colonne selon l'extrait suivant.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

## **Rendu des graphiques**

Les API Aspose.Cells supportent la conversion des graphiques Excel en images et formats PDF sans nécessiter d'outils ou d'applications supplémentaires. Afin de fournir un support de rendu, la classe [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) a exposé les méthodes [**toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage-java.io.OutputStream-com.aspose.cells.ImageOrPrintOptions-) et [**toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf-java.io.OutputStream-) avec une variété de surcharges pour convenir au mieux aux besoins de l'application.

### **Rendu des graphiques en images**

La méthode [**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage-java.io.OutputStream-com.aspose.cells.ImageOrPrintOptions-) comporte une variété de surcharges pour prendre en charge un rendu simple ainsi qu'un rendu avancé. Si l'exigence de l'application est de rendre le graphique dans ses dimensions par défaut, nous vous suggérons d'utiliser la méthode [**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage-java.io.OutputStream-com.aspose.cells.ImageOrPrintOptions-) comme suit.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-RenderChartsToImages-RenderChartsToImages.java" >}}

Il est également possible de rendre les graphiques en images avec des paramètres avancés. Les API Aspose.Cells ont exposé une version surchargée de la méthode [**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage-java.io.OutputStream-com.aspose.cells.ImageOrPrintOptions-) qui pourrait accepter une instance de [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) tout en permettant de spécifier des paramètres tels que la résolution, les indications de rendu, le format d'image, etc.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChartRendering-ChartRendering.java" >}}

### **Rendu du graphique en PDF**

Afin de rendre le graphique au format PDF, les API Aspose.Cells ont exposé la méthode [**Chart.toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf-java.io.OutputStream-) avec la possibilité de stocker le PDF résultant sur le chemin du disque ou une instance de OutputStream.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-chartsRenderChartsToPdf-RenderChartsToPdf.java" >}}

## **Types de graphiques supportés pour le rendu**

Il existe quelques types de graphiques qui ne sont actuellement pas pris en charge pour le rendu. Ces types de graphiques contiennent **N** dans la colonne **Pris en charge** du tableau ci-dessous.

|**Type de graphique**|**Sous-type de graphique**|**Pris en charge**|
| :- | :- | :- |
|**Column**|Column|**Y**|
| |ColumnStacked|**Y**|
| |Column100PercentStacked|**Y**|
| |Column3DClustered|**Y**|
| |Column3DStacked|**Y**|
| |Column3D100PercentStacked|**Y**|
| |Column3D|**Y**|
|**Bar**|Bar|**Y**|
| |BarStacked|**Y**|
| |Bar100PercentStacked|**Y**|
| |Bar3DClustered|**Y**|
| |Bar3DStacked|**Y**|
| |Bar3D100PercentStacked|**Y**|
|**Line**|Line|**Y**|
| |LineStacked|**Y**|
| |Line100PercentStacked|**Y**|
| |LineWithDataMarkers|**Y**|
| |LineStackedWithDataMarkers|**Y**|
| |Line100PercentStackedWithDataMarkers|**Y**|
| |Line3D|**Y**|
|**Pie**|Pie|**Y**|
| |Pie3D|**Y**|
| |PiePie|**Y**|
| |PieExploded|**Y**|
| |Pie3DExploded|**Y**|
| |PieBar|**Y**|
|**Scatter**|Scatter|**Y**|
| |ScatterConnectedByCurvesWithDataMarker|**Y**|
| |ScatterConnectedByCurvesWithoutDataMarker|**Y**|
| |ScatterConnectedByLinesWithDataMarker|**Y**|
| |ScatterConnectedByLinesWithoutDataMarker|**Y**|
|**Area**|Area|**Y**|
| |AreaStacked|**Y**|
| |Area100PercentStacked|**Y**|
| |Area3D|**Y**|
| |Area3DStacked|**Y**|
| |Area3D100PercentStacked|**Y**|
|**Doughnut**|Doughnut|**Y**|
| |DoughnutExploded|**Y**|
|**Radar**|Radar|**Y**|
| |RadarWithDataMarkers|**Y**|
| |RadarFilled|**Y**|
|**Surface**|Surface3D|N|
| |SurfaceWireframe3D|N|
| |SurfaceContour|N|
| |SurfaceContourWireframe|N|
|**Bubble**|Bubble|**Y**|
| |Bubble3D|N|
|**Stock**|StockHighLowClose|**Y**|
| |StockOpenHighLowClose|**Y**|
| |StockVolumeHighLowClose|**Y**|
| |StockVolumeOpenHighLowClose|**Y**|
|**Cylinder**|Cylinder|**Y**|
| |CylinderStacked|**Y**|
| |Cylinder100PercentStacked|**Y**|
| |CylindricalBar|**Y**|
| |CylindricalBarStacked|**Y**|
| |CylindricalBar100PercentStacked|**Y**|
| |CylindricalColumn3D|**Y**|
|**Cone**|Cone|**Y**|
| |ConeStacked|**Y**|
| |Cone100PercentStacked|**Y**|
| |ConicalBar|**Y**|
| |ConicalBarStacked|**Y**|
| |ConicalBar100PercentStacked|**Y**|
| |ConicalColumn3D|**Y**|
|**Pyramid**|Pyramid|**Y**|
| |PyramidStacked|**Y**|
| |Pyramid100PercentStacked|**Y**|
| |PyramidBar|**Y**|
| |PyramidBarStacked|**Y**|
| |PyramidBar100PercentStacked|**Y**|
| |PyramidColumn3D|**Y**|
|**BoxWhisker**|BoxWhisker|Y|
|**Funnel**|Funnel|**Y**|
|**ParetoLine**|ParetoLine|**Y**|
|**Sunburst**|Sunburst|**Y**|
|**Treemap**|Treemap|**Y**|
|**Waterfall**|Waterfall|**Y**|
|**Histogram**|Histogram|Y|
|**Map**|Map|**N**|

{{% alert color="primary" %}}

Dans le cas où vous tenteriez de rendre les types de graphiques non pris en charge en image ou en PDF, vous pourriez obtenir des images de taille 0 ou un PDF vierge.

{{% /alert %}}


## **Sujets avancés**
- [Conversion de graphique en image au format SVG](/cells/fr/java/converting-chart-to-image-in-svg-format/)
- [Créer un PDF de graphique avec la taille de page souhaitée](/cells/fr/java/create-chart-pdf-with-desired-page-size/)
- [Exportation du graphique en SVG avec l'attribut viewBox](/cells/fr/java/export-chart-to-svg-with-viewbox-attribute/)
{{< app/cells/assistant language="java" >}}
