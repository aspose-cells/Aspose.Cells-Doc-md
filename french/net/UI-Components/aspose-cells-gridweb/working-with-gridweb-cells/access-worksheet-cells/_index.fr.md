---
title: Accéder à la cellule de feuille de calcul
type: docs
weight: 10
url: /fr/net/aspose-cells-gridweb/access-worksheet-cell/
keywords: GridWeb,cell,GridCell
description: Cet article présente comment obtenir la cellule (GridCell) dans GridWeb.
---

{{% alert color="primary" %}} 

Ce sujet aborde les cellules, en examinant la fonction la plus élémentaire d'Aspose.Cells.GridWeb : l'accès aux cellules.

{{% /alert %}} 
## **Accéder aux cellules dans une feuille de calcul**
Chaque feuille de calcul contient une propriété portant le nom de Cells qui est en fait une collection d'objets GridCell où un objet GridCell représente une cellule dans Aspose.Cells.GridWeb. Il est possible d'accéder à n'importe quelle cellule en utilisant Aspose.Cells.GridWeb. Il existe deux méthodes préférées, dont chacune est discutée ci-dessous.


### **Utilisation du nom de la cellule**
Toutes les cellules ont un nom unique. Par exemple, A1, A2, B1, B2, etc. Aspose.Cells.GridWeb permet aux développeurs d'accéder à n'importe quelle cellule désirée en utilisant le nom de la cellule. Il suffit de passer le nom de la cellule (en tant qu'index) à la collection Cells de GridWorksheet.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByName.cs" >}}


**Remarque**

Accéder à la grilleCell en utilisant cells[cellName] peut consommer plus de mémoire. Cela créera toujours un nouvel objet de cellule (GridCell) peu importe si la cellule est nulle ou non.


### **Utilisation des Indices de Ligne & Colonne**


Une cellule peut également être reconnue par son emplacement en termes d'indices de ligne et de colonne. Il suffit de passer les indices de ligne et de colonne d'une cellule à la collection Cells de GridWorksheet. Cette approche est plus rapide que la précédente.

**Meilleures pratiques**

Si nous voulons obtenir la valeur de la cellule ou le style de la cellule et que nous ne voulons pas effectuer l'opération de mise à jour, nous pouvons utiliser la méthode **CheckCell** qui renverra null si la cellule n'existe pas. Cela **économisera la mémoire**.
~~~C#
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   GridCell cell = cells.CheckCell(1, 1);
   if(cell!=null)
   {
    Console.WriteLine(cell.ToString());
   }
~~~


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByRowColumnIndex.cs" >}}



**Meilleures pratiques**
### Parcourir les cellules
si nous voulons accéder à toutes les cellules de la feuille de calcul une par une, nous pouvons utiliser des **itérateurs** pour parcourir les cellules existantes. cela **économisera la mémoire**.
~~~C#
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   foreach (GridCell c in cells)
  {
      Console.WriteLine(c.ToString());
   }
~~~
comparez le code ci-dessous qui est **mauvais**, cela créera tous les objets de cellules même s'il est nul, ce qui causera des problèmes de mémoire, donc veuillez **ne pas** utiliser cette méthode
~~~C#
 GridCells cells = GridWeb1.ActiveSheet.Cells;
 for(int r=0;r< cells.MaxRow;r++)
 {
     for(int c=0;c< cells.MaxColumn; c++)
     {
         Console.WriteLine(cells[r,c].ToString());
     }
 }
~~~
