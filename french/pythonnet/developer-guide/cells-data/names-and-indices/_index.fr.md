---
title: Conversion entre le nom de cellule et l index de ligne/colonne
linktitle: Conversion entre le nom de cellule et l index
type: docs
weight: 10
url: /fr/python-net/names-and-indices/
description: Apprenez à obtenir la conversion entre le nom de cellule et l index de ligne/colonne à travers l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Python Excel, Obtenir le nom de cellule à partir des indices de ligne et de colonne en Python, Obtenir les indices de ligne et de colonne à partir du nom de cellule en Python, Créer des noms de feuille de travail sécurisés en Python, Ajouter des noms de feuille de travail sécurisés en Python
---

## **Obtenir le nom de cellule à partir des indices de ligne et de colonne**
Il est possible de trouver le nom d'une cellule en donnant l'index de ligne et de colonne. Cet article explique comment faire.
Aspose.Cells pour Python via .NET fournit la méthode [**CellsHelper.cell_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_index_to_name/#int-int) qui permet aux développeurs d'obtenir le nom d'une cellule s'ils fournissent l'index de ligne et de colonne.

{{% alert color="primary" %}} 

Contrairement à Microsoft Excel, où les indices de ligne et de colonne commencent à 1, Aspose.Cells for Python via .NET commence à compter les indices de ligne et de colonne à partir de 0.

{{% /alert %}} 

Le code d'exemple suivant illustre comment utiliser [**CellsHelper.cell_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_index_to_name/#int-int) pour accéder au nom de la cellule en fonction d'un indice de ligne et de colonne connu. Le code génère la sortie suivante.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-IndexToName-1.py" >}}

## **Obtenir les indices de ligne et de colonne à partir du nom de la cellule**
Il est possible de trouver un indice de ligne et de colonne de la cellule à partir de son nom. Cet article explique comment.
Aspose.Cells for Python via .NET fournit la méthode [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any) qui permet aux développeurs d'obtenir un indice de ligne et de colonne à partir du nom de la cellule.

{{% alert color="primary" %}} 

Contrairement à Microsoft Excel, où les indices de ligne et de colonne commencent à 1, Aspose.Cells for Python via .NET commence à compter les indices de ligne et de colonne à partir de 0.

{{% /alert %}} 

Le code d'exemple suivant illustre comment utiliser [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any) pour obtenir l'indice de ligne et de colonne à partir du nom de la cellule. Le code génère la sortie suivante.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-NameToIndex-1.py" >}}

## **Créer des noms de feuille sécurisés**
Parfois, il est nécessaire d'attribuer le nom de la feuille à l'exécution. Dans ce scénario, il peut y avoir des noms de feuille qui peuvent contenir certains caractères supplémentaires comme <>+(?”. Il est nécessaire de remplacer tout caractère de ce type, qui n'est pas autorisé en tant que nom de feuille, par un caractère prédéfini fourni par l'utilisateur. De même, la longueur peut dépasser 31 caractères, ce qui doit être tronqué. Apache POI fournit certaines fonctionnalités de création de noms sécurisés, donc une fonctionnalité similaire est fournie par Aspose.Cells pour Python via .NET pour gérer tous ces problèmes. Le code d'exemple suivant illustre cette fonctionnalité :



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-CreateSafeSheetNames.py" >}}

Sortie :

c'est le premier nom qui est créé

`  ` <> + (adj. Privé _ "Privé"
