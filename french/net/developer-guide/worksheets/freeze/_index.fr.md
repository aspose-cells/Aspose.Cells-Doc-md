---
title: Geler les volets de la feuille de calcul Excel
linktitle: Geler les volets
type: docs
weight: 190
url: /fr/net/how-to-freeze-panes-of-excel-worksheet
description: Dans cet article, vous apprendrez comment geler les volets des feuilles de calcul Excel de manière programmée en utilisant la bibliothèque C# avec l API .NET.
keywords: Geler les volets, geler la fenêtre.
---

## **Introduction**

Dans cet article, nous apprendrons comment geler les volets. Lorsque vous avez une énorme quantité de données sous un en-tête commun, vous ne pouvez pas voir l'en-tête lorsque vous faites défiler la feuille de calcul. Et chaque enregistrement contient de nombreuses données. Vous pouvez geler les volets afin de voir la portion figée même lorsque le reste des données est en cours de défilement. Vous pouvez facilement voir les en-têtes dans les lignes supérieures ou les premières colonnes. Geler et dégeler les volets ne change que la vue des données sans changer les données elles-mêmes.

## **Dans Excel**

**![Geler les volets dans Excel](Freeze-panes.png)**


1. Si vous voulez geler les volets, geler les lignes et les colonnes, sélectionnez d'abord une cellule (par exemple B2)
2. Cliquez sur Affichage > Fenêtres figées.
3. Dans le menu déroulant, cliquez sur Geler les volets.
4. Si vous faites défiler vers le bas ou vers la droite, la première ligne et la première colonne restent figées.

**![Volets figés](Frozen-Panes.png)**

Comme vous pouvez le voir, la 1ère ligne et la colonne A sont figées, la deuxième ligne est 32 et la deuxième colonne visible est D. 

Les volets gelés vous permettent de visualiser vos grandes données sans suivre de légende de ligne ou de colonne.




## **Fixer les volets avec Aspose.Cells pour .Net**
Il est simple de fixer les volets avec Aspose.Cells pour .Net. Veuillez utiliser la méthode [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/) pour fixer les volets à la cellule sélectionnée.
1. Construisez un classeur pour ouvrir le fichier ou créez un fichier vide.
2. Fixer les volets avec la méthode Worksheet.FreezePanes().
3. Enregistrez le fichier.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Pane.cs" >}}

Fichier Excel source [exemple joint](Freeze.xlsx).
