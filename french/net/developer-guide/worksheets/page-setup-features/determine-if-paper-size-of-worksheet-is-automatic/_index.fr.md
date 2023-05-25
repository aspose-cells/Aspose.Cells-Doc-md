---
title: Déterminer si la taille du papier de la feuille de calcul est automatique
type: docs
weight: 90
url: /fr/net/determine-if-paper-size-of-worksheet-is-automatic/
description: Cet article explique comment utiliser l'exemple de code de la bibliothèque C# API ou .NET pour déterminer si la taille du papier de la feuille de calcul est automatique par programme.
keywords: determine if paper size of worksheet automatic c#
---
##  **Scénarios d'utilisation possibles**

 La plupart du temps, le format de papier de la feuille de calcul est automatique. Lorsqu'il est automatique, il est souvent défini sur *Lettre*. Parfois, l'utilisateur définit le format de papier de la feuille de calcul en fonction de ses besoins. Dans ce cas, le format du papier n'est pas automatique. Vous pouvez savoir si le format de papier de la feuille de calcul est automatique ou non en utilisant le[**Feuille de calcul.PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/isautomaticpapersize)propriété.

##  **Déterminer si la taille du papier de la feuille de calcul est automatique**

L'exemple de code ci-dessous charge les deux fichiers Excel suivants

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

et trouver si le format de papier de leur première feuille de calcul est automatique ou non. Dans Microsoft Excel, vous pouvez vérifier si le format du papier est automatique ou non via la fenêtre Mise en page, comme indiqué dans cette capture d'écran.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

##  **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.cs" >}}

##  **Sortie console**

Voici la sortie de la console de l'exemple de code ci-dessus lorsqu'il est exécuté avec les exemples de fichiers Excel donnés.

{{< highlight "java" >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
