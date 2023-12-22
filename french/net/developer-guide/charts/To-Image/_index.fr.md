---
title: Graphique en image
description: Découvrez comment utiliser Aspose.Cells for .NET pour convertir un graphique en un format d'image, tel que JPEG ou PNG. Notre guide vous montrera comment exporter un graphique à partir d'Excel Microsoft et l'enregistrer en tant qu'image autonome pour une utilisation et une manipulation ultérieures.
keywords: Aspose.Cells for .NET, Chart to Image, Microsoft Excel, Image Conversion, Export, Standalone Image.
linktitle: Graphique en image
type: docs
weight: 46
url: /fr/net/chart-to-image/
---
##  **Graphiques de rendu**

 Aspose.Cells Prise en charge des API pour convertir les graphiques Excel en formats d'images sans nécessiter d'outils ou d'applications supplémentaires. Afin de fournir un support de rendu, le[**Graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) la classe a exposé[**VersImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) méthodes avec une multitude de surcharges pour répondre au mieux aux exigences de l'application.

###  **Rendu de graphiques en images**

 Le[**Graphique.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) La méthode a une multitude de surcharges pour prendre en charge le rendu simple et avancé. Si l'exigence de l'application est de restituer le graphique dans ses dimensions par défaut, nous vous suggérons d'utiliser l'option[**Graphique.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)méthode comme suit.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

 Il est également possible de restituer les graphiques en images avec des paramètres avancés. Aspose.Cells Les API ont exposé une version en surcharge de[**Graphique.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) méthode qui pourrait accepter une instance de[**OptionsImageOuImpression**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)tout en permettant de spécifier des paramètres tels que la résolution, le mode de lissage, le format d'image, etc.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

##  **Types de graphiques pris en charge pour le rendu**

 Certains types de graphiques ne sont actuellement pas pris en charge pour le rendu. Ces types de graphiques contiennent**N** dans le **Supporté** colonne du tableau ci-dessous.

|**Type de graphique**|**Sous-type de graphique**|**Prise en charge**|
| :- | :- | :- |
|**Colonne**|Colonne|*O**|
| |ColonneStacked|*O**|
| |Colonne100PercentStacked|*O**|
| |Colonne3DCclustérisée|*O**|
| |Colonne3DStacked|*O**|
| |Colonne3D100PourcentageStacked|*O**|
| |Colonne3D|*O**|
|**Bar**|Bar|*O**|
| |BarStacked|*O**|
| |Bar100PourcentEmpilé|*O**|
| |Bar3DCluster|*O**|
| |Bar3DSempilé|*O**|
| |Bar3D100PourcentageEmpilé|*O**|
|**Doubler**|Doubler|*O**|
| |LigneStacked|*O**|
| |Ligne100PercentStacked|*O**|
| |LigneAvecDataMarkers|*O**|
| |LineStackedWithDataMarkers|*O**|
| |Ligne100PercentStackedWithDataMarkers|*O**|
| |Ligne3D|*O**|
|**Tarte**|Tarte|*O**|
| |Tarte3D|*O**|
| |TarteTarte|*O**|
| |TarteExplodé|*O**|
| |Tarte3DExplodé|*O**|
| |TarteBar|*O**|
|**Dispersion**|Dispersion|*O**|
| |DispersionConnectéeByCurvesWithDataMarker|*O**|
| |DispersionConnectedByCurvesWithoutDataMarker|*O**|
| |DispersionConnectedByLinesWithDataMarker|*O**|
| |DispersionConnectedByLinesWithoutDataMarker|*O**|
|**Zone**|Zone|*O**|
| |ZoneStacked|*O**|
| |Zone100PourcentageStacked|*O**|
| |Zone3D|*O**|
| |Area3DSacked|*O**|
| |Surface3D100PourcentageStacked|*O**|
|**Donut**|Donut|*O**|
| |BeignetExplosé|*O**|
|**Radar**|Radar|*O**|
| |RadarAvecDataMarkers|*O**|
| |RadarRempli|*O**|
|**Surface**|Surface3D|N|
| |SurfaceFilaire3D|N|
| |Contour de surface|N|
| |SurfaceContourFilaire|N|
|**Bulle**|Bulle|*O**|
| |Bulle3D|N|
|**Action**|StockHautBasFermer|*O**|
| |StockOuvertHautBasFermer|*O**|
| |StockVolumeÉlevéFaibleFermer|*O**|
| |StockVolumeOuvertHautBasFermer|*O**|
|**Cylindre**|Cylindre|*O**|
| |CylindreStacked|*O**|
| |Cylindre100PourcentEmpilé|*O**|
| |Barre Cylindrique|*O**|
| |CylindriqueBarEmpilé|*O**|
| |CylindriqueBar100PourcentEmpilé|*O**|
| |CylindriqueColonne3D|*O**|
|**Cône**|Cône|*O**|
| |CôneEmpilé|*O**|
| |Cône100PourcentEmpilé|*O**|
| |Barre conique|*O**|
| |ConiqueBarEmpilé|*O**|
| |ConiqueBar100PourcentEmpilé|*O**|
| |ConiqueColonne3D|*O**|
|**Pyramide**|Pyramide|*O**|
| |PyramideEmpilé|*O**|
| |Pyramide100PourcentEmpilé|*O**|
| |PyramideBar|*O**|
| |PyramideBarEmpilé|*O**|
| |PyramideBar100PourcentEmpilé|*O**|
| |PyramideColonne3D|*O**|
|**BoîteWhisker**|BoîteWhisker|Y|
|**Entonnoir**|Entonnoir|*O**|
|**Ligne Pareto**|Ligne Pareto|*O**|
|**Coup de soleil**|Coup de soleil|*O**|
|**Treemap**|Treemap|*O**|
|**Cascade**|Cascade|*O**|
|**Histogramme**|Histogramme|Y|
|**Carte**|Carte|*N**|

{{% alert color="primary" %}}

Si vous essayez de restituer les types de graphiques non pris en charge en image ou PDF, vous risquez de vous retrouver avec des images de taille 0 ou PDF vierge.

{{% /alert %}}

##  **Sujets avancés**
- [Convertir le graphique en PDF](/cells/fr/net/chart-to-pdf/)
