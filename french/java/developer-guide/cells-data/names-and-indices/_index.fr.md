---
title: Conversion entre le nom de cellule et l index de ligne/colonne
linktitle: Conversion entre le nom de cellule et l index
type: docs
weight: 5
url: /fr/java/names-and-indices/
description: Apprenez comment obtenir le résultat de conversion entre le nom de la cellule et l index de ligne/colonne avec Aspose.Cells for Java API.
keywords: Java Convertir l index de cellule en nom, Convertir le nom de cellule en index de ligne/colonne en utilisant des API java, Comment obtenir le nom de cellule à partir des indices de ligne et de colonne avec java, Java Comment obtenir les indices de ligne et de colonne à partir du nom de cellule.
---

## **Comment obtenir le nom de cellule à partir des indices de ligne et de colonne**
Il est possible de trouver le nom d'une cellule en donnant l'index de ligne et de colonne. Cet article explique comment faire.

Aspose.Cells fournit la méthode [CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) qui permet aux développeurs d'obtenir le nom d'une cellule s'ils fournissent l'index de ligne et de colonne.

{{% alert color="primary" %}} 

Microsoft Excel commence à compter les indices de lignes et de colonnes à partir de 1. Contrairement à Microsoft Excel, Aspose.Cells commence à compter les indices de lignes et de colonnes à partir de 0.

{{% /alert %}} 

Le code d'exemple suivant illustre comment utiliser [CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) pour accéder au nom de la cellule donné à un index de ligne et de colonne connu. Le code génère la sortie suivante.

{{< highlight java >}}

Cell Name at [0, 0]: A1

Cell Name at [4, 0]: A5

Cell Name at [0, 4]: E1

Cell Name at [2, 2]: C3

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
## **Comment obtenir les indices de ligne et de colonne à partir du nom de la cellule**
Il est possible de trouver un indice de ligne et de colonne de la cellule à partir de son nom. Cet article explique comment.

Aspose.Cells fournit la méthode [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) qui permet aux développeurs d'obtenir un indice de ligne et de colonne à partir du nom de la cellule.

{{% alert color="primary" %}} 

Microsoft Excel commence à compter les indices de lignes et de colonnes à partir de 1. Contrairement à Microsoft Excel, Aspose.Cells commence à compter les indices de lignes et de colonnes à partir de 0.

{{% /alert %}} 

Le code d'exemple suivant illustre comment utiliser [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) pour obtenir l'indice de ligne et de colonne à partir du nom de la cellule. Le code génère la sortie suivante.

{{< highlight java >}}

Row Index of Cell C6: 5

Column Index of Cell C6: 2

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
## **Comment créer des noms de feuille sécurisés**
Parfois, il est nécessaire d'attribuer le nom de la feuille à l'exécution. Dans ce scénario, il peut y avoir des noms de feuilles qui peuvent contenir certains caractères supplémentaires comme <>+(?”. Il est nécessaire de remplacer tout caractère qui n'est pas autorisé en tant que nom de feuille par un caractère prédéfini fourni par l'utilisateur. De même, la longueur peut augmenter à plus de 31 caractères, ce qui doit être tronqué. Apache POI offre certaines fonctionnalités de création de noms sécurisés, donc une fonctionnalité similaire est fournie par Aspose.Cells pour gérer tous ces problèmes. Le code d'exemple suivant démontre cette fonctionnalité.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**Sortie console**

c'est le premier nom qui est créé

{{< highlight java >}}

` `<> + (adj.Private _ " Private"

{{< /highlight >}}
