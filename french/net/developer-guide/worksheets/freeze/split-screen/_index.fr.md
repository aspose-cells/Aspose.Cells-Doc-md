---
title: Écran scindé de la feuille de calcul Excel
linktitle: Écran scindé
type: docs
weight: 190
url: /fr/net/how-to-split-screen-of-excel-worksheet
description: Dans cet article, vous apprendrez comment afficher certaines lignes et/ou colonnes dans des volets séparés en divisant la feuille de calcul en deux ou quatre parties de manière programmatique en utilisant la bibliothèque C# avec l API .NET.
keywords: Geler les premières lignes, Geler la première ligne.
---

## **Introduction**

Dans cet article, nous allons apprendre comment afficher certaines lignes et/ou colonnes dans des volets séparés en divisant la feuille de calcul en deux ou quatre parties. Lors de la manipulation de grands ensembles de données, nous devons voir quelques zones de la même feuille de calcul à un moment donné pour comparer différents sous-ensembles de données. La fonction de division d'écran peut répondre à vos besoins.

## **Comment scinder l'écran dans Excel**
Pour diviser une feuille de calcul en deux ou quatre parties, procédez comme suit :

1. Sélectionnez la ligne/colonne/cellule avant laquelle vous souhaitez placer la division.
2. Sur l'onglet Affichage, dans le groupe Fenêtres, cliquez sur le bouton Fractionner.

**![Écran partagé](Split-Screen.png)**

## **Fractionner la feuille de calcul verticalement sur les colonnes**

Pour séparer deux zones de la feuille de calcul verticalement, sélectionnez la colonne à droite de la colonne où vous souhaitez afficher la division et cliquez sur le bouton Fractionner dans Excel.

Il est facile de fractionner la feuille de calcul verticalement sur les colonnes de manière programmée avec Aspose.Cells pour .Net, nous devons uniquement sélectionner une cellule dans la ligne supérieure en tant que cellule active, puis
fractionner avec la méthode [**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Vertically-Split.cs" >}}

## **Fractionner la feuille de calcul horizontalement sur les lignes**
Pour séparer votre fenêtre Excel horizontalement, sélectionnez la ligne en dessous de la ligne où vous souhaitez que la division se produise dans Excel.

Il est facile de fractionner la feuille de calcul horizontalement sur les lignes de manière programmée avec Aspose.Cells pour .Net, nous devons uniquement sélectionner une cellule dans la colonne de gauche en tant que cellule active, puis
fractionner avec la méthode [**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Horizontally-Split.cs" >}}

## **Fractionner la feuille de calcul en quatre parties**
Pour afficher quatre sections différentes de la même feuille de calcul simultanément, divisez votre écran à la fois verticalement et horizontalement dans Excel.

Il est facile de fractionner la feuille de calcul verticalement sur les colonnes de manière programmée avec Aspose.Cells pour .Net, nous devons uniquement sélectionner une cellule qui n'est pas dans la première ligne et la première colonne en tant que cellule active, puis
fractionner avec la méthode [**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Split-Four.cs" >}}

## **Comment supprimer la division**
Pour supprimer la division de la feuille de calcul, il suffit de cliquer à nouveau sur le bouton Fractionner.

Aspose.Cells pour .Net fournit une méthode [**Worksheet.RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/removesplit/) pour supprimer le paramètre de division.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Remove-Split.cs" >}}
