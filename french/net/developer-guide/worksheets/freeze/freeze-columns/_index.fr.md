---
title: Geler la ou les premières colonnes de la feuille de calcul Excel
linktitle: Geler les colonnes
type: docs
weight: 190
url: /fr/net/how-to-freeze-columns-of-excel-worksheet
description: Dans cet article, vous apprendrez comment geler les colonnes de gauche des feuilles de calcul Excel par programme à l'aide de la bibliothèque C# avec .NET API.
keywords: Freeze left columns, Feeze first columns, Lock the column(s)
---
{{% alert color="primary" %}}

Dans cet article, nous apprendrons comment figer la ou les colonnes de gauche.
Lorsque vous avez une énorme quantité de données dans une rangée, vous ne pouvez pas voir les colonnes de gauche lorsque vous faites défiler horizontalement la feuille de calcul. Vous pouvez geler et verrouiller la ou les premières colonnes afin de pouvoir voir cette partie gelée même lorsque le reste des données défile. Vous pouvez facilement voir les en-têtes dans les colonnes de gauche.

{{% /alert %}}

##  **Geler les colonnes dans Excel**

**![Geler la ou les colonnes de gauche dans Excel](freeze-columns.png)**


1. Si vous souhaitez geler la ou les colonnes de gauche, sélectionnez d'abord la colonne sous la colonne qui doit être gelée.
2. Cliquez sur Affichage > Figer les volets.
3. Dans le menu déroulant, cliquez sur Geler la première colonne.
4. Si vous faites défiler vers le bas, la première colonne est toujours dans la vue de gauche.

**![Colonne Fonzen](frozen-columns.png)**

Comme vous pouvez le voir, la 1ère colonne est figée, la première colonne est toujours verrouillée en haut de la vue lorsque vous faites défiler horizontalement.

Geler les colonnes vous permet de visualiser vos données longues sans aucune trace de la première colonne.




##  **Geler les colonnes avec Aspose.Cells pour .Net**
Il est simple de geler la ou les premières colonnes avec Aspose.Cells pour .Net.
 Veuillez utiliser le[**Feuille de travail.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)méthode pour figer la ou les colonnes sur la colonne sélectionnée.
1. Construisez un classeur pour ouvrir le fichier ou créez un fichier vide.
2. Gelez la première colonne avec la méthode Worksheet.FreezePanes().
3. Enregistrez le fichier.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Column.cs" >}}

 Ci-joint[exemple de fichier Excel source](Freeze.xlsx).
