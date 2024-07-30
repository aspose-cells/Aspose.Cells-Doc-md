---
title: Écran scindé de la feuille de calcul Excel
linktitle: Écran scindé
type: docs
weight: 190
url: /fr/python-net/how-to-split-screen-of-excel-worksheet
description: Dans cet article, vous apprendrez comment afficher certaines lignes et/ou colonnes dans des volets séparés en divisant la feuille de calcul en deux ou quatre parties de manière programmée en utilisant les APIs Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Python Excel, Congeler les lignes supérieures en Python, Congeler la ligne supérieure en Python, Diviser la feuille de calcul verticalement sur les colonnes en Python, Diviser la feuille de calcul horizontalement sur les lignes en Python, Diviser la feuille de calcul en quatre parties en Python Comment supprimer la division.
---

## **Introduction**

Dans cet article, nous allons apprendre comment afficher certaines lignes et/ou colonnes dans des volets séparés en divisant la feuille de calcul en deux ou quatre parties. Lors de la manipulation de grands ensembles de données, nous devons voir quelques zones de la même feuille de calcul à un moment donné pour comparer différents sous-ensembles de données. La fonction de division d'écran peut répondre à vos besoins.

## **Comment scinder l'écran dans Excel**
Pour diviser une feuille de calcul en deux ou quatre parties, procédez comme suit :

1. Sélectionnez la ligne/colonne/cellule avant laquelle vous souhaitez placer la division.
2. Sur l'onglet Affichage, dans le groupe Fenêtres, cliquez sur le bouton Fractionner.

**![Écran partagé](Split-Screen.png)**

## **Comment Diviser la Feuille de Calcul Verticalement par Colonnes**

Pour séparer deux zones de la feuille de calcul verticalement, sélectionnez la colonne à droite de la colonne où vous souhaitez afficher la division et cliquez sur le bouton Fractionner dans Excel.

Il est facile de diviser la feuille de calcul verticalement par colonnes de manière programmée avec Aspose.Cells pour Python via .NET, il suffit de sélectionner une cellule dans la ligne supérieure comme cellule active, puis
fractionner avec la méthode [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Vertically-Split.py" >}}

## **Comment Diviser la Feuille de Calcul Horizontalement par Lignes**
Pour séparer votre fenêtre Excel horizontalement, sélectionnez la ligne en dessous de la ligne où vous souhaitez que la division se produise dans Excel.

Il est facile de diviser la feuille de calcul horizontalement par lignes de manière programmée avec Aspose.Cells pour Python via .NET, il suffit de sélectionner une cellule dans la colonne de gauche comme cellule active, puis
fractionner avec la méthode [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Horizontally-Split.py" >}}

## **Comment Diviser la Feuille de Calcul en Quatre Parties**
Pour afficher quatre sections différentes de la même feuille de calcul simultanément, divisez votre écran à la fois verticalement et horizontalement dans Excel.

Il est facile de diviser la feuille de calcul verticalement par colonnes de manière programmée avec Aspose.Cells pour Python via .NET, il suffit de sélectionner une cellule qui n'est pas dans la première ligne et colonne comme cellule active, puis
fractionner avec la méthode [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Split-Four.py" >}}

## **Comment Supprimer la Division**
Pour supprimer la division de la feuille de calcul, il suffit de cliquer à nouveau sur le bouton Fractionner.

Aspose.Cells pour Python via .NET fournit une méthode [**Worksheet.remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split/) pour supprimer le paramètre de division.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Remove-Split.py" >}}
