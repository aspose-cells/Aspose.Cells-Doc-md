---
title: Accéder à GridRow dans une feuille de calcul
type: docs
weight: 10
url: /fr/net/aspose-cells-griddesktop/access-row-in-a-worksheet/
keywords: GridDesktop,GridRow,obtenir une ligne
description: Cet article présente comment obtenir l objet ligne (GridRow) dans la feuille de calcul dans GridDesktop.
---
### Parcourir les lignes
**Meilleures pratiques**
si nous voulons accéder à toutes les lignes de la feuille de calcul une par une, nous pouvons utiliser des **itérateurs** pour parcourir les lignes existantes. cela **économisera de la mémoire**.
~~~C#
   Worksheet sheet = gridDesktop1.GetActiveWorksheet();
// Accéder à une ligne à l'aide des itérateurs
   GridCells cells = sheet.Cells;
   foreach (GridRow row in cells.Rows)
  {
      Console.WriteLine(row.Index+" "+row.Height);
   }
~~~
comparez le code ci-dessous, cela créera tous les objets de ligne, peu importe s'ils sont nuls, ce qui causera des problèmes de mémoire, donc s'il vous plaît **ne pas** utiliser cette méthode
~~~C#
 Worksheet sheet = gridDesktop1.GetActiveWorksheet();
 GridCells cells = sheet.Cells;
 for(int r=0;r< sheet.RowsCount;r++)
 {
     GridRow row=cells.Rows[r];
     Console.WriteLine(row.Index+" "+row.Height);
 }
~~~
Cependant, vous pouvez utiliser la méthode CheckRow, pour vérifier si la ligne est vide
~~~C#
 Worksheet sheet = gridDesktop1.GetActiveWorksheet();
 GridCells cells = sheet.Cells;
 for(int r=0;r< sheet.RowsCount;r++)
 {
     GridRow row=cells.CheckRow(r);
     if(row==null){
       Console.WriteLine("the row is empty:"+r);
     }else{
       Console.WriteLine(row.Index+" "+row.Height);
     }
 }
~~~
