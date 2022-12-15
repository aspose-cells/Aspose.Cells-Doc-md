---
title: Formatage des données
type: docs
weight: 80
url: /fr/java/data-formatting/
---
## **Approches pour formater les données dans Cells**
C'est un fait commun que si les cellules de la feuille de calcul sont correctement formatées, il devient plus facile pour les utilisateurs de lire le contenu (données) de la cellule. Il existe de nombreuses façons de formater les cellules et leur contenu. Le moyen le plus simple consiste à formater les cellules à l'aide d'Excel Microsoft dans un environnement WYSIWYG lors de la création d'une feuille de calcul Designer. Une fois la feuille de calcul du concepteur créée, vous pouvez ouvrir la feuille de calcul à l'aide de Aspose.Cells en conservant tous les paramètres de format enregistrés avec la feuille de calcul. Une autre façon de formater les cellules et leur contenu consiste à utiliser Aspose.Cells API. Dans cette rubrique, nous décrirons deux approches pour formater les cellules et leur contenu avec l'utilisation de Aspose.Cells API.
### **Formatage Cells**
 Les développeurs peuvent formater les cellules et leur contenu à l'aide du flexible API de Aspose.Cells. Aspose.Cells fournit une classe,[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , qui représente un fichier Excel Microsoft. La[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe contient un[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer. La[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe fournit une collection Cells. Chaque élément de la[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells)collection représente un objet de**Cell** classer.

 Aspose.Cells fournit le[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) propriété dans le[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) classe, utilisée pour définir le style de formatage d'une cellule. De plus, Aspose.Cells fournit également un[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) classe qui est utilisée pour servir le même but. Appliquez différents types de styles de mise en forme sur les cellules pour définir leurs couleurs d'arrière-plan ou de premier plan, les bordures, les polices, les alignements horizontaux et verticaux, le niveau d'indentation, la direction du texte, l'angle de rotation et bien plus encore.
#### **Utilisation de la méthode setStyle**
 Lorsque vous appliquez différents styles de mise en forme à différentes cellules, il est préférable d'utiliser la méthode setStyle du[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) classer. Un exemple est donné ci-dessous pour démontrer l'utilisation de la méthode setStyle pour appliquer divers paramètres de mise en forme sur une cellule.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formatting-FormattingCellsUsingsetStyleMethod-1.java" >}}




#### **Utilisation de l'objet Style**
 Lorsque vous appliquez le même style de mise en forme à différentes cellules, utilisez la[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) objet.

1.  Ajouter un[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) objet à la collection Styles du[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe en appelant la méthode createStyle de la classe Workbook.
1. Accédez à l'objet Style nouvellement ajouté à partir de la collection Styles.
1. Définissez les propriétés souhaitées de l'objet Style pour appliquer les paramètres de mise en forme souhaités.
1. Attribuez l'objet Style configuré à la propriété Style de n'importe quelle cellule souhaitée.

Cette approche peut grandement améliorer l'efficacité de vos applications et également économiser de la mémoire.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingCellsUsingStyleObject-FormattingCellsUsingStyleObject.java" >}}




#### **Application d'effets de remplissage dégradé**
Pour appliquer les effets de remplissage dégradé souhaités à la cellule, utilisez la méthode setTwoColorGradient de l'objet Style en conséquence.
#### **Exemple de code**
 La sortie suivante est obtenue en exécutant le code ci-dessous.

**Application d'effets de remplissage dégradé** 

![tâche : image_autre_texte](data-formatting_1.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ApplyGradientFillEffects-ApplyGradientFillEffects.java" >}}




## **Configuration des paramètres d'alignement**
Quiconque a utilisé Microsoft Excel pour formater des cellules connaîtra les paramètres d'alignement dans Microsoft Excel.

**Paramètres d'alignement dans Microsoft Excel** 

![tâche : image_autre_texte](data-formatting_2.png)

Comme vous pouvez le voir sur la figure ci-dessus, il existe différents types d'options d'alignement :

- [Alignement du texte](/cells/fr/java/data-formatting/) (horizontal Vertical)
- [Échancrure](/cells/fr/java/data-formatting/).
- [Orientation](/cells/fr/java/data-formatting/).
- [Contrôle du texte](/cells/fr/java/data-formatting/).
- [Sens du texte](/cells/fr/java/data-formatting/).

Tous ces paramètres d'alignement sont entièrement pris en charge par Aspose.Cells et sont discutés plus en détail ci-dessous.
### **Configuration des paramètres d'alignement**
 Aspose.Cells fournit une classe,[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , qui représente un fichier Excel. La classe Workbook contient une WorksheetCollection qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer.

 La classe Worksheet fournit une collection Cells. Chaque pièce de la collection Cells représente un objet de la[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) classer.

Aspose.Cells fournit la méthode setStyle dans le[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) classe utilisée pour la mise en forme d'une cellule. La[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) La classe fournit des propriétés utiles pour configurer les paramètres de police.

Sélectionnez n'importe quel type d'alignement de texte à l'aide de l'énumération TextAlignmentType. Les types d'alignement de texte prédéfinis dans l'énumération TextAlignmentType sont :

|**Types d'alignement de texte**|**La description**|
|:- |:- |
|Fond|Représente l'alignement du texte inférieur|
|Centre|Représente l'alignement du texte au centre|
|CenterAcross|Représente le centre sur l'alignement du texte|
|Distribué|Représente l'alignement de texte distribué|
|Remplir|Représente l'alignement du texte de remplissage|
|Général|Représente l'alignement général du texte|
|Justifier|Représente l'alignement du texte justifié|
|La gauche|Représente l'alignement du texte à gauche|
|Droit|Représente l'alignement du texte à droite|
|Haut|Représente l'alignement supérieur du texte|
{{% alert color="primary" %}} 

Vous pouvez également appliquer le paramètre Justify Distributed à l'aide de la méthode Style.setJustifyDistributed().

{{% /alert %}} 
#### **Alignement horizontal**
 Utilisez le[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) méthode setHorizontalAlignment de l'objet pour aligner le texte horizontalement.

La sortie suivante est obtenue en exécutant l'exemple de code ci-dessous :

**Aligner le texte horizontalement** 

![tâche : image_autre_texte](data-formatting_3.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentHorizontal-TextAlignmentHorizontal.java" >}}




#### **Alignement vertical**
 Utilisez le[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) la méthode setVerticalAlignment de l'objet pour aligner le texte verticalement.

La sortie suivante est obtenue lorsque VerticalAlignment est défini sur center.

**Aligner le texte verticalement** 

![tâche : image_autre_texte](data-formatting_4.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentVertical-TextAlignmentVertical.java" >}}




### **Échancrure**
 Il est possible de définir le niveau d'indentation du texte dans une cellule en utilisant la[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) la méthode setIndentLevel de l'objet.

La sortie suivante est obtenue lorsque IndentLevel est défini sur 2.

**Niveau d'indentation ajusté à 2** 

![tâche : image_autre_texte](data-formatting_5.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Indentation-ImportingfromResultSet.java" >}}




### **Orientation**
 Définissez l'orientation (rotation) du texte dans une cellule avec la[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) méthode setRotationAngle de l'objet.

La sortie suivante est obtenue lorsque l'angle de rotation est réglé sur 25.

**Angle de rotation réglé sur 25** 

![tâche : image_autre_texte](data-formatting_6.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Orientation-Orientation.java" >}}




### **Contrôle du texte**
La section suivante explique comment contrôler le texte en définissant l'habillage du texte, le rétrécissement et d'autres options de formatage.
#### **Habillage du texte**
L'habillage du texte dans une cellule facilite la lecture : la hauteur de la cellule s'ajuste pour s'adapter à tout le texte, au lieu de le couper ou de déborder dans les cellules adjacentes.

 Activez ou désactivez l'habillage du texte avec le[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) la méthode setTextWrapped de l'objet.

La sortie suivante est obtenue lorsque l'habillage du texte est activé.

**Texte enveloppé à l'intérieur de la cellule** 

![tâche : image_autre_texte](data-formatting_7.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WrapText-WrapText.java" >}}




#### **Rétrécir pour s'adapter**
 Une option d'habillage du texte dans un champ consiste à réduire la taille du texte pour l'adapter aux dimensions d'une cellule. Cela se fait en réglant le[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) la propriété IsTextWrapped de l'objet à**vrai**.

La sortie suivante est obtenue lorsque le texte est rétréci pour tenir dans la cellule.

**Texte rétréci pour tenir à l'intérieur des limites de la cellule** 

![tâche : image_autre_texte](data-formatting_8.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ShrinkingToFit-ShrinkingToFit.java" >}}




#### **Fusion Cells**
Comme Microsoft Excel, Aspose.Cells prend en charge la fusion de plusieurs cellules en une seule.

La sortie suivante est obtenue si les trois cellules de la première ligne sont fusionnées pour créer une grande cellule unique.

**Trois cellules fusionnées pour créer une grande cellule** 

![tâche : image_autre_texte](data-formatting_9.png)

 Utilisez le[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells) la méthode Merge de la collection pour fusionner les cellules. La méthode Merge prend les paramètres suivants :

- Première ligne, la première ligne à partir de laquelle commencer la fusion.
- Première colonne, la première colonne à partir de laquelle commencer la fusion.
- Nombre de lignes, le nombre de lignes à fusionner.
- Nombre de colonnes, le nombre de colonnes à fusionner.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}




### **Sens du texte**
Il est possible de définir l'ordre de lecture du texte dans les cellules. L'ordre de lecture est l'ordre visuel dans lequel les caractères, les mots, etc. sont affichés. Par exemple, l'anglais est une langue de gauche à droite tandis que l'arabe est une langue de droite à gauche.

 L'ordre de lecture est défini avec le[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) propriété TextDirection de l'objet. Aspose.Cells fournit des types de direction de texte prédéfinis dans l'énumération TextDirectionType.

|**Types d'orientation du texte**|**La description**|
|:- |:- |
|Le contexte|L'ordre de lecture cohérent avec la langue du premier caractère saisi|
|De gauche à droite|Ordre de lecture de gauche à droite|
|De droite à gauche|Ordre de lecture de droite à gauche|






{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ChangeTextDirection-ChangeTextDirection.java" >}}





La sortie suivante est obtenue si l'ordre de lecture du texte est défini de droite à gauche.

**Réglage de l'ordre de lecture du texte de droite à gauche** 

![tâche : image_autre_texte](data-formatting_10.png)
## **Formatage des caractères sélectionnés dans un Cell**
[Gestion des paramètres de police](/cells/fr/java/dealing-with-font-settings/)expliqué comment formater les cellules, mais seulement comment formater le contenu de toutes les cellules. Que faire si vous souhaitez formater uniquement les caractères sélectionnés ?

Aspose.Cells prend en charge cette fonctionnalité. Cette rubrique explique comment utiliser cette fonctionnalité.
### **Formatage des caractères sélectionnés**
 Aspose.Cells fournit une classe,[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , qui représente un fichier Excel Microsoft. La classe Workbook contient une collection Worksheets qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer. La classe Worksheet fournit une collection Cells. Chaque pièce de la collection Cells représente un objet de la[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) classer.

La classe Cell fournit une méthode de caractères qui prend les paramètres suivants pour sélectionner une plage de caractères dans une cellule :

- **Index de départ**, l'index du caractère à partir duquel commencer la sélection.
- **Nombre de caractères**, le nombre de caractères à sélectionner.

Dans le fichier de sortie, dans la cellule A1", le mot 'Visite' est formaté avec la police par défaut mais 'Aspose!' est gras et bleu.

**Formatage des caractères sélectionnés** 

![tâche : image_autre_texte](data-formatting_11.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}







{{% alert color="primary" %}} 

 Si tu es interessé par[mise en forme d'une partie de texte enrichi dans une [cellule]](/cells/fr/java/access-and-update-the-portions-of-rich-text-of-cell/) , pensez à utiliser les méthodes Cell.getCharacters & Cell.setCharacters. La méthode Cell.getCharacters doit être utilisée pour accéder aux parties du texte, puis les modifications peuvent être effectuées à l'aide de la méthode Cell.setCharacters alors que la**obtenir** La méthode renvoie un tableau d'objets FontSetting qui peuvent être manipulés pour définir diverses propriétés nom de police, couleur de police, gras, etc. et**Positionner** peut être utilisée pour appliquer les modifications.

{{% /alert %}} 
## **Activer des feuilles et activer un Cell ou sélectionner une plage de Cells dans la feuille de calcul**
Parfois, vous devrez peut-être activer une feuille de calcul spécifique pour qu'elle soit la première à s'afficher lorsque quelqu'un ouvre le fichier dans Microsoft Excel. Vous devrez peut-être également activer une cellule spécifique de manière à ce que les barres de défilement défilent jusqu'à la cellule active afin qu'elle soit clairement visible. Aspose.Cells est capable de faire toutes les tâches mentionnées ci-dessus.

Une feuille active est la feuille sur laquelle vous travaillez dans un classeur. Le nom sur l'onglet de la feuille active est en gras par défaut. Une cellule active, quant à elle, est la cellule qui est sélectionnée et dans laquelle les données sont saisies lorsque vous commencez à taper. Une seule cellule est active à la fois. La cellule active est entourée d'une bordure épaisse pour la faire apparaître par rapport aux autres cellules. Aspose.Cells vous permet également de sélectionner une plage de cellules dans la feuille de calcul.
### **Activer une feuille et rendre un Cell actif**
Aspose.Cells fournit un API spécifique pour ces tâches. Par exemple, la méthode WorksheetCollection.setActiveSheetIndex est utile pour définir une feuille active. De même, la méthode Worksheet.setActiveCell est utilisée pour définir et obtenir une cellule active dans une feuille de calcul.

Si vous souhaitez que les barres de défilement horizontales et verticales défilent jusqu'à la position d'index de ligne et de colonne pour donner une bonne vue des données sélectionnées lorsque le fichier est ouvert dans Microsoft Excel, utilisez les propriétés Worksheet.setFirstVisibleRow et Worksheet.setFirstVisibleColumn.

L'exemple suivant montre comment activer une feuille de calcul et rendre active une cellule de celle-ci. Les barres de défilement défilent pour faire de la 2e ligne et de la 2e colonne leur première ligne et colonne visibles.

**Définir la cellule B2 comme cellule active** 

![tâche : image_autre_texte](data-formatting_12.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MakeCellActive-MakeCellActive.java" >}}




#### **Sélection d'une plage de Cells dans la feuille de calcul**
Aspose.Cells fournit la méthode Worksheet.selectRange(int startRow, int startColumn, int totalRows, int totalColumns, bool removeOthers). En utilisant le dernier paramètre - removeOthers - sur true, les autres sélections de cellules ou de plages de cellules de la feuille sont supprimées.

L'exemple suivant montre comment sélectionner une plage de cellules dans la feuille de calcul active.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SelectRangeofCellsinWorksheet-SelectRangeofCellsinWorksheet.java" >}}







{{% alert color="primary" %}} 

Toutes les classes et méthodes ci-dessus sont disponibles avec la version sous licence de Aspose.Cells.

{{% /alert %}} 
## **Formatage des lignes et des colonnes**
Le formatage des lignes et des colonnes dans une feuille de calcul pour donner un aspect au rapport est probablement la fonctionnalité la plus largement utilisée de l'application Excel. Les API Aspose.Cells fournissent également cette fonctionnalité via son modèle de données en exposant la classe Style qui gère principalement toutes les fonctionnalités liées au style telles que la police et ses attributs, l'alignement du texte, les couleurs d'arrière-plan/de premier plan, les bordures, le format d'affichage des nombres et des littéraux de date, etc. . Une autre classe utile fournie par les API Aspose.Cells est le StyleFlag qui permet la réutilisation de l'objet Style.

Dans cet article, nous allons essayer d'expliquer comment utiliser Aspose.Cells for Java API pour appliquer la mise en forme aux lignes et aux colonnes.
### **Formatage des lignes et des colonnes**
 Aspose.Cells fournit une classe,[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) qui représente un fichier Excel Microsoft. La[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contient une WorksheetCollection qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe Worksheet. La[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fournit la collection Cells. La collection Cells fournit une collection Rows.
#### **Formater une ligne**
Chaque élément de la collection Rows représente un objet Row. L'objet Row propose la méthode applyStyle utilisée pour appliquer une mise en forme à une ligne.

Pour appliquer le même formatage à une ligne, utilisez l'objet Style :

1. Ajoutez un objet Style à la classe Workbook en appelant sa méthode createStyle.
1. Définissez les propriétés de l'objet Style pour appliquer les paramètres de mise en forme.
1. Affectez l'objet Style configuré à la méthode applyStyle d'un objet Row.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingARow-FormattingARow.java" >}}




#### **Formater une colonne**
La collection Cells fournit une collection Columns. Chaque élément de la collection Columns représente un objet Column. Semblable à l'objet Row, l'objet Column propose la méthode applyStyle utilisée pour définir la mise en forme de la colonne. Utilisez la méthode applyStyle de l'objet Column pour mettre en forme une colonne de la même manière qu'une ligne.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingAColumn-FormattingAColumn.java" >}}




#### **Définition du format d'affichage des nombres et des dates pour les lignes et les colonnes**
Si l'exigence est de définir le format d'affichage des nombres et des dates pour une ligne ou une colonne complète, le processus est plus ou moins le même que celui décrit ci-dessus, cependant, au lieu de définir des paramètres pour le contenu textuel, vous définirez le formatage des nombres et les dates en utilisant Style.Number ou Style.Custom. Veuillez noter que la propriété Style.Number est de type entier et fait référence aux formats de nombre et de date intégrés, tandis que la propriété Style.Custom est de type chaîne et accepte les modèles valides.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingDisplayFormat-SettingDisplayFormat.java" >}}







{{% alert color="primary" %}} 

 Veuillez consulter l'article détaillé sur[Réglage des formats d'affichage des nombres et des [dates]](/cells/fr/java/data-formatting/).

{{% /alert %}}
