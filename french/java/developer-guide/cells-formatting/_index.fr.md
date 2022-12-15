---
title: Formats Cells
type: docs
weight: 100
url: /fr/java/cells-formatting/
---
## **Ajout de bordures au Cells**
Microsoft Excel permet aux utilisateurs de formater les cellules en ajoutant des bordures.

**Paramètres des bordures dans Microsoft Excel** 

![tâche : image_autre_texte](cells-formatting_1.png)

Le type de bordure dépend de l'endroit où elle est ajoutée. Par exemple, une bordure supérieure est une bordure ajoutée à la position supérieure d'une cellule. Les utilisateurs peuvent également modifier le style de ligne et la couleur des bordures.

Avec Aspose.Cells, les développeurs peuvent ajouter des bordures et personnaliser leur apparence de la même manière flexible qu'avec Microsoft Excel.
### **Ajout de bordures au Cells**
 Aspose.Cells fournit une classe,[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) qui représente un fichier Excel Microsoft. La[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) classe contient un[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classer. La[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la classe offre une[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) le recueil. Chaque élément de la[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection représente un objet de la[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)classer.

 Aspose.Cells fournit le[setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\) ) méthode dans le[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) classe utilisée pour définir le style de formatage d'une cellule. Aussi, l'objet de la[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)La classe est utilisée et fournit des propriétés pour configurer les paramètres de police.
#### **Ajout de bordures à un Cell**
 Ajouter des bordures à une cellule avec le[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) objets[setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\) ) méthode. Le type de bordure est passé en paramètre. Tous les types de bordures sont prédéfinis dans le[Type de bordure](https://reference.aspose.com/cells/java/com.aspose.cells/BorderType)énumération.

|**Types de bordure**|**La description**|
|:- |:- |
|[BOTTOM_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#BOTTOM_BORDER)|La ligne de bordure inférieure|
|[DIAGONAL_DOWN](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_DOWN)|Une ligne diagonale du haut à gauche vers le bas à droite|
|[DIAGONALE_HAUT](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_UP)|Une ligne diagonale du bas à gauche vers le haut à droite|
|[LEFT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#LEFT_BORDER)|La frontière gauche|
|[RIGHT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#RIGHT_BORDER)|La frontière droite|
|[TOP_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#TOP_BORDER)|La ligne de bordure supérieure|
|[HORIZONTAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#HORIZONTAL)|Uniquement pour le style dynamique, comme la mise en forme conditionnelle.|
|[VERTICAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#VERTICAL)|Uniquement pour le style dynamique, comme la mise en forme conditionnelle.|
 Pour définir la couleur de la ligne, sélectionnez une couleur à l'aide des[Couleur](https://reference.aspose.com/cells/java/com.aspose.cells/Color) énumération et la transmettre au[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) objets[setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\) ) paramètre Couleur de la méthode. Les styles de ligne sont prédéfinis dans le[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)énumération.

|**Styles de ligne**|**La description**|
|:- |:- |
|[DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT)|Représente une fine ligne pointillée|
|[SE PRÉCIPITER_POINT_POINT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT_DOT)|Représente une fine ligne tiret-point-pointillé|
|[POINTILLÉ](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASHED)|Représente la ligne pointillée|
|[POINTÉ](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOTTED)|Représente la ligne pointillée|
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOUBLE)|Représente une double ligne|
|[CHEVEU](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#HAIR)|Représente la ligne des cheveux|
|[MOYEN_SE PRÉCIPITER_POINT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT)|Représente une ligne pointillée moyenne|
|[MOYEN_SE PRÉCIPITER_POINT_POINT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT_DOT)|Représente une ligne tiret-point-pointillé moyen|
|[MEDIUM_DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASHED)|Représente une ligne pointillée moyenne|
|[RIEN](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#NONE)|Ne représente aucune ligne|
|[MOYEN](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM)|Représente la ligne moyenne|
|[INCLINÉ_SE PRÉCIPITER_POINT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#SLANTED_DASH_DOT)|Représente une ligne pointillée moyenne inclinée|
|[ÉPAIS](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THICK)|Représente une ligne épaisse|
|[MINCE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THIN)|Représente une ligne fine|
 Sélectionnez l'un des styles de ligne ci-dessus, puis attribuez-le au[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)objets[setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) méthode.

La sortie suivante est générée lors de l'exécution du code ci-dessous.

**Bordures appliquées sur tous les côtés d'une cellule** 

![tâche : image_autre_texte](cells-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBordersToCells-AddingBordersToCells.java" >}}
#### **Ajout de bordures à une plage de Cells**
 Il est possible d'ajouter des bordures à une plage de cellules plutôt qu'à une seule cellule. Tout d'abord, créez une plage de cellules en appelant le[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) de la collection[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)) méthode, qui prend les paramètres suivants :

- **Première rangée**, la première ligne de la plage.
- **Première colonne**, la première colonne de la plage.
- **Nombre de rangées**, le nombre de lignes dans la plage.
- **Le nombre de colonnes**, le nombre de colonnes dans la plage.

 La[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\) ) La méthode renvoie un[Intervalle](https://reference.aspose.com/cells/java/com.aspose.cells/Range) objet, qui contient la plage spécifiée. La[Intervalle](https://reference.aspose.com/cells/java/com.aspose.cells/Range) l'objet fournit un[setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)) méthode qui prend les paramètres suivants :

- **CellBorderType**, le style de bordure, sélectionné dans le[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)énumération.
- **Couleur**, la couleur de la bordure, sélectionnée parmi les[Couleur](https://reference.aspose.com/cells/java/com.aspose.cells/Color)énumération.

La sortie suivante est générée lors de l'exécution du code ci-dessous.

**Bordures appliquées sur une plage de cellules** 

![tâche : image_autre_texte](cells-formatting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBorderstoRange-AddingBorderstoRange.java" >}}
## **Couleurs et Palette**
Une palette est le nombre de couleurs disponibles pour la création d'une image. L'utilisation d'une palette standardisée dans une présentation permet à l'utilisateur de créer un look cohérent. Chaque fichier Excel Microsoft (97-2003) possède une palette de 56 couleurs pouvant être appliquées aux cellules, polices, quadrillages, objets graphiques, remplissages et lignes d'un graphique.

**Paramètres de la palette dans Microsoft Excel** 

![tâche : image_autre_texte](cells-formatting_4.png)

Avec Aspose.Cells, il est non seulement possible d'utiliser des couleurs existantes, mais également des couleurs personnalisées. Avant d'utiliser une couleur personnalisée, ajoutez-la à la palette. Cette rubrique explique comment ajouter des couleurs personnalisées à la palette.
### **Ajout de couleurs personnalisées à la palette**
Aspose.Cells prend également en charge une palette de 56 couleurs. Une palette de couleurs standard est illustrée ci-dessus. Si vous souhaitez utiliser une couleur personnalisée qui n'est pas définie dans la palette, vous devrez ajouter cette couleur à la palette avant utilisation.

{{% alert color="primary" %}} 

La palette ne contient que 56 couleurs. Lorsque vous ajoutez une couleur personnalisée à la palette, la palette est modifiée et tout élément du fichier formaté avec la couleur précédente est modifié. Donc, lorsque vous changez de palette, soyez très prudent. De plus, il s'agit de la limitation du format de fichier XLS (Excel 97 - 2003) uniquement, car il n'y a pas de telle limitation pour XLSX ou d'autres formats de fichier avancés MS Excel (2007/2010).

{{% /alert %}} 

Aspose.Cells fournit une classe,[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), qui représente un fichier Excel Microsoft. La classe fournit la[changerPalette](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#changePalette\(com.aspose.cells.Color,%20int\)) qui prend les paramètres suivants pour ajouter une couleur personnalisée afin de modifier la palette :

- **Couleur personnalisée**, la couleur personnalisée à ajouter à la palette.
- **Indice**, l'index de la couleur qui sera remplacée par la couleur personnalisée. Doit être compris entre 0 et 55.

L'exemple ci-dessous ajoute une couleur personnalisée à la palette avant de l'appliquer sur une police.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndPalette-ColorsAndPalette.java" >}}
## **Couleurs et motifs de fond**
Microsoft Excel peut définir les couleurs de premier plan (contour) et d'arrière-plan (remplissage) des cellules et des motifs d'arrière-plan comme indiqué ci-dessous.

**Définition des couleurs et des motifs d'arrière-plan dans Microsoft Excel** 

![tâche : image_autre_texte](cells-formatting_5.png)

Aspose.Cells prend également en charge ces fonctionnalités de manière flexible. Dans cette rubrique, nous apprenons à utiliser ces fonctionnalités en utilisant Aspose.Cells.
### **Définition des couleurs et des motifs d'arrière-plan**
Aspose.Cells fournit une classe,[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), qui représente un fichier Excel Microsoft. La[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)classe contient un[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)classer. La[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)la classe offre une[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)le recueil. Chaque élément de la[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection représente un objet de la[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)classer.

Aspose.Cells fournit le[setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) méthode dans le[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)classe utilisée pour définir la mise en forme d'une cellule. Aussi, l'objet de la[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)class peut être utilisé pour configurer les paramètres de police.

{{% alert color="primary" %}} 

 Pour définir la couleur de premier plan ou d'arrière-plan d'une cellule, utilisez la[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) objets[setBackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) ou[setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) Propriétés. Ces propriétés n'entrent en vigueur que si le[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) objets[setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) propriété est configurée.

{{% /alert %}} 

La[setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)La propriété définit la couleur d'ombrage de la cellule.

La[setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) La propriété spécifie le motif d'arrière-plan utilisé pour la couleur de premier plan ou d'arrière-plan. Aspose.Cells fournit le[Type d'arrière-plan](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)énumération qui contient un ensemble de types prédéfinis de motifs d'arrière-plan.

|**Type de motif**|**La description**|
|:- |:- |
|[DIAGONAL_CROSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_CROSSHATCH)|Représente le motif hachuré en diagonale|
|[DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_STRIPE)|Représente le motif à rayures diagonales|
|[GRIS_6](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_6)|Représente un motif gris de 6,25 %|
|[GRIS_12](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_12)|Représente un motif gris de 12,5 %|
|[GRIS_25](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_25)|Représente 25 % de motif gris|
|[GRIS_50](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_50)|Représente un motif gris à 50 %|
|[GRIS_75](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_75)|Représente un motif gris à 75 %|
|[HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#HORIZONTAL_STRIPE)|Représente le motif de rayures horizontales|
|[RIEN](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)|Ne représente aucun arrière-plan|
|[INVERSE_DIAGONALE_BANDE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#REVERSE_DIAGONAL_STRIPE)|Représente le motif à rayures diagonales inversées|
|[SOLIDE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)|Représente un motif solide|
|[ÉPAIS_DIAGONALE_HACHURE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THICK_DIAGONAL_CROSSHATCH)|Représente un motif hachuré diagonal épais|
|[MINCE_DIAGONALE_HACHURE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_CROSSHATCH)|Représente un motif de hachures diagonales minces|
|[MINCE_DIAGONALE_BANDE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_STRIPE)|Représente un motif à fines rayures diagonales|
|[MINCE_HORIZONTAL_HACHURE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_CROSSHATCH)|Représente un motif hachuré horizontal fin|
|[MINCE_HORIZONTAL_BANDE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_STRIPE)|Représente un motif de fines rayures horizontales|
|[MINCE_INVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_REVERSE_DIAGONAL_STRIPE)|Représente un motif à fines rayures diagonales inversées|
|[MINCE_VERTICAL_BANDE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_VERTICAL_STRIPE)|Représente un motif de fines rayures verticales|
|[VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#VERTICAL_STRIPE)|Représente le motif de rayures verticales|
Dans l'exemple ci-dessous, la couleur de premier plan de la cellule A1 est définie, mais A2 est configuré pour avoir à la fois des couleurs de premier plan et d'arrière-plan avec un motif d'arrière-plan à rayures verticales.

La sortie suivante est générée lors de l'exécution du code.

**Couleurs de premier plan et d'arrière-plan appliquées aux cellules avec des motifs d'arrière-plan** 

![tâche : image_autre_texte](cells-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndBackground-ColorsAndBackground.java" >}}
### **Important à savoir**
{{% alert color="primary" %}} 

-  Pour définir la couleur de premier plan ou d'arrière-plan d'une cellule, utilisez la[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) objets[Couleur de premier plan](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) ou[Couleur de l'arrière plan](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) Propriétés. Les deux propriétés ne prendront effet que si le[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) objets[Motif](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) propriété est configurée.
-  La[Couleur de premier plan](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) La propriété définit la couleur de nuance de la cellule.
 La[Motif](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) La propriété spécifie le type de motif d'arrière-plan utilisé pour la couleur de premier plan ou d'arrière-plan. Aspose.Cells fournit une énumération,[Type d'arrière-plan](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)qui contient un ensemble de types prédéfinis de motifs d'arrière-plan.
-  Si vous sélectionnez[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) valeur de la[Type d'arrière-plan](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType) énumération, la couleur de premier plan n'est pas appliquée.
 De même, la couleur d'arrière-plan n'est pas appliquée si vous sélectionnez le[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) ou[BackgroundType.SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID) valeurs.
-  Lors de la récupération de la couleur d'ombrage/de remplissage de la cellule, si[Style.Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) est[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE), [Style.ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) reviendra*Couleur.Vide*.

{{% /alert %}} 
## **Formatage des caractères sélectionnés dans un Cell**
[Gestion des paramètres de police](/cells/fr/java/dealing-with-font-settings/) expliqué comment formater les cellules, mais seulement comment formater le contenu des cellules entières. Que faire si vous souhaitez formater uniquement les caractères sélectionnés ?

Aspose.Cells prend en charge cette fonctionnalité. Cette rubrique explique comment utiliser cette fonctionnalité.
### **Formatage des caractères sélectionnés**
Aspose.Cells fournit une classe,[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), qui représente un fichier Excel Microsoft. La[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)classe contient un[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)classer. La[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)la classe offre une[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)le recueil. Chaque élément de la[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection représente un objet de la[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)classer.

La[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) la classe fournit[personnages](https://reference.aspose.com/cells/java/com.aspose.cells/cell#characters\(int,%20int\)) qui utilise les paramètres suivants pour sélectionner une plage de caractères dans une cellule :

- **Index de départ**, l'index du caractère à partir duquel commencer la sélection.
- **Nombre de caractères**, le nombre de caractères à sélectionner.

Dans le fichier de sortie, dans la cellule A1", le mot 'Visite' est formaté avec la police par défaut mais 'Aspose!' est gras et bleu.

**Formatage des caractères sélectionnés** 

![tâche : image_autre_texte](cells-formatting_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}

{{% alert color="primary" %}} 

 Si tu es interessé par[mise en forme d'une partie de texte enrichi dans une cellule](/cells/fr/java/access-and-update-the-portions-of-rich-text-of-cell/) , pensez à utiliser le[Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\) ) & Cell.setCharacters méthodes. La[Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\) ) doit être utilisée pour accéder aux parties du texte, puis les modifications peuvent être effectuées à l'aide de la méthode Cell.setCharacters alors que la**obtenir**méthode renvoie un tableau de[FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) des objets qui peuvent être manipulés pour définir diverses propriétés telles que le nom de la police, la couleur de la police, l'audace, etc. et**Positionner** peut être utilisée pour appliquer les modifications.

{{% /alert %}}

## **Sujets avancés**
- [Paramètres d'alignement](/cells/fr/java/cells-alignment-settings/)
- [Mise en forme conditionnelle](/cells/fr/java/conditional-formatting/)
- [Formatage des données](/cells/fr/java/data-formatting/)
- [Thèmes et couleurs Excel](/cells/fr/java/excel-2007-themes-and-colors/)
- [Gestion des paramètres de police](/cells/fr/java/dealing-with-font-settings/)
- [Formater la feuille de calcul Cells dans un classeur](/cells/fr/java/format-worksheet-cells-in-a-workbook/)
- [Mettre en œuvre le système de date 1904](/cells/fr/java/implement-1904-date-system/)
- [Fusion et défusion Cells](/cells/fr/java/merging-and-unmerging-cells/)
- [Paramètres du numéro](/cells/fr/java/cells-number-settings/)
- [Conserver le préfixe de guillemets simples de la valeur ou de la plage Cell](/cells/fr/java/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Style et formatage des données](/cells/fr/java/styling-and-data-formatting/)
