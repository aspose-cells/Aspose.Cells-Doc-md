---
title: Rendu graphique
type: docs
weight: 30
url: /fr/cpp/chart-rendering/
---
## **Création de graphiques**

Aspose.Cells Prise en charge des API pour créer une vérité de graphiques Excel comme détaillé sous le sujet[Création et personnalisation de graphiques Excel](/cells/fr/cpp/creating-and-customizing-charts/)Afin de démontrer l'utilisation des API Aspose.Cells pour afficher les graphiques au format image et PDF, nous allons créer un graphique de type Colonne selon l'extrait suivant.

{{< highlight "cpp" >}}

     // Create a new workbook

	intrusive_ptr<IWorkbook> workbook = Factory::CreateIWorkbook();

	// Get first worksheet which is created by default

	intrusive_ptr<IWorksheet> worksheet = workbook->GetIWorksheets()->GetObjectByIndex(0);

	// Adding sample values to cells

	worksheet->GetICells()->GetObjectByIndex(new String("A1"))->PutValue(50);

	worksheet->GetICells()->GetObjectByIndex(new String("A2"))->PutValue(100);

	worksheet->GetICells()->GetObjectByIndex(new String("A3"))->PutValue(150);

	worksheet->GetICells()->GetObjectByIndex(new String("B1"))->PutValue(4);

	worksheet->GetICells()->GetObjectByIndex(new String("B2"))->PutValue(20);

	worksheet->GetICells()->GetObjectByIndex(new String("B3"))->PutValue(50);

	// Adding a chart to the worksheet

	int chartIndex = worksheet->GetICharts()->Add(Aspose::Cells::Charts::ChartType::ChartType_Column, 5, 0, 20, 8);

	// Accessing the instance of the newly added chart

	intrusive_ptr<Aspose::Cells::Charts::IChart> chart = worksheet->GetICharts()->GetObjectByIndex(chartIndex);

	// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"

	chart->GetNISeries()->Add(new String("A1:B3"), true);

{{< /highlight >}}

## **Graphiques de rendu**

Aspose.Cells Prise en charge des API pour convertir les graphiques Excel en images et en formats PDF sans nécessiter d'outils ou d'applications supplémentaires. Afin de fournir la prise en charge du rendu, la classe Chart a exposé les méthodes ToImage et ToPdf avec une multitude de surcharges pour répondre au mieux aux exigences de l'application.

### **Rendu des graphiques en images**

La méthode Chart.toImage a une vérité de surcharges pour prendre en charge le rendu simple et avancé. Si l'exigence de l'application est de rendre le graphique dans ses dimensions par défaut, nous vous suggérons d'utiliser la méthode Chart.toImage comme suit.

{{< highlight "cpp" >}}

 // Output directory path

StringPtr outDir = new String("..\\Data\\02_OutputDirectory\\");

// Path of output image file

StringPtr outputChartImage = outDir->StringAppend(new String("out1image.png"));

// Saving the chart to image file

chart->ToImage(outputChartImage, Aspose::Cells::System::Drawing::Imaging::ImageFormat::GetPng());

{{< /highlight >}}

### **Graphique de rendu au format PDF**

Afin de rendre le graphique au format PDF, les API Aspose.Cells ont exposé la méthode Chart.ToPdf avec la possibilité de stocker le PDF résultant sur le chemin du disque ou Stream.

{{< highlight "cpp" >}}

 // Path of output pdf file

StringPtr outputPdfFile = outDir->StringAppend(new String("out1pdf.pdf"));

// Saving chart to PDF

chart->ToPdf(outputPdfFile);

{{< /highlight >}}

## **Types de graphiques pris en charge pour le rendu**

Il existe quelques types de graphiques qui ne sont actuellement pas pris en charge pour le rendu. Ces types de graphiques contiennent**N ** dans le**Colonne prise en charge** du tableau ci-dessous.

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
|Stocker|StockHautBasFermer|**O**|
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
