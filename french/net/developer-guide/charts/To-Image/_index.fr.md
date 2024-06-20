---
title: Graphique vers image
description: Apprenez comment utiliser Aspose.Cells for .NET pour convertir un graphique en un format d image, tel que JPEG ou PNG. Notre guide vous montrera comment exporter un graphique depuis Microsoft Excel et le sauvegarder en tant qu image autonome pour une utilisation ultérieure et une manipulation.
keywords: Aspose.Cells for .NET, Graphique vers image, Microsoft Excel, Conversion d image, Exportation, Image autonome.
linktitle: Graphique vers image
type: docs
weight: 46
url: /fr/net/chart-to-image/
---

## **Rendu des graphiques**

Les API Aspose.Cells prennent en charge la conversion des graphiques Excel vers des formats d'images sans nécessiter d'outils ou d'applications supplémentaires. Afin de fournir un support de rendu, la classe [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) a exposé [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) méthodes avec une variété de surcharges pour mieux répondre aux exigences de l'application.

### **Rendu des graphiques en images**

La méthode [**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) a une variété de surcharges pour prendre en charge un rendu simple ainsi qu'avancé. Si l'exigence de l'application est de rendre le graphique dans ses dimensions par défaut, nous vous suggérons d'utiliser la méthode [**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) comme suit.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

Il est également possible de rendre les graphiques en images avec des paramètres avancés. Les API Aspose.Cells ont exposé une version de surcharge de la méthode [**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) pouvant accepter une instance de [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), tout en permettant de spécifier des paramètres tels que la résolution, le mode lissage, le format d'image, etc.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

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
- [Convertir le graphique en PDF](/cells/fr/net/chart-to-pdf/)
