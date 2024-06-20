---
title: Copier les paramètres de mise en page de la feuille de calcul source dans la feuille de calcul de destination
type: docs
weight: 80
url: /fr/net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Cet article explique comment utiliser le code d exemple de l API C# ou de la bibliothèque .NET pour copier les paramètres de mise en page de la feuille de calcul source dans la feuille de calcul de destination de manière programmatique.
keywords: copier les paramètres de configuration de la page en c#, copier les paramètres de configuration de la page vers la feuille de calcul cible en c#
---

## **Scénarios d'utilisation possibles**

Lorsque vous ajoutez une nouvelle feuille à un classeur, elle contient les paramètres par défaut de *configuration de la page*. Il peut arriver que vous ayez besoin de transférer les paramètres ([**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)) d'une feuille à une autre. Ce document explique comment copier les paramètres de configuration de la page d'une feuille à une autre à l'aide des API Aspose.Cells.

## **Copier les paramètres de configuration de la page de la feuille source dans la feuille de destination**

Le code d'exemple suivant illustre comment copier les *paramètres de configuration de la page* d'une feuille à une autre en utilisant la méthode [**PageSetup.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/copy). Veuillez consulter le code d'exemple suivant et sa sortie console pour référence.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.cs" >}}

## **Sortie console**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
