---
title: Accéder à GridRow dans une feuille de calcul
type: docs
weight: 10
url: /fr/net/aspose-cells-gridweb/access-row-in-a-worksheet/
keywords: GridWeb,GridRow,obtenir la ligne
description: Cet article présente comment obtenir l objet de ligne (GridRow) dans la feuille de calcul dans GridWeb.
---
### Parcourir les lignes
**Meilleures pratiques**
si nous voulons accéder à toutes les lignes de la feuille de calcul une par une, nous pouvons utiliser des **itérateurs** pour parcourir les lignes existantes. cela **économisera de la mémoire**.
~~~C#

// Accéder à une ligne à l'aide des itérateurs
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   foreach (GridRow row in cells.Rows)
  {
      Console.WriteLine(row.Index+" "+row.Height);
   }
~~~
comparez le code ci-dessous, cela créera tous les objets de ligne, peu importe s'ils sont nuls, ce qui causera des problèmes de mémoire, donc s'il vous plaît **ne pas** utiliser cette méthode
~~~C#
 GridCells cells = GridWeb1.ActiveSheet.Cells;
 for(int r=0;r<=cells.MaxRow;r++)
 {
     GridRow row=cells.Rows[r];
     Console.WriteLine(row.Index+" "+row.Height);
 }
~~~
Cependant, vous pouvez utiliser la méthode CheckRow, pour vérifier si la ligne est vide
~~~C#
 GridCells cells = GridWeb1.ActiveSheet.Cells;
 for(int r=0;r<=cells.MaxRow;r++)
 {
     GridRow row=cells.CheckRow(r);
     if(row==null){
       Console.WriteLine("the row is empty:"+r);
     }else{
       Console.WriteLine(row.Index+" "+row.Height);
     }
 }
~~~
