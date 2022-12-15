---
title: Formatage du graphique
type: docs
weight: 20
url: /fr/java/chart-formatting/
---
## **Réglage de l'apparence du graphique**

 Dans[Types de graphiques](/cells/fr/java/chart-types/), nous avons donné une brève introduction aux types de graphiques et d'objets graphiques proposés par Aspose.Cells.

Dans cet article, nous expliquons comment personnaliser l'apparence des graphiques en définissant un certain nombre de propriétés différentes :

- [Définition de la zone du graphique](/cells/fr/java/chart-formatting/#setting-chart-area).
- [Définition des lignes du graphique](/cells/fr/java/chart-formatting/#setting-chart-lines).
- [Appliquer des thèmes](/cells/fr/java/chart-formatting/#applying-microsoft-excel-20072010-themes-to-charts).
- [Définition des titres des graphiques et des axes](/cells/fr/java/chart-formatting/#setting-the-titles-of-charts-or-axes).
- [Travailler avec des quadrillages](/cells/fr/java/chart-formatting/#setting-major-gridlines).
- [Définition des bordures pour les murs arrière et latéraux](/cells/fr/java/chart-formatting/#setting-borders-for-back-and-side-walls).

### **Réglage de la zone graphique**

Il existe différents types de zones dans un graphique et Aspose.Cells offre la possibilité de modifier l'apparence de chaque zone. Les développeurs peuvent appliquer différents paramètres de mise en forme sur une zone en modifiant sa couleur de premier plan, sa couleur d'arrière-plan et son format de remplissage, etc.

Dans l'exemple ci-dessous, nous avons appliqué différents paramètres de mise en forme sur différents types de zones d'un graphique. Ces domaines comprennent :

- Superficie du terrain
- Zone graphique
- [**SérieCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) Région
- L'aire d'un seul point dans un[**SérieCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)

Après avoir exécuté l'exemple de code, un histogramme sera ajouté à la feuille de calcul comme indiqué ci-dessous :

**Un histogramme avec des zones remplies** 

![tâche : image_autre_texte](chart-formatting_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartArea-SettingChartArea.java" >}}

### **Définition des lignes de graphique**

 Les développeurs peuvent également appliquer différents types de styles sur les lignes ou les marqueurs de données du[**SérieCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)comme indiqué ci-dessous dans l'exemple. L'exécution de l'exemple de code ajoute un histogramme à la feuille de calcul, comme indiqué ci-dessous :

**Diagramme à colonnes après application des styles de ligne** 

![tâche : image_autre_texte](chart-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartLines-SettingChartLines.java" >}}

### **Application des thèmes Microsoft Excel 2007/2010 aux graphiques**

 Les développeurs peuvent appliquer différents thèmes et couleurs Excel Microsoft au[**SérieCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)ou d'autres objets de graphique comme indiqué dans l'exemple ci-dessous.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ApplyingThemes-ApplyingThemes.java" >}}

### **Définition des titres des graphiques ou des axes**

Vous pouvez utiliser Microsoft Excel pour définir les titres d'un graphique et ses axes dans un environnement WYSIWYG comme indiqué ci-dessous.

**Définition des titres d'un graphique et de ses axes à l'aide d'Excel Microsoft** 

![tâche : image_autre_texte](chart-formatting_3.png)

Aspose.Cells permet également aux développeurs de définir les titres d'un graphique et ses axes lors de l'exécution. Tous les graphiques et leurs axes contiennent un[**Titre.setText**](https://reference.aspose.com/cells/java/com.aspose.cells/title#Text)méthode qui peut être utilisée pour définir leurs titres comme indiqué ci-dessous dans un exemple. Après avoir exécuté l'exemple de code, un histogramme sera ajouté à la feuille de calcul comme indiqué ci-dessous :

**Diagramme à colonnes après avoir défini les titres** 

![tâche : image_autre_texte](chart-formatting_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingTitlesAxes-SettingTitlesAxes.java" >}}

### **Définition du quadrillage principal**

#### **Masquer le quadrillage principal**

 Les développeurs peuvent contrôler la visibilité des principaux quadrillages en utilisant le[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/line#IsVisible) méthode de la[**Ligne**](https://reference.aspose.com/cells/java/com.aspose.cells/Line)objet. Après avoir masqué le quadrillage principal, un histogramme ajouté à la feuille de calcul a l'apparence suivante :

**Un histogramme avec un quadrillage principal caché** 

![tâche : image_autre_texte](chart-formatting_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-MajorGridlines-1.java" >}}

#### **Modification des paramètres du quadrillage principal**

Les développeurs peuvent non seulement contrôler la visibilité des principaux quadrillages, mais également d'autres propriétés, notamment sa couleur, etc. Après avoir défini la couleur des principaux quadrillages, un histogramme ajouté à la feuille de calcul aura l'apparence suivante :

**Diagramme à colonnes avec quadrillage principal coloré** 

![tâche : image_autre_texte](chart-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-ChangingMajorGridlines-1.java" >}}

### **Définition des bordures pour les murs arrière et latéraux**

 Depuis la sortie de Microsoft Excel 2007, les parois d'un graphique 3D ont été divisées en deux parties : paroi latérale et paroi arrière, nous devons donc utiliser deux[**Des murs**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls) objets pour les représenter séparément et vous pouvez y accéder en utilisant[**Graphique.getBackWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#BackWall) et[**Graphique.getSideWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#SideWall).

L'exemple ci-dessous montre comment définir la bordure du flanc en utilisant différents attributs.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-SettingBorders-1.java" >}}

## **Modifier la position et la taille du graphique**

 Parfois, vous souhaitez modifier la position ou la taille du graphique nouveau ou existant dans la feuille de calcul. Aspose.Cells fournit le[**Graphique.getChartObject()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#ChartObject) propriété pour y parvenir. Vous pouvez utiliser ses sous-propriétés pour redimensionner le graphique avec de nouvelles**la taille** et**largeur** ou repositionnez-le avec de nouveaux** X** et**Coordonnées Y**.

### **Modification de la position et de la taille du graphique**

Pour modifier la position (coordonnées X, Y) et la taille (hauteur, largeur) du graphique, utilisez ces propriétés :

1. [**Graphique.getChartObject().get/setWidth()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Width)
1. [**Graphique.getChartObject().get/setHeight()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Height)
1. [**Graphique.getChartObject().get/setX()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#X)
1. [**Graphique.getChartObject().get/setY()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Y)

L'exemple suivant explique l'utilisation des propriétés ci-dessus. Il charge le classeur existant qui contient un graphique dans sa première feuille de calcul. Ensuite, il redimensionne et repositionne le graphique et enregistre le classeur.

Avant l'exécution de l'exemple de code, le fichier source ressemble à ceci :

**Taille et position du graphique avant l'exécution de l'exemple de code** 

![tâche : image_autre_texte](chart-formatting_7.png)

Après l'exécution, le fichier de sortie ressemble à ceci :

**Taille et position du graphique après l'exécution de l'exemple de code** 

![tâche : image_autre_texte](chart-formatting_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChangeChartPositionAndSize-ChangeChartPositionAndSize.java" >}}

## **Manipulation des graphiques de concepteur**

Il peut arriver que vous ayez besoin de manipuler ou de modifier les graphiques dans vos fichiers de modèle de concepteur. Aspose.Cells prend entièrement en charge la manipulation des graphiques de concepteur avec son contenu et ses éléments. Les données, le contenu du graphique, l'image d'arrière-plan et la mise en forme peuvent être conservés avec précision.

### **Manipulation des graphiques Designer dans les fichiers de modèle**

 Pour manipuler des graphiques de concepteur dans un fichier de modèle, utilisez tous les appels API liés au graphique. Par exemple, utilisez[**Feuille de calcul.getCharts**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Charts) propriété pour obtenir la collection de graphiques existante dans le fichier de modèle.

#### **Création d'un graphique**

L'exemple suivant montre comment créer un graphique à secteurs. Nous manipulerons ce graphique plus tard. La sortie suivante est générée par le code.

**Le camembert d'entrée** 

![tâche : image_autre_texte](chart-formatting_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

#### **Manipulation du graphique**

L'exemple suivant montre comment manipuler le graphique existant. Dans cet exemple, nous modifions le graphique créé ci-dessus. La sortie suivante est générée par le code. Notez que la couleur du titre du graphique est passée du bleu au noir et que "Angleterre 30000" a été remplacée par "Royaume-Uni, 30K".

**Le camembert a été modifié** 

![tâche : image_autre_texte](chart-formatting_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyPieChart-ModifyPieChart.java" >}}

#### **Manipulation d'un graphique en courbes dans le modèle Designer**

Dans cet exemple, nous allons manipuler un graphique linéaire. Nous ajouterons des séries de données au graphique existant et modifierons les couleurs de leurs lignes.

Tout d'abord, jetez un œil au graphique linéaire du concepteur.

**Le graphique en courbes d'entrée** 

![tâche : image_autre_texte](chart-formatting_11.png)

 Maintenant, nous manipulons le graphique en courbes (qui est contenu dans le**graphique en courbes.xls** fichier) en utilisant le code suivant. La sortie suivante est générée par le code.

**Le graphique linéaire manipulé** 

![tâche : image_autre_texte](chart-formatting_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyLineChart-ModifyLineChart.java" >}}

## **Utiliser des graphiques sparkline**

Microsoft Excel 2010 peut analyser les informations de plus de façons que jamais auparavant. Il permet aux utilisateurs de suivre et de mettre en évidence les tendances importantes des données grâce à de nouveaux outils d'analyse et de visualisation des données. Les graphiques sparkline sont des mini-graphiques que vous pouvez placer à l'intérieur des cellules afin de pouvoir afficher les données et le graphique sur le même tableau. Lorsque les graphiques sparkline sont utilisés correctement, l'analyse des données est plus rapide et plus précise. Ils fournissent également une vue simple des informations, évitant les feuilles de calcul surchargées avec beaucoup de graphiques occupés.

Aspose.Cells fournit un API pour manipuler les sparklines dans les feuilles de calcul.

### **Sparklines dans Microsoft Excel**

Pour insérer des sparklines dans Microsoft Excel 2010 :

1. Sélectionnez les cellules où vous souhaitez que les sparklines apparaissent. Pour faciliter leur visualisation, sélectionnez des cellules à côté des données.
1.  Cliquez sur**Insérer** sur le ruban, puis choisissez**colonne** dans le**Sparklines** groupe.

![tâche : image_autre_texte](chart-formatting_13.png)

1. Sélectionnez ou entrez la plage de cellules de la feuille de calcul contenant les données source.
 Les graphiques apparaissent.

Les Sparklines vous aident à voir les tendances, par exemple, ou le record de victoires ou de défaites pour une ligue de softball. Sparklines peut même résumer toute la saison de chaque équipe de la ligue.

![tâche : image_autre_texte](chart-formatting_14.png)

### **Sparklines utilisant Aspose.Cells**

Les développeurs peuvent créer, supprimer ou lire des sparklines (dans le fichier de modèle) à l'aide du API fourni par Aspose.Cells. En ajoutant des graphiques personnalisés pour une plage de données donnée, les développeurs ont la liberté d'ajouter différents types de petits graphiques aux zones de cellule sélectionnées.

L'exemple ci-dessous illustre la fonctionnalité Sparklines. L'exemple montre comment :

1. Ouvrez un fichier modèle simple.
1. Lire les informations sparklines pour une feuille de calcul.
1. Ajoutez de nouveaux graphiques sparkline pour une plage de données donnée à une zone de cellule.
1. Enregistre le fichier Excel sur le disque.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-UsingSparklines-UsingSparklines.java" >}}

## **Application du format 3D au graphique**

Vous aurez peut-être besoin de styles de graphique 3D pour obtenir uniquement les résultats de votre scénario. Les API Aspose.Cells fournissent le API pertinent pour appliquer le formatage Microsoft Excel 2007 3D comme illustré dans cet article.

### **Définition du format 3D sur le graphique**

Un exemple complet est donné ci-dessous pour montrer comment créer un graphique et appliquer le formatage Microsoft Excel 2007 3D. Après avoir exécuté l'exemple de code ci-dessus, un histogramme (avec effets 3D) sera ajouté à la feuille de calcul, comme indiqué ci-dessous.

**Un histogramme au format 3D**

![tâche : image_autre_texte](chart-formatting_15.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-Applying3DFormat-Applying3DFormat.java" >}}

{{% alert color="primary" %}}

 Pour une liste complète des graphiques 2D et 3D pris en charge, voir[Types de graphiques pris en charge pour le rendu](/cells/fr/java/chart-rendering/#supported-chart-types-for-rendering).

{{% /alert %}}

## **Sujets avancés**
- [Définir l'image comme arrière-plan Remplir le graphique](/cells/fr/java/set-picture-as-background-fill-in-the-chart/)
