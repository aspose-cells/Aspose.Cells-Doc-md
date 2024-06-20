---
title: Déterminer si la taille du papier de la feuille de calcul est automatique
type: docs
weight: 90
url: /fr/net/determine-if-paper-size-of-worksheet-is-automatic/
description: Cet article explique comment utiliser l API C# ou le code d exemple de la bibliothèque .NET pour déterminer si la taille du papier de la feuille de calcul est automatique de manière programmatique.
keywords: déterminer si la taille du papier de la feuille de calcul est automatique en c#
---

## **Scénarios d'utilisation possibles**

La plupart du temps, la taille du papier de la feuille de calcul est automatique. Lorsqu'elle est automatique, elle est souvent définie comme *Lettre*. Parfois, l'utilisateur définit la taille du papier de la feuille de calcul selon ses besoins. Dans ce cas, la taille du papier n'est pas automatique. Vous pouvez déterminer si la taille du papier de la feuille de calcul est automatique ou non en utilisant la propriété [**Worksheet.PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/isautomaticpapersize).

## **Déterminer si la taille du papier de la feuille de calcul est automatique**

Le code d'exemple ci-dessous charge les deux fichiers Excel suivants

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

et détermine si la taille du papier de leur première feuille de calcul est automatique ou non. Dans Microsoft Excel, vous pouvez vérifier si la taille du papier est automatique ou non via la fenêtre de configuration de la page comme indiqué dans cette capture d'écran.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.cs" >}}

## **Sortie console**

Voici la sortie console du code d'exemple ci-dessus lorsqu'il est exécuté avec les fichiers Excel d'exemple donnés.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
