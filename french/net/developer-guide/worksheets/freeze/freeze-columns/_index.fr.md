---
title: Geler la (les) première(s) colonne(s) de la feuille de calcul Excel
linktitle: Geler les colonnes
type: docs
weight: 190
url: /fr/net/how-to-freeze-columns-of-excel-worksheet
description: Dans cet article, vous apprendrez à geler les premières colonnes des feuilles de calcul Excel de manière programmable à l aide de la bibliothèque C# avec API .NET.
keywords: Geler les colonnes de gauche, Geler les premières colonnes, Verrouiller la (les) colonne(s)
---

## **Introduction**

Dans cet article, nous allons apprendre à geler la colonne de gauche. Lorsque vous avez un grand volume de données dans une ligne, il est impossible de voir les colonnes de gauche lors du défilement horizontal de la feuille de calcul. Vous pouvez geler et verrouiller la première colonne(s) pour pouvoir voir cette partie figée même lorsque le reste des données est défilé. Vous pouvez facilement voir les en-têtes dans les colonnes de gauche.


## **Geler les colonnes dans Excel**

**![Geler la ou les premières colonnes dans Excel](freeze-columns.png)**


1. Si vous voulez geler la ou les premières colonnes, sélectionnez d'abord la colonne sous la colonne qui doit être gelée
2. Cliquez sur Affichage > Fenêtres figées.
3. Dans le menu déroulant, cliquez sur Geler la première colonne.
4. Si vous faites défiler vers le bas, la première colonne est toujours dans la vue de gauche.

**![Colonnes figées](frozen-columns.png)**

Comme vous pouvez le voir, la 1ère colonne est gelée, elle reste toujours fixée en haut de la vue lorsque vous faites défiler horizontalement.

Geler les colonnes vous permet de visualiser vos longues données sans avoir à suivre la première colonne.




## **Geler les colonnes avec Aspose.Cells pour .Net**
C'est simple de geler la ou les premières colonnes avec Aspose.Cells pour .Net. 
Veuillez utiliser la méthode [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/) pour geler la ou les colonnes sélectionnées.
1. Construisez un classeur pour ouvrir le fichier ou créez un fichier vide.
2. Gelez la première colonne avec la méthode Worksheet.FreezePanes().
3. Enregistrez le fichier.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Column.cs" >}}

Fichier Excel source [exemple joint](Freeze.xlsx).
