---
title: Comment vérifier l'état gelé sans Excel.
linktitle: État gelé
type: docs
weight: 190
url: /fr/net/how-to-check-frozen-state-of-excel-worksheet
description: Dans cet article, vous apprendrez comment vérifier l'état gelé d'une feuille de calcul Excel par programme à l'aide de la bibliothèque C# avec .NET API.
---
{{% alert color="primary" %}}

Dans cet article, nous apprendrons comment vérifier par programme l’état gelé d’une feuille de calcul Excel.
Nous pouvons simplement savoir si la feuille de calcul est gelée ou divisée dans MS Excel. Mais existe-t-il un moyen de savoir s'il est gelé ou divisé avec CSharp.
Nous pouvons simplement le faire avec Aspose.Cells pour .Net.
{{% /alert %}}

##  **Les vitres des fenêtres sont-elles gelées**
Avec Aspose.Cells pour .Net, nous pouvons vérifier si la fenêtre est gelée et combien de lignes et de colonnes sont verrouillées.

 Veuillez utiliser le[**Feuille de calcul.PaneState**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/PaneState/) propriété pour vérifier l'état des vitres des fenêtres
 et obtient des lignes et des colonnes verrouillées avec[**Feuille de travail.GetFreezedPanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFreezedPanes/)méthode.
1. Construisez Workbook pour ouvrir le fichier.
2. Vérifiez si la feuille de calcul est gelée.
3. Obtient la ligne et les colonnes verrouillées

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Is-Worksheet-Frozen.cs" >}}