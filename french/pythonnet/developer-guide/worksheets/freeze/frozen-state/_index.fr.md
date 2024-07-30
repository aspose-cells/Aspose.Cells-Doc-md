---
title: Comment vérifier l état figé sans Excel.
linktitle: État figé
type: docs
weight: 190
url: /fr/python-net/how-to-check-frozen-state-of-excel-worksheet
description: Dans cet article, vous apprendrez comment vérifier l état figé d une feuille de calcul Excel de manière programmable en utilisant Aspose.Cells pour Python via .NET APIs.
keywords: Bibliothèque Excel Python, Comment vérifier l état figé sans Excel, Vérifier l état figé sans Excel en Python.
---

## **Introduction**

Dans cet article, nous apprendrons comment vérifier l'état figé d'une feuille de calcul Excel de manière programmable. Nous pouvons simplement savoir si la feuille de calcul est figée ou divisée dans MS Excel. Mais y a-t-il un moyen de savoir si elle est figée ou divisée avec CSharp. Nous pouvons simplement le faire avec Aspose.Cells pour Python via .NET.

## **Comment vérifier l'état figé**
Avec Aspose.Cells pour Python via .NET, nous pouvons vérifier si la fenêtre est figée et combien de lignes et de colonnes sont verrouillées.

Veuillez utiliser la propriété [**Worksheet.pane_state**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/pane_state/) pour vérifier l'état des volets de la fenêtre 
et obtenir les lignes et colonnes verrouillées avec la méthode [**Worksheet.get_freezed_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/get_freezed_panes/#any-any-any-any)
1. Construisez un classeur pour ouvrir le fichier.
2. Vérifiez si la feuille de calcul est gelée.
3. Obtenez les lignes et colonnes verrouillées

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Is-Worksheet-Frozen.py" >}}
