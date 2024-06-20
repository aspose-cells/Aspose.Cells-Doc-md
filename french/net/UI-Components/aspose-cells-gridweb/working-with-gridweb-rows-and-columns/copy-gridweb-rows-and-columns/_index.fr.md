---
title: Copiez les lignes et colonnes de GridWeb
type: docs
weight: 80
url: /fr/net/aspose-cells-gridweb/copy-gridweb-rows-and-columns/
keywords: GridWeb, copier
description: Cet article présente comment copier des lignes et des colonnes dans GridWeb.
---

{{% alert color="primary" %}} 

Le composant Aspose.Cells.GridWeb offre la possibilité de copier des lignes et des colonnes grâce à la classe GridCells. Cet article démontre l'utilisation des API exposées par Aspose.Cells.GridWeb pour copier des lignes et des colonnes sur l'interface GridWeb. 

Les méthodes GridCells.CopyRow, GridCells.CopyColumn, GridCells.CopyRows & GridCells.CopyColumns copieront le contenu, le style et les formules de la ligne et de la colonne source vers la destination.

{{% /alert %}} 
## **Copier des lignes et des colonnes**
Si vous n'êtes pas encore familiarisé avec le composant Aspose.Cells.GridWeb, nous vous suggérons fortement de consulter l'[Introduction à Aspose.Cells.GridWeb](https://docs.aspose.com/cells/net/aspose-cells-gridweb/browsers-capabilities/) ainsi que l'article détaillé sur [Comment ajouter le composant Aspose.Cells.GridWeb dans une application WebForms](https://docs.aspose.com/cells/net/aspose-cells-gridweb/add-gridweb-to-web-form/).
### **Copie d'une seule ligne**
Afin de garder l'exemple simple, l'article utilise une feuille de calcul existante avec une seule ligne et une formule simple qui additionne toutes les valeurs de la ligne. Voici comment la feuille de calcul est affichée dans l'interface Aspose.Cells.GridWeb avant de copier la ligne.

![todo:image_alt_text](copy-gridweb-rows-and-columns_1.png)

L'extrait de code est simple, comme le montre l'accès à l'objet GridCells de la feuille de calcul active pour copier la première ligne vers la ligne suivante.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyRow.cs" >}}


Voici comment se présente Aspose.Cells.GridWeb après l'opération de copie de ligne.

![todo:image_alt_text](copy-gridweb-rows-and-columns_2.png)
### **Copier une seule colonne**
L'exemple suivant utilise une feuille de calcul existante avec une seule colonne et une formule simple qui additionne toutes les valeurs de la colonne. Voici comment la feuille de calcul est affichée dans l'interface Aspose.Cells.GridWeb avant de copier la colonne.

![todo:image_alt_text](copy-gridweb-rows-and-columns_3.png)

Similairement à l'exemple précédent, l'extrait de code suivant accède à l'objet GridCells de la feuille de calcul active pour copier la première colonne vers la colonne suivante.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyColumn.cs" >}}



Voici comment se présente Aspose.Cells.GridWeb après l'opération de copie de colonne.

![todo:image_alt_text](copy-gridweb-rows-and-columns_4.png)

{{% alert color="primary" %}} 

Vous pouvez utiliser les méthodes GridCells.CopyRow & GridCells.CopyColumn dans une boucle pour copier la ligne et la colonne source vers plusieurs lignes et colonnes respectivement.

{{% /alert %}} 
### **Copier plusieurs lignes**
Il est également possible de copier plusieurs lignes vers une nouvelle destination en utilisant la méthode GridCells.CopyRows, qui prend un paramètre supplémentaire de type entier pour spécifier le nombre de lignes source à copier.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleRows.cs" >}}



Voici comment Aspose.Cells.GridWeb apparaît avant et après l'opération de copie des colonnes.

![todo:image_alt_text](copy-gridweb-rows-and-columns_5.png)

![todo:image_alt_text](copy-gridweb-rows-and-columns_6.png)
### **Copier plusieurs colonnes**
La classe GridCells fournit également la méthode CopyColumns, qui prend un paramètre supplémentaire de type entier pour spécifier le nombre de colonnes source à copier.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleColumns.cs" >}}



Voici comment Aspose.Cells.GridWeb apparaît avant et après l'opération de copie des colonnes.

![todo:image_alt_text](copy-gridweb-rows-and-columns_7.png)

![todo:image_alt_text](copy-gridweb-rows-and-columns_8.png)
