---
title: Créer et gérer un graphique
description: Apprenez à utiliser Aspose.Cells for .NET pour créer des graphiques dans Microsoft Excel. Notre guide présentera les différents types de graphiques qui peuvent être créés, ainsi que la personnalisation de leur apparence et de leur format.
keywords: Aspose.Cells for .NET, Création de graphiques, Microsoft Excel, Types de graphiques, Personnalisation, Apparence, Formatage.
linktitle: Graphiques
type: docs
weight: 130
url: /fr/net/creating-charts/
description: Créer un graphique en CSharp pour des fichiers Excel et ODS.
keywords: créer un graphique, faire un graphique 
---

{{% alert color="primary" %}}

Il est possible d'ajouter divers graphiques aux feuilles de calcul avec Aspose.Cells. Aspose.Cells propose de nombreux objets de création de graphiques flexibles. Ce sujet traite des objets de création de graphiques d'Aspose.Cells.

{{% /alert %}}

## **Création de graphiques**

### **Création simple d'un graphique**
Il est simple de créer un graphique avec Aspose.Cells avec les codes d'exemple suivants:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateColumnChart-1.cs" >}}

### **Choses à savoir pour créer un graphique**

Avant de créer des graphiques, il est important de comprendre certains concepts de base qui sont utiles lors de la création de graphiques à l'aide d'Aspose.Cells.

#### **Objets de graphiques**

Aspose.Cells fournit un ensemble spécial de classes dans l'espace de noms [**Aspose.Cells.Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts) utilisées pour créer les graphiques pris en charge par Aspose.Cells. Ces classes sont utilisées pour créer des **objets de graphique**, qui agissent comme les éléments de construction du graphique. Les objets de graphique sont énumérés ci-dessous :

- Série, une seule série de données dans un graphique.
- Axe, un axe de graphique.
- Graphique, un seul graphique Excel.
- Zone de graphique, la zone de graphique dans la feuille de calcul.
- Table de données du graphique, une table de données de graphique.
- Cadre de graphique, l'objet de cadre dans un graphique.
- Point de graphique, un point unique dans une série dans un graphique.
- Collection de points de graphique, une collection qui contient tous les points dans une série.
- Graphiques, une collection d'objets de graphique.
- Étiquettes de données, une collection de tous les objets d'étiquette de données pour la série spécifiée.
- Format de remplissage, format de remplissage pour une forme.
- Sol, le sol d'un graphique 3D.
- Légende, la légende du graphique.
- Ligne, la ligne de graphique.
- Collection de séries, une collection d'objets de série.
- TickLabels, les étiquettes de repère associées aux repères sur un axe de graphique.
- Title, le titre d'un graphique ou d'un axe.
- Trendline, une tendance dans un graphique.
- TrendlineCollection, une collection de tous les objets Trendline pour la série de données spécifiée.
- Walls, les murs d'un graphique 3D.

#### **Utilisation des objets de graphique**

Comme mentionné ci-dessus, tous les objets de graphique sont des instances de leurs classes respectives et fournissent des propriétés et des méthodes spécifiques pour effectuer des tâches spécifiques. Utilisez les objets de graphique pour créer des graphiques.

Ajoutez n'importe quel type de graphique à une feuille de calcul en utilisant la collection de [**Charts**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts). Chaque élément dans la collection de [**Charts**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) représente un objet [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart). Un objet [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) encapsule tous les autres objets de graphique nécessaires pour personnaliser l'apparence du graphique. La prochaine section montre comment utiliser quelques objets de graphique de base pour créer un graphique simple.

### **Créer un graphique en utilisant Aspose.Cells**

**Étapes:**

1. Ajoutez des données à des cellules de feuille de calcul avec la méthode [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) de l'objet [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).
   Cela sera utilisé comme la source de données pour le graphique.
1. Ajoutez un graphique à la feuille de calcul en appelant la méthode [**Add**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection/methods/add) de la collection [**Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection), encapsulée dans l'objet [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).
1. Spécifiez le type de graphique avec l'énumération [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).
   Par exemple, l'exemple ci-dessous utilise la valeur [**ChartType.Pyramid**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) comme type de graphique.
1. Accédez au nouvel objet [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) de la collection [**Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection) en passant son index.
1. Utilisez l'un quelconque des objets de graphique encapsulés dans l'objet [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) pour gérer le graphique.
   L'exemple ci-dessous utilise l'objet de graphique [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) pour spécifier la source de données du graphique.

Lors de l'ajout de données source au graphique, la source de données peut être une plage de cellules (comme "A1:C3"), ou une séquence de cellules non contiguës (comme "A1, A3, A5"), ou une séquence de valeurs (comme "1,2,3").

Ces étapes générales vous permettent de créer n'importe quel type de graphique. Utilisez différents objets de graphique pour créer différents graphiques.

Il est possible de créer de nombreux types de graphiques avec Aspose.Cells. Tous les graphiques standard pris en charge par Aspose.Cells sont prédéfinis dans une énumération nommée [**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).

Les types de graphiques prédéfinis sont :

|**Types de graphiques**|**Description**|
| :- | :- |
|Column|Représente un graphique à colonnes groupées|
|ColumnStacked|Représente un graphique à colonnes empilées|
|Column100PercentStacked|Représente un graphique à colonnes empilées à 100 %|
|Column3DClustered|Représente un graphique à colonnes groupées en 3D|
|Column3DStacked|Représente un graphique à colonnes empilées en 3D|
|Column3D100PercentStacked|Représente un graphique à colonnes empilées à 100 % en 3D|
|Column3D|Représente un graphique à colonnes en 3D|
|Bar|Représente un graphique à barres groupées|
|BarStacked|Représente un graphique à barres empilées|
|Bar100PercentStacked|Représente un graphique à barres empilées à 100 %|
|Bar3DClustered|Représente un graphique à barres groupées en 3D|
|Bar3DStacked|Représente un graphique à barres empilées en 3D|
|Bar3D100PercentStacked|Représente un graphique à barres empilées à 100 % en 3D|
|Line|Représente un graphique linéaire|
|LineStacked|Représente un graphique linéaire empilé|
|Line100PercentStacked|Représente un graphique linéaire empilé à 100 %|
|LineWithDataMarkers|Représente un graphique linéaire avec des repères de données|
|LineStackedWithDataMarkers|Représente un graphique en courbes empilées avec des marqueurs de données|
|Line100PercentStackedWithDataMarkers|Représente un graphique en courbes empilées à 100 % avec des marqueurs de données|
|Line3D|Représente un graphique en courbes 3D|
|Pie|Représente un graphique circulaire|
|Pie3D|Représente un graphique circulaire 3D|
|PiePie|Représente un graphique secteur dans un graphique circulaire|
|PieExploded|Représente un graphique circulaire éclaté|
|Pie3DExploded|Représente un graphique circulaire 3D éclaté|
|PieBar|Représente un graphique en barres dans un graphique circulaire|
|Scatter|Représente un graphique de dispersion|
|ScatterConnectedByCurvesWithDataMarker|Représente un graphique de dispersion connecté par des courbes, avec des marqueurs de données|
|ScatterConnectedByCurvesWithoutDataMarker|Représente un graphique de dispersion connecté par des courbes, sans marqueurs de données|
|ScatterConnectedByLinesWithDataMarker|Représente un graphique de dispersion connecté par des lignes, avec des marqueurs de données|
|ScatterConnectedByLinesWithoutDataMarker|Représente un graphique de dispersion connecté par des lignes, sans marqueurs de données|
|Area|Représente un graphique en aires|
|AreaStacked|Représente un graphique en aires empilées|
|Area100PercentStacked|Représente un graphique en aires empilées à 100 %|
|Area3D|Représente un graphique en aires 3D|
|Area3DStacked|Représente un graphique en aires 3D empilées|
|Area3D100PercentStacked|Représente un graphique en aires 3D empilées à 100 %
|Doughnut|Représente le graphique en anneau |
|DoughnutExploded|Représente le graphique en anneau explosé |
|Radar|Représente le graphique radar |
|RadarWithDataMarkers|Représente le graphique radar avec des marqueurs de données |
|RadarFilled|Représente le graphique radar rempli |
|Surface3D|Représente le graphique de surface 3D |
|SurfaceWireframe3D|Représente le graphique de surface 3D à structure filaire |
|SurfaceContour|Représente le graphique de contour |
|SurfaceContourWireframe|Représente le graphique de contour à structure filaire |
|Bubble|Représente le graphique de bulles |
|Bubble3D|Représente le graphique de bulles 3D |
|Cylinder|Représente le graphique cylindrique |
|CylinderStacked|Représente le graphique cylindrique empilé |
|Cylinder100PercentStacked|Représente le graphique cylindrique 100% empilé |
|CylindericalBar|Représente le graphique de barres cylindriques |
|CylindericalBarStacked|Représente le graphique de barres cylindriques empilées |
|CylindericalBar100PercentStacked|Représente le graphique de barres cylindriques 100% empilées |
|CylindericalColumn3D|Représente le graphique de colonnes cylindriques 3D |
|Cone|Représente le graphique en cône |
|ConeStacked|Représente le graphique en cône empilé |
|Cone100PercentStacked|Représente un diagramme en cônes empilés à 100 %|
|ConicalBar|Représente un diagramme en barres coniques|
|ConicalBarStacked|Représente un diagramme en barres coniques empilées|
|ConicalBar100PercentStacked|Représente un diagramme en barres coniques empilées à 100 %|
|ConicalColumn3D|Représente un diagramme en colonnes coniques 3D|
|Pyramid|Représente un diagramme en pyramide|
|PyramidStacked|Représente un diagramme en pyramide empilée|
|Pyramid100PercentStacked|Représente un diagramme en pyramide empilée à 100 %|
|PyramidBar|Représente un diagramme en barres pyramidal|
|PyramidBarStacked|Représente un diagramme en barres pyramidal empilées|
|PyramidBar100PercentStacked|Représente un diagramme en barres pyramidal empilées à 100 %|
|PyramidColumn3D|Représente un diagramme en colonnes pyramidal 3D|
{{% alert color="primary" %}}

Lorsque vous attribuez une plage de cellules comme source de données, vous ne pouvez définir la plage que de haut en bas à gauche. Par exemple, "A1:C3" est valide tandis que "C3:A1" est invalide.

{{% /alert %}}

#### **Diagramme en pyramide**

Lorsque le code exemple est exécuté, un diagramme en pyramide est ajouté à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreatePyramidChart-1.cs" >}}

#### **Diagramme linéaire**

Dans l'exemple ci-dessus, il suffit de changer le [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) par *Line* pour créer un diagramme linéaire. Le code complet est fourni ci-dessous. Lorsque le code est exécuté, un diagramme linéaire est ajouté à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateLineChart-1.cs" >}}

#### **Diagramme en bulles**

Pour créer un diagramme en bulles, le [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) doit être défini sur [**ChartType.Bubble**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) et quelques propriétés supplémentaires telles que BubbleSizes, Values & XValues doivent être configurées en conséquence. Après l'exécution du code suivant, un diagramme en bulles est ajouté à la feuille de calcul.

#### **Diagramme linéaire avec marqueur de données**

Pour créer une ligne avec le graphique de marques de données, [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) doit être défini sur *ChartType.LineWithDataMarkers* et quelques propriétés supplémentaires telles que la zone de fond, les marqueurs de séries, les valeurs et les XValues doivent être définies en conséquence. En exécutant le code suivant, une ligne avec le graphique de marques de données est ajoutée à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-CreateLineWithDataMarkerChart-1.cs" >}}

## **Sujets avancés**
- [Lire et manipuler les graphiques Excel 2016](/cells/fr/net/read-and-manipulate-excel-2016-charts/)
- [Gérer les axes des graphiques Excel](/cells/fr/net/chart-axes/)
- [Réglage de l’apparence du graphique](/cells/fr/net/setting-chart-appearance/)
- [Types de graphiques](/cells/fr/net/chart-types/)
- [Personnalisation des graphiques](/cells/fr/net/customizing-charts/)
- [Définir la source de données pour le graphique](/cells/fr/net/data-formatting-in-charts/)
- [Gérer les étiquettes de données des graphiques Excel](/cells/fr/net/insert-datalabels-to-chart/)
- [Générer un graphique en traitant des marqueurs intelligents](/cells/fr/net/generate-chart-by-processing-smart-markers/)
- [Obtenir la feuille de calcul du graphique](/cells/fr/net/get-worksheet-of-the-chart/)
- [Gérer la légende des graphiques Excel](/cells/fr/net/chart-legend/)
- [Manipuler la position, la taille et le design du graphique](/cells/fr/net/manipulate-position-size-and-designer-chart/)
- [Créer un graphique circulaire avec des lignes de repère](/cells/fr/net/creating-pie-chart-with-leader-lines/)
- [Formes dans les graphiques](/cells/fr/net/controls-in-charts/)
- [Gérer les titres des graphiques Excel](/cells/fr/net/chart-and-axis-titles/)
- [Rendu du graphique](/cells/fr/net/chart-rendering/)
- [Obtenir le texte de l'équation de la tendance du graphique](/cells/fr/net/get-equation-text-of-chart-trendline/)
