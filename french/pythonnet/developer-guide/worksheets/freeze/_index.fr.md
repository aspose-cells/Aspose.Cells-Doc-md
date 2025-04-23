---
title: Geler les volets de la feuille de calcul Excel
linktitle: Geler les volets
type: docs
weight: 190
url: /fr/python-net/how-to-freeze-panes-of-excel-worksheet
description: Dans cet article, vous apprendrez comment figer les volets des feuilles de calcul Excel de manière programmatique en utilisant les API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Excel Python, figer les volets, verrouiller la fenêtre dans Python.
---

## **Introduction**

Dans cet article, nous apprendrons comment geler les volets. Lorsque vous avez une énorme quantité de données sous un en-tête commun, vous ne pouvez pas voir l'en-tête lorsque vous faites défiler la feuille de calcul. Et chaque enregistrement contient de nombreuses données. Vous pouvez geler les volets afin de voir la portion figée même lorsque le reste des données est en cours de défilement. Vous pouvez facilement voir les en-têtes dans les lignes supérieures ou les premières colonnes. Geler et dégeler les volets ne change que la vue des données sans changer les données elles-mêmes.

## ***Comment figer les volets dans Excel**

**![Geler les volets dans Excel](Freeze-panes.png)**


1. Si vous voulez geler les volets, geler les lignes et les colonnes, sélectionnez d'abord une cellule (par exemple B2)
2. Cliquez sur Affichage > Fenêtres figées.
3. Dans le menu déroulant, cliquez sur Geler les volets.
4. Si vous faites défiler vers le bas ou vers la droite, la première ligne et la première colonne restent figées.

**![Volets figés](Frozen-Panes.png)**

Comme vous pouvez le voir, la 1ère ligne et la colonne A sont figées, la deuxième ligne est 32 et la deuxième colonne visible est D. 

Les volets gelés vous permettent de visualiser vos grandes données sans suivre de légende de ligne ou de colonne.




## **Comment figer les volets avec la bibliothèque Excel Aspose.Cells pour Python**
Il est simple de figer les volets avec Aspose.Cells pour Python via .NET. Veuillez utiliser la méthode [**Worksheet.freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int) pour figer les volets à la cellule sélectionnée.
1. Construisez un classeur pour ouvrir le fichier ou créez un fichier vide.
2. Fixer les volets avec la méthode Worksheet.FreezePanes().
3. Enregistrez le fichier.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Freeze-Pane.py" >}}

Fichier Excel source [exemple joint](Freeze.xlsx).
