---
title: Comment vérifier l état de gel sans Excel.
linktitle: État figé
type: docs
weight: 190
url: /fr/python-net/how-to-check-frozen-state-of-excel-worksheet
description: Dans cet article, vous apprendrez comment vérifier l état de gel d une feuille Excel de manière programmatique en utilisant Aspose.Cells pour Python via .NET APIs.
keywords: Bibliothèque Excel Python, Comment vérifier l état de gel sans Excel en Python, Vérifier l état de gel sans Excel en Python.
---

## **Introduction**

Dans cet article, nous apprendrons comment vérifier de manière programmatique l'état de gel d'une feuille Excel. Nous pouvons simplement vérifier si la feuille est gelée ou splittée dans MS Excel. Mais existe-t-il une méthode pour le faire en CSharp ? Nous pouvons le faire simplement avec Aspose.Cells pour Python via .NET.

## **Comment vérifier l'état de gel**
Avec Aspose.Cells pour Python via .NET, nous pouvons vérifier si la fenêtre est gelée et combien de lignes et colonnes sont verrouillées.

Veuillez utiliser la propriété [**Worksheet.pane_state**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/pane_state/) pour vérifier l'état des volets de la fenêtre 
et obtenir les lignes et colonnes verrouillées avec la méthode [**Worksheet.get_freezed_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/get_freezed_panes/#any-any-any-any)
1. Construisez un classeur pour ouvrir le fichier.
2. Vérifiez si la feuille de calcul est gelée.
3. Obtenez les lignes et colonnes verrouillées

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Is-Worksheet-Frozen.py" >}}
{{< app/cells/assistant language="python-net" >}}
