---
title: Paramètres de bordure
type: docs
weight: 40
url: /fr/net/cells-border-settings/
---
## **Ajout de bordures au Cells**

Microsoft Excel permet aux utilisateurs de formater les cellules en ajoutant des bordures. Le type de bordure dépend de l'endroit où elle est ajoutée. Par exemple, une bordure supérieure est une bordure ajoutée à la position supérieure d'une cellule. Les utilisateurs peuvent également modifier le style de ligne et la couleur des bordures.

Avec Aspose.Cells, les développeurs peuvent ajouter des bordures et personnaliser leur apparence de la même manière flexible que dans Microsoft Excel.

### **Ajout de bordures au Cells**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Excel Microsoft. La[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer. La[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fournit la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) le recueil. Chaque élément de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection représente un objet de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classer.

 Aspose.Cells fournit le[**ObtenirStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index)méthode dans la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classer. La[**DéfinirStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index)La méthode est utilisée pour définir le style de formatage d'une cellule. La[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)La classe fournit des propriétés pour ajouter des bordures aux cellules.

#### **Ajout de bordures à un Cell**

Les développeurs peuvent ajouter des bordures à une cellule en utilisant le[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objets[**Les frontières**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) le recueil. Le type de bordure est transmis sous forme d'index au[**Les frontières**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) le recueil. Tous les types de bordures sont prédéfinis dans le[**Type de bordure**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) énumération.

**Dénombrement des frontières**

|**Types de bordure**|**La description**|
|:- |:- |
|BordureInférieure|Une ligne de bordure inférieure|
|DiagonaleBas|Une ligne diagonale du haut à gauche vers le bas à droite|
|Diagonale vers le haut|Une ligne diagonale du bas à gauche vers le haut à droite|
|Borduregauche|Une frontière gauche|
|Borduredroite|Une frontière droite|
|Bordure supérieure|Une ligne de frontière supérieure|

La[**Les frontières**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)collection stocke toutes les frontières. Chaque frontière dans le[**Les frontières**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) la collection est représentée par un[**Frontière**](https://reference.aspose.com/cells/net/aspose.cells/border) objet qui fournit deux propriétés,[**Couleur**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color) et[**Style de ligne**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle)pour définir respectivement la couleur et le style de ligne d'une bordure.

Pour définir la couleur de ligne d'une bordure, sélectionnez une couleur à l'aide de l'énumération Color (qui fait partie du Framework .NET) et affectez-la à la propriété Color de l'objet Border.

 Le style de ligne de la bordure est défini en sélectionnant un style de ligne dans le[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)énumération.

**Énumération CellBorderTypeCellBorderType énumération**

|**Styles de ligne**|**La description**|
|:- |:- |
|TiretPoint|Ligne pointillée fine|
|TiretPointPoint|Ligne fine tiret-point-pointillé|
|Pointillé|Ligne pointillée|
|Pointé|Ligne pointillée|
|Double|Ligne double|
|Cheveux|Racine des cheveux|
|PointTraitMoyen|Ligne pointillée moyenne|
|MoyenTraitPointPoint|Ligne tiret-point-pointillé moyen|
|Pointillé moyen|Ligne pointillée moyenne|
|Aucun|Pas de ligne|
|Moyen|Ligne moyenne|
|PointTraitIncliné|Ligne pointillée moyenne inclinée|
|Épais|Ligne épaisse|
|Mince|Ligne fine|
Sélectionnez l'un des styles de ligne, puis affectez-le au[**Frontière**](https://reference.aspose.com/cells/net/aspose.cells/border) objets[**Style de ligne**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) propriété.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

Vous devez définir à la fois le style de ligne et la couleur. Les deux bordures diagonales doivent avoir le même style de ligne et la même couleur.

{{% /alert %}}

#### **Ajout de bordures à une plage de Cells**

Il est également possible d'ajouter des bordures à une plage de cellules plutôt qu'à une seule cellule. Pour ce faire, commencez par créer une plage de cellules en appelant le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) de la collection[**CréerPlage**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) méthode. Il prend les paramètres suivants :

- First Row, la première ligne de la gamme.
- Première colonne, représente la première colonne de la plage.
- Nombre de lignes, le nombre de lignes dans la plage.
- Nombre de colonnes, le nombre de colonnes dans la plage.

 La[**CréerPlage**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) méthode renvoie un[**Intervalle**](https://reference.aspose.com/cells/net/aspose.cells/range) objet, qui contient la plage de cellules spécifiée. La[**Intervalle**](https://reference.aspose.com/cells/net/aspose.cells/range) l'objet fournit un[**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) méthode qui prend les paramètres suivants pour ajouter une bordure à la plage de cellules :

- **Type de bordure** , le type de bordure, sélectionné dans le[**Type de bordure**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)énumération.
- **Style de ligne** , le style de bordure, sélectionné dans le[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)énumération.
- **Couleur**, la couleur de ligne, sélectionnée dans l'énumération Couleur.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}

## **Couleurs et Palette**

Une palette est le nombre de couleurs disponibles pour la création d'une image. L'utilisation d'une palette standardisée dans une présentation permet à l'utilisateur de créer un look cohérent. Chaque fichier Excel Microsoft (97-2003) possède une palette de 56 couleurs pouvant être appliquées aux cellules, polices, quadrillages, objets graphiques, remplissages et lignes d'un graphique.

Avec Aspose.Cells, il est possible non seulement d'utiliser les couleurs existantes de la palette, mais également des couleurs personnalisées. Avant d'utiliser une couleur personnalisée, ajoutez-la d'abord à la palette.

Cette rubrique explique comment ajouter des couleurs personnalisées à la palette.

### **Ajout de couleurs personnalisées à la palette**

Aspose.Cells prend en charge la palette de 56 couleurs d'Excel Microsoft. Pour utiliser une couleur personnalisée qui n'est pas définie dans la palette, ajoutez la couleur à la palette.

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , qui représente un fichier Excel Microsoft. La[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe offre une[**ChangerPalette**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) méthode qui prend les paramètres suivants pour ajouter une couleur personnalisée pour modifier la palette :

- Couleur personnalisée, la couleur personnalisée à ajouter.
- Index, l'index de la couleur dans la palette que la couleur personnalisée remplacera. Doit être compris entre 0 et 55.

L'exemple ci-dessous ajoute une couleur personnalisée (Orchidée) à la palette avant de l'appliquer sur une police.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

La palette ne contient que 56 couleurs. Lorsque vous ajoutez une couleur personnalisée à la palette, la palette est modifiée et tout élément du fichier formaté avec la couleur précédente est modifié. Donc, lorsque vous changez de palette, soyez très prudent. De plus, il s'agit de la limitation du format de fichier XLS (Excel 97 - 2003) uniquement, car il n'y a pas de telle limitation pour XLSX ou d'autres formats de fichier MS Excel avancés (2007/2010 ou 2013).

{{% /alert %}}


