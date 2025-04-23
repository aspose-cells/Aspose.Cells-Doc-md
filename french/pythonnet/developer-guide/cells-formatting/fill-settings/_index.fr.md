---
title: Paramètres de remplissage
description: Aspose.Cells est une bibliothèque Python pour travailler avec des fichiers de feuilles de calcul. Elle supporte la définition des réglages de remplissage des cellules, permettant aux utilisateurs de personnaliser l arrière plan et le style des cellules. Cet article présente comment utiliser la bibliothèque Aspose.Cells pour Python via .NET pour définir les paramètres de remplissage des cellules.
keywords: Aspose.Cells pour Python via .NET, Cellules, Paramètres de remplissage, Arrière plan, Style
type: docs
weight: 50
url: /fr/python-net/cells-fill-settings/
---

## **Couleurs et motifs d'arrière-plan**

Microsoft Excel peut définir les couleurs avant-plan (contour) et arrière-plan (remplissage) des cellules et les motifs d'arrière-plan.

Aspose.Cells pour Python via .NET supporte également ces fonctionnalités de manière flexible. Dans ce sujet, nous apprenons à utiliser ces fonctionnalités avec Aspose.Cells.

### **Définition de couleurs et motifs d'arrière-plan**

Aspose.Cells pour Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) qui permet d’accéder à chaque feuille dans le fichier Excel. Une feuille est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Chaque élément de la collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

La méthode [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) et [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) permettent de récupérer et de définir la mise en forme d'une cellule. La classe [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) fournit des propriétés pour définir les couleurs de premier plan et d'arrière-plan des cellules. Aspose.Cells pour Python via .NET offre une énumération [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype) qui contient un ensemble de types de motifs de fond prédéfinis, listés ci-dessous.

|**Motifs d'arrière-plan**|**Description**|
| :- | :- |
|DIAGONAL_CROSSHATCH|Représente un motif de croisillons diagonaux|
|DIAGONAL_STRIPE|Représente un motif de rayures diagonales|
|GRAY6|Représente le motif de gris à 6,25%|
|GRAY12|Représente le motif de gris à 12,5%|
|GRAY25|Représente le motif de gris à 25%|
|GRAY50|Représente le motif de gris à 50%|
|GRAY75|Représente le motif de gris à 75%|
|HORIZONTAL_STRIPE|Représente le motif de rayures horizontales|
|NONE|Représente l'absence de fond|
|REVERSE_DIAGONAL_STRIPE|Représente le motif de rayures diagonales inversées|
|SOLID|Représente un motif plein|
|THICK_DIAGONAL_CROSSHATCH|Représente le motif de hachures croisées diagonales épaisses|
|THIN_DIAGONAL_CROSSHATCH|Représente le motif de hachures croisées diagonales fines|
|THIN_DIAGONAL_STRIPE|Représente le motif de rayures diagonales fines|
|THIN_HORIZONTAL_CROSSHATCH|Représente le motif de hachures horizontales fines|
|THIN_HORIZONTAL_STRIPE|Représente le motif de rayures horizontales fines|
|THIN_REVERSE_DIAGONAL_STRIPE|Représente le motif de rayures diagonales inversées fines|
|THIN_VERTICAL_STRIPE|Représente le motif de rayures verticales fines|
|VERTICAL_STRIPE|Représente le motif de rayures verticales|

Dans l'exemple ci-dessous, la couleur de premier plan de la cellule A1 est définie, mais A2 est configurée pour avoir à la fois des couleurs de premier plan et d'arrière-plan avec un motif d'arrière-plan de rayures verticales.|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ColorsAndBackground-1.py" >}}

### **Important à savoir**

{{% alert color="primary" %}}

- Pour définir la couleur d'avant-plan ou d'arrière-plan d'une cellule, utilisez les propriétés [**foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) ou [**background_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/background_color) de l'objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). Ces deux propriétés prendront effet seulement si la propriété [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) de l'objet [**pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) est configurée.
- La propriété [**foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) définit la couleur d'ombrage de la cellule.
  La propriété [**pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) spécifie le type de motif de fond utilisé pour la couleur de l'avant-plan ou de l'arrière-plan. Aspose.Cells pour Python via .NET fournit une énumération, [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype), qui contient un ensemble de types de motifs de fond prédéfinis.
- Si vous sélectionnez la valeur *BackgroundType.None* de l'énumération [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype), la couleur d'avant-plan n'est pas appliquée.
  De même, la couleur d'arrière-plan n'est pas appliquée si vous sélectionnez les valeurs *BackgroundType.None* ou *BackgroundType.Solid*.
- Lors de la récupération de la couleur d'ombrage/remplissage d'une cellule, si [**Style.pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) est *BackgroundType.None*, [**Style.foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) renverra *Color.Empty*.

{{% /alert %}}

### **Application d'effets de remplissage dégradé**

Pour appliquer vos effets de remplissage dégradé souhaités à la cellule, utilisez la méthode [**set_two_color_gradient**](https://reference.aspose.com/cells/python-net/aspose.cells/style/set_two_color_gradient) de l'objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) en conséquence.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApplyingGradientFillEffects-1.py" >}}

## **Couleurs et palette**

Une palette est le nombre de couleurs disponibles pour créer une image. L'utilisation d'une palette normalisée dans une présentation permet à l'utilisateur de créer un aspect cohérent. Chaque fichier Microsoft Excel (97-2003) possède une palette de 56 couleurs qui peuvent être appliquées aux cellules, polices, quadrillages, objets graphiques, remplissages et lignes dans un graphique.

Avec Aspose.Cells pour Python via .NET, il est possible non seulement d'utiliser les couleurs existantes de la palette, mais aussi des couleurs personnalisées. Avant d'utiliser une couleur personnalisée, ajoutez-la d'abord à la palette.

Ce sujet traite de l'ajout de couleurs personnalisées à la palette.

### **Ajout de couleurs personnalisées à la palette**

Aspose.Cells pour Python via .NET prend en charge la palette de 56 couleurs de Microsoft Excel. Pour utiliser une couleur personnalisée non définie dans la palette, ajoutez-la à la palette.

Aspose.Cells pour Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) fournit une méthode [**change_palette**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/change_palette) qui prend les paramètres suivants pour ajouter une couleur personnalisée afin de modifier la palette :

- Couleur personnalisée, la couleur personnalisée à ajouter.
- Index, l'index de la couleur dans la palette que la couleur personnalisée remplacera. Doit être compris entre 0 et 55.

L'exemple ci-dessous ajoute une couleur personnalisée (Orchid) à la palette avant de l'appliquer sur une police.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ColorsAndPalette-1.py" >}}

{{% alert color="primary" %}}

La palette ne contient que 56 couleurs. Lorsque vous ajoutez une couleur personnalisée à la palette, la palette est modifiée et tout élément dans le fichier formaté avec la couleur précédente est modifié. Ainsi, lorsque vous modifiez la palette, veuillez être très prudent. De plus, il s'agit d'une limitation du format de fichier XLS (Excel 97 - 2003) uniquement car il n'y a pas de telle limitation pour les formats de fichier XLSX ou d'autres formats avancés de MS Excel (2007/2010 ou 2013).

{{% /alert %}}

