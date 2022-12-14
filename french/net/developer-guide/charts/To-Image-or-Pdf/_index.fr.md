---
title: Rendu graphique
linktitle: Vers Image ou Pdf
type: docs
weight: 45
url: /fr/net/chart-rendering/
---
## **Graphiques de rendu**

 Aspose.Cells Prise en charge des API pour convertir les graphiques Excel en images et en formats PDF sans nécessiter d'outils ou d'applications supplémentaires. Afin de fournir un support de rendu, le[**Graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) la classe a exposé[**VersImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) & [**VersPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)méthodes avec une multitude de surcharges pour répondre au mieux aux exigences de l'application.

### **Rendu des graphiques en images**

 La[**Chart.ToImageChart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) & [**VersPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index) La méthode a une vérité de surcharges pour prendre en charge le rendu simple et avancé. Si l'exigence de l'application est de rendre le graphique dans ses dimensions par défaut, nous vous suggérons d'utiliser le[**Chart.ToImageChart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)méthode comme suit.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

 Il est également possible de rendre les graphiques en images avec des paramètres avancés. Aspose.Cells Les API ont exposé une version de surcharge de[**Chart.ToImageChart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) méthode qui pourrait accepter une instance de[**Options d'image ou d'impression**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), tout en permettant de spécifier des paramètres tels que la résolution, le mode de lissage, le format d'image, etc.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

### **Graphique de rendu au format PDF**

 Afin de rendre le graphique au format PDF, les API Aspose.Cells ont exposé le[**Graphique.VersPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)méthode avec la possibilité de stocker le PDF résultant sur le chemin du disque ou Stream.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToPDF.cs" >}}

## **Types de graphiques pris en charge pour le rendu**

 Il existe quelques types de graphiques qui ne sont actuellement pas pris en charge pour le rendu. Ces types de graphiques contiennent** N ** dans le**Colonne Pris en charge** du tableau ci-dessous.

|**Type de graphique**|**Sous-type de graphique**|**Prise en charge**|
|:- |:- |:- |
|**Colonne**|Colonne|**O**|
||Colonneempilée|**O**|
||Colonne100PercentStacked|**O**|
||Colonne3DCluster|**O**|
||Colonne3DSempilé|**O**|
||Column3D100PercentStacked|**O**|
||Colonne3D|**O**|
|**Bar**|Bar|**O**|
||Barreempilée|**O**|
||Barre100PercentStacked|**O**|
||Bar3DCluster|**O**|
||Bar3DStacked|**O**|
||Barre3D100Pourcentage empilé|**O**|
|**Ligne**|Ligne|**O**|
||Ligneempilée|**O**|
||Line100PercentStacked|**O**|
||LineWithDataMarkers|**O**|
||LineStackedWithDataMarkers|**O**|
||Line100PercentStackedWithDataMarkers|**O**|
||Ligne3D|**O**|
|**Tarte**|Tarte|**O**|
||Pie3D|**O**|
||TarteTarte|**O**|
||TarteExplosée|**O**|
||Tarte3DÉclaté|**O**|
||PieBar|**O**|
|**Dispersion**|Dispersion|**O**|
||ScatterConnectedByCurvesWithDataMarker|**O**|
||ScatterConnectedByCurvesWithoutDataMarker|**O**|
||ScatterConnectedByLinesWithDataMarker|**O**|
||ScatterConnectedByLinesWithoutDataMarker|**O**|
|**Zone**|Zone|**O**|
||Zoneempilée|**O**|
||Area100PercentStacked|**O**|
||Zone3D|**O**|
||Area3DStacked|**O**|
||Area3D100PercentStacked|**O**|
|**Donut**|Donut|**O**|
||BeignetÉclaté|**O**|
|**Radar**|Radar|**O**|
||RadarAvecMarqueursDeDonnées|**O**|
||Radar Rempli|**O**|
|**Surface**|Surface3D|N|
||SurfaceWireframe3D|N|
||Contour de surface|N|
||SurfaceContourWireframe|N|
|**Bulle**|Bulle|**O**|
||Bulle3D|N|
|**Stocker**|StockHautBasFermer|**O**|
||StockOuvertHautBasFermer|**O**|
||StockVolumeHautBasFermer|**O**|
||StockVolumeOuvertHautBasFermer|**O**|
|**Cylindre**|Cylindre|**O**|
||CylindreEmpilé|**O**|
||Cylindre100PercentStacked|**O**|
||CylindriqueBar|**O**|
||CylindriqueBarEmpilés|**O**|
||CylindriqueBar100PercentStacked|**O**|
||CylindriqueColonne3D|**O**|
|**Cône**|Cône|**O**|
||ConeStacked|**O**|
||Cône100PercentStacked|**O**|
||Barre conique|**O**|
||ConiqueBarEmpilés|**O**|
||ConicalBar100PercentStacked|**O**|
||ConicalColumn3D|**O**|
|**Pyramide**|Pyramide|**O**|
||PyramideEmpilés|**O**|
||Pyramid100PercentStacked|**O**|
||PyramidBar|**O**|
||PyramideBarEmpilés|**O**|
||PyramidBar100PercentStacked|**O**|
||PyramideColonne3D|**O**|
|**BoxWhisker**|BoxWhisker|Oui|
|**Entonnoir**|Entonnoir|**O**|
|**Ligne de Pareto**|Ligne de Pareto|**O**|
|**Coup de soleil**|Coup de soleil|**O**|
|**Treemap**|Treemap|**O**|
|**Cascade**|Cascade|**O**|
|**Histogramme**|Histogramme|Oui|
|**Carte**|Carte|**N**|

{{% alert color="primary" %}}

Si vous essayez de rendre les types de graphiques non pris en charge en image ou en PDF, vous risquez de vous retrouver avec des images de taille 0 ou un PDF vierge.

{{% /alert %}}

## **Sujets avancés**
- [Convertir le graphique en PDF avec la taille de page souhaitée](/cells/fr/net/chart-to-pdf/)
