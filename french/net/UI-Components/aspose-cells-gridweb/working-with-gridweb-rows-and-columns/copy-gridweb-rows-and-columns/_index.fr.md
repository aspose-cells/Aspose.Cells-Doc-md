---
title: Copier les lignes et les colonnes de GridWeb
type: docs
weight: 80
url: /fr/net/copy-gridweb-rows-and-columns/
---
{{% alert color="primary" %}} 

 Le composant Aspose.Cells.GridWeb offre le moyen de copier une ligne et une colonne tout en utilisant la classe GridCells. Cet article illustre l'utilisation des API exposées par le Aspose.Cells.GridWeb pour copier des lignes et des colonnes sur l'interface GridWeb.

Les méthodes GridCells.CopyRow, GridCells.CopyColumn, GridCells.CopyRows et GridCells.CopyColumns copient le contenu, le style et les formules de la ligne et de la colonne source vers la destination.

{{% /alert %}} 
## **Copier des lignes et des colonnes**
 Si vous ne connaissez pas déjà le composant Aspose.Cells.GridWeb, nous vous suggérons fortement de vérifier le[Présentation de Aspose.Cells.GridWeb](https://docs.aspose.com/cells/net/browsers-capabilities/) et article détaillé sur[Comment ajouter le composant Aspose.Cells.GridWeb dans une application WebForms](https://docs.aspose.com/cells/net/add-gridweb-to-web-form/).
### **Copie d'une seule ligne**
Afin de garder l'exemple simple, l'article utilise une feuille de calcul existante avec une ligne et une formule simple qui additionne toutes les valeurs de la ligne. Voici comment la feuille de calcul est affichée dans l'interface Aspose.Cells.GridWeb avant de copier la ligne.

![tâche : image_autre_texte](copy-gridweb-rows-and-columns_1.png)

L'extrait de code est simple, comme illustré ci-dessous. Il accède à l'objet GridCells de l'ordre de feuille de calcul actif pour faire une copie de la première ligne vers la ligne suivante.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyRow.cs" >}}


Voici à quoi ressemble le Aspose.Cells.GridWeb après l'opération de copie de ligne.

![tâche : image_autre_texte](copy-gridweb-rows-and-columns_2.png)
### **Copie d'une seule colonne**
L'exemple suivant utilise une feuille de calcul existante avec une colonne et une formule simple qui additionne toutes les valeurs de la colonne. Voici comment la feuille de calcul est affichée dans l'interface Aspose.Cells.GridWeb avant de copier la colonne.

![tâche : image_autre_texte](copy-gridweb-rows-and-columns_3.png)

Semblable à l'exemple ci-dessus, l'extrait de code suivant accède à l'objet GridCells de l'ordre de feuille de calcul actif pour faire une copie de la première colonne dans la colonne suivante.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyColumn.cs" >}}



Voici à quoi ressemble le Aspose.Cells.GridWeb après l'opération de copie de colonne.

![tâche : image_autre_texte](copy-gridweb-rows-and-columns_4.png)

{{% alert color="primary" %}} 

Vous pouvez utiliser les méthodes GridCells.CopyRow & GridCells.CopyColumn en boucle pour copier la ligne et la colonne source sur plusieurs lignes et colonnes respectivement.

{{% /alert %}} 
### **Copie de plusieurs lignes**
Il est également possible de copier plusieurs lignes vers une nouvelle destination en utilisant la méthode GridCells.CopyRows, qui prend un paramètre supplémentaire de type entier pour spécifier le nombre de lignes source à copier.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleRows.cs" >}}



Voici à quoi ressemble Aspose.Cells.GridWeb avant et après l'opération de copie de lignes.

![tâche : image_autre_texte](copy-gridweb-rows-and-columns_5.png)

![tâche : image_autre_texte](copy-gridweb-rows-and-columns_6.png)
### **Copie de plusieurs colonnes**
La classe GridCells fournit également la méthode CopyColumns, qui prend un paramètre supplémentaire de type entier pour spécifier le nombre de colonnes source à copier.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleColumns.cs" >}}



Voici à quoi ressemble Aspose.Cells.GridWeb avant et après l'opération de copie de lignes.

![tâche : image_autre_texte](copy-gridweb-rows-and-columns_7.png)

![tâche : image_autre_texte](copy-gridweb-rows-and-columns_8.png)
