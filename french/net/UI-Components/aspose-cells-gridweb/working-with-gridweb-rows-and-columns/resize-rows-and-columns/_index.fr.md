---
title: Redimensionner les lignes et les colonnes
type: docs
weight: 30
url: /fr/net/resize-rows-and-columns/
---
{{% alert color="primary" %}} 

Parfois, les valeurs des cellules sont plus larges que la cellule dans laquelle elles se trouvent ou se trouvent sur plusieurs lignes. Ces valeurs ne sont pas entièrement visibles pour les utilisateurs, sauf si elles modifient la hauteur et la largeur des lignes et des colonnes. Aspose.Cells.GridWeb prend entièrement en charge la définition des hauteurs de ligne et de la largeur de colonne. Cette rubrique décrit ces fonctionnalités en détail à l'aide d'exemples.

{{% /alert %}} 
## **Travailler avec les hauteurs de ligne et la largeur de colonne**
### **Définition de la hauteur de ligne**
Pour définir la hauteur d'une ligne :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à votre formulaire Web.
1. Accédez à la collection Cells de la feuille de calcul.
1. Définissez la hauteur de toutes les cellules dans n'importe quelle ligne spécifiée.

{{% alert color="primary" %}} 

Les méthodes SetRowHeight et SetColumnWidth de la collection Cells proposent également des variantes pour définir les mesures de hauteur de ligne et de largeur de colonne en pouces et en pixels.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetRowHeight.cs" >}}
### **Définition de la largeur de colonne**
Pour définir la largeur d'une colonne :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à votre formulaire Web.
1. Accédez à la collection Cells de la feuille de calcul.
1. Définissez la largeur de toutes les cellules dans une colonne spécifiée.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetColumnWidth.cs" >}}
