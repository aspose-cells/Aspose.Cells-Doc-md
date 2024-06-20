---
title: Accéder à GridCell dans une feuille de calcul
type: docs
weight: 10
url: /fr/net/aspose-cells-griddesktop/access-cell-in-a-worksheet/
keywords: GridDesktop,GridCell,get cell
description: Cet article présente comment obtenir l objet cellule (GridCell) dans la feuille de calcul de GridDesktop.
---

{{% alert color="primary" %}} 

Nous avons discuté jusqu'à présent du travail avec des feuilles de calcul, des lignes et des colonnes, mais il est maintenant temps d'approfondir davantage et de parler des cellules. Donc, dans ce sujet, nous commencerions notre discussion sur les cellules avec une fonctionnalité de base d'accès aux cellules.

{{% /alert %}} 
## **Accéder à une cellule dans une feuille de calcul**
Nous pouvons accéder à n'importe quelle cellule d'une feuille de calcul en utilisant l'API de Aspose.Cells.GridDesktop. Il pourrait y avoir trois façons possibles d'accéder à une cellule comme suit :

- **Utilisation du nom de la cellule**
- **Utilisation des indices de ligne et de colonne**
- **Obtention de la cellule focus**

Discutons de toutes les trois approches ci-dessus une par une.
### **Utilisation du nom de la cellule**
Toutes les cellules d'une feuille de calcul ont un nom unique. Par exemple, A1, A2, B1, B2 etc. Aspose.Cells.GridDesktop permet aux développeurs d'accéder à n'importe quelle cellule désirée en utilisant son nom de cellule. Il suffit de passer le nom de la cellule (en tant qu'index) à la collection **Cells** de la **Worksheet**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByName.cs" >}}

**Remarque**

Accéder à la grilleCell en utilisant cells[cellName] peut consommer plus de mémoire. Cela créera toujours un nouvel objet de cellule (GridCell) peu importe si la cellule est nulle ou non.

### **Utilisation des indices de ligne et de colonne de la cellule**

**Meilleures pratiques**

Si nous voulons obtenir la valeur de la cellule ou le style de la cellule et que nous ne voulons pas effectuer l'opération de mise à jour, nous pouvons utiliser la méthode **CheckCell** qui renverra null si la cellule n'existe pas. Cela **économisera la mémoire**.
~~~C#
Worksheet sheet = gridDesktop1.GetActiveWorksheet();
// Accéder à une cellule en utilisant ses indices de ligne et de colonne
GridCell cell = sheet.Cells.CheckCell(1, 1);
   if(cell!=null)
   {
    Console.WriteLine(cell.ToString());
   }
~~~

Une cellule dans une feuille de calcul peut également être reconnue en utilisant son emplacement en termes de ses indices de ligne et de colonne. Il suffit de passer les indices de ligne et de colonne de la cellule à la collection **Cells** de la **Worksheet**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByIndices.cs" >}}

**Remarque**

Accéder à la grilleCell en utilisant cells[rowIndex, columnIndex] peut consommer plus de mémoire. Cela créera toujours un nouvel objet de cellule (GridCell) peu importe si la cellule est nulle ou non.


### **Obtenir la cellule focalisée**
Si vous ne savez pas précisément quelle cellule doit être accédée. Alors Aspose.Cells.GridDesktop vous permet également d'accéder à une cellule qui est actuellement au centre de l'attention de l'utilisateur. En utilisant cette fonctionnalité, vous pouvez permettre à un utilisateur de sélectionner n'importe quelle cellule, puis vous pouvez accéder à cette cellule en arrière-plan. Cela peut simplement être réalisé en utilisant la méthode **GetFocusedCell** de la **FeuilleDeCalcul**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessFocusedCell.cs" >}}

**Meilleures pratiques**
### Parcourir les cellules
si nous voulons accéder à toutes les cellules de la feuille de calcul une par une, nous pouvons utiliser des **itérateurs** pour parcourir les cellules existantes. cela **économisera la mémoire**.
~~~C#
   Worksheet sheet = gridDesktop1.GetActiveWorksheet();

   GridCells cells = sheet.Cells;
   foreach (GridCell c in cells)
  {
      Console.WriteLine(c.ToString());
   }
~~~
comparez le code ci-dessous qui est **mauvais**, cela créera tous les objets de cellules même s'il est nul, ce qui causera des problèmes de mémoire, donc veuillez **ne pas** utiliser cette méthode
~~~C#
 Worksheet sheet = gridDesktop1.GetActiveWorksheet();
 for(int r=0;r< sheet.RowsCount;r++)
 {
     for(int c=0;c< sheet.ColumnsCount; c++)
     {
         Console.WriteLine(sheet.Cells[r,c].ToString());
     }
 }
~~~

