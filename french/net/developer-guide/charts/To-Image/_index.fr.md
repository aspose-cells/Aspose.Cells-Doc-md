---
title: Graphique à image
linktitle: Graphique à image
type: docs
weight: 46
url: /fr/net/chart-to-image/
---
##  **Graphiques de rendu**

 Aspose.Cells Prise en charge des API pour convertir les graphiques Excel en formats d'images sans nécessiter d'outils ou d'applications supplémentaires. Afin de fournir un support de rendu, le[**Graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) la classe a exposé[**VersImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) méthodes avec une multitude de surcharges pour répondre au mieux aux exigences de l'application.

###  **Rendu des graphiques en images**

 Le[**Chart.ToImageChart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) La méthode a une vérité de surcharges pour prendre en charge le rendu simple et avancé. Si l'exigence de l'application est de rendre le graphique dans ses dimensions par défaut, nous vous suggérons d'utiliser le[**Chart.ToImageChart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)méthode comme suit.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

 Il est également possible de rendre les graphiques en images avec des paramètres avancés. Aspose.Cells Les API ont exposé une version de surcharge de[**Chart.ToImageChart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) méthode qui pourrait accepter une instance de[**Options d'image ou d'impression**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), tout en permettant de spécifier des paramètres tels que la résolution, le mode de lissage, le format d'image, etc.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

##  **Types de graphiques pris en charge pour le rendu**

 Il existe quelques types de graphiques qui ne sont actuellement pas pris en charge pour le rendu. Ces types de graphiques contiennent**N** dans le **pris en charge** colonne du tableau ci-dessous.

|**Type de graphique**|**Sous-type de graphique**|**Prise en charge**|
| :- | :- | :- |
|**Colonne**|Colonne|*Y**|
| |Colonneempilée|*Y**|
| |Colonne100PercentStacked|*Y**|
| |Colonne3DCluster|*Y**|
| |Colonne3DSempilé|*Y**|
| |Column3D100PercentStacked|*Y**|
| |Colonne3D|*Y**|
|**Bar**|Bar|*Y**|
| |Barreempilée|*Y**|
| |Barre100PercentStacked|*Y**|
| |Bar3DCluster|*Y**|
| |Bar3DStacked|*Y**|
| |Barre3D100Pourcentage empilé|*Y**|
|**Doubler**|Doubler|*Y**|
| |Ligneempilée|*Y**|
| |Line100PercentStacked|*Y**|
| |LineWithDataMarkers|*Y**|
| |LineStackedWithDataMarkers|*Y**|
| |Line100PercentStackedWithDataMarkers|*Y**|
| |Ligne3D|*Y**|
|**Tarte**|Tarte|*Y**|
| |Pie3D|*Y**|
| |TarteTarte|*Y**|
| |TarteExplosée|*Y**|
| |Tarte3DÉclaté|*Y**|
| |PieBar|*Y**|
|**Dispersion**|Dispersion|*Y**|
| |ScatterConnectedByCurvesWithDataMarker|*Y**|
| |ScatterConnectedByCurvesWithoutDataMarker|*Y**|
| |ScatterConnectedByLinesWithDataMarker|*Y**|
| |ScatterConnectedByLinesWithoutDataMarker|*Y**|
|**Zone**|Zone|*Y**|
| |Zoneempilée|*Y**|
| |Area100PercentStacked|*Y**|
| |Zone3D|*Y**|
| |Area3DStacked|*Y**|
| |Area3D100PercentStacked|*Y**|
|**Donut**|Donut|*Y**|
| |BeignetÉclaté|*Y**|
|**Radar**|Radar|*Y**|
| |RadarAvecMarqueursDeDonnées|*Y**|
| |Radar Rempli|*Y**|
|**Surface**|Surface3D|N|
| |SurfaceWireframe3D|N|
| |Contour de surface|N|
| |SurfaceContourWireframe|N|
|**Bulle**|Bulle|*Y**|
| |Bulle3D|N|
|**Action**|StockHautBasFermer|*Y**|
| |StockOuvertHautBasFermer|*Y**|
| |StockVolumeHautBasFermer|*Y**|
| |StockVolumeOuvertHautBasFermer|*Y**|
|**Cylindre**|Cylindre|*Y**|
| |CylindreEmpilé|*Y**|
| |Cylindre100PercentStacked|*Y**|
| |CylindriqueBar|*Y**|
| |CylindriqueBarEmpilés|*Y**|
| |CylindriqueBar100PercentStacked|*Y**|
| |CylindriqueColonne3D|*Y**|
|**Cône**|Cône|*Y**|
| |ConeStacked|*Y**|
| |Cône100PercentStacked|*Y**|
| |Barre conique|*Y**|
| |ConiqueBarEmpilés|*Y**|
| |ConicalBar100PercentStacked|*Y**|
| |ConicalColumn3D|*Y**|
|**Pyramide**|Pyramide|*Y**|
| |PyramideEmpilés|*Y**|
| |Pyramid100PercentStacked|*Y**|
| |PyramidBar|*Y**|
| |PyramideBarEmpilés|*Y**|
| |PyramidBar100PercentStacked|*Y**|
| |PyramideColonne3D|*Y**|
|**BoxWhisker**|BoxWhisker|Y|
|**Entonnoir**|Entonnoir|*Y**|
|**Ligne de Pareto**|Ligne de Pareto|*Y**|
|**Coup de soleil**|Coup de soleil|*Y**|
|**Treemap**|Treemap|*Y**|
|**Cascade**|Cascade|*Y**|
|**Histogramme**|Histogramme|Y|
|**Carte**|Carte|*N**|

{{% alert color="primary" %}}

Si vous essayez de rendre les types de graphiques non pris en charge à l'image ou PDF, vous pouvez vous retrouver avec des images de taille 0 ou vide PDF.

{{% /alert %}}

##  **Sujets avancés**
- [Convertir le graphique en PDF](/cells/fr/net/chart-to-pdf/)
