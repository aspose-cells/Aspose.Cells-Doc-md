---
title: Geler le ou les premières lignes de la feuille de calcul Excel
linktitle: Geler les lignes
type: docs
weight: 190
url: /fr/python-net/how-to-freeze-rows-of-excel-worksheet
description: Dans cet article, vous apprendrez comment figer les lignes du haut des feuilles Excel de manière programmatique en utilisant Aspose.Cells pour Python via .NET APIs.
keywords: Bibliothèque Excel Python, Figer les lignes du haut en Python, Figer la première ligne en Python.
---

## **Introduction**

Dans cet article, nous allons apprendre à geler la ligne du haut. Lorsque vous avez un grand volume de données sous un en-tête commun, il est impossible de voir l'en-tête lors du défilement vertical de la feuille de calcul. Vous pouvez geler la ligne(s) du haut pour pouvoir voir cette partie figée même lorsque le reste des données est défilé. Vous pouvez facilement voir les en-têtes dans les lignes du haut.

## **Comment figer les lignes dans Excel**

**![Figer la rangée(s) supérieure(s) dans Excel](Freeze-Rows.png)**


1. Si vous souhaitez figer la rangée(s) supérieure(s), sélectionnez d'abord la rangée sous la rangée qui doit être figée
2. Cliquez sur Affichage > Fenêtres figées.
3. Dans le menu déroulant, cliquez sur Figer la rangée supérieure.
4. Si vous faites défiler vers le bas, la première rangée est toujours en vue en haut.

**![Fonzen row](Frozen-Row.png)**

Comme vous pouvez le voir, la 1ère rangée est figée, elle reste toujours en haut de la vue lorsque vous faites défiler vers le bas.

Figer les rangées vous permet de voir vos grandes données sans avoir à suivre l'étiquette de la rangée.




## **Comment figer les lignes avec Aspose.Cells pour la bibliothèque Excel Python**
Il est simple de geler la ou les lignes avec Aspose.Cells pour Python via .NET. Veuillez utiliser la méthode [**Worksheet.freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int) pour figer la ou les lignes à la ligne sélectionnée.
1. Construisez un classeur pour ouvrir le fichier ou créez un fichier vide.
2. Figez la première rangée avec la méthode Worksheet.FreezePanes().
3. Enregistrez le fichier.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Freeze-Row.py" >}}

Fichier Excel source d'exemple joint [échantillon](../Freeze.xlsx).
{{< app/cells/assistant language="python-net" >}}
