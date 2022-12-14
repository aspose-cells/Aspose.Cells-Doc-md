---
title: Accéder à la feuille de travail Cells
type: docs
weight: 10
url: /fr/net/access-worksheet-cells/
---
{{% alert color="primary" %}} 

Cette rubrique traite des cellules, en examinant la fonctionnalité la plus élémentaire de Aspose.Cells.GridWeb : l'accès aux cellules.

{{% /alert %}} 
## **Accéder à Cells dans une feuille de calcul**
Chaque feuille de calcul contient une propriété du nom de Cells qui est en fait une collection d'objets GridCell où un objet GridCell représente une cellule dans Aspose.Cells.GridWeb. Il est possible d'accéder à n'importe quelle cellule en utilisant Aspose.Cells.GridWeb. Il existe deux méthodes préférées, dont chacune est décrite ci-dessous.


### **Utilisation du nom Cell**
Toutes les cellules ont un nom unique. Par exemple, A1, A2, B1, B2 etc. Aspose.Cells.GridWeb permet aux développeurs d'accéder à n'importe quelle cellule souhaitée en utilisant le nom de la cellule. Transmettez simplement le nom de la cellule (en tant qu'index) à la collection Cells de GridWorksheet.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByName.cs" >}}


### **Utilisation des indices de ligne et de colonne**
Une cellule peut également être reconnue par son emplacement en termes d'indices de ligne et de colonne. Passez simplement les indices de ligne et de colonne d'une cellule à la collection Cells de GridWorksheet. Cette approche est plus rapide que la précédente.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByRowColumnIndex.cs" >}}
