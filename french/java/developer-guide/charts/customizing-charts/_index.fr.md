---
title: Personnalisation des graphiques
type: docs
weight: 15
url: /fr/java/creating-and-customizing-charts/
alias: [/java/customizing-charts/]
---
##  **Création de graphiques**

Il est possible d'ajouter une variété de graphiques aux feuilles de calcul avec Aspose.Cells. Aspose.Cells fournit de nombreux objets graphiques flexibles. Cette rubrique traite des objets graphiques Aspose.Cells.

###  **Créer simplement un graphique**

Il est simple de créer un graphique avec Aspose.Cells avec les exemples de codes suivants :

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


###  **Choses à savoir pour créer un graphique**

Avant de créer des graphiques, il est important de comprendre certains concepts de base utiles lors de la création de graphiques à l'aide de Aspose.Cells.

####  **Graphiquer des objets**

Aspose.Cells fournit un ensemble spécial de classes utilisées pour créer toutes sortes de graphiques. Ces classes sont utilisées pour créer des *objets graphiques**, qui servent de blocs de construction du graphique. Les objets graphiques sont répertoriés ci-dessous :

- [**Axe**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis), l'axe d'un graphique.
- [**Graphique**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart), un seul graphique Excel.
- [**ZoneGraphique**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea), la zone graphique de la feuille de calcul.
- [**GraphiqueDonnéesTable**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable), un tableau de données graphiques.
- [**Cadre graphique**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame), l'objet frame dans un graphique.
- [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), un seul point dans une série dans un graphique.
- [**ChartPointCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection), une collection qui contient tous les points d'une série.
- [**Collection de graphiques**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) une collection de[**Graphique**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)objets.
-  DataLabels, DataLabels pour le spécifié[**Série**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), [**Ligne de tendance**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), etc.
- [**RemplirFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat), remplissez le format d'une forme.
- [**Sol**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor), le sol d'un graphique 3D.
- [**Légende**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend), la légende du graphique.
- [**Doubler**](https://reference.aspose.com/cells/java/com.aspose.cells/Line), la ligne du graphique.
- [**SérieCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) une collection de[**Série**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)objets.
- [**Série**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), représente une seule série de données dans un graphique.
- [**Étiquettes de tiques**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels), les étiquettes de graduation associées aux graduations sur un axe du graphique.
- [**Titre**](https://reference.aspose.com/cells/java/com.aspose.cells/Title), le titre d'un graphique ou d'un axe.
- [**Ligne de tendance**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), une ligne de tendance dans un graphique.
- [**Collection de lignes de tendance**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection), une collection de tous les objets Trendline pour la série de données spécifiée.
- [**Des murs**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls), les murs d'un graphique 3D.

####  **Utiliser des objets graphiques**

Comme mentionné ci-dessus, tous les objets graphiques sont des instances de leurs classes respectives et fournissent des propriétés et des méthodes spécifiques pour effectuer des tâches spécifiques. Utilisez des objets graphiques pour créer des graphiques.

 Ajoutez n'importe quel type de graphique à une feuille de calcul à l'aide de l'outil[**Collection de graphiques**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) collection. Chaque élément du[**Collection de graphiques**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) la collection représente un[**Graphique**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) objet. UN[**Graphique**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)L'objet encapsule tous les objets graphiques requis pour personnaliser l'apparence du graphique. La section suivante montre comment utiliser quelques objets graphiques de base pour créer un graphique simple.

###  **Créer un graphique simple**

Il est possible de créer de nombreux types de graphiques différents avec Aspose.Cells. Tous les graphiques standards pris en charge par Aspose.Cells sont prédéfinis dans une énumération nommée[**Type de graphique**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType). Les types de graphiques prédéfinis sont :

|**Types de graphiques**|**Description**|
| :- | :- |
|Colonne|Représente le graphique à colonnes groupées|
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
|Dispersion|Représente le graphique à nuages de points|
|DispersionConnectéeByCurvesWithDataMarker|Représente le graphique à nuages de points relié par des courbes, avec des marqueurs de données|
|DispersionConnectedByCurvesWithoutDataMarker|Représente le graphique à nuages de points connecté par des courbes, sans marqueurs de données|
|DispersionConnectedByLinesWithDataMarker|Représente le graphique à nuages de points relié par des lignes, avec des marqueurs de données|
|DispersionConnectedByLinesWithoutDataMarker|Représente le graphique à nuages de points relié par des lignes, sans marqueurs de données|
|Zone|Représente un graphique en aires|
|ZoneStacked|Représente un graphique à aires empilées|
|Zone100PourcentageStacked|Représente un graphique à zones empilées à 100 %|
|Zone3D|Représente un graphique en aires 3D|
|Area3DSacked|Représente un graphique à zones empilées 3D|
|Surface3D100PourcentageStacked|Représente un graphique 3D à zones empilées à 100 %|
|Donut|Représente le graphique en beignet|
|BeignetExplosé|Représente un graphique en anneau éclaté|
|Radar|Représente la carte radar|
|RadarAvecDataMarkers|Représente le graphique radar avec des marqueurs de données|
|RadarRempli|Représente un graphique radar rempli|
|Surface3D|Représente un graphique de surface 3D|
|SurfaceFilaire3D|Représente le graphique de surface 3D filaire|
|Contour de surface|Représente le graphique de contour|
|SurfaceContourFilaire|Représente un graphique de contour filaire|
|Bulle|Représente un graphique à bulles|
|Bulle3D|Représente un graphique à bulles 3D|
|Cylindre|Représente le diagramme de cylindre|
|CylindreStacked|Représente un graphique de cylindres empilés|
|Cylindre100PourcentEmpilé|Représente un tableau de cylindres empilés à 100 %|
|Barre Cylindrique|Représente un graphique à barres cylindriques.|
|CylindriqueBarEmpilé|Représente un graphique à barres cylindriques empilées|
|CylindriqueBar100PourcentEmpilé|Représente un graphique à barres cylindriques empilées à 100 %|
|CylindriqueColonne3D|Représente un graphique à colonnes cylindriques 3D|
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
|PyramideBar|Représente le graphique à barres pyramidales|
|PyramideBarEmpilé|Représente un graphique à barres pyramidales empilées|
|PyramideBar100PourcentEmpilé|Représente un graphique à barres pyramidales empilées à 100 %|
|PyramideColonne3D|Représente un diagramme à colonnes pyramidal 3D|
Pour créer un graphique en utilisant Aspose.Cells :

1. Ajoutez des données aux cellules de la feuille de calcul avec le[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) objets[**définirValeur**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)méthode.
 Ceci sera utilisé comme source de données pour le graphique.
1.  Ajoutez un graphique à la feuille de calcul en appelant le[**Collection de graphiques**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) la collection[*ajouter*](https://reference.aspose.com/cells/java/com.aspose.cells/chartcollection#add(int,%20int,%20int,%20int,%20int) ), encapsulée dans le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)objet.
1.  Spécifiez le type de graphique avec le[**Type de graphique**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)énumération.
 Par exemple, l'exemple utilise le[**ChartType.PYRAMID**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID)valeur comme type de graphique.
1.  Accédez au nouveau[**Graphique**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) objet du[**Collection de graphiques**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)collection en passant son index.
1.  Utilisez n'importe lequel des objets graphiques encapsulés dans le[**Graphique**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)objet pour gérer le graphique.
 L'exemple ci-dessous utilise le[**SérieCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)objet graphique pour spécifier la source de données du graphique.

Lors de l'ajout de données source au graphique, la source de données peut être une plage de cellules (telle que "A1:C3"), ou une séquence de cellules non contiguës (telle que "A1, A3, A5"), ou une séquence de valeurs (telles que "1,2,3").

{{% alert color="primary" %}}

Lorsque vous attribuez une plage de cellules comme source de données, vous ne pouvez définir la plage que du coin supérieur gauche au coin inférieur droit. Par exemple, « A1:C3 » est valide tandis que « C3:A1 » n'est pas valide.

{{% /alert %}}

Ces étapes générales vous permettent de créer tout type de graphique. Utilisez différents objets graphiques pour créer différents graphiques.

Lorsque l'exemple de code est exécuté, un graphique pyramidal est ajouté à la feuille de calcul comme indiqué ci-dessous.

**Graphique pyramidal avec sa source de données**

![tâche : image_alt_text](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

 Pour créer un graphique à bulles, le[**Type de graphique**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)doit être réglé sur[**ChartType.BUBBLE**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE)et quelques propriétés supplémentaires telles que BubbleSizes, Values et XValues doivent être définies en conséquence. Lors de l'exécution du code suivant, un graphique à bulles est ajouté à la feuille de calcul comme indiqué ci-dessous.

**Graphique à bulles avec sa source de données**

![tâche : image_alt_text](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

####  **Ligne avec graphique de marqueurs de données**

Pour créer une ligne avec un graphique de marqueurs de données, le[**Type de graphique**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)doit être réglé sur[**ChartType.LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE_WITH_DATA_MARKERS) et quelques propriétés supplémentaires telles que la zone d'arrière-plan, les marqueurs de série, les valeurs et les valeurs XV doivent être définies en conséquence. Lors de l'exécution du code suivant, une ligne avec un graphique de marqueurs de données est ajoutée à la feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

##  **Création de graphiques personnalisés**

Jusqu'à présent, lorsque nous avons discuté des graphiques, nous avons examiné les graphiques standard dotés de leurs paramètres de formatage standard. Nous définissons uniquement la source de données, définissons quelques propriétés et le graphique est créé avec ses paramètres de format par défaut. Mais Aspose.Cells prend également en charge la création de graphiques personnalisés qui permettent aux développeurs de créer des graphiques avec leurs propres paramètres de format.

###  **Création de graphiques personnalisés**

Les développeurs peuvent créer des graphiques personnalisés au moment de l'exécution en utilisant le simple Aspose.Cells API.

 Un graphique est composé d'une série de données. Chaque série de données dans Aspose.Cells est représentée par un[**Série**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)objet alors que le[**SérieCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) l'objet sert de collection de[**Série**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)objets. Lors de la création d'un graphique personnalisé, les développeurs ont la liberté d'utiliser différents types de graphiques pour différentes séries de données (collectées dans un[**SérieCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)objet).

{{% alert color="primary" %}}

 Actuellement, la version Aspose.Cells ne prend en charge que les graphiques personnalisés combinant des graphiques à secteurs, en courbes, en colonnes et en colonnes, mais davantage de graphiques seront pris en charge dans les versions futures. Pour une liste complète des cartes standard prises en charge par Aspose.Cells, lisez le[Types de graphiques](/cells/fr/java/chart-types/) article.

{{% /alert %}}

L'exemple de code ci-dessous montre comment créer des graphiques personnalisés. Dans cet exemple, nous allons utiliser un histogramme pour la première série de données et un graphique linéaire pour la deuxième série. Le résultat est que nous ajoutons un histogramme, combiné à un graphique linéaire, à la feuille de calcul.

**Graphique personnalisé combinant des graphiques à colonnes et à courbes**

![tâche : image_alt_text](creating-and-customizing-charts_3.png)

**Exemple de programmation**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

Pour voir une liste des types de graphiques pris en charge, lisez le[Types de graphiques](/cells/fr/java/chart-types/) article.

{{% /alert %}}

