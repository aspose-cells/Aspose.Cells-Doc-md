---
title: Écran scindé de la feuille de calcul Excel
linktitle: Écran scindé
type: docs
weight: 190
url: /fr/python-net/how-to-split-screen-of-excel-worksheet
description: Dans cet article, vous apprendrez comment afficher certaines lignes et/ou colonnes dans des volets séparés en divisant la feuille en deux ou quatre parties de manière programmatique en utilisant Aspose.Cells pour Python via .NET APIs.
keywords: Bibliothèque Excel Python, Figer les lignes du haut en Python, Figer la première ligne en Python, Diviser la feuille verticalement sur les colonnes, Diviser la feuille horizontalement sur les lignes, Diviser la feuille en quatre parties, Comment supprimer la division.
---

## **Introduction**

Dans cet article, nous allons apprendre comment afficher certaines lignes et/ou colonnes dans des volets séparés en divisant la feuille de calcul en deux ou quatre parties. Lors de la manipulation de grands ensembles de données, nous devons voir quelques zones de la même feuille de calcul à un moment donné pour comparer différents sous-ensembles de données. La fonction de division d'écran peut répondre à vos besoins.

## **Comment scinder l'écran dans Excel**
Pour diviser une feuille de calcul en deux ou quatre parties, procédez comme suit :

1. Sélectionnez la ligne/colonne/cellule avant laquelle vous souhaitez placer la division.
2. Sur l'onglet Affichage, dans le groupe Fenêtres, cliquez sur le bouton Fractionner.

**![Écran partagé](Split-Screen.png)**

## **Comment diviser la feuille verticalement sur les colonnes**

Pour séparer deux zones de la feuille de calcul verticalement, sélectionnez la colonne à droite de la colonne où vous souhaitez afficher la division et cliquez sur le bouton Fractionner dans Excel.

Il est facile de diviser la feuille verticalement sur les colonnes de manière programmatique avec Aspose.Cells pour Python via .NET, il suffit de sélectionner une cellule dans la ligne supérieure comme cellule active, puis
fractionner avec la méthode [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Vertically-Split.py" >}}

## **Comment diviser la feuille horizontalement sur les lignes**
Pour séparer votre fenêtre Excel horizontalement, sélectionnez la ligne en dessous de la ligne où vous souhaitez que la division se produise dans Excel.

Il est facile de diviser la feuille horizontalement sur les lignes de manière programmatique avec Aspose.Cells pour Python via .NET, il suffit de sélectionner une cellule dans la colonne de gauche comme cellule active, puis
fractionner avec la méthode [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Horizontally-Split.py" >}}

## **Comment diviser la feuille en quatre parties**
Pour afficher quatre sections différentes de la même feuille de calcul simultanément, divisez votre écran à la fois verticalement et horizontalement dans Excel.

Il est facile de diviser la feuille verticalement sur les colonnes de manière programmatique avec Aspose.Cells pour Python via .NET, il suffit de sélectionner une cellule qui n'est pas dans la première ligne et la première colonne comme cellule active, puis
fractionner avec la méthode [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Split-Four.py" >}}

## **Comment supprimer la division**
Pour supprimer la division de la feuille de calcul, il suffit de cliquer à nouveau sur le bouton Fractionner.

Aspose.Cells pour Python via .NET fournit une méthode [**Worksheet.remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split/) pour supprimer la configuration de division.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Remove-Split.py" >}}
{{< app/cells/assistant language="python-net" >}}
