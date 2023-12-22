---
title: Écran partagé de la feuille de calcul Excel
linktitle: Écran divisé
type: docs
weight: 190
url: /fr/net/how-to-split-screen-of-excel-worksheet
description: Dans cet article, vous apprendrez comment afficher certaines lignes et/ou colonnes dans des volets séparés en divisant la feuille de calcul en deux ou quatre parties par programme à l'aide de la bibliothèque C# avec .NET API.
keywords: Freeze top rows, Feeze top row.
---
{{% alert color="primary" %}}

Dans cet article, nous apprendrons comment afficher certaines lignes et/ou colonnes dans des volets séparés en divisant la feuille de calcul en deux ou quatre parties.
Lorsque nous travaillons avec de grands ensembles de données, nous devons voir quelques zones de la même feuille de calcul à la fois pour comparer différents sous-ensembles de données.
La fonction d'écran partagé peut répondre à vos besoins.

{{% /alert %}}

##  **Comment diviser l'écran dans Excel**
Pour diviser une feuille de calcul en deux ou quatre parties, procédez comme suit :

1. Sélectionnez la ligne/colonne/cellule avant laquelle vous souhaitez placer la division.
2. Sous l'onglet Affichage, dans le groupe Windows, cliquez sur le bouton Fractionner.

**![Écran partagé](Split-Screen.png)**

##  **Diviser la feuille de calcul verticalement sur les colonnes**

Pour séparer verticalement deux zones de la feuille de calcul, sélectionnez la colonne à droite de la colonne dans laquelle vous souhaitez que la division apparaisse et cliquez sur le bouton Fractionner dans Excel.

Il est facile de diviser une feuille de calcul verticalement en colonnes par programme avec Aspose.Cells pour .Net, il suffit de sélectionner une cellule dans la rangée supérieure comme cellule active, puis
se séparer avec[**Feuille de calcul.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) méthode.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Vertically-Split.cs" >}}

##  **Diviser la feuille de calcul horizontalement sur les lignes**
Pour séparer votre fenêtre Excel horizontalement, sélectionnez la ligne située sous la ligne où vous souhaitez que la division se produise dans Excel.

Il est facile de diviser une feuille de calcul horizontalement en lignes par programme avec Aspose.Cells pour .Net, il suffit de sélectionner une cellule dans la colonne de gauche comme cellule active, puis
se séparer avec[**Feuille de calcul.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) méthode.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Horizontally-Split.cs" >}}

##  **Diviser la feuille de calcul en quatre parties**
Pour afficher simultanément quatre sections différentes de la même feuille de calcul, divisez votre écran verticalement et horizontalement dans Excel.

Il est facile de diviser une feuille de calcul verticalement en colonnes par programme avec Aspose.Cells pour .Net, il suffit de sélectionner une cellule qui ne se trouve pas dans la première ligne et la première colonne comme cellule active, puis
se séparer avec[**Feuille de calcul.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) méthode.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Split-Four.cs" >}}

##  **Comment supprimer la scission**
Pour supprimer le fractionnement de la feuille de calcul, cliquez simplement à nouveau sur le bouton Fractionner.

 Aspose.Cells pour .Net fournit un[**Feuille de calcul.RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/removesplit/) méthode pour supprimer le paramètre de partage.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Remove-Split.cs" >}}