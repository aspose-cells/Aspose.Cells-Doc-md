---
title: Personnalisation des graphiques
type: docs
weight: 15
url: /fr/java/creating-and-customizing-charts/
alias: [/java/customizing-charts/]
---

## **Création de graphiques**

Il est possible d'ajouter divers graphiques aux feuilles de calcul avec Aspose.Cells. Aspose.Cells propose de nombreux objets de création de graphiques flexibles. Ce sujet traite des objets de création de graphiques d'Aspose.Cells.

### **Création simple d'un graphique**

Il est simple de créer un graphique avec Aspose.Cells avec les codes d'exemple suivants :

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


### **Choses à savoir pour créer un graphique**

Avant de créer des graphiques, il est important de comprendre certains concepts de base qui sont utiles lors de la création de graphiques à l'aide d'Aspose.Cells.

#### **Objets de graphiques**

Aspose.Cells fournit un ensemble spécial de classes utilisées pour créer tous types de graphiques. Ces classes sont utilisées pour créer des **objets de création de graphiques**, qui agissent comme les blocs de construction du graphique. Les objets de création de graphiques sont énumérés ci-dessous :

- [**Axis**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis), un axe de graphique.
- [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart), un seul graphique Excel.
- [**ChartArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea), la zone de graphique dans la feuille de calcul.
- [**ChartDataTable**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable), un tableau de données de graphique.
- [**ChartFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame), l'objet de trame dans un graphique.
- [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), un seul point dans une série dans un graphique.
- [**ChartPointCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection), une collection qui contient tous les points dans une série.
- [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection), une collection de [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) objets.
- DataLabels, DataLabels pour le [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) spécifié, [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), [**Trendline**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), etc.
- [**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat), format de remplissage pour une forme.
- [**Floor**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor), le sol d'un graphique 3D.
- [**Legend**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend), la légende du graphique.
- [**Line**](https://reference.aspose.com/cells/java/com.aspose.cells/Line), la ligne du graphique.
- [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection), une collection de [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) objets.
- [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), représente une seule série de données dans un graphique.
- [**TickLabels**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels), les étiquettes de repère associées aux repères sur un axe de graphique.
- [**Title**](https://reference.aspose.com/cells/java/com.aspose.cells/Title), le titre d'un graphique ou d'un axe.
- [**Trendline**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), une courbe de tendance dans un graphique.
- [**TrendlineCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection), une collection de tous les objets de courbe de tendance pour la série de données spécifiée.
- [**Walls**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls), les murs d'un graphique 3D.

#### **Utilisation des objets de graphique**

Comme mentionné ci-dessus, tous les objets de graphique sont des instances de leurs classes respectives et fournissent des propriétés et des méthodes spécifiques pour effectuer des tâches spécifiques. Utilisez les objets de graphique pour créer des graphiques.

Ajoutez n'importe quel type de graphique à une feuille de calcul en utilisant la collection [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection). Chaque élément de la collection [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) représente un objet [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart). Un objet [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) encapsule tous les objets de graphique nécessaires pour personnaliser l'apparence du graphique. La section suivante montre comment utiliser quelques objets de graphique de base pour créer un graphique simple.

### **Création d'un graphique simple**

Il est possible de créer de nombreux types différents de graphiques avec Aspose.Cells. Tous les graphiques standards pris en charge par Aspose.Cells sont prédéfinis dans une énumération nommée [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType). Les types de graphiques prédéfinis sont :

|**Types de graphiques**|**Description**|
| :- | :- |
|Column|Représente le graphique en colonnes groupées|
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
|Scatter|Représente le graphique de dispersion|
|ScatterConnectedByCurvesWithDataMarker|Représente le graphique de dispersion connecté par des courbes, avec des marqueurs de données|
|ScatterConnectedByCurvesWithoutDataMarker|Représente le graphique de dispersion connecté par des courbes, sans marqueurs de données|
|ScatterConnectedByLinesWithDataMarker|Représente le graphique de dispersion connecté par des lignes, avec des marqueurs de données|
|ScatterConnectedByLinesWithoutDataMarker|Représente le graphique de dispersion connecté par des lignes, sans marqueurs de données|
|Area|Représente un graphique en aires|
|AreaStacked|Représente un graphique en aires empilées|
|Area100PercentStacked|Représente un graphique en aires empilées à 100 %|
|Area3D|Représente un graphique en aires 3D|
|Area3DStacked|Représente un graphique en aires 3D empilées|
|Area3D100PercentStacked|Représente un graphique en aires 3D empilées à 100 %
|Doughnut|Représente le graphique en anneau |
|DoughnutExploded|Représente le graphique en anneau explosé |
|Radar|Représente le graphique en radar|
|RadarWithDataMarkers|Représente le graphique en radar avec des marqueurs de données|
|RadarFilled|Représente le graphique radar rempli |
|Surface3D|Représente le graphique de surface 3D |
|SurfaceWireframe3D|Représente le graphique en surface 3D avec maillage|
|SurfaceContour|Représente le graphique de contour |
|SurfaceContourWireframe|Représente le graphique de contour à structure filaire |
|Bubble|Représente le graphique de bulles |
|Bubble3D|Représente le graphique de bulles 3D |
|Cylinder|Représente le graphique cylindrique |
|CylinderStacked|Représente le graphique cylindrique empilé |
|Cylinder100PercentStacked|Représente le graphique cylindrique 100% empilé |
|CylindricalBar|Représente le graphique en barres cylindriques|
|CylindricalBarStacked|Représente le graphique en barres cylindriques empilées|
|CylindricalBar100PercentStacked|Représente le graphique en barres cylindriques empilées à 100%|
|CylindricalColumn3D|Représente le graphique en colonnes cylindriques 3D|
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
|PyramidBar|Représente un diagramme à barres en pyramide|
|PyramidBarStacked|Représente un diagramme en barres pyramidal empilées|
|PyramidBar100PercentStacked|Représente un diagramme en barres pyramidal empilées à 100 %|
|PyramidColumn3D|Représente un diagramme en colonnes pyramidal 3D|
Pour créer un graphique à l'aide d'Aspose.Cells:

1. Ajoutez des données à des cellules de feuille de calcul avec la méthode [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) de l'objet [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell).
   Cela sera utilisé comme la source de données pour le graphique.
1. Ajoutez un graphique à la feuille de calcul en appelant la collection [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) [*add*](https://reference.aspose.com/cells/java/com.aspose.cells/chartcollection#add-int-int-int-int-int-) méthode, encapsulée dans l'objet [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet).
1. Spécifiez le type de graphique avec l'énumération [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType).
   Par exemple, l'exemple utilise la valeur [**ChartType.PYRAMID**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID) comme type de graphique.
1. Accédez au nouvel objet [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) de la collection [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) en passant son index.
1. Utilisez l'un quelconque des objets de graphique encapsulés dans l'objet [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) pour gérer le graphique.
   L'exemple ci-dessous utilise l'objet de graphique [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) pour spécifier la source de données du graphique.

Lors de l'ajout de données source au graphique, la source de données peut être une plage de cellules (comme "A1:C3"), ou une séquence de cellules non contiguës (comme "A1, A3, A5"), ou une séquence de valeurs (comme "1,2,3").

{{% alert color="primary" %}}

Lorsque vous attribuez une plage de cellules en tant que source de données, vous ne pouvez définir la plage que du coin supérieur gauche au coin inférieur droit. Par exemple, "A1:C3" est valide tandis que "C3:A1" est invalide.

{{% /alert %}}

Ces étapes générales vous permettent de créer n'importe quel type de graphique. Utilisez différents objets de graphique pour créer différents graphiques.

Lorsque le code d'exemple est exécuté, un graphique en pyramide est ajouté à la feuille de calcul comme le montre l'exemple ci-dessous.

**Graphique en pyramide avec sa source de données**

![todo:image_alt_text](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

Pour créer un graphique à bulles, le [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType) doit être défini sur [**ChartType.BUBBLE**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE) et quelques propriétés supplémentaires telles que BubbleSizes, Values et XValues doivent être définies en conséquence. Après l'exécution du code suivant, un graphique à bulles est ajouté à la feuille de calcul comme indiqué ci-dessous.

**Graphique à bulles avec sa source de données**

![todo:image_alt_text](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

#### **Diagramme linéaire avec marqueur de données**

Pour créer un graphique de ligne avec des marqueurs de données, le [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType) doit être défini sur [**ChartType.LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE-WITH-DATA-MARKERS) et quelques propriétés supplémentaires telles qu'une zone de fond, des marqueurs de série, des valeurs et des XValues doivent être définies en conséquence. Après l'exécution du code suivant, un graphique de ligne avec des marqueurs de données est ajouté à la feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

## **Création de graphiques personnalisés**

Jusqu'à présent, lorsque nous avons discuté des graphiques, nous avons examiné des graphiques standard avec leurs paramètres de formatage standard. Nous définissons simplement la source de données, définissons quelques propriétés et le graphique est créé avec ses paramètres de format par défaut. Mais Aspose.Cells prend également en charge la création de graphiques personnalisés qui permet aux développeurs de créer des graphiques avec leurs propres paramètres de formatage.

### **Création de graphiques personnalisés**

Les développeurs peuvent créer des graphiques personnalisés à l'exécution en utilisant l'API simple d'Aspose.Cells.

Un graphique est composé d'une série de données. Chaque série de données dans Aspose.Cells est représentée par un objet [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) tandis que l'objet [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) sert de collection d'objets [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series). Lors de la création d'un graphique personnalisé, les développeurs ont la liberté d'utiliser différents types de graphiques pour différentes séries de données (collectées dans un objet [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)).

{{% alert color="primary" %}}

Actuellement, Aspose.Cells prend en charge uniquement les graphiques personnalisés combinant des graphiques circulaires, des graphiques de ligne, des graphiques de colonnes et des graphiques empilés de colonnes, mais d'autres graphiques seront pris en charge dans les prochaines versions. Pour une liste complète des graphiques standard pris en charge par Aspose.Cells, consultez l'article [Types de graphiques](/cells/fr/java/chart-types/).

{{% /alert %}}

Le code d'exemple ci-dessous montre comment créer des graphiques personnalisés. Dans cet exemple, nous allons utiliser un graphique en colonnes pour la première série de données et un graphique linéaire pour la deuxième série. Le résultat est que nous ajoutons un graphique en colonnes, combiné à un graphique linéaire, à la feuille de calcul.

**Graphique personnalisé combinant des graphiques en colonnes et en lignes**

![todo:image_alt_text](creating-and-customizing-charts_3.png)

**Exemple de programmation**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

Pour voir une liste des types de graphiques pris en charge, lisez l'article [Types de graphiques](/cells/fr/java/chart-types/).

{{% /alert %}}

{{< app/cells/assistant language="java" >}}
