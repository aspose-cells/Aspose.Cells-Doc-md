---
title: Application de styles sur Cells
type: docs
weight: 50
url: /fr/net/applying-styles-on-cells/
---
{{% alert color="primary" %}} 

Cette rubrique traite de l'application de styles sur les cellules, nous allons donc essayer de couvrir presque tout ce qui peut être utilisé pour appliquer un style sur une cellule. Outre certains paramètres de mise en forme de base, nous aborderons également en détail le dessin des bordures et la définition du format numérique des cellules.

{{% /alert %}} 
## **Application d'un style personnalisé sur un Cell - Un exemple**
Pour modifier la police et la couleur d'une cellule à l'aide de Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

-  Accédez à tout**Feuille de travail**
-  Accéder à un**Cell** sur lequel on veut appliquer une**Style**
-  Obtenir**Style** du**Cell**
-  Ensemble**Style** propriétés selon vos besoins personnalisés
-  Enfin, réglez**Style** du**Cell** avec la mise à jour

 Il existe de nombreuses propriétés et méthodes utiles offertes par**Style** objet qui peut être utilisé par les développeurs pour personnaliser le style en fonction de leurs besoins. Dans le code ci-dessous, il est démontré comment appliquer un style personnalisé sur la cellule.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-ApplyStyle.cs" >}}
## **Bordures de dessin de Cells**
 En utilisant**Style**objet, nous pouvons dessiner les bordures d'une cellule très facilement. Les bordures peuvent être dessinées dans n'importe quelle couleur. De plus, les développeurs ont également la possibilité de choisir un type de ligne spécifique qui sera utilisé pour tracer des bordures autour de la cellule. Les développeurs peuvent utiliser**SetBorderLine** et**Définir la couleur de la bordure** Méthodes de**Style** objet pour dessiner des bordures de tout type et couleurs. De même, pour obtenir des informations sur les frontières de n'importe quelle cellule, les développeurs peuvent également utiliser**GetBorderLine** et**GetBorderColor** Méthodes de**Style** objet.
### **Types de bordures**
Il existe six types de bordures pris en charge par Aspose.Cells.GridDesktop comme suit :

- **Gauche** , représente la bordure gauche
- **Droit** , représente la bordure droite
- **Haut** , représente la bordure supérieure
- **Fond** , représente la bordure inférieure
- **DiagonaleBas** , représente la bordure diagonale vers le bas
- **Diagonale vers le haut** , représente la bordure diagonale vers le haut
### **Types de lignes frontalières**
Une bordure est composée d'une ligne. Changer le type de ligne, change l'apparence d'une bordure. Il existe de nombreux types de lignes de bordure prises en charge par Aspose.Cells.GridDesktop, qui sont également répertoriés ci-dessous :

- **Aucun** , ne représente aucune frontière
- **Mince** , représente une bordure en trait plein
- **Moyen** , représente une bordure en trait plein avec une largeur de trait égale à 2f
- **Pointillé** , représente la bordure en pointillés
- **Pointé** , représente la bordure en pointillé
- **Épais** , représente une bordure en trait plein avec une largeur de trait égale à 3f
- **Pointillé moyen** , représente une bordure en pointillés avec une largeur de ligne égale à 2f
- **ThinDashDotted** , représente la bordure de la ligne pointillée en tiret
- **Tiret moyenpointillé** , représente une bordure en pointillés avec une largeur de ligne égale à 2f
- **ThinDashDotDotted** , représente le tiret point pointillé bordure
- **MoyenTraitPointPointillé** , représente une bordure en pointillé pointillé avec une largeur de ligne égale à 2f
## **Résumer tous ensemble - Exemple**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SummingUp.cs" >}}
## **Définition des formats de nombre**
Aspose.Cells.GridDesktop fournit également une fonction puissante de définition des formats numériques pour les valeurs entrées dans les cellules. Il existe 58 formats de nombres intégrés proposés par Aspose.Cells.GridDesktop. Pour voir une liste complète de tous les formats numériques pris en charge, veuillez consulter[Formats de nombre pris en charge.](/cells/fr/net/list-of-supported-number-formats/)

 Tous les formats numériques intégrés se voient attribuer un**Indice** Numéro.**Par exemple** le**Indice** nombre de**0.00E+00** le format numérique est**11** . Pour utiliser un format numérique intégré dans n'importe quelle cellule, les développeurs peuvent définir la propriété NumberFormat de**Style** s'opposer à la**Indice** nombre de ce format de nombre spécifique. Cependant, si les développeurs ont besoin d'avoir leur propre format de nombre personnalisé, ils peuvent également utiliser la propriété personnalisée de**Style** objet.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SetNumberFormat.cs" >}}
