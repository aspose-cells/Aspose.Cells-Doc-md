---
title: Paramètres de remplissage
description: Aspose.Cells est une bibliothèque .NET pour travailler avec des fichiers de feuille de calcul. Il prend en charge le paramétrage des paramètres de remplissage des cellules, permettant aux utilisateurs de personnaliser l arrière plan et le style des cellules. Cet article présentera comment utiliser la bibliothèque Aspose.Cells pour définir les paramètres de remplissage des cellules.
keywords: Aspose.Cells, Cells, Paramètres de remplissage, Arrière plan, Style
type: docs
weight: 50
url: /fr/net/cells-fill-settings/
---

## **Couleurs et motifs d'arrière-plan**

Microsoft Excel peut définir les couleurs avant-plan (contour) et arrière-plan (remplissage) des cellules et les motifs d'arrière-plan.

Aspose.Cells prend également en charge ces fonctionnalités de manière flexible. Dans ce sujet, nous apprenons à utiliser ces fonctionnalités en utilisant Aspose.Cells.

### **Définition de couleurs et motifs d'arrière-plan**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Chaque élément de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

La classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) possède les méthodes [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) et [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) qui sont utilisées pour obtenir et définir la mise en forme d'une cellule. La classe [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) fournit des propriétés pour définir les couleurs avant-plan et arrière-plan des cellules. Aspose.Cells fournit une énumération [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype) qui contient un ensemble de types prédéfinis de motifs d'arrière-plan qui sont donnés ci-dessous.

|**Motifs d'arrière-plan**|**Description**|
| :- | :- |
|DiagonalCrosshatch|Représente le motif de quadrillage en diagonale|
|DiagonalStripe|Représente un motif de rayures diagonales|
|Gray6|Représente un motif de gris à 6,25%|
|Gray12|Représente un motif de gris à 12,5%|
|Gray25|Représente un motif de gris à 25%|
|Gray50|Représente un motif de gris à 50%|
|Gray75|Représente un motif de gris à 75%|
|HorizontalStripe|Représente un motif de rayures horizontales|
|None|Représente pas d'arrière-plan|
|ReverseDiagonalStripe|Représente un motif de rayures inversées diagonales|
|Solid|Représente un motif solide|
|ThickDiagonalCrosshatch|Représente un motif de quadrillage diagonal épais|
|ThinDiagonalCrosshatch|Représente un motif de quadrillage diagonal fin|
|ThinDiagonalStripe|Représente un motif de rayures diagonales fines|
|ThinHorizontalCrosshatch|Représente un motif de quadrillage horizontal fin|
|ThinHorizontalStripe|Représente un motif de rayures horizontales fines|
|ThinReverseDiagonalStripe|Représente un motif de rayures inversées diagonales fines|
|ThinVerticalStripe|Représente un motif de rayures verticales fines|
|VerticalStripe|Représente un motif de rayures verticales|

Dans l'exemple ci-dessous, la couleur de premier plan de la cellule A1 est définie, mais A2 est configurée pour avoir à la fois des couleurs de premier plan et d'arrière-plan avec un motif d'arrière-plan de rayures verticales.|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

### **Important à savoir**

{{% alert color="primary" %}}

- Pour définir la couleur d'avant-plan ou d'arrière-plan d'une cellule, utilisez les propriétés [**ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) ou [**BackgroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor) de l'objet [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style). Ces deux propriétés prendront effet seulement si la propriété [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) de l'objet [**Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) est configurée.
- La propriété [**ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) définit la couleur d'ombrage de la cellule.
  La propriété [**Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) spécifie le type de motif de fond utilisé pour la couleur d'avant-plan ou d'arrière-plan. Aspose.Cells fournit une énumération, [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype), qui contient un ensemble de types prédéfinis de motifs de fond.
- Si vous sélectionnez la valeur *BackgroundType.None* de l'énumération [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype), la couleur d'avant-plan n'est pas appliquée.
  De même, la couleur d'arrière-plan n'est pas appliquée si vous sélectionnez les valeurs *BackgroundType.None* ou *BackgroundType.Solid*.
- Lors de la récupération de la couleur d'ombrage/remplissage d'une cellule, si [**Style.Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) est *BackgroundType.None*, [**Style.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) renverra *Color.Empty*.

{{% /alert %}}

### **Application d'effets de remplissage dégradé**

Pour appliquer vos effets de remplissage dégradé souhaités à la cellule, utilisez la méthode [**SetTwoColorGradient**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient) de l'objet [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) en conséquence.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

## **Couleurs et palette**

Une palette est le nombre de couleurs disponibles pour créer une image. L'utilisation d'une palette normalisée dans une présentation permet à l'utilisateur de créer un aspect cohérent. Chaque fichier Microsoft Excel (97-2003) possède une palette de 56 couleurs qui peuvent être appliquées aux cellules, polices, quadrillages, objets graphiques, remplissages et lignes dans un graphique.

Avec Aspose.Cells, il est possible non seulement d'utiliser les couleurs existantes de la palette mais aussi des couleurs personnalisées. Avant d'utiliser une couleur personnalisée, ajoutez-la d'abord à la palette.

Ce sujet traite de l'ajout de couleurs personnalisées à la palette.

### **Ajout de couleurs personnalisées à la palette**

Aspose.Cells prend en charge la palette de 56 couleurs de Microsoft Excel. Pour utiliser une couleur personnalisée qui n'est pas définie dans la palette, ajoutez la couleur à la palette.

Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) fournit une méthode [**ChangePalette**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) qui prend les paramètres suivants pour ajouter une couleur personnalisée pour modifier la palette :

- Couleur personnalisée, la couleur personnalisée à ajouter.
- Index, l'index de la couleur dans la palette que la couleur personnalisée remplacera. Doit être compris entre 0 et 55.

L'exemple ci-dessous ajoute une couleur personnalisée (Orchid) à la palette avant de l'appliquer sur une police.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

La palette ne contient que 56 couleurs. Lorsque vous ajoutez une couleur personnalisée à la palette, la palette est modifiée et tout élément dans le fichier formaté avec la couleur précédente est modifié. Ainsi, lorsque vous modifiez la palette, veuillez être très prudent. De plus, il s'agit d'une limitation du format de fichier XLS (Excel 97 - 2003) uniquement car il n'y a pas de telle limitation pour les formats de fichier XLSX ou d'autres formats avancés de MS Excel (2007/2010 ou 2013).

{{% /alert %}}
