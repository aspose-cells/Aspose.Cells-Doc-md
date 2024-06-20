---
title: Comment vérifier l état figé sans Excel.
linktitle: État figé
type: docs
weight: 190
url: /fr/net/how-to-check-frozen-state-of-excel-worksheet
description: Dans cet article, vous apprendrez comment vérifier l état gelé de la feuille de calcul Excel de manière programmatique en utilisant la bibliothèque C# avec l API .NET.

---

## **Introduction**

Dans cet article, nous allons apprendre comment vérifier l'état figé de la feuille de calcul Excel de manière programmatique. Nous pouvons simplement savoir si la feuille de calcul est figée ou divisée dans MS Excel. Mais existe-t-il un moyen de savoir si elle est figée ou divisée avec CSharp. Nous pouvons simplement le faire avec Aspose.Cells pour .Net.

## **Les volets de fenêtre sont-ils gelés**
Avec Aspose.Cells pour .Net, nous pouvons vérifier si la fenêtre est gelée et combien de lignes et de colonnes sont verrouillées.

Veuillez utiliser la propriété [**Worksheet.PaneState**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/PaneState/) pour vérifier l'état des volets de la fenêtre 
et obtenir les lignes et colonnes verrouillées avec la méthode [**Worksheet.GetFreezedPanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFreezedPanes/)
1. Construisez un classeur pour ouvrir le fichier.
2. Vérifiez si la feuille de calcul est gelée.
3. Obtenez les lignes et colonnes verrouillées

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Is-Worksheet-Frozen.cs" >}}
