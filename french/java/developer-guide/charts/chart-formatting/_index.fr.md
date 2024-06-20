---
title: Formatage du graphique
type: docs
weight: 20
url: /fr/java/chart-formatting/
---

## **Réglage de l’apparence du graphique**

Dans les [Types de graphique](/cells/fr/java/chart-types/), nous avons brièvement présenté les types de graphiques et d'objets de graphique offerts par Aspose.Cells.

Dans cet article, nous discutons de la personnalisation de l'apparence des graphiques en définissant un certain nombre de propriétés différentes :

- [Définir la zone du graphique](/cells/fr/java/chart-formatting/#setting-chart-area).
- [Définir les lignes du graphique](/cells/fr/java/chart-formatting/#setting-chart-lines).
- [Appliquer des thèmes](/cells/fr/java/chart-formatting/#applying-microsoft-excel-20072010-themes-to-charts).
- [Définir les titres des graphiques et des axes](/cells/fr/java/chart-formatting/#setting-the-titles-of-charts-or-axes).
- [Travailler avec les lignes de quadrillage](/cells/fr/java/chart-formatting/#setting-major-gridlines).
- [Définir les bordures des parois arrière et latérales](/cells/fr/java/chart-formatting/#setting-borders-for-back-and-side-walls).

### **Définition de la zone du graphique**

Il existe différents types de zones dans un graphique et Aspose.Cells offre la flexibilité de modifier l'apparence de chaque zone. Les développeurs peuvent appliquer différents paramètres de formatage sur une zone en modifiant sa couleur avant-plan, sa couleur d'arrière-plan et son format de remplissage, etc.

Dans l'exemple ci-dessous, nous avons appliqué différents paramètres de mise en forme sur différents types de zones d'un graphique. Ces zones comprennent :

- Zone de traçage
- Zone du graphique
- Zone [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)
- La zone d'un seul point dans un [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)

Après l'exécution du code d'exemple, un histogramme à colonnes sera ajouté à la feuille de calcul comme indiqué ci-dessous :

**Un histogramme à colonnes avec des zones remplies** 

![todo:image_alt_text](chart-formatting_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartArea-SettingChartArea.java" >}}

### **Définition des lignes du graphique**

Les développeurs peuvent également appliquer différents types de styles sur les lignes ou les repères de données du [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) comme indiqué ci-dessous dans l'exemple. L'exécution du code d'exemple ajoute un histogramme à colonnes à la feuille de calcul comme indiqué ci-dessous :

**Histogramme à colonnes après application des styles de ligne** 

![todo:image_alt_text](chart-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartLines-SettingChartLines.java" >}}

### **Application des thèmes Microsoft Excel 2007/2010 aux graphiques**

Les développeurs peuvent appliquer différents thèmes et couleurs Microsoft Excel au [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) ou à d'autres objets graphiques comme indiqué dans l'exemple ci-dessous.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ApplyingThemes-ApplyingThemes.java" >}}

### **Configuration des titres des graphiques ou des axes**

Vous pouvez utiliser Microsoft Excel pour définir les titres d'un graphique et de ses axes dans un environnement WYSIWYG comme indiqué ci-dessous.

**Définition des titres d'un graphique et de ses axes à l'aide de Microsoft Excel** 

![todo:image_alt_text](chart-formatting_3.png)

Aspose.Cells permet également aux développeurs de définir les titres d'un graphique et de ses axes à l'exécution. Tous les graphiques et leurs axes contiennent une méthode [**Title.setText**](https://reference.aspose.com/cells/java/com.aspose.cells/title#Text) qui peut être utilisée pour définir leurs titres comme indiqué dans l'exemple ci-dessous. Après l'exécution du code d'exemple, un histogramme à colonnes sera ajouté à la feuille de calcul comme indiqué ci-dessous :

**Histogramme à colonnes après la définition des titres** 

![todo:image_alt_text](chart-formatting_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingTitlesAxes-SettingTitlesAxes.java" >}}

### **Définition des principales lignes de la grille**

#### **Masquer les grandes lignes de la grille**

Les développeurs peuvent contrôler la visibilité des grandes lignes de la grille en utilisant la méthode [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/line#IsVisible) de l'objet [**Line**](https://reference.aspose.com/cells/java/com.aspose.cells/Line). Après avoir masqué les grandes lignes de la grille, un graphique à colonnes ajouté à la feuille de calcul présente l'apparence suivante :

**Un graphique à colonnes avec des grandes lignes de grille masquées** 

![todo:image_alt_text](chart-formatting_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-MajorGridlines-1.java" >}}

#### **Changer les paramètres des grandes lignes de la grille**

Les développeurs peuvent non seulement contrôler la visibilité des grandes lignes de la grille, mais aussi d'autres propriétés telles que sa couleur, etc. Après avoir défini la couleur des grandes lignes de la grille, un graphique à colonnes ajouté à la feuille de calcul aura l'apparence suivante :

**Graphique à colonnes avec des grandes lignes de grille colorées** 

![todo:image_alt_text](chart-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-ChangingMajorGridlines-1.java" >}}

### **Définition des bordures pour les parois arrière et latérales**

Depuis la sortie de Microsoft Excel 2007, les parois d'un graphique 3D ont été divisées en deux parties : paroi latérale et paroi arrière, donc nous devons utiliser deux objets [**Walls**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls) pour les représenter séparément et vous pouvez y accéder en utilisant [**Chart.getBackWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#BackWall) et [**Chart.getSideWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#SideWall).

L'exemple ci-dessous montre comment définir la bordure de la paroi latérale en utilisant différentes attributs.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-SettingBorders-1.java" >}}

## **Modifier la position et la taille du graphique**

Parfois, vous souhaitez modifier la position ou la taille du graphique nouvellement ajouté ou existant à l'intérieur de la feuille de calcul. Aspose.Cells fournit la propriété [**Chart.getChartObject()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#ChartObject) pour y parvenir. Vous pouvez utiliser ses sous-propriétés pour redimensionner le graphique avec une nouvelle **hauteur** et **largeur** ou le repositionner avec de nouvelles coordonnées **X** et **Y**.

### **Modifier la position et la taille du graphique**

Pour changer la position (coordonnées X, Y) et la taille (hauteur, largeur) du graphique, utilisez ces propriétés :

1. [**Chart.getChartObject().get/setWidth()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Width)
1. [**Chart.getChartObject().get/setHeight()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Height)
1. [**Chart.getChartObject().get/setX()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#X)
1. [**Chart.getChartObject().get/setY()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Y)

L'exemple suivant explique l'utilisation des propriétés ci-dessus. Il charge le classeur existant contenant un graphique dans sa première feuille de calcul. Ensuite, il redimensionne et repositionne le graphique et enregistre le classeur.

Avant l'exécution du code d'exemple, le fichier source ressemble à ceci :

**Taille et position du graphique avant l'exécution du code d'exemple** 

![todo:image_alt_text](chart-formatting_7.png)

Après l'exécution, le fichier de sortie ressemble à ceci:

**Taille et position du graphique après l'exécution du code d'exemple** 

![todo:image_alt_text](chart-formatting_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChangeChartPositionAndSize-ChangeChartPositionAndSize.java" >}}

## **Manipulation des graphiques de concepteur**

Il arrive que vous deviez manipuler ou modifier les graphiques dans vos fichiers de modèle de créateur. Aspose.Cells prend en charge entièrement la manipulation des graphiques du créateur avec leurs contenus et éléments. Les données, les contenus des graphiques, l'image de fond et le formatage peuvent être préservés avec précision.

### **Manipulation des graphiques du créateur dans les fichiers de modèle**

Pour manipuler les graphiques du créateur dans un fichier de modèle, utilisez tous les appels d'API liés aux graphiques. Par exemple, utilisez la propriété [**Worksheet.getCharts**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Charts) pour obtenir la collection de graphiques existante dans le fichier de modèle.

#### **Création d'un graphique**

L'exemple suivant montre comment créer un graphique circulaire. Nous manipulerons ce graphique par la suite. La sortie suivante est générée par le code.

**Le graphique circulaire d'entrée** 

![todo:image_alt_text](chart-formatting_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

#### **Manipulation du graphique**

L'exemple suivant montre comment manipuler le graphique existant. Dans cet exemple, nous modifions le graphique créé précédemment. La sortie suivante est générée par le code. Notez que la couleur du titre du graphique est passée du bleu au noir, et 'Angleterre 30000' a été modifié en 'Royaume-Uni, 30K'.

**Le graphique circulaire a été modifié** 

![todo:image_alt_text](chart-formatting_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyPieChart-ModifyPieChart.java" >}}

#### **Manipulation d'un graphique linéaire dans le modèle de concepteur**

Dans cet exemple, nous manipulerons un graphique linéaire. Nous ajouterons des séries de données au graphique existant et changerons leurs couleurs de ligne.

Tout d'abord, jetez un œil au graphique linéaire du créateur.

**Le graphique linéaire d'entrée** 

![todo:image_alt_text](chart-formatting_11.png)

Maintenant, nous manipulons le graphique linéaire (qui est contenu dans le fichier **linechart.xls**) en utilisant le code suivant. La sortie suivante est générée par le code.

**Le graphique linéaire manipulé** 

![todo:image_alt_text](chart-formatting_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyLineChart-ModifyLineChart.java" >}}

## **Utilisation des sparklines**

Microsoft Excel 2010 peut analyser les informations de plus de façons que jamais. Il permet aux utilisateurs de suivre et de mettre en évidence les tendances importantes des données avec de nouveaux outils d'analyse et de visualisation des données. Les sparklines sont des mini-graphiques que vous pouvez placer à l'intérieur des cellules afin de visualiser les données et le graphique sur la même table. Lorsque les sparklines sont utilisés correctement, l'analyse des données est plus rapide et plus directe. Ils offrent également une vue simple des informations, évitant les feuilles de calcul surchargées avec de nombreux graphiques complexes.

Aspose.Cells fournit une API pour manipuler les sparklines dans les feuilles de calcul.

### **Sparklines dans Microsoft Excel**

Pour insérer des sparklines dans Microsoft Excel 2010 :

1. Sélectionnez les cellules où vous souhaitez voir apparaître les sparklines. Pour les rendre faciles à visualiser, sélectionnez les cellules à côté des données.
1. Cliquez sur **Insérer** dans le ruban, puis choisissez **colonne** dans le groupe **Sparklines**.

![todo:image_alt_text](chart-formatting_13.png)

1. Sélectionnez ou saisissez la plage de cellules dans la feuille de calcul qui contient les données source.
   Les graphiques apparaissent.

Les sparklines vous aident à voir les tendances, par exemple, ou le bilan des victoires ou des défaites pour une ligue de softball. Les sparklines peuvent même résumer toute la saison de chaque équipe de la ligue.

![todo:image_alt_text](chart-formatting_14.png)

### **Sparklines en utilisant Aspose.Cells**

Les développeurs peuvent créer, supprimer ou lire les sparklines (dans le fichier modèle) en utilisant l'API fournie par Aspose.Cells. En ajoutant des graphiques personnalisés pour une plage de données donnée, les développeurs ont la liberté d'ajouter différents types de petits graphiques aux zones de cellules sélectionnées.

L'exemple ci-dessous illustre la fonctionnalité des Sparklines. L'exemple montre comment :

1. Ouvrir un fichier modèle simple.
1. Lire les informations des sparklines pour une feuille de calcul.
1. Ajouter de nouvelles sparklines pour une plage de données donnée à une zone de cellules.
1. Enregistrer le fichier Excel sur le disque.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-UsingSparklines-UsingSparklines.java" >}}

## **Application du format 3D au graphique**

Vous pourriez avoir besoin de styles de graphique 3D pour obtenir les résultats correspondant à votre scénario. Les API Aspose.Cells fournissent l'API pertinente pour appliquer la mise en forme 3D de Microsoft Excel 2007 comme démontré dans cet article.

### **Réglage du format 3D au graphique**

Un exemple complet est donné ci-dessous pour démontrer comment créer un graphique et lui appliquer la mise en forme 3D de Microsoft Excel 2007. Après l'exécution du code d'exemple ci-dessus, un graphique en colonnes (avec des effets 3D) sera ajouté à la feuille de calcul comme indiqué ci-dessous.

**Un graphique en colonnes avec mise en forme 3D**

![todo:image_alt_text](chart-formatting_15.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-Applying3DFormat-Applying3DFormat.java" >}}

{{% alert color="primary" %}}

Pour obtenir une liste complète des types de graphiques 2D et 3D pris en charge, voir [Types de graphiques pris en charge pour le rendu](/cells/fr/java/chart-rendering/#supported-chart-types-for-rendering).

{{% /alert %}}

## **Sujets avancés**
- [Définir une image comme remplissage d'arrière-plan dans le graphique](/cells/fr/java/set-picture-as-background-fill-in-the-chart/)
