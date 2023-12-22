---
title: Conversion entre le nom de la cellule et l'index de ligne/colonne
linktitle: Cell Conversion de nom et d'index
type: docs
weight: 10
url: /fr/net/names-and-indices/
description: Découvrez comment obtenir la conversion entre le nom de cellule et l'index de ligne/colonne via le Aspose.Cells for .NET API.
keywords: Get Cell Name from Row and Column Indices, Get Row and Column Indices from Cell Name, Create safe worksheet names, Add safe worksheet names
---
##  **Obtenez le nom Cell à partir des index de lignes et de colonnes**
Il est possible de trouver le nom d'une cellule à partir de l'index de la ligne et de la colonne. Cet article explique comment.
Aspose.Cells fournit la méthode CellsHelper.CellIndexToName qui permet aux développeurs d'obtenir le nom d'une cellule s'ils fournissent l'index de ligne et de colonne.

{{% alert color="primary" %}} 

Contrairement à Microsoft Excel, où les indices de ligne et de colonne commencent à 1, Aspose.Cells commence à compter les indices de ligne et de colonne à partir de 0.

{{% /alert %}} 

L'exemple de code suivant illustre comment utiliser CellsHelper.CellIndexToName pour accéder au nom de la cellule à partir d'un index de ligne et de colonne connu. Le code génère la sortie suivante.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-IndexToName-1.cs" >}}
##  **Obtenir les indices de lignes et de colonnes à partir du nom Cell**
Il est possible de retrouver un index de ligne et de colonne de la cellule à partir de son nom. Cet article explique comment.
Aspose.Cells fournit la méthode CellsHelper.CellNameToIndex qui permet aux développeurs d'obtenir un index de ligne et de colonne à partir du nom de la cellule.

{{% alert color="primary" %}} 

Contrairement à Microsoft Excel, où les indices de ligne et de colonne commencent à 1, Aspose.Cells commence à compter les indices de ligne et de colonne à partir de 0.

{{% /alert %}} 

L'exemple de code suivant illustre comment utiliser CellsHelper.CellNameToIndex pour obtenir l'index de ligne et de colonne à partir du nom de la cellule. Le code génère la sortie suivante.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-NameToIndex-1.cs" >}}
##  **Créer des noms de feuilles sécurisées**
 Il est parfois nécessaire d'attribuer le nom de la feuille au moment de l'exécution. Dans ce scénario, il peut y avoir des noms de feuilles pouvant contenir des caractères supplémentaires tels que<>+(?". Il est nécessaire de remplacer tout caractère de ce type, qui n'est pas autorisé comme nom de feuille, par un caractère prédéfini fourni par l'utilisateur. De même, la longueur peut augmenter jusqu'à plus de 31 caractères qui doivent être tronqués. Apache POI fournit certaines fonctionnalités de création de noms sécurisés, c'est pourquoi une fonctionnalité similaire est fournie par Aspose.Cells pour gérer tous ces problèmes. L'exemple de code suivant illustre cette fonctionnalité :



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-CreateSafeSheetNames.cs" >}}

Sortir:

c'est le prénom qui est cre

` `<> + (adj.Privé _ " Privé"
