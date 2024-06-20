---
title: Appliquer un style sur une cellule
type: docs
weight: 50
url: /fr/net/aspose-cells-griddesktop/apply-style-on-cell/
keywords: GridDesktop, format, style, formats de nombre, format de nombre, NumberFormat
description: Cet article présente comment obtenir ou définir le format de style dans la cellule de la feuille de calcul de GridDesktop.
---

{{% alert color="primary" %}} 

Ce sujet traite de l'application d'un format de style sur une cellule, nous couvrirons presque toutes les propriétés associées qui peuvent être utilisées pour appliquer un style sur une cellule. En plus de certains paramètres de base de mise en forme, nous discuterons également de la définition de bordures et du paramétrage du format de nombre sur la cellule en détail.

{{% /alert %}} 
## **Appliquer un style personnalisé sur une cellule - Un exemple**
Pour changer la police et la couleur d'une cellule avec Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

- Accédez à n'importe quelle **Worksheet** souhaitée
- Accéder à une **Cellule** sur laquelle nous voulons appliquer un **Style**
- Obtenir le **Style** de la **Cellule**
- Définir les propriétés du **Style** selon vos besoins personnalisés
- Enfin, définissez le **Style** de la **Cellule** avec celui mis à jour

Il existe de nombreuses propriétés et méthodes utiles offertes par l'objet **Style** qui peuvent être utilisées par les développeurs pour personnaliser le style selon leurs besoins. Dans le code ci-dessous, il est démontré comment appliquer un style personnalisé à une cellule.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-ApplyStyle.cs" >}}
## **Dessiner les bordures des cellules**
En utilisant l'objet **Style**, nous pouvons dessiner facilement les bordures d'une cellule. Les bordures peuvent être dessinées dans n'importe quelle couleur. De plus, les développeurs ont également la flexibilité de choisir un type de ligne spécifique qui sera utilisé pour dessiner les bordures autour de la cellule. Les développeurs peuvent utiliser les méthodes **SetBorderLine** et **SetBorderColor** de l'objet **Style** pour dessiner des bordures de différents types et couleurs. De même, pour obtenir des informations sur les bordures d'une cellule, les développeurs peuvent également utiliser les méthodes **GetBorderLine** et **GetBorderColor** de l'objet **Style**.
### **Types de bordures**
Il existe six types de bordures pris en charge par Aspose.Cells.GridDesktop comme suit :

- **Gauche** , représente la bordure gauche
- **Droite** , représente la bordure droite
- **Haut** , représente la bordure supérieure
- **Bas** , représente la bordure inférieure
- **DiagonaleBas** , représente la bordure diagonale descendante
- **DiagonaleHaut** , représente la bordure diagonale ascendante
### **Types de lignes de bordure**
Une bordure est composée d'une ligne. Changer le type de ligne change l'apparence d'une bordure. Aspose.Cells.GridDesktop prend en charge de nombreux types de lignes de bordure, qui sont également répertoriés ci-dessous :

- **Aucune** , représente aucune bordure
- **Fine** , représente une bordure à ligne pleine
- **Moyenne** , représente une bordure à ligne pleine avec une largeur de ligne égale à 2f
- **Pointillée** , représente une bordure à ligne pointillée
- **En traits** , représente une bordure à ligne en tirets
- **Épaisse** , représente une bordure à ligne pleine avec une largeur de ligne égale à 3f
- **MediumDashed** , représente une bordure en pointillés de ligne avec une largeur de ligne égale à 2f
- **ThinDashDotted** , représente une bordure en pointillés tiretés
- **MediumDashDotted** , représente une bordure en pointillés tiretés avec une largeur de ligne égale à 2f
- **ThinDashDotDotted** , représente une bordure en pointillés, tiretés et pointillés
- **MediumDashDotDotted** , représente une bordure en pointillés, tiretés et pointillés avec une largeur de ligne égale à 2f
## **Résumant tout ensemble - Exemple**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SummingUp.cs" >}}
## **Réglage des formats de nombre**
Aspose.Cells.GridDesktop fournit également des paramètres de formats de nombre. Il existe 58 formats de nombre intégrés offerts par Aspose.Cells.GridDesktop. Pour voir une liste complète de tous les formats de nombre pris en charge, veuillez vous référer à [Formats de nombre pris en charge.](/cells/fr/net/list-of-supported-number-formats/)

Tous les formats de nombre intégrés se voient attribuer un numéro **d'index**. **Par exemple**, le numéro **d'index** du format de nombre **0.00E+00** est **11** . Pour utiliser un format de nombre intégré dans n'importe quelle cellule, les développeurs peuvent définir la propriété NumberFormat de l'objet **Style** sur le numéro **d'index** de ce format de nombre spécifique. Cependant, si les développeurs ont besoin de leur propre format de nombre personnalisé, ils peuvent également utiliser la propriété Custom de l'objet **Style**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SetNumberFormat.cs" >}}
