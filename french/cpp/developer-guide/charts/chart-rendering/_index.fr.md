---
title: Rendu graphique
type: docs
weight: 30
url: /fr/cpp/chart-rendering/
---
##  **Création de graphiques**

Aspose.Cells Prise en charge des API pour créer une multitude de graphiques Excel comme détaillé dans le sujet[Création et personnalisation de graphiques Excel](/cells/fr/cpp/creating-and-customizing-charts/). Afin de démontrer l'utilisation des API Aspose.Cells pour restituer les graphiques au format image et PDF, nous allons créer un graphique de type Colonne selon l'extrait suivant.

{{< highlight "cpp" >}}

Aspose::Cells::Startup();

// Output directory path
U16String outDir(u"..\\Data\\02_OutputDirectory\\");

// Create a new workbook
Workbook workbook;

// Get first worksheet which is created by default
Worksheet worksheet = workbook.GetWorksheets().Get(0);

// Adding sample values to cells
worksheet.GetCells().Get(u"A1").PutValue(50);
worksheet.GetCells().Get(u"A2").PutValue(100);
worksheet.GetCells().Get(u"A3").PutValue(150);
worksheet.GetCells().Get(u"B1").PutValue(4);
worksheet.GetCells().Get(u"B2").PutValue(20);
worksheet.GetCells().Get(u"B3").PutValue(50);

// Adding a chart to the worksheet
int chartIndex = worksheet.GetCharts().Add(Aspose::Cells::Charts::ChartType::Column, 5, 0, 20, 8);

// Accessing the instance of the newly added chart
Chart chart = worksheet.GetCharts().Get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.GetNSeries().Add(u"A1:B3", true);

// Path of output image file
U16String outputChartImage = outDir + u"out1image.png";
chart.ToImage(outputChartImage, ImageType::Png);

// Path of output pdf file
U16String outputPdfFile = outDir + u"out1pdf.pdf";

// Saving chart to PDF
chart.ToPdf(outputPdfFile);

Aspose::Cells::Cleanup();

{{< /highlight >}}

##  **Graphiques de rendu**

Prise en charge des API Aspose.Cells pour convertir les graphiques Excel en images et formats PDF sans nécessiter d'outils ou d'applications supplémentaires. Afin de fournir la prise en charge du rendu, la classe Chart a exposé les méthodes ToImage et ToPdf avec une multitude de surcharges pour répondre au mieux aux exigences de l'application.

###  **Rendu de graphiques en images**

La méthode Chart.toImage dispose d'une multitude de surcharges pour prendre en charge un rendu simple et avancé. Si l'exigence de l'application est de restituer le graphique dans ses dimensions par défaut, nous vous suggérons d'utiliser la méthode Chart.toImage comme suit.

{{< highlight "cpp" >}}

// Path of output image file
U16String outputChartImage = outDir + u"out1image.png";

// Saving the chart to image file
chart.ToImage(outputChartImage, ImageType::Png);

{{< /highlight >}}

###  **Tableau de rendu au PDF**

Afin de restituer le graphique au format PDF, les API Aspose.Cells ont exposé la méthode Chart.ToPdf avec la possibilité de stocker le PDF résultant sur un chemin de disque ou un flux.

{{< highlight "cpp" >}}

// Path of output pdf file
U16String outputPdfFile = outDir + u"out1pdf.pdf";

// Saving chart to PDF
chart.ToPdf(outputPdfFile);

{{< /highlight >}}

##  **Types de graphiques pris en charge pour le rendu**

Certains types de graphiques ne sont actuellement pas pris en charge pour le rendu. Ces types de graphiques contiennent**N** dans le **Supporté**colonne du tableau ci-dessous.

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
|Action|StockHautBasFermer|*O**|
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
