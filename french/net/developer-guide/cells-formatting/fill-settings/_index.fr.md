---
title: Paramètres de remplissage
type: docs
weight: 50
url: /fr/net/cells-fill-settings/
---
## **Couleurs et motifs de fond**

Microsoft Excel peut définir les couleurs de premier plan (contour) et d'arrière-plan (remplissage) des cellules et des motifs d'arrière-plan.

Aspose.Cells prend également en charge ces fonctionnalités de manière flexible. Dans cette rubrique, nous apprenons à utiliser ces fonctionnalités en utilisant Aspose.Cells.

### **Définition des couleurs et des motifs d'arrière-plan**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Excel Microsoft. La[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer. La[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe offre une[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) le recueil. Chaque élément de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection représente un objet de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classer.

 La[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) a la[**ObtenirStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) et[**DéfinirStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) méthodes utilisées pour obtenir et définir la mise en forme d'une cellule. La[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)fournit des propriétés pour définir les couleurs de premier plan et d'arrière-plan des cellules. Aspose.Cells fournit un[**Type d'arrière-plan**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)énumération qui contient un ensemble de types prédéfinis de motifs d'arrière-plan qui sont donnés ci-dessous.

|**Motifs de fond**|**La description**|
|:- |:- |
|DiagonaleHachure|Représente le motif hachuré en diagonale|
|Bande diagonale|Représente le motif à rayures diagonales|
|Gris6|Représente un motif gris de 6,25 %|
|Gris12|Représente un motif gris de 12,5 %|
|Gris25|Représente 25 % de motif gris|
|Gris50|Représente un motif gris à 50 %|
|Gris75|Représente un motif gris à 75 %|
|Bande horizontale|Représente le motif de rayures horizontales|
|Aucun|Ne représente aucun arrière-plan|
|Bande diagonale inversée|Représente le motif à rayures diagonales inversées|
|Solide|Représente un motif solide|
|ÉpaisDiagonalCrosshatch|Représente un motif hachuré diagonal épais|
|MinceDiagonalCrosshatch|Représente un motif de hachures diagonales minces|
|Fine bande diagonale|Représente un motif à fines rayures diagonales|
|ThinHorizontalCrosshatch|Représente un motif hachuré horizontal fin|
|Fines rayures horizontales|Représente un motif de fines rayures horizontales|
|ThinReverseDiagonalStripe|Représente un motif à fines rayures diagonales inversées|
|ThinVerticalStripe|Représente un motif de fines rayures verticales|
|Bande verticale|Représente le motif de rayures verticales|

Dans l'exemple ci-dessous, la couleur de premier plan de la cellule A1 est définie, mais A2 est configuré pour avoir à la fois des couleurs de premier plan et d'arrière-plan avec un motif d'arrière-plan à rayures verticales.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

### **Important à savoir**

{{% alert color="primary" %}}

-  Pour définir la couleur de premier plan ou d'arrière-plan d'une cellule, utilisez la[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objets[**Couleur de premier plan**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) ou[**Couleur de l'arrière plan**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor) Propriétés. Les deux propriétés ne prendront effet que si le[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objets[**Motif**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)propriété est configurée.
-  La[**Couleur de premier plan**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)La propriété définit la couleur de nuance de la cellule.
 La[**Motif**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)La propriété spécifie le type de motif d'arrière-plan utilisé pour la couleur de premier plan ou d'arrière-plan. Aspose.Cells fournit une énumération,[**Type d'arrière-plan**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)qui contient un ensemble de types prédéfinis de motifs d'arrière-plan.
-  Si vous sélectionnez*BackgroundType.None* valeur de la[**Type d'arrière-plan**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)énumération, la couleur de premier plan n'est pas appliquée.
 De même, la couleur d'arrière-plan n'est pas appliquée si vous sélectionnez le*BackgroundType.None* ou*BackgroundType.Solid* valeurs.
-  Lors de la récupération de la couleur d'ombrage/de remplissage de la cellule, si[**Style.Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) est*BackgroundType.None*, [**Style.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) reviendra*Couleur.Vide*.

{{% /alert %}}

### **Application d'effets de remplissage dégradé**

 Pour appliquer les effets de remplissage dégradé souhaités à la cellule, utilisez le[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objets[**SetTwoColorGradient**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient)méthode en conséquence.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

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
