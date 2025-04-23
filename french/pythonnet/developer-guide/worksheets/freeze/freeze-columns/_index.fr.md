---
title: Geler la (les) première(s) colonne(s) de la feuille de calcul Excel
linktitle: Geler les colonnes
type: docs
weight: 190
url: /fr/python-net/how-to-freeze-columns-of-excel-worksheet
description: Dans cet article, vous apprendrez comment figer les colonnes de gauche des feuilles Excel de manière programmatique en utilisant Aspose.Cells pour Python via .NET APIs.
keywords: Bibliothèque Excel Python, Figer les colonnes de gauche en Python, Figer la première colonne en Python, Verrouiller les colonnes en Python.
---

## **Introduction**

Dans cet article, nous allons apprendre à geler la colonne de gauche. Lorsque vous avez un grand volume de données dans une ligne, il est impossible de voir les colonnes de gauche lors du défilement horizontal de la feuille de calcul. Vous pouvez geler et verrouiller la première colonne(s) pour pouvoir voir cette partie figée même lorsque le reste des données est défilé. Vous pouvez facilement voir les en-têtes dans les colonnes de gauche.


## **Comment figer les colonnes dans Excel**

**![Geler la ou les premières colonnes dans Excel](freeze-columns.png)**


1. Si vous voulez geler la ou les premières colonnes, sélectionnez d'abord la colonne sous la colonne qui doit être gelée
2. Cliquez sur Affichage > Fenêtres figées.
3. Dans le menu déroulant, cliquez sur Geler la première colonne.
4. Si vous faites défiler vers le bas, la première colonne est toujours dans la vue de gauche.

**![Colonnes figées](frozen-columns.png)**

Comme vous pouvez le voir, la 1ère colonne est gelée, elle reste toujours fixée en haut de la vue lorsque vous faites défiler horizontalement.

Geler les colonnes vous permet de visualiser vos longues données sans avoir à suivre la première colonne.




## **Comment figer les colonnes avec Aspose.Cells pour la bibliothèque Excel Python**
Il est simple de figer la ou les premières colonnes avec Aspose.Cells pour Python via .NET. Veuillez utiliser la méthode [**Worksheet.freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int) pour figer la ou les colonnes à la colonne sélectionnée.
1. Construisez un classeur pour ouvrir le fichier ou créez un fichier vide.
2. Gelez la première colonne avec la méthode Worksheet.FreezePanes().
3. Enregistrez le fichier.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Freeze-Column.py" >}}

Fichier Excel source [exemple joint](Freeze.xlsx).
