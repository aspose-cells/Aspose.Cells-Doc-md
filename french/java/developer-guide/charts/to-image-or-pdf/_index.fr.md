---
title: Rendu graphique
linktitle: Vers Image ou Pdf
type: docs
weight: 40
url: /fr/java/chart-rendering/
---
## **Création de graphiques**

 Aspose.Cells Prise en charge des API pour créer une vérité de graphiques Excel comme détaillé sous le sujet[Création et personnalisation de graphiques Excel](/cells/fr/java/creating-and-customizing-charts/)Afin de démontrer l'utilisation des API Aspose.Cells pour afficher les graphiques au format image et PDF, nous allons créer un graphique de type Colonne selon l'extrait suivant.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

## **Graphiques de rendu**

 Aspose.Cells Prise en charge des API pour convertir les graphiques Excel en images et en formats PDF sans nécessiter d'outils ou d'applications supplémentaires. Afin de fournir un support de rendu, le[**Graphique**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)la classe a exposé[**àImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) & [**versPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf(java.io.OutputStream)) méthodes avec une multitude de surcharges pour répondre au mieux aux exigences de l'application.

### **Rendu des graphiques en images**

 La[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) a une vérité de surcharges pour prendre en charge le rendu simple et avancé. Si l'exigence de l'application est de rendre le graphique dans ses dimensions par défaut, nous vous suggérons d'utiliser le[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) méthode comme suit.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-RenderChartsToImages-RenderChartsToImages.java" >}}

Il est également possible de rendre les graphiques en images avec des paramètres avancés. Aspose.Cells Les API ont exposé une version de surcharge de[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions) ) méthode qui pourrait accepter une instance de[**Options d'image ou d'impression**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)tout en permettant de spécifier des paramètres tels que la résolution, les astuces de rendu, le format d'image, etc.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChartRendering-ChartRendering.java" >}}

### **Graphique de rendu au format PDF**

 Afin de rendre le graphique au format PDF, les API Aspose.Cells ont exposé le[**Graphique.toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf(java.io.OutputStream)) méthode avec la possibilité de stocker le PDF résultant sur le chemin du disque ou une instance de OutputStream.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-chartsRenderChartsToPdf-RenderChartsToPdf.java" >}}

## **Types de graphiques pris en charge pour le rendu**

 Il existe quelques types de graphiques qui ne sont actuellement pas pris en charge pour le rendu. Ces types de graphiques contiennent** N ** dans le**Colonne prise en charge** du tableau ci-dessous.

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
- [Conversion d'un graphique en image au format SVG](/cells/fr/java/converting-chart-to-image-in-svg-format/)
- [Créer un graphique PDF avec la taille de page souhaitée](/cells/fr/java/create-chart-pdf-with-desired-page-size/)
- [Exporter le graphique vers SVG avec l'attribut viewBox](/cells/fr/java/export-chart-to-svg-with-viewbox-attribute/)
