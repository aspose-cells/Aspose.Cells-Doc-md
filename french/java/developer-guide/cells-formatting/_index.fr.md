---
title: Formats de cellules 
type: docs
weight: 100
url: /fr/java/cells-formatting/
---

## **Ajout de bordures aux cellules**
Microsoft Excel permet aux utilisateurs de formater les cellules en ajoutant des bordures.

**Paramètres des bordures dans Microsoft Excel** 

![todo:image_alt_text](cells-formatting_1.png)

Le type de bordure dépend de son emplacement. Par exemple, une bordure supérieure est ajoutée à la position supérieure d'une cellule. Les utilisateurs peuvent également modifier le style de ligne et la couleur des bordures.

Avec Aspose.Cells, les développeurs peuvent ajouter des bordures et personnaliser leur apparence de la même manière flexible qu'ils le peuvent dans Microsoft Excel.
### **Ajout de bordures aux cellules**
Aspose.Cells fournit une classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) contient une [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fournit une collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Chaque élément de la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) représente un objet de la classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

Aspose.Cells fournit la méthode [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) dans la classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) utilisée pour définir le style de formatage d'une cellule. De plus, l'objet de la classe [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) est utilisé et fournit des propriétés pour configurer les paramètres de la police.
#### **Ajout de bordures à une cellule**
Ajoutez des bordures à une cellule avec la méthode [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) de l'objet [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style). Le type de bordure est passé en paramètre. Tous les types de bordures sont prédéfinis dans l'énumération [BorderType](https://reference.aspose.com/cells/java/com.aspose.cells/BorderType).

|**Types de bordures**|**Description**|
| :- | :- |
|[BOTTOM_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#BOTTOM_BORDER)|La ligne de bordure inférieure
|[DIAGONAL_DOWN](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_DOWN)|Une ligne diagonale du coin supérieur gauche au coin inférieur droit
|[DIAGONAL_UP](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_UP)|Une ligne diagonale du coin inférieur gauche au coin supérieur droit
|[LEFT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#LEFT_BORDER)|La ligne de bordure gauche
|[RIGHT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#RIGHT_BORDER)|La ligne de bordure droite
|[TOP_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#TOP_BORDER)|La ligne de bordure supérieure
|[HORIZONTAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#HORIZONTAL)|Uniquement pour le style dynamique, tel que le formatage conditionnel.
|[VERTICAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#VERTICAL)|Uniquement pour le style dynamique, tel que le formatage conditionnel.
Pour définir la couleur de la ligne, sélectionnez une couleur en utilisant l'énumération [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color) et passez-la en paramètre Colour de la méthode [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) de l'objet [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style). Les styles de lignes sont prédéfinis dans l'énumération [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType).

|**Styles de ligne**|**Description**|
| :- | :- |
|[DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT)|Représente une ligne pointillée fine
|[DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT_DOT)|Représente une ligne en pointillés fins et points
|[DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASHED)|Représente une ligne en pointillés
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOTTED)|Représente une ligne en pointillés
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOUBLE)|Représente une double ligne
|[HAIR](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#HAIR)|Représente une ligne fine
|[MEDIUM_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT)|Représente une ligne en pointillé moyen|
|[MEDIUM_DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT_DOT)|Représente une ligne en tiret pointé moyen|
|[MEDIUM_DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASHED)|Représente une ligne en pointillé moyen|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#NONE)|Représente aucune ligne|
|[MEDIUM](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM)|Représente une ligne moyenne|
|[SLANTED_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#SLANTED_DASH_DOT)|Représente une ligne en pointillé moyen inclinée|
|[THICK](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THICK)|Représente une ligne épaisse|
|[THIN](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THIN)|Représente une ligne fine|
Sélectionnez l'un des styles de ligne ci-dessus, puis attribuez-le à la méthode [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) de l'objet [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style).

La sortie suivante est générée lors de l'exécution du code ci-dessous.

**Bordures appliquées de tous les côtés d'une cellule** 

![todo:image_alt_text](cells-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBordersToCells-AddingBordersToCells.java" >}}
#### **Ajout de bordures à une plage de cellules**
Il est possible d'ajouter des bordures à une plage de cellules plutôt qu'à une seule cellule. Tout d'abord, créez une plage de cellules en appelant la méthode [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)) de la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), qui prend les paramètres suivants :

- **Première ligne**, la première ligne de la plage.
- **Première colonne**, la première colonne de la plage.
- **Nombre de lignes**, le nombre de lignes dans la plage.
- **Nombre de colonnes**, le nombre de colonnes dans la plage.

La méthode [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)) renvoie un objet [Range](https://reference.aspose.com/cells/java/com.aspose.cells/Range) qui contient la plage spécifiée. L'objet [Range](https://reference.aspose.com/cells/java/com.aspose.cells/Range) fournit une méthode [setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)) qui prend les paramètres suivants :

- **Type de bordure de cellule**, le style de ligne de bordure, sélectionné dans l'énumération [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType).
- **Couleur**, la couleur de la ligne de bordure, sélectionnée dans l'énumération [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color).

La sortie suivante est générée lors de l'exécution du code ci-dessous.

**Bordures appliquées sur une plage de cellules** 

![todo:image_alt_text](cells-formatting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBorderstoRange-AddingBorderstoRange.java" >}}
## **Couleurs et palette**
Une palette est le nombre de couleurs disponibles pour créer une image. L'utilisation d'une palette normalisée dans une présentation permet à l'utilisateur de créer un aspect cohérent. Chaque fichier Microsoft Excel (97-2003) possède une palette de 56 couleurs qui peuvent être appliquées aux cellules, polices, quadrillages, objets graphiques, remplissages et lignes dans un graphique.

**Paramètres de la palette dans Microsoft Excel** 

![todo:image_alt_text](cells-formatting_4.png)

Avec Aspose.Cells, il est non seulement possible d'utiliser des couleurs existantes, mais aussi des couleurs personnalisées. Avant d'utiliser une couleur personnalisée, ajoutez-la à la palette. Ce sujet explique comment ajouter des couleurs personnalisées à la palette.
### **Ajout de couleurs personnalisées à la palette**
Aspose.Cells prend également en charge une palette de 56 couleurs. Une palette de couleurs standard est illustrée ci-dessus. Si vous souhaitez utiliser une couleur personnalisée non définie dans la palette, vous devrez l'ajouter à la palette avant de l'utiliser.

{{% alert color="primary" %}} 

La palette ne contient que 56 couleurs. Lorsque vous ajoutez une couleur personnalisée à la palette, celle-ci est modifiée et tout élément du fichier formaté avec la couleur précédente est changé. Donc, lorsque vous modifiez la palette, soyez très prudent. De plus, c'est la limitation du format de fichier XLS (Excel 97-2003) seulement car il n'y a pas de telle limitation pour les formats de fichiers MS Excel plus avancés (2007/2010).

{{% /alert %}} 

Aspose.Cells fournit une classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), qui représente un fichier Microsoft Excel. La classe fournit la méthode [changePalette](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#changePalette\(com.aspose.cells.Color,%20int\)) qui prend les paramètres suivants pour ajouter une couleur personnalisée à modifier dans la palette :

- **Couleur personnalisée**, la couleur personnalisée à ajouter à la palette.
- **Index**, l'index de la couleur qui sera remplacée par la couleur personnalisée. Doit être compris entre 0 et 55.

L'exemple ci-dessous ajoute une couleur personnalisée à la palette avant de l'appliquer à une police.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndPalette-ColorsAndPalette.java" >}}
## **Couleurs et motifs d'arrière-plan**
Microsoft Excel peut définir les couleurs de premier plan (contour) et d'arrière-plan (remplissage) des cellules et les motifs de fond comme illustré ci-dessous.

**Paramétrage des couleurs et motifs de fond dans Microsoft Excel** 

![todo:image_alt_text](cells-formatting_5.png)

Aspose.Cells prend également en charge ces fonctionnalités de manière flexible. Dans ce sujet, nous apprenons à utiliser ces fonctionnalités en utilisant Aspose.Cells.
### **Paramétrage des couleurs et motifs de fond**
Aspose.Cells fournit une classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) contient une [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fournit une collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Chaque élément de la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) représente un objet de la classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

Aspose.Cells fournit la méthode [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) dans la classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) qui est utilisée pour définir la mise en forme d'une cellule. De plus, l'objet de la classe [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) peut être utilisé pour configurer les paramètres de police.

{{% alert color="primary" %}} 

Pour définir la couleur d'avant-plan ou d'arrière-plan d'une cellule, utilisez les propriétés [setBackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) ou [setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) de l'objet [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style). Ces propriétés n'entrent en vigueur que si la propriété [setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) de l'objet [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) est configurée.

{{% /alert %}} 

La propriété [setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) définit la couleur de l'ombrage de la cellule.

La propriété [setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) spécifie le motif d'arrière-plan utilisé pour la couleur d'avant-plan ou d'arrière-plan. Aspose.Cells fournit l'énumération [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType) qui contient un ensemble de types prédéfinis de motifs d'arrière-plan.

|**Type de motif**|**Description**|
| :- | :- |
|[DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_CROSSHATCH)| Représente un motif de croisillons diagonaux
|[DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_STRIPE)| Représente un motif de rayures diagonales
|[GRAY_6](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_6)| Représente un motif gris à 6,25%
|[GRAY_12](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_12)| Représente un motif gris à 12,5%
|[GRAY_25](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_25)| Représente un motif gris à 25%
|[GRAY_50](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_50)| Représente un motif gris à 50%
|[GRAY_75](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_75)| Représente un motif gris à 75%
|[HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#HORIZONTAL_STRIPE)| Représente un motif de rayures horizontales
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)| Représente aucun arrière-plan
|[REVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#REVERSE_DIAGONAL_STRIPE)| Représente un motif de rayures diagonales inversées
|[SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)| Représente un motif solide
|[THICK_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THICK_DIAGONAL_CROSSHATCH)| Représente un motif de croisillons diagonaux épais
|[THIN_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_CROSSHATCH)| Représente un motif de croisillons diagonaux fins
|[THIN_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_STRIPE)| Représente un motif de rayures diagonales fins
|[THIN_HORIZONTAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_CROSSHATCH)| Représente un motif de croisillons horizontaux fins
|[THIN_HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_STRIPE)| Représente un motif de rayures horizontales fins
|[THIN_REVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_REVERSE_DIAGONAL_STRIPE)|Représente un motif de rayures diagonales inversées minces|
|[THIN_VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_VERTICAL_STRIPE)|Représente un motif de rayures verticales minces|
|[VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#VERTICAL_STRIPE)|Représente un motif de rayures verticales|
Dans l'exemple ci-dessous, la couleur de premier plan de la cellule A1 est définie, mais A2 est configurée pour avoir à la fois des couleurs de premier plan et d'arrière-plan avec un motif d'arrière-plan de rayures verticales.|

La sortie ci-dessous est générée lors de l'exécution du code.

**Couleurs d'avant-plan et d'arrière-plan appliquées sur des cellules avec des motifs de fond** 

![todo:image_alt_text](cells-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndBackground-ColorsAndBackground.java" >}}
### **Important à savoir**
{{% alert color="primary" %}} 

- Pour définir la couleur d'avant-plan ou d'arrière-plan d'une cellule, utilisez les propriétés [ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) ou [BackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) de l'objet [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style). Ces deux propriétés prendront effet uniquement si la propriété [Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) de l'objet [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) est configurée.
- La propriété [ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) définit la couleur d'ombrage de la cellule.
  La propriété [Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) spécifie le type de motif de fond utilisé pour la couleur d'avant-plan ou d'arrière-plan. Aspose.Cells fournit une énumération, [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType), qui contient un ensemble de types prédéfinis de motifs de fond.
- Si vous sélectionnez la valeur [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) de l'énumération [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType), la couleur d'avant-plan n'est pas appliquée.
  De même, la couleur d'arrière-plan n'est pas appliquée si vous sélectionnez les valeurs [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) ou [BackgroundType.SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID).
- Lors de la récupération de la couleur de remplissage/d'ombrage de la cellule, si [Style.Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) est [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE), [Style.ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) retournera *Color.Empty*.

{{% /alert %}} 
## **Formatage de caractères sélectionnés dans une cellule**
[Gestion des paramètres de police](/cells/fr/java/dealing-with-font-settings/) expliqué comment formater des cellules mais seulement comment formater le contenu de l'intégralité des cellules. Et si vous voulez formater uniquement certains caractères?

Aspose.Cells prend en charge cette fonctionnalité. Ce sujet explique comment l'utiliser.
### **Formatage de caractères sélectionnés**
Aspose.Cells fournit une classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) contient une [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fournit une collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Chaque élément de la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) représente un objet de la classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

La classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) fournit la méthode [characters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#characters\(int,%20int\)) qui prend les paramètres suivants pour sélectionner une plage de caractères dans une cellule:

- **Index de départ**, l'index du caractère à partir duquel commencer la sélection.
- **Nombre de caractères**, le nombre de caractères à sélectionner.

Dans le fichier de sortie, dans la cellule A1, le mot 'Visite' est formaté avec la police par défaut mais 'Aspose!' est en gras et en bleu.

**Mise en forme des caractères sélectionnés** 

![todo:image_alt_text](cells-formatting_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}

{{% alert color="primary" %}} 

Si vous êtes intéressé par [formater une partie du texte enrichi dans une cellule](/cells/fr/java/access-and-update-the-portions-of-rich-text-of-cell/), envisagez d'utiliser les méthodes [Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\)) & Cell.setCharacters. La méthode [Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\)) est utilisée pour accéder aux parties du texte, puis les modifications peuvent être apportées en utilisant la méthode Cell.setCharacters, tandis que la méthode **get** renvoie un tableau d'objets [FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) qui peuvent être manipulés pour définir diverses propriétés telles que le nom de la police, la couleur de la police, la graisse, etc, et la méthode **set** peut être utilisée pour appliquer les modifications.

{{% /alert %}}

## **Sujets avancés**
- [Paramètres d'alignement](/cells/fr/java/cells-alignment-settings/)
- [Formatage conditionnel](/cells/fr/java/conditional-formatting/)
- [Formatage des données](/cells/fr/java/data-formatting/)
- [Thèmes et couleurs d'Excel](/cells/fr/java/excel-2007-themes-and-colors/)
- [Gestion des paramètres de police](/cells/fr/java/dealing-with-font-settings/)
- [Formater les cellules de feuille de calcul dans un classeur](/cells/fr/java/format-worksheet-cells-in-a-workbook/)
- [Mise en œuvre du système de date 1904](/cells/fr/java/implement-1904-date-system/)
- [Fusionner et scinder des cellules](/cells/fr/java/merging-and-unmerging-cells/)
- [Paramètres de nombre](/cells/fr/java/cells-number-settings/)
- [Préserver le préfixe d'apostrophe unique de la valeur de la cellule ou de la plage](/cells/fr/java/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Mise en forme et formatage des données](/cells/fr/java/styling-and-data-formatting/)
