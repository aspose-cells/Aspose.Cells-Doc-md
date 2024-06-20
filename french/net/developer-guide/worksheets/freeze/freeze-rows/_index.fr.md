---
title: Geler le ou les premières lignes de la feuille de calcul Excel
linktitle: Geler les lignes
type: docs
weight: 190
url: /fr/net/how-to-freeze-rows-of-excel-worksheet
description: Dans cet article, vous apprendrez comment geler les premières lignes des feuilles Excel de manière programmatique en utilisant une bibliothèque C# avec l API .NET.
keywords: Geler les premières lignes, Geler la première ligne.
---

## **Introduction**

Dans cet article, nous allons apprendre à geler la ligne du haut. Lorsque vous avez un grand volume de données sous un en-tête commun, il est impossible de voir l'en-tête lors du défilement vertical de la feuille de calcul. Vous pouvez geler la ligne(s) du haut pour pouvoir voir cette partie figée même lorsque le reste des données est défilé. Vous pouvez facilement voir les en-têtes dans les lignes du haut.

## **Figer les rangées dans Excel**

**![Figer la rangée(s) supérieure(s) dans Excel](Freeze-Rows.png)**


1. Si vous souhaitez figer la rangée(s) supérieure(s), sélectionnez d'abord la rangée sous la rangée qui doit être figée
2. Cliquez sur Affichage > Fenêtres figées.
3. Dans le menu déroulant, cliquez sur Figer la rangée supérieure.
4. Si vous faites défiler vers le bas, la première rangée est toujours en vue en haut.

**![Fonzen row](Frozen-Row.png)**

Comme vous pouvez le voir, la 1ère rangée est figée, elle reste toujours en haut de la vue lorsque vous faites défiler vers le bas.

Figer les rangées vous permet de voir vos grandes données sans avoir à suivre l'étiquette de la rangée.




## **Figer les rangées avec Aspose.Cells pour .Net**
Il est simple de figer des rangées avec Aspose.Cells pour .Net. 
Veuillez utiliser la méthode [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/) pour figer des rangées à la rangée sélectionnée.
1. Construisez un classeur pour ouvrir le fichier ou créez un fichier vide.
2. Figez la première rangée avec la méthode Worksheet.FreezePanes().
3. Enregistrez le fichier.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Row.cs" >}}

Fichier Excel source d'exemple joint [échantillon](../Freeze.xlsx).
