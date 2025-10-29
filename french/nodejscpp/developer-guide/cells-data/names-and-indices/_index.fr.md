---
title: Conversion entre le nom de cellule et l index de ligne/colonne
linktitle: Conversion entre le nom de cellule et l index
type: docs
weight: 10
url: /fr/nodejs-cpp/names-and-indices/
description: Apprenez comment obtenir la conversion entre le nom de la cellule et l’indice de ligne/colonne via l’API Aspose.Cells for Node.js via C++.
keywords: Obtenir le nom de la cellule à partir des indices de ligne et de colonne en Node.js en C++, obtenir les indices de ligne et de colonne à partir du nom de la cellule, créer des noms de feuilles de calcul sûrs, ajouter des noms de feuilles de calcul sûrs
---

## **Obtenir le nom de cellule à partir des indices de ligne et de colonne**
Il est possible de trouver le nom d'une cellule en donnant l'index de ligne et de colonne. Cet article explique comment faire.
Aspose.Cells for Node.js via C++ fournit la méthode CellsHelper.cellIndexToName qui permet aux développeurs d’obtenir le nom d’une cellule si ils fournissent l’indice de ligne et de colonne.

{{% alert color="primary" %}} 

Microsoft Excel commence à compter les index de lignes et de colonnes à partir de 1. Contrairement à Microsoft Excel, Aspose.Cells for Node.js via C++ commence à compter à partir de 0.

{{% /alert %}} 

Le code exemple ci-dessous illustre comment utiliser CellsHelper.cellIndexToName pour accéder au nom de la cellule étant donné un index de ligne et de colonne connus. Le code génère la sortie suivante.



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-IndexToName-1.js" >}}
## **Obtenir les indices de ligne et de colonne à partir du nom de la cellule**
Il est possible de trouver un indice de ligne et de colonne de la cellule à partir de son nom. Cet article explique comment.
Aspose.Cells for Node.js via C++ fournit la méthode CellsHelper.cellNameToIndex qui permet aux développeurs d’obtenir un indice de ligne et de colonne à partir du nom d’une cellule.

{{% alert color="primary" %}} 

Microsoft Excel commence à compter les index de lignes et de colonnes à partir de 1. Contrairement à Microsoft Excel, Aspose.Cells for Node.js via C++ commence à compter à partir de 0.

{{% /alert %}} 

Le code d'exemple suivant illustre comment utiliser CellsHelper.cellNameToIndex pour obtenir l'indice de ligne et de colonne à partir du nom de la cellule. Le code génère la sortie suivante.



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-NameToIndex-1.js" >}}

## **Créer des noms de feuille sécurisés**
Parfois, il est nécessaire d'assigner le nom de la feuille au moment de l'exécution. Dans ce scénario, il peut y avoir des noms de feuilles qui contiennent des caractères supplémentaires tels que <>, +(?”. Il est nécessaire de remplacer tout caractère non autorisé comme nom de feuille par un caractère prédéfini fourni par l'utilisateur. De même, la longueur peut augmenter à plus de 31 caractères, ce qui nécessite d'être tronqué. Apache POI fournit certaines fonctionnalités pour créer des noms sûrs, donc une fonctionnalité similaire est fournie par Aspose.Cells for Node.js via C++ pour gérer tous ces problèmes. Le code d'exemple suivant démontre cette fonctionnalité :



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-CreateSafeSheetNames.js" >}}

Sortie :

c'est le premier nom qui est créé

`  ` <> + (adj. Privé _ "Privé"
{{< app/cells/assistant language="nodejs-cpp" >}}
