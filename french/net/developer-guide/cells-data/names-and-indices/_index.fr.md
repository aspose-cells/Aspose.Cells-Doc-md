---
title: Conversion entre le nom de cellule et l index de ligne/colonne
linktitle: Conversion entre le nom de cellule et l index
type: docs
weight: 10
url: /fr/net/names-and-indices/
description: Apprenez comment obtenir la conversion entre le nom de la cellule et l index de ligne/colonne via l API Aspose.Cells for .NET.
keywords: Obtenir le nom de la cellule à partir des index de ligne et de colonne, obtenir les index de ligne et de colonne à partir du nom de la cellule, créer des noms de feuille de calcul sécurisés, ajouter des noms de feuille de calcul sécurisés
---

## **Obtenir le nom de cellule à partir des indices de ligne et de colonne**
Il est possible de trouver le nom d'une cellule en donnant l'index de ligne et de colonne. Cet article explique comment faire.
Aspose.Cells fournit la méthode CellsHelper.CellIndexToName qui permet aux développeurs d'obtenir le nom d'une cellule s'ils fournissent l'index de ligne et de colonne.

{{% alert color="primary" %}} 

Contrairement à Microsoft Excel, où les index de lignes et de colonnes commencent à 1, Aspose.Cells commence à compter les index de lignes et de colonnes à partir de 0.

{{% /alert %}} 

Le code d'exemple suivant illustre comment utiliser CellsHelper.CellIndexToName pour accéder au nom de la cellule en connaissant un index de ligne et de colonne donné. Le code génère la sortie suivante.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-IndexToName-1.cs" >}}
## **Obtenir les indices de ligne et de colonne à partir du nom de la cellule**
Il est possible de trouver un indice de ligne et de colonne de la cellule à partir de son nom. Cet article explique comment.
Aspose.Cells fournit la méthode CellsHelper.CellNameToIndex qui permet aux développeurs d'obtenir l'index de ligne et de colonne à partir du nom de la cellule.

{{% alert color="primary" %}} 

Contrairement à Microsoft Excel, où les index de lignes et de colonnes commencent à 1, Aspose.Cells commence à compter les index de lignes et de colonnes à partir de 0.

{{% /alert %}} 

Le code d'exemple suivant illustre comment utiliser CellsHelper.CellNameToIndex pour obtenir l'index de ligne et de colonne à partir du nom de la cellule. Le code génère la sortie suivante.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-NameToIndex-1.cs" >}}
## **Créer des noms de feuille sécurisés**
Parfois, il est nécessaire d'attribuer le nom de la feuille à l'exécution. Dans ce scénario, il peut y avoir des noms de feuille contenant des caractères supplémentaires comme <>+(?”. Il est nécessaire de remplacer tout caractère de ce type, qui n'est pas autorisé en tant que nom de feuille, par un caractère prédéfini fourni par l'utilisateur. De même, la longueur peut augmenter à plus de 31 caractères, ce qui doit être tronqué. Apache POI fournit certaines fonctionnalités de création de noms sécurisés, par conséquent, une fonctionnalité similaire est fournie par Aspose.Cells pour gérer tous ces problèmes. Le code d'exemple suivant illustre cette fonctionnalité:



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-CreateSafeSheetNames.cs" >}}

Sortie :

c'est le premier nom qui est créé

`  ` <> + (adj. Privé _ "Privé"
