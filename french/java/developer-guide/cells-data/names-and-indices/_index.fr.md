---
title: Conversion entre le nom de la cellule et l'index de ligne/colonne
linktitle: Cell Conversion de nom et d'index
type: docs
weight: 5
url: /fr/java/names-and-indices/
description: Découvrez comment obtenir le résultat de la conversion entre le nom de cellule et l'index de ligne/colonne avec les API Aspose.Cells for Java.
keywords: Java Convert cell index to name, Convert cell name to row/column index using java apis, How to Get Cell Name from Row and Column Indices with java, Java How to Get Row and Column Indices from Cell Name.
---
##  **Comment obtenir le nom Cell à partir des index de lignes et de colonnes**
Il est possible de trouver le nom d'une cellule à partir de l'index de la ligne et de la colonne. Cet article explique comment.

 Aspose.Cells fournit le[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) méthode qui permet aux développeurs d'obtenir le nom d'une cellule s'ils fournissent l'index des lignes et des colonnes.

{{% alert color="primary" %}} 

Contrairement à Microsoft Excel, où les indices de ligne et de colonne commencent à 1, Aspose.Cells commence à compter les indices de ligne et de colonne à partir de 0.

{{% /alert %}} 

 L'exemple de code suivant illustre comment utiliser[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) pour accéder au nom de la cellule donné à un index de ligne et de colonne connu. Le code génère la sortie suivante.



Cell Nom à [0, 0] : A1

Cell Nom à [4, 0] : A5

Cell Nom à [0, 4] : E1

Cell Nom à [2, 2] : C3

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
##  **Comment obtenir des indices de lignes et de colonnes à partir du nom Cell**
Il est possible de retrouver un index de ligne et de colonne de la cellule à partir de son nom. Cet article explique comment.

 Aspose.Cells fournit le[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) méthode qui permet aux développeurs d'obtenir un index de ligne et de colonne à partir du nom de la cellule.

{{% alert color="primary" %}} 

Contrairement à Microsoft Excel, où les indices de ligne et de colonne commencent à 1, Aspose.Cells commence à compter les indices de ligne et de colonne à partir de 0.

{{% /alert %}} 

 L'exemple de code suivant illustre comment utiliser[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) pour obtenir l'index de ligne et de colonne à partir du nom de la cellule. Le code génère la sortie suivante.



Indice de ligne de Cell C6 : 5

Index de colonne du Cell C6 : 2

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
##  **Comment créer des noms de feuilles sécurisées**
 Il est parfois nécessaire d'attribuer le nom de la feuille au moment de l'exécution. Dans ce scénario, il peut y avoir des noms de feuilles pouvant contenir des caractères supplémentaires tels que<>+(?". Il est nécessaire de remplacer tout caractère de ce type, qui n'est pas autorisé comme nom de feuille, par un caractère prédéfini fourni par l'utilisateur. De même, la longueur peut augmenter jusqu'à plus de 31 caractères qui doivent être tronqués. Apache POI fournit certaines fonctionnalités de création de noms sécurisés, c'est pourquoi une fonctionnalité similaire est fournie par Aspose.Cells pour gérer tous ces problèmes. L'exemple de code suivant illustre cette fonctionnalité :



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**Sortie console**

c'est le prénom qui est cre

` `<> + (adj.Privé _ " Privé"
