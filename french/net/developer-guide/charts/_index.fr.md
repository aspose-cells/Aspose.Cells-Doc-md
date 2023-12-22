---
title: Créer et gérer un graphique
description: Découvrez comment utiliser Aspose.Cells for .NET pour créer des graphiques dans Microsoft Excel. Notre guide présentera les différents types de graphiques pouvant être créés, ainsi que la manière de personnaliser leur apparence et leur formatage.
keywords: Aspose.Cells for .NET, Chart Creation, Microsoft Excel, Chart Types, Customization, Appearance, Formatting.
linktitle: Graphiques
type: docs
weight: 130
url: /fr/net/creating-charts/
description: Créez un graphique dans CSharp pour les fichiers Excel et ODS.
keywords: create a chart, make a graph 
---
{{% alert color="primary" %}}

Il est possible d'ajouter une variété de graphiques aux feuilles de calcul avec Aspose.Cells. Aspose.Cells fournit de nombreux objets graphiques flexibles. Cette rubrique traite des objets graphiques Aspose.Cells.

{{% /alert %}}

##  **Création de graphiques**

###  **Créer simplement un graphique**
Il est simple de créer un graphique avec Aspose.Cells avec les exemples de codes suivants :
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateColumnChart-1.cs" >}}

###  **Choses à savoir pour créer un graphique**

Avant de créer des graphiques, il est important de comprendre certains concepts de base utiles lors de la création de graphiques à l'aide de Aspose.Cells.

####  **Graphiquer des objets**

 Aspose.Cells propose un ensemble spécial de cours dans le[**Aspose.Cells.Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts)espace de noms utilisé pour créer les graphiques pris en charge par Aspose.Cells. Ces classes sont utilisées pour créer des *objets graphiques**, qui agissent comme des blocs de construction de graphiques. Les objets graphiques sont répertoriés ci-dessous :

- Série, une seule série de données dans un graphique.
- Axis, l'axe d'un graphique.
- Graphique, un seul graphique Excel.
- ChartArea, la zone graphique dans la feuille de calcul.
- ChartDataTable, un tableau de données graphiques.
- ChartFrame, l'objet frame dans un graphique.
- ChartPoint, un seul point dans une série dans un graphique.
- ChartPointCollection, une collection qui contient tous les points d'une série.
- Graphiques, une collection d’objets Chart.
- DataLabels, une collection de tous les objets DataLabel pour la série spécifiée.
- FillFormat, format de remplissage d'une forme.
- Étage, l'étage d'un graphique 3D.
- Légende, la légende du graphique.
- Line, la ligne du graphique.
- SeriesCollection, une collection d’objets Series.
- TickLabels, les étiquettes de graduation associées aux graduations sur un axe du graphique.
- Titre, le titre d'un graphique ou d'un axe.
- Trendline, une ligne de tendance dans un graphique.
- TrendlineCollection, une collection de tous les objets Trendline pour la série de données spécifiée.
- Murs, les murs d'une carte 3D.

####  **Utiliser des objets graphiques**

Comme mentionné ci-dessus, tous les objets graphiques sont des instances de leurs classes respectives et fournissent des propriétés et des méthodes spécifiques pour effectuer des tâches spécifiques. Utilisez des objets graphiques pour créer des graphiques.

 Ajoutez n'importe quel type de graphique à une feuille de calcul à l'aide de l'outil[**Graphiques**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) collection. Chaque élément du[**Graphiques**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) la collection représente un[**Graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) objet. UN[**Graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)L'objet encapsule tous les autres objets graphiques requis pour personnaliser l'apparence du graphique. La section suivante montre comment utiliser quelques objets graphiques de base pour créer un graphique simple.

###  **Créer un graphique à l'aide du Aspose.Cells**

**Pas:**

1. Ajoutez des données aux cellules de la feuille de calcul avec le[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) objets[**Valeur de put**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)méthode.
 Ceci sera utilisé comme source de données pour le graphique.
1.  Ajoutez un graphique à la feuille de calcul en appelant le[**Graphiques**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection) la collection[**Ajouter**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection/methods/add) méthode, encapsulée dans le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)objet.
1.  Spécifiez le type de graphique avec le[**Type de graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)énumération.
 Par exemple, l'exemple ci-dessous utilise le[**ChartType.Pyramide**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)valeur comme type de graphique.
1.  Accédez au nouveau[**Graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) objet du[**Graphiques**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)collection en passant son index.
1.  Utilisez n'importe lequel des objets graphiques encapsulés dans le[**Graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)objet pour gérer le graphique.
 L'exemple ci-dessous utilise le[**SérieCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)objet graphique pour spécifier la source de données du graphique.

Lors de l'ajout de données source au graphique, la source de données peut être une plage de cellules (telle que "A1:C3"), ou une séquence de cellules non contiguës (telle que "A1, A3, A5"), ou une séquence de valeurs (telles que "1,2,3").

Ces étapes générales vous permettent de créer tout type de graphique. Utilisez différents objets graphiques pour créer différents graphiques.

Il est possible de créer de nombreux types de graphiques différents avec Aspose.Cells. Tous les graphiques standards pris en charge par Aspose.Cells sont prédéfinis dans une énumération nommée[**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).

Les types de graphiques prédéfinis sont :

|**Types de graphiques**|**Description**|
| :- | :- |
|Colonne|Représente un histogramme groupé|
|ColonneStacked|Représente un graphique à colonnes empilées|
|Colonne100PercentStacked|Représente un graphique à colonnes empilées à 100 %|
|Colonne3DCclustérisée|Représente un histogramme groupé 3D|
|Colonne3DStacked|Représente un graphique à colonnes empilées en 3D|
|Colonne3D100PourcentageStacked|Représente un graphique à colonnes 3D empilé à 100 %|
|Colonne3D|Représente un histogramme 3D|
|Bar|Représente un graphique à barres groupées|
|BarStacked|Représente un graphique à barres empilées|
|Bar100PourcentEmpilé|Représente un graphique à barres empilées à 100 %|
|Bar3DCluster|Représente un graphique à barres groupées 3D|
|Bar3DSempilé|Représente un graphique à barres empilées 3D|
|Bar3D100PourcentageEmpilé|Représente un graphique à barres empilées 3D à 100 %|
|Doubler|Représente un graphique linéaire|
|LigneStacked|Représente un graphique en courbes empilées|
|Ligne100PercentStacked|Représente un graphique en courbes empilées à 100 %|
|LigneAvecDataMarkers|Représente un graphique linéaire avec des marqueurs de données|
|LineStackedWithDataMarkers|Représente un graphique en courbes empilées avec des marqueurs de données|
|Ligne100PercentStackedWithDataMarkers|Représente un graphique linéaire empilé à 100 % avec des marqueurs de données|
|Ligne3D|Représente un graphique linéaire 3D|
|Tarte|Représente un diagramme circulaire|
|Tarte3D|Représente un diagramme circulaire 3D|
|TarteTarte|Représente un diagramme circulaire|
|TarteExplodé|Représente un diagramme circulaire éclaté|
|Tarte3DExplodé|Représente un diagramme circulaire éclaté en 3D|
|TarteBar|Représente la barre du graphique à secteurs|
|Dispersion|Représente un graphique à nuages de points|
|DispersionConnectéeByCurvesWithDataMarker|Représente un graphique à nuages de points relié par des courbes, avec des marqueurs de données|
|DispersionConnectedByCurvesWithoutDataMarker|Représente un graphique à nuages de points connecté par des courbes, sans marqueurs de données|
|DispersionConnectedByLinesWithDataMarker|Représente un graphique à nuages de points relié par des lignes, avec des marqueurs de données|
|DispersionConnectedByLinesWithoutDataMarker|Représente un graphique à nuages de points relié par des lignes, sans marqueurs de données|
|Zone|Représente un graphique en aires|
|ZoneStacked|Représente un graphique à aires empilées|
|Zone100PourcentageStacked|Représente un graphique à zones empilées à 100 %|
|Zone3D|Représente un graphique en aires 3D|
|Area3DSacked|Représente un graphique à zones empilées 3D|
|Surface3D100PourcentageStacked|Représente un graphique 3D à zones empilées à 100 %|
|Donut|Représente le graphique en beignet|
|BeignetExplosé|Représente un graphique en anneau éclaté|
|Radar|Représente la carte radar|
|RadarAvecDataMarkers|Représente un graphique radar avec des marqueurs de données|
|RadarRempli|Représente un graphique radar rempli|
|Surface3D|Représente un graphique de surface 3D|
|SurfaceFilaire3D|Représente un graphique de surface 3D filaire|
|Contour de surface|Représente le graphique de contour|
|SurfaceContourFilaire|Représente un graphique de contour filaire|
|Bulle|Représente un graphique à bulles|
|Bulle3D|Représente un graphique à bulles 3D|
|Cylindre|Représente le diagramme de cylindre|
|CylindreStacked|Représente un graphique de cylindres empilés|
|Cylindre100PourcentEmpilé|Représente un tableau de cylindres empilés à 100 %|
|Barre Cylindrique|Représente un graphique à barres cylindriques.|
|CylindriqueBarEmpilé|Représente un graphique à barres cylindriques empilées|
|CylindreBarre100PourcentEmpilé|Représente un graphique à barres cylindriques empilées à 100 %|
|CylindreColonne3D|Représente un graphique à colonnes cylindriques 3D|
|Cône|Représente un graphique conique|
|CôneEmpilé|Représente un graphique à cônes empilés|
|Cône100PourcentEmpilé|Représente un graphique à cônes empilés à 100 %|
|Barre conique|Représente un graphique à barres coniques|
|ConiqueBarEmpilé|Représente un graphique à barres coniques empilées|
|ConiqueBar100PourcentEmpilé|Représente un graphique à barres coniques empilées à 100 %|
|ConiqueColonne3D|Représente un graphique à colonnes coniques 3D|
|Pyramide|Représente un graphique pyramidal|
|PyramideEmpilé|Représente un graphique pyramidal empilé|
|Pyramide100PourcentEmpilé|Représente un graphique pyramidal empilé à 100 %|
|PyramideBar|Représente un graphique à barres pyramidales|
|PyramideBarEmpilé|Représente un graphique à barres pyramidales empilées|
|PyramideBar100PourcentEmpilé|Représente un graphique à barres pyramidales empilées à 100 %|
|PyramideColonne3D|Représente un diagramme à colonnes pyramidal 3D|
{{% alert color="primary" %}}

Lorsque vous attribuez une plage de cellules comme source de données, vous ne pouvez définir la plage que du coin supérieur gauche au coin inférieur droit. Par exemple, « A1:C3 » est valide tandis que « C3:A1 » n'est pas valide.

{{% /alert %}}

####  **Graphique pyramidal**

Lorsque l'exemple de code est exécuté, un graphique pyramidal est ajouté à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreatePyramidChart-1.cs" >}}

####  **Graphique en ligne**

 Dans l'exemple ci-dessus, il suffit de changer le[**Type de graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) à*Doubler*crée un graphique linéaire. La source complète est fournie ci-dessous. lorsque le code est exécuté, un graphique linéaire est ajouté à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateLineChart-1.cs" >}}

####  **Graphique à bulles**

 Afin de créer un graphique à bulles, le[**Type de graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) doit être réglé sur[**ChartType.Bulle**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)et quelques propriétés supplémentaires telles que BubbleSizes, Values et XValues doivent être définies en conséquence. Lors de l'exécution du code suivant, un graphique à bulles est ajouté à la feuille de calcul.

####  **Ligne avec graphique de marqueurs de données**

 Afin de créer une ligne avec le graphique des marqueurs de données,[**Type de graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)doit être réglé sur*ChartType.LineWithDataMarkers*et quelques propriétés supplémentaires telles que la zone d'arrière-plan, les marqueurs de série, les valeurs et les valeurs XV doivent être définies en conséquence. Lors de l'exécution du code suivant, une ligne avec le graphique des marqueurs de données est ajoutée à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-CreateLineWithDataMarkerChart-1.cs" >}}

##  **Sujets avancés**
- [Lire et manipuler des graphiques Excel 2016](/cells/fr/net/read-and-manipulate-excel-2016-charts/)
- [Gérer les axes des graphiques Excel](/cells/fr/net/chart-axes/)
- [Définition de l'apparence du graphique](/cells/fr/net/setting-chart-appearance/)
- [Types de graphiques](/cells/fr/net/chart-types/)
- [Personnalisation des graphiques](/cells/fr/net/customizing-charts/)
- [Définir la source de données pour le graphique](/cells/fr/net/data-formatting-in-charts/)
- [Gérer les DataLabels des graphiques Excel](/cells/fr/net/insert-datalabels-to-chart/)
- [Générer un graphique en traitant des marqueurs intelligents](/cells/fr/net/generate-chart-by-processing-smart-markers/)
- [Obtenir la feuille de calcul du graphique](/cells/fr/net/get-worksheet-of-the-chart/)
- [Gérer la légende des graphiques Excel](/cells/fr/net/chart-legend/)
- [Manipuler la taille de la position et le graphique du concepteur](/cells/fr/net/manipulate-position-size-and-designer-chart/)
- [Création d'un diagramme circulaire avec des lignes de repère](/cells/fr/net/creating-pie-chart-with-leader-lines/)
- [Formes dans les graphiques](/cells/fr/net/controls-in-charts/)
- [Gérer les titres des graphiques Excel](/cells/fr/net/chart-and-axis-titles/)
- [Rendu graphique](/cells/fr/net/chart-rendering/)
- [Obtenir le texte de l'équation de la ligne de tendance du graphique](/cells/fr/net/get-equation-text-of-chart-trendline/)
