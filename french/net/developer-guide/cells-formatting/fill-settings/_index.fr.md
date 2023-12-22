---
title: Paramètres de remplissage
description: Aspose.Cells est une bibliothèque .NET permettant de travailler avec des feuilles de calcul. Il prend en charge la définition des paramètres de remplissage des cellules, permettant aux utilisateurs de personnaliser l'arrière-plan et le style des cellules. Cet article explique comment utiliser la bibliothèque Aspose.Cells pour définir les paramètres de remplissage des cellules.
keywords: Aspose.Cells, Cells, Fill Settings, Background, Style
type: docs
weight: 50
url: /fr/net/cells-fill-settings/
---
##  **Couleurs et motifs de fond**

Microsoft Excel peut définir les couleurs de premier plan (contour) et d'arrière-plan (remplissage) des cellules et des motifs d'arrière-plan.

Aspose.Cells prend également en charge ces fonctionnalités de manière flexible. Dans cette rubrique, nous apprenons à utiliser ces fonctionnalités à l'aide du Aspose.Cells.

###  **Définition des couleurs et des motifs d'arrière-plan**

 Aspose.Cells propose un cours,[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Excel Microsoft. Le[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection qui permet d’accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fournit un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection. Chaque élément du[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) la collection représente un objet de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe.

 Le[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) a la[**ObtenirStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) et[**Définir le style**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) méthodes utilisées pour obtenir et définir le formatage d’une cellule. Le[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)La classe fournit des propriétés permettant de définir les couleurs de premier plan et d’arrière-plan des cellules. Aspose.Cells fournit un[**Type d'arrière-plan**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)énumération qui contient un ensemble de types prédéfinis de modèles d’arrière-plan qui sont donnés ci-dessous.

|**Motifs de fond**|**Description**|
| :- | :- |
|DiagonaleCrosshatch|Représente un motif hachuré en diagonale|
|Bande Diagonale|Représente un motif à rayures diagonales|
|Gris6|Représente 6,25 % de motif gris|
|Gris12|Représente 12,5% de motif gris|
|Gris25|Représente 25 % de motif gris|
|Gris50|Représente 50 % de motif gris|
|Gris75|Représente 75% de motif gris|
|Bande horizontale|Représente un motif à rayures horizontales|
|Aucun|Ne représente aucun arrière-plan|
|BandeDiagonale Inversée|Représente un motif de rayures diagonales inversées|
|Solide|Représente un motif solide|
|ÉpaisDiagonalCrosshatch|Représente un motif hachuré diagonal épais|
|MinceDiagonaleCrosshatch|Représente un fin motif hachuré en diagonale|
|ThinDiagonalStripe|Représente un motif à fines rayures diagonales|
|MinceHorizontalCrosshatch|Représente un fin motif de hachures horizontales|
|MinceHorizontalStripe|Représente un motif à fines rayures horizontales|
|ThinReverseDiagonalStripe|Représente un motif à fines rayures diagonales inversées.|
|MinceVerticalStripe|Représente un motif à fines rayures verticales|
|Bande verticale|Représente un motif à rayures verticales|

Dans l'exemple ci-dessous, la couleur de premier plan de la cellule A1 est définie mais A2 est configurée pour avoir à la fois des couleurs de premier plan et d'arrière-plan avec un motif d'arrière-plan à rayures verticales.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

###  **Important à savoir**

{{% alert color="primary" %}}

-  Pour définir la couleur de premier plan ou d'arrière-plan d'une cellule, utilisez l'option[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objets[**Couleur de premier plan**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) ou[**Couleur de l'arrière plan**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor) propriétés. Les deux propriétés ne prendront effet que si le[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objets[**Modèle**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)la propriété est configurée.
-  Le[**Couleur de premier plan**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)La propriété définit la couleur de nuance de la cellule.
 Le[**Modèle**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)La propriété spécifie le type de motif d'arrière-plan utilisé pour la couleur de premier plan ou d'arrière-plan. Aspose.Cells fournit une énumération,[**Type d'arrière-plan**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype). qui contient un ensemble de types prédéfinis de motifs d'arrière-plan.
-  Si vous sélectionnez*Type d'arrière-plan. Aucun* valeur de la[**Type d'arrière-plan**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)énumération, la couleur de premier plan n’est pas appliquée.
 De même, la couleur d'arrière-plan n'est pas appliquée si vous sélectionnez l'option*Type d'arrière-plan. Aucun* ou*Type d'arrière-plan.Solid* valeurs.
-  Lors de la récupération de la couleur d'ombrage/de remplissage de la cellule, si[**Style.Motif**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) est *BackgroundType.None*,[**Style.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) renverra *Color.Empty*.

{{% /alert %}}

###  **Application d'effets de remplissage dégradé**

 Pour appliquer les effets de remplissage dégradé souhaités à la cellule, utilisez le[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objets[**DéfinirTwoColorGradient**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient)méthode en conséquence.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

##  **Couleurs et palette**

Une palette est le nombre de couleurs disponibles pour créer une image. L'utilisation d'une palette standardisée dans une présentation permet à l'utilisateur de créer une apparence cohérente. Chaque fichier Excel Microsoft (97-2003) possède une palette de 56 couleurs qui peuvent être appliquées aux cellules, polices, quadrillages, objets graphiques, remplissages et lignes d'un graphique.

Avec le Aspose.Cells, il est possible d'utiliser non seulement les couleurs existantes de la palette mais aussi des couleurs personnalisées. Avant d'utiliser une couleur personnalisée, ajoutez-la d'abord à la palette.

Cette rubrique explique comment ajouter des couleurs personnalisées à la palette.

###  **Ajout de couleurs personnalisées à la palette**

Aspose.Cells prend en charge la palette de 56 couleurs d'Excel Microsoft. Pour utiliser une couleur personnalisée qui n'est pas définie dans la palette, ajoutez la couleur à la palette.

 Aspose.Cells propose un cours,[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , cela représente un fichier Excel Microsoft. Le[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe fournit un[**Changer la palette**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) méthode qui prend les paramètres suivants pour ajouter une couleur personnalisée afin de modifier la palette :

- Couleur personnalisée, la couleur personnalisée à ajouter.
- Index, l'index de la couleur dans la palette que la couleur personnalisée remplacera. Doit être compris entre 0 et 55.

L'exemple ci-dessous ajoute une couleur personnalisée (Orchidée) à la palette avant de l'appliquer sur une police.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

La palette ne contient que 56 couleurs. Lorsque vous ajoutez une couleur personnalisée à la palette, la palette est modifiée et tout élément du fichier formaté avec la couleur précédente est modifié. Donc, lorsque vous changez de palette, soyez très prudent. De plus, il s'agit de la limitation du format de fichier XLS (Excel 97 - 2003) uniquement, car il n'existe pas de limitation de ce type pour XLSX ou d'autres formats de fichiers MS Excel avancés (2007/2010 ou 2013).

{{% /alert %}}
