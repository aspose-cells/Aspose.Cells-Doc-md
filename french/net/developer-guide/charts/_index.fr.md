---
title: Créer et gérer un graphique
linktitle: Graphiques
type: docs
weight: 130
url: /fr/net/creating-charts/
description: Créez un graphique dans CSharp pour les fichiers Excel et ODS.
keywords: create a chart, make a graph 
---
{{% alert color="primary" %}}

Il est possible d'ajouter une variété de graphiques aux feuilles de calcul avec Aspose.Cells. Aspose.Cells fournit de nombreux objets graphiques flexibles. Cette rubrique traite des objets graphiques Aspose.Cells'.

{{% /alert %}}

## **Création de graphiques**

### **Créer simplement un graphique**
Il est simple de créer un graphique avec Aspose.Cells avec les exemples de codes suivants :
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateColumnChart-1.cs" >}}

### **Ce qu'il faut savoir pour créer un graphique**

Avant de créer des graphiques, il est important de comprendre certains concepts de base utiles lors de la création de graphiques à l'aide de Aspose.Cells.

#### **Objets graphiques**

Aspose.Cells fournit un ensemble spécial de classes dans le[**Aspose.Cells.Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts) espace de noms utilisé pour créer les graphiques pris en charge par Aspose.Cells. Ces classes sont utilisées pour créer**tracer des objets**, qui agissent comme les blocs de construction du graphique. Les objets graphiques sont répertoriés ci-dessous :

- Série, une seule série de données dans un graphique.
- Axe, l'axe d'un graphique.
- Graphique, un seul graphique Excel.
- ChartArea, la zone de graphique dans la feuille de calcul.
- ChartDataTable, une table de données de graphique.
- ChartFrame, l'objet cadre dans un graphique.
- ChartPoint, un seul point d'une série dans un graphique.
- ChartPointCollection, une collection qui contient tous les points d'une série.
- Charts, une collection d'objets Chart.
- DataLabels, une collection de tous les objets DataLabel pour la série spécifiée.
- FillFormat, format de remplissage pour une forme.
- Sol, le sol d'un graphique 3D.
- Légende, la légende du graphique.
- Ligne, la ligne du graphique.
- SeriesCollection, une collection d'objets Series.
- TickLabels, les étiquettes de graduation associées aux graduations sur un axe de graphique.
- Titre, le titre d'un graphique ou d'un axe.
- Trendline, une ligne de tendance dans un graphique.
- TrendlineCollection, une collection de tous les objets Trendline pour la série de données spécifiée.
- Murs, les murs d'un graphique 3D.

#### **Utilisation d'objets graphiques**

Comme mentionné ci-dessus, tous les objets graphiques sont des instances de leurs classes respectives et fournissent des propriétés et des méthodes spécifiques pour effectuer des tâches spécifiques. Utilisez des objets graphiques pour créer des graphiques.

Ajoutez n'importe quel type de graphique à une feuille de calcul à l'aide de la[**Graphiques**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) le recueil. Chaque élément de la[**Graphiques**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) la collection représente un[**Graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) objet. UNE[**Graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)L'objet encapsule tous les autres objets graphiques requis pour personnaliser l'apparence du graphique. La section suivante montre comment utiliser quelques objets graphiques de base pour créer un graphique simple.

### **Créer un graphique à l'aide de Aspose.Cells**

**Pas:**

1.  Ajoutez des données aux cellules de la feuille de calcul avec le[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) objets[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)méthode.
 Il sera utilisé comme source de données pour le graphique.
1.  Ajoutez un graphique à la feuille de calcul en appelant le[**Graphiques**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection) de la collection[**Ajouter**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection/methods/add) méthode, encapsulée dans le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)objet.
1.  Spécifiez le type de graphique avec le[**Type de graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)énumération.
 Par exemple, l'exemple ci-dessous utilise le[**Type de graphique. Pyramide**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)valeur comme type de graphique.
1.  Accéder au nouveau[**Graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) objet de la[**Graphiques**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)collection en passant son index.
1.  Utilisez n'importe lequel des objets graphiques encapsulés dans le[**Graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)objet pour gérer le graphique.
 L'exemple ci-dessous utilise le[**SérieCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)objet de graphique pour spécifier la source de données du graphique.

Lors de l'ajout de données source au graphique, la source de données peut être une plage de cellules (telle que "A1:C3"), ou une séquence de cellules non contiguës (telle que "A1, A3, A5"), ou une séquence de valeurs (telles que "1,2,3").

Ces étapes générales vous permettent de créer n'importe quel type de graphique. Utilisez différents objets graphiques pour créer différents graphiques.

 Il est possible de créer de nombreux types de graphiques différents avec Aspose.Cells. Tous les graphiques standard pris en charge par Aspose.Cells sont prédéfinis dans une énumération nommée[**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).

Les types de graphiques prédéfinis sont :

|**Types de graphiques**|**Description**|
|:- |:- |
|Colonne|Représente l'histogramme groupé|
|Colonneempilée|Représente un graphique à colonnes empilées|
|Colonne100PercentStacked|Représente un graphique à colonnes empilées à 100 %|
|Colonne3DCluster|Représente l'histogramme groupé 3D|
|Colonne3DSempilé|Représente un graphique à colonnes empilées 3D|
|Column3D100PercentStacked|Représente un graphique à colonnes empilées 3D à 100 %|
|Colonne3D|Représente l'histogramme 3D|
|Bar|Représente un graphique à barres groupées|
|Barreempilée|Représente un graphique à barres empilées|
|Barre100PercentStacked|Représente un graphique à barres empilées à 100 %|
|Bar3DCluster|Représente un graphique à barres groupées 3D|
|Bar3DStacked|Représente un graphique à barres empilées 3D|
|Barre3D100Pourcentage empilé|Représente un graphique à barres empilées 3D à 100 %|
|La ligne|Représente le graphique en courbes|
|Ligneempilée|Représente un graphique en courbes empilées|
|Line100PercentStacked|Représente un graphique linéaire empilé à 100 %|
|LineWithDataMarkers|Représente le graphique linéaire avec des marqueurs de données|
|LineStackedWithDataMarkers|Représente un graphique en courbes empilées avec des marqueurs de données|
|Line100PercentStackedWithDataMarkers|Représente un graphique linéaire empilé à 100 % avec des marqueurs de données|
|Ligne3D|Représente un graphique en courbes 3D|
|Tarte|Représente le graphique à secteurs|
|Pie3D|Représente un graphique à secteurs 3D|
|TarteTarte|Représente Pie of Pie Chart|
|TarteExplosée|Représente un graphique à secteurs éclaté|
|Tarte3DÉclaté|Représente un graphique à secteurs éclaté en 3D|
|PieBar|Représente la barre du graphique à secteurs|
|Dispersion|Représente le nuage de points|
|ScatterConnectedByCurvesWithDataMarker|Représente le diagramme de dispersion relié par des courbes, avec des marqueurs de données|
|ScatterConnectedByCurvesWithoutDataMarker|Représente le diagramme de dispersion relié par des courbes, sans marqueurs de données|
|ScatterConnectedByLinesWithDataMarker|Représente le diagramme de dispersion relié par des lignes, avec des marqueurs de données|
|ScatterConnectedByLinesWithoutDataMarker|Représente le diagramme de dispersion connecté par des lignes, sans marqueurs de données|
|Surface|Représente le graphique en aires|
|Zoneempilée|Représente un graphique en aires empilées|
|Area100PercentStacked|Représente un graphique en aires empilées à 100 %|
|Zone3D|Représente le graphique en aires 3D|
|Area3DStacked|Représente un graphique en aires empilées 3D|
|Area3D100PercentStacked|Représente un graphique en aires empilées 3D à 100 %|
|Donut|Représente le graphique en anneau|
|BeignetÉclaté|Représente le graphique en anneau éclaté|
|Radar|Représente le graphique radar|
|RadarAvecMarqueursDeDonnées|Représente le graphique radar avec des marqueurs de données|
|Radar Rempli|Représente le graphique radar rempli|
|Surface3D|Représente le graphique de surface 3D|
|SurfaceWireframe3D|Représente le graphique de surface filaire 3D|
|Contour de surface|Représente le graphique de contour|
|SurfaceContourWireframe|Représente le graphique de contour filaire|
|Bulle|Représente le graphique à bulles|
|Bulle3D|Représente le graphique à bulles 3D|
|Cylindre|Représente le diagramme de cylindre|
|CylindreEmpilé|Représente un diagramme de cylindres empilés|
|Cylindre100PercentStacked|Représente un tableau de cylindres empilés à 100 %|
|Barre Cylindrique|Représente un graphique à barres cylindriques.|
|CylindriqueBarEmpilés|Représente un graphique à barres cylindriques empilés|
|CylindriqueBar100PercentStacked|Représente un graphique à barres cylindriques empilés à 100 %|
|CylindriqueColonne3D|Représente l'histogramme cylindrique 3D|
|Cône|Représente le graphique en cône|
|ConeStacked|Représente un graphique en cône empilé|
|Cône100PercentStacked|Représente un graphique en cône empilé à 100 %|
|Barre conique|Représente un graphique à barres coniques|
|ConiqueBarEmpilés|Représente un graphique à barres coniques empilées|
|ConicalBar100PercentStacked|Représente un graphique à barres coniques empilées à 100 %|
|ConicalColumn3D|Représente l'histogramme conique 3D|
|Pyramide|Représente un graphique pyramidal|
|PyramideEmpilés|Représente un graphique pyramidal empilé|
|Pyramid100PercentStacked|Représente un graphique pyramidal empilé à 100 %|
|PyramidBar|Représente un graphique à barres pyramidal|
|PyramideBarEmpilés|Représente un graphique à barres pyramidal empilé|
|PyramidBar100PercentStacked|Représente un graphique à barres pyramidal empilé à 100 %|
|PyramideColonne3D|Représente l'histogramme pyramidal 3D|
{{% alert color="primary" %}}

Lorsque vous affectez une plage de cellules comme source de données, vous ne pouvez définir la plage que du haut à gauche au bas à droite. Par exemple, "A1:C3" est valide alors que "C3:A1" n'est pas valide.

{{% /alert %}}

#### **Graphique pyramidal**

Lorsque l'exemple de code est exécuté, un graphique pyramidal est ajouté à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreatePyramidChart-1.cs" >}}

#### **Graphique en ligne**

 Dans l'exemple ci-dessus, il suffit de changer le[**Type de graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) à*La ligne*crée un graphique en courbes. La source complète est fournie ci-dessous. lorsque le code est exécuté, un graphique linéaire est ajouté à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateLineChart-1.cs" >}}

#### **Graphique à bulles**

 Pour créer un graphique à bulles, le[**Type de graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) doit être réglé sur[**Type de graphique. Bulle**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)et quelques propriétés supplémentaires telles que BubbleSizes, Values & XValues doivent être définies en conséquence. Lors de l'exécution du code suivant, un graphique à bulles est ajouté à la feuille de calcul.

#### **Ligne avec graphique de marqueur de données**

 Afin de créer une ligne avec le tableau des marqueurs de données,[**Type de graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)doit être réglé sur*ChartType.LineWithDataMarkersChartType.LineWithDataMarkersChartType.LineWithDataMarkers*et quelques propriétés supplémentaires telles que la zone d'arrière-plan, les marqueurs de série, les valeurs et les XValues doivent être définies en conséquence. Lors de l'exécution du code suivant, une ligne avec le graphique de marqueur de données est ajoutée à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-CreateLineWithDataMarkerChart-1.cs" >}}

## **Sujets avancés**
- [Lire et manipuler des graphiques Excel 2016](/cells/fr/net/read-and-manipulate-excel-2016-charts/)
- [Gérer les axes des graphiques Excel](/cells/fr/net/chart-axes/)
- [Réglage de l'apparence du graphique](/cells/fr/net/setting-chart-appearance/)
- [Types de graphiques](/cells/fr/net/chart-types/)
- [Personnalisation des graphiques](/cells/fr/net/customizing-charts/)
- [Définir la source de données pour le graphique](/cells/fr/net/data-formatting-in-charts/)
- [Gérer les DataLabels des graphiques Excel](/cells/fr/net/insert-datalabels-to-chart/)
- [Générer un graphique en traitant des marqueurs intelligents](/cells/fr/net/generate-chart-by-processing-smart-markers/)
- [Obtenir la feuille de calcul du graphique](/cells/fr/net/get-worksheet-of-the-chart/)
- [Gérer la légende des graphiques Excel](/cells/fr/net/chart-legend/)
- [Manipuler la taille de la position et le graphique du concepteur](/cells/fr/net/manipulate-position-size-and-designer-chart/)
- [Création d'un graphique à secteurs avec des lignes de repère](/cells/fr/net/creating-pie-chart-with-leader-lines/)
- [Formes dans les graphiques](/cells/fr/net/controls-in-charts/)
- [Gérer les titres des graphiques Excel](/cells/fr/net/chart-and-axis-titles/)
- [Rendu graphique](/cells/fr/net/chart-rendering/)
- [Obtenir le texte de l'équation de la ligne de tendance du graphique](/cells/fr/net/get-equation-text-of-chart-trendline/)
