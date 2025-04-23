---
title: Mise en forme des données
type: docs
weight: 80
url: /fr/java/data-formatting/
---

## **Approches pour formater les données dans les cellules**
Il est communément admis que si les cellules de la feuille de calcul sont formatées correctement, il est plus facile pour les utilisateurs de lire le contenu (les données) de la cellule. Il existe de nombreuses façons de formater les cellules et leur contenu. La façon la plus simple est de formater les cellules en utilisant Microsoft Excel dans un environnement WYSIWYG lors de la création d'une feuille de calcul de concepteur. Une fois la feuille de calcul de concepteur créée, vous pouvez ouvrir la feuille de calcul en utilisant Aspose.Cells en conservant tous les paramètres de format enregistrés avec la feuille de calcul. Une autre façon de formater les cellules et leur contenu est d'utiliser l'API Aspose.Cells. Dans ce sujet, nous décrirons deux approches pour formater les cellules et leur contenu à l'aide de l'API Aspose.Cells.
### **Mise en forme des cellules**
Les développeurs peuvent formater les cellules et leur contenu en utilisant l'API flexible d'Aspose.Cells. Aspose.Cells fournit une classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contient une [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fournit une collection Cells. Chaque élément de la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells) représente un objet de la classe **Cell**.

Aspose.Cells fournit la propriété [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) dans la classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell), utilisée pour définir le style de formatage d'une cellule. De plus, Aspose.Cells fournit également une classe [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) utilisée pour le même but. Appliquez différents types de styles de formatage sur les cellules pour définir leurs couleurs d'arrière-plan ou de premier plan, les bordures, les polices, les alignements horizontal et vertical, le niveau d'indentation, la direction du texte, l'angle de rotation et bien plus encore.
#### **Utilisation de la méthode setStyle**
Lors de l'application de différents styles de formatage à différentes cellules, il est préférable d'utiliser la méthode setStyle de la classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell). Un exemple est donné ci-dessous pour illustrer l'utilisation de la méthode setStyle pour appliquer divers paramètres de formatage sur une cellule.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formatting-FormattingCellsUsingsetStyleMethod-1.java" >}}




#### **Utilisation de l'objet Style**
Lors de l'application du même style de formatage à différentes cellules, utilisez l'objet [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style).

1. Ajoutez un objet [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) à la collection Styles de la classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) en appelant la méthode createStyle de la classe Workbook.
1. Accédez au nouvel objet Style ajouté depuis la collection Styles.
1. Définissez les propriétés souhaitées de l'objet Style pour appliquer les paramètres de formatage souhaités.
1. Attribuez l'objet Style configuré à la propriété Style de n'importe quelle cellule souhaitée.

Cette approche peut grandement améliorer l'efficacité de vos applications et économiser de la mémoire également.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingCellsUsingStyleObject-FormattingCellsUsingStyleObject.java" >}}




#### **Application d'effets de remplissage dégradé**
Pour appliquer les effets de remplissage en dégradé désirés à la cellule, utilisez la méthode setTwoColorGradient de l'objet Style en conséquence.
#### **Exemple de code**
La sortie suivante est obtenue en exécutant le code ci-dessous. 

**Application des effets de remplissage en dégradé** 

![todo:image_alt_text](data-formatting_1.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ApplyGradientFillEffects-ApplyGradientFillEffects.java" >}}




## **Configuration des paramètres d'alignement**
Toute personne ayant utilisé Microsoft Excel pour formater des cellules sera familière avec les paramètres d'alignement dans Microsoft Excel.

**Paramètres d'alignement dans Microsoft Excel** 

![todo:image_alt_text](data-formatting_2.png)

Comme vous pouvez le voir sur la figure ci-dessus, il existe différents types d'options d'alignement :

- [Alignement du texte](/cells/fr/java/data-formatting/) (horizontal & vertical)
- [Indentation](/cells/fr/java/data-formatting/)
- [Orientation](/cells/fr/java/data-formatting/)
- [Contrôle du texte](/cells/fr/java/data-formatting/)
- [Direction du texte](/cells/fr/java/data-formatting/)

Tous ces paramètres d'alignement sont entièrement pris en charge par Aspose.Cells et sont discutés plus en détail ci-dessous.
### **Configuration des paramètres d'alignement**
Aspose.Cells fournit une classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), qui représente un fichier Excel. La classe Workbook contient une WorksheetCollection qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

La classe Worksheet fournit une collection Cells. Chaque élément de la collection Cells représente un objet de la classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

Aspose.Cells fournit la méthode setStyle dans la classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) qui est utilisée pour formater une cellule. La classe [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) fournit des propriétés utiles pour configurer les paramètres de la police.

Sélectionnez n'importe quel type d'alignement de texte en utilisant l'énumération TextAlignmentType. Les types d'alignement de texte prédéfinis dans l'énumération TextAlignmentType sont :

|**Types d'alignement de texte**|**Description**|
| :- | :- |
|Bottom|Représente un alignement de texte en bas|
|Center|Représente un alignement de texte au centre|
|CenterAcross|Représente un alignement de texte centré sur plusieurs cellules|
|Distributed|Représente un alignement de texte distribué|
|Fill|Représente un alignement de texte en remplissage|
|General|Représente un alignement de texte général|
|Justify|Représente un alignement de texte justifié|
|Left|Représente un alignement de texte à gauche|
|Right|Représente un alignement de texte à droite|
|Top|Représente un alignement de texte en haut|
{{% alert color="primary" %}} 

Vous pouvez également appliquer le paramètre de justifie distribué en utilisant la méthode Style.setJustifyDistributed().

{{% /alert %}} 
#### **Alignement horizontal**
Utilisez la méthode setHorizontalAlignment de l'objet [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) pour aligner le texte horizontalement.

La sortie suivante est obtenue en exécutant le code d'exemple ci-dessous :

**Aligner le texte horizontalement** 

![todo:image_alt_text](data-formatting_3.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentHorizontal-TextAlignmentHorizontal.java" >}}




#### **Alignement vertical**
Utilisez la méthode setVerticalAlignment de l'objet [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) pour aligner le texte verticalement.

La sortie suivante est obtenue lorsque VerticalAlignment est défini sur centre.

**Aligner le texte verticalement** 

![todo:image_alt_text](data-formatting_4.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentVertical-TextAlignmentVertical.java" >}}




### **Indentation**
Il est possible de définir le niveau d'indentation du texte dans une cellule en utilisant la méthode setIndentLevel de l'objet [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style).

La sortie suivante est obtenue lorsque IndentLevel est défini sur 2.

**Niveau d'indentation ajusté à 2** 

![todo:image_alt_text](data-formatting_5.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Indentation-ImportingfromResultSet.java" >}}




### **Orientation**
Définir l'orientation (rotation) du texte dans une cellule avec la méthode setRotationAngle de l'objet [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style).

La sortie suivante est obtenue lorsque l'angle de rotation est défini sur 25.

**Angle de rotation défini à 25** 

![todo:image_alt_text](data-formatting_6.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Orientation-Orientation.java" >}}




### **Contrôle du texte**
La section suivante aborde comment contrôler le texte en définissant le retour à la ligne, le rétrécissement pour s'adapter et d'autres options de mise en forme.
#### **Retour à la ligne du texte**
Le retour à la ligne du texte dans une cellule rend la lecture plus facile : la hauteur de la cellule s'ajuste pour s'adapter à tout le texte, au lieu de le couper ou de déborder sur les cellules voisines.

Activez ou désactivez le retour à la ligne avec la méthode [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) de l'objet setTextWrapped.

Le résultat suivant est obtenu lorsque le retour à la ligne du texte est activé.

**Texte retourné à l'intérieur de la cellule** 

![todo:image_alt_text](data-formatting_7.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WrapText-WrapText.java" >}}




#### **Rétrécissement pour s'adapter**
Une option pour le retour à la ligne du texte dans un champ est de réduire la taille du texte pour qu'il tienne dans les dimensions d'une cellule. Ceci est fait en définissant la propriété IsTextWrapped de l'objet [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) sur **true**.

Le résultat suivant est obtenu lorsque le texte est réduit pour tenir dans la cellule.

**Texte rétréci pour tenir à l'intérieur des limites de la cellule** 

![todo:image_alt_text](data-formatting_8.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ShrinkingToFit-ShrinkingToFit.java" >}}




#### **Fusion de cellules**
Comme Microsoft Excel, Aspose.Cells prend en charge la fusion de plusieurs cellules en une seule.

Le résultat suivant est obtenu si les trois cellules de la première ligne sont fusionnées pour créer une seule grande cellule.

**Trois cellules fusionnées pour créer une grande cellule** 

![todo:image_alt_text](data-formatting_9.png)

Utilisez la méthode Merge de la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells) pour fusionner des cellules. La méthode Merge prend les paramètres suivants :

- Première ligne, la première ligne à partir de laquelle commencer la fusion.
- Première colonne, la première colonne à partir de laquelle commencer la fusion.
- Nombre de lignes, le nombre de lignes à fusionner.
Nombre de colonnes, le nombre de colonnes à fusionner.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}




### **Direction du texte**
Il est possible de définir l'ordre de lecture du texte dans les cellules. L'ordre de lecture est l'ordre visuel dans lequel les caractères, les mots, etc. sont affichés. Par exemple, l'anglais est une langue de gauche à droite tandis que l'arabe est une langue de droite à gauche.

L'ordre de lecture est défini avec la propriété TextDirection de l'objet [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style). Aspose.Cells fournit des types de direction de texte prédéfinis dans l'énumération TextDirectionType.

|**Types de direction du texte**|**Description**|
| :- | :- |
|Context|L'ordre de lecture en accord avec la langue du premier caractère saisi|
|LeftToRight|Ordre de lecture de gauche à droite|
|RightToLeft|Ordre de lecture de droite à gauche|






{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ChangeTextDirection-ChangeTextDirection.java" >}}





La sortie suivante est obtenue si l'ordre de lecture du texte est défini de droite à gauche.

**Définir l'ordre de lecture du texte de droite à gauche** 

![todo:image_alt_text](data-formatting_10.png)
## **Formatage de caractères sélectionnés dans une cellule**
[Traitement des paramètres de police](/cells/fr/java/dealing-with-font-settings/) a expliqué comment formater des cellules mais seulement comment formater le contenu complet des cellules. Et si vous voulez formater uniquement certains caractères ?

Aspose.Cells prend en charge cette fonctionnalité. Ce sujet explique comment l'utiliser.
### **Formatage de caractères sélectionnés**
Aspose.Cells fournit une classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe Workbook contient une collection de feuilles de calcul qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe Worksheet fournit une collection de cellules. Chaque élément de la collection Cells représente un objet de la classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

La classe Cell fournit une méthode characters qui prend les paramètres suivants pour sélectionner une plage de caractères dans une cellule :

- **Index de départ**, l'index du caractère à partir duquel commencer la sélection.
- **Nombre de caractères**, le nombre de caractères à sélectionner.

Dans le fichier de sortie, dans la cellule A1, le mot 'Visite' est formaté avec la police par défaut mais 'Aspose!' est en gras et en bleu.

**Mise en forme des caractères sélectionnés** 

![todo:image_alt_text](data-formatting_11.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}







{{% alert color="primary" %}} 

Si vous êtes intéressé par la mise en forme d'une partie du Rich Text dans une [cellule](/cells/fr/java/access-and-update-the-portions-of-rich-text-of-cell/), considérez l'utilisation des méthodes Cell.getCharacters & Cell.setCharacters. La méthode Cell.getCharacters est utilisée pour accéder aux parties du texte et les modifications peuvent être effectuées en utilisant la méthode Cell.setCharacters tandis que la méthode **get** renvoie un tableau d'objets FontSetting qui peuvent être manipulés pour définir diverses propriétés telles que le nom de la police, la couleur de la police, la graisse, etc, et la méthode **set** peut être utilisée pour appliquer les modifications.

{{% /alert %}} 
## **Activation des feuilles et mise en place d'une cellule active ou sélection d'une plage de cellules dans la feuille de calcul**
Parfois, vous pouvez avoir besoin d'activer une feuille de calcul spécifique afin qu'elle soit la première à s'afficher lorsque quelqu'un ouvre le fichier dans Microsoft Excel. Vous pouvez également avoir besoin d'activer une cellule spécifique de manière à ce que les barres de défilement se déplacent vers la cellule active pour qu'elle soit clairement visible. Aspose.Cells est capable d'effectuer toutes les tâches mentionnées ci-dessus.

Une feuille active est la feuille sur laquelle vous travaillez dans un classeur. Le nom de l'onglet de la feuille active est en gras par défaut. Une cellule active, quant à elle, est la cellule sélectionnée dans laquelle les données sont saisies lorsque vous commencez à taper. Seule une cellule est active à la fois. La cellule active est entourée d'une bordure épaisse pour la faire ressortir des autres cellules. Aspose.Cells vous permet également de sélectionner une plage de cellules dans la feuille de calcul.
### **Activation d'une feuille et mise en place d'une cellule active**
Aspose.Cells fournit une API spécifique pour ces tâches. Par exemple, la méthode WorksheetCollection.setActiveSheetIndex est utile pour définir une feuille active. De même, la méthode Worksheet.setActiveCell est utilisée pour définir et obtenir une cellule active dans une feuille de calcul.

Si vous souhaitez que les barres de défilement horizontales et verticales se déplacent jusqu'à la position de l'index de ligne et de colonne pour donner une bonne vue des données sélectionnées lorsque le fichier est ouvert dans Microsoft Excel, utilisez les propriétés Worksheet.setFirstVisibleRow et Worksheet.setFirstVisibleColumn.

L'exemple suivant montre comment activer une feuille de calcul et rendre une cellule active. Les barres de défilement sont déplacées pour faire de la 2e ligne et de la 2e colonne leur première ligne et colonne visible.

**Définition de la cellule B2 comme cellule active** 

![todo:image_alt_text](data-formatting_12.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MakeCellActive-MakeCellActive.java" >}}




#### **Sélection d'une plage de cellules dans la feuille de calcul**
Aspose.Cells fournit la méthode Worksheet.selectRange(int startRow, int startColumn, int totalRows, int totalColumns, bool removeOthers). En utilisant le dernier paramètre - removeOthers - à true, les autres sélections de cellules ou de plages de cellules dans la feuille sont supprimées.

L'exemple suivant montre comment sélectionner une plage de cellules dans la feuille de calcul active.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SelectRangeofCellsinWorksheet-SelectRangeofCellsinWorksheet.java" >}}







{{% alert color="primary" %}} 

Toutes les classes et méthodes ci-dessus sont disponibles avec la version sous licence de Aspose.Cells.

{{% /alert %}} 
## **Formatage des lignes et colonnes**
Mettre en forme les lignes et les colonnes dans une feuille de calcul pour donner au rapport un aspect est probablement la fonctionnalité la plus largement utilisée de l'application Excel. Les API Aspose.Cells offrent également cette fonctionnalité grâce à son modèle de données en exposant la classe Style qui gère principalement toutes les fonctionnalités liées au style telles que la police et ses attributs, l'alignement du texte, les couleurs de fond/avant-plan, les bordures, le format d'affichage pour les chiffres et les littéraux de date, etc. Une autre classe utile fournie par les API Aspose.Cells est StyleFlag qui permet la réutilisation de l'objet Style. 

Dans cet article, nous essaierons d'expliquer comment utiliser l'API Aspose.Cells for Java pour appliquer une mise en forme aux lignes et aux colonnes. 
### **Mise en forme des lignes & colonnes**
Aspose.Cells fournit une classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contient une WorksheetCollection qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe Worksheet. La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fournit la collection Cells.
#### **Formatage d'une ligne**
Chaque élément de la collection Rows représente un objet Row. L'objet Row offre la méthode applyStyle utilisée pour appliquer une mise en forme à une ligne.

Pour appliquer le même formatage à une ligne, utilisez l'objet Style :

1. Ajoutez un objet Style à la classe Workbook en appelant sa méthode createStyle.
1. Définissez les propriétés de l'objet Style pour appliquer les paramètres de formatage.
1. Assignez l'objet Style configuré à la méthode applyStyle d'un objet Row.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingARow-FormattingARow.java" >}}




#### **Formatage d'une colonne**
La collection Cells fournit une collection Columns. Chaque élément de la collection Columns représente un objet Column. Similaire à l'objet Row, l'objet Column offre la méthode applyStyle utilisée pour définir le formatage de la colonne. Utilisez la méthode applyStyle de l'objet Column pour formater une colonne de la même manière qu'une ligne.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingAColumn-FormattingAColumn.java" >}}




#### **Définir le format d'affichage des chiffres et des dates pour les lignes et les colonnes**
Si l'exigence est de définir le format d'affichage des chiffres et des dates pour une ligne ou une colonne complète, le processus est plus ou moins le même que celui discuté ci-dessus, cependant, au lieu de définir des paramètres pour le contenu textuel, vous définirez le formatage pour les chiffres et les dates en utilisant le Style.Number ou le Style.Custom. Veuillez noter que la propriété Style.Number est de type entier et fait référence aux formats de nombre et de date intégrés, tandis que la propriété Style.Custom est de type chaîne et accepte les modèles valides.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingDisplayFormat-SettingDisplayFormat.java" >}}







{{% alert color="primary" %}} 

Veuillez consulter l'article détaillé sur [Réglage des formats d'affichage des chiffres et des [Dates](/cells/fr/java/data-formatting/).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
