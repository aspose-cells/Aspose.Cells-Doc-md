---  
title: Paramètres de remplissage
linktitle: Paramètres de remplissage  
description: Apprenez à personnaliser les paramètres de remplissage, l arrière plan et le style des cellules en utilisant la bibliothèque Aspose.Cells pour Node.js via C++.  
keywords: Aspose.Cells, Cellules, Paramètres de remplissage, Arrière plan, Style, Node.js via C++  
type: docs  
weight: 50  
url: /fr/nodejs-cpp/cells-fill-settings/  
---  

## **Couleurs et motifs d'arrière-plan**  

Microsoft Excel peut définir les couleurs avant-plan (contour) et arrière-plan (remplissage) des cellules et les motifs d'arrière-plan.  

Aspose.Cells prend également en charge ces fonctionnalités de manière flexible. Dans ce sujet, nous apprenons à utiliser ces fonctionnalités en utilisant Aspose.Cells.  

### **Définition de couleurs et motifs d'arrière-plan**  

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Chaque élément de la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).  

La classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) possède les méthodes [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) et [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) utilisées pour obtenir et définir la mise en forme d'une cellule. La classe [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) fournit des propriétés pour définir les couleurs de premier plan et d'arrière-plan des cellules. Aspose.Cells propose une énumération [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype) contenant un ensemble de types de motifs de fond prédéfinis, ci-dessous.  

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

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-SetColorsAndBackgroundPatterns.js" >}}


### **Important à savoir**  

{{% alert color="primary" %}}  

- Pour définir la couleur de premier plan ou d'arrière-plan d'une cellule, utilisez la méthode [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) de l'objet [**setForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundColor-color-) ou [**setBackgroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setBackgroundColor-color-). Les deux méthodes n'auront d'effet que si la propriété [**Pattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-) de l'objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) est configurée.  
- La méthode [**setForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundColor-color-) définit la couleur de nuance de la cellule.  
  La méthode [**setPattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-) précise le type de motif d'arrière-plan utilisé pour la couleur de premier plan ou d'arrière-plan. Aspose.Cells fournit une énumération [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype) contenant une liste de types de motifs d'arrière-plan prédéfinis.  
- Si vous sélectionnez la valeur *BackgroundType.None* dans l'énumération [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype), la couleur de premier plan n'est pas appliquée.  
  De même, la couleur d'arrière-plan n'est pas appliquée si vous sélectionnez les valeurs *BackgroundType.None* ou *BackgroundType.Solid*.  
- Lors de la récupération de la couleur d'ombrage/remplissage d'une cellule, si [**Style.setPattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-) est *BackgroundType.None*, [**Style.getForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#getForegroundColor--) renverra *Color.Empty*.  

{{% /alert %}}  

### **Application d'effets de remplissage dégradé**  

Pour appliquer vos effets de dégradé de remplissage souhaités à la cellule, utilisez la méthode [**setTwoColorGradient**](https://reference.aspose.com/cells/nodejs-cpp/style/#setTwoColorGradient-color-color-gradientstyletype-number-) de l'objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) en conséquence.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-ApplyGradientFillEffects.js" >}}


## **Couleurs et palette**  

Une palette est le nombre de couleurs disponibles pour créer une image. L'utilisation d'une palette normalisée dans une présentation permet à l'utilisateur de créer un aspect cohérent. Chaque fichier Microsoft Excel (97-2003) possède une palette de 56 couleurs qui peuvent être appliquées aux cellules, polices, quadrillages, objets graphiques, remplissages et lignes dans un graphique.  

Avec Aspose.Cells, il est possible non seulement d'utiliser les couleurs existantes de la palette mais aussi des couleurs personnalisées. Avant d'utiliser une couleur personnalisée, ajoutez-la d'abord à la palette.  

Ce sujet traite de l'ajout de couleurs personnalisées à la palette.  

### **Ajout de couleurs personnalisées à la palette**  

Aspose.Cells prend en charge la palette de 56 couleurs de Microsoft Excel. Pour utiliser une couleur personnalisée qui n'est pas définie dans la palette, ajoutez la couleur à la palette.  

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) fournit une méthode [**changePalette**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#changePalette-color-number-) qui prend les paramètres suivants pour ajouter une couleur personnalisée afin de modifier la palette :  

- Couleur personnalisée, la couleur personnalisée à ajouter.  
- Index, l'index de la couleur dans la palette que la couleur personnalisée remplacera. Doit être compris entre 0 et 55.  

L'exemple ci-dessous ajoute une couleur personnalisée (Orchid) à la palette avant de l'appliquer sur une police.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-AddCustomColorsToPalette.js" >}}


{{% alert color="primary" %}}  

La palette ne contient que 56 couleurs. Lorsque vous ajoutez une couleur personnalisée à la palette, la palette est modifiée et tout élément dans le fichier formaté avec la couleur précédente est modifié. Ainsi, lorsque vous modifiez la palette, veuillez être très prudent. De plus, il s'agit d'une limitation du format de fichier XLS (Excel 97 - 2003) uniquement car il n'y a pas de telle limitation pour les formats de fichier XLSX ou d'autres formats avancés de MS Excel (2007/2010 ou 2013).  

{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
