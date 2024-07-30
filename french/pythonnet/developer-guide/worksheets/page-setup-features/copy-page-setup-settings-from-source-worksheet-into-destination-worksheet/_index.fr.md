---
title: Copier les paramètres de mise en page de la feuille de calcul source dans la feuille de calcul de destination
type: docs
weight: 80
url: /fr/python-net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Cet article explique comment utiliser le code d exemple Aspose.Cells pour Python via .NET pour copier les paramètres de configuration de page de la feuille de calcul source dans la feuille de calcul de destination de manière programmée.
keywords: Bibliothèque Python Excel, Copier les paramètres de configuration de page, Copier les paramètres de configuration de page vers la feuille de calcul cible en Python.
---

## **Scénarios d'utilisation possibles**

Lorsque vous ajoutez une nouvelle feuille à un classeur, elle contient les paramètres de *configuration de page* par défaut. Il peut arriver que vous ayez besoin de transférer les paramètres ([**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)) d'une feuille de calcul à une autre feuille de calcul. Ce document explique comment copier les paramètres de configuration de page d'une feuille de calcul à une autre en utilisant les APIs Aspose.Cells pour Python via .NET.

## **Copier les paramètres de configuration de la page de la feuille source dans la feuille de destination**

Le code d'exemple suivant illustre comment copier les *paramètres de configuration de la page* d'une feuille à une autre en utilisant la méthode [**PageSetup.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/copy/#aspose.cells.PageSetup-aspose.cells.CopyOptions). Veuillez consulter le code d'exemple suivant et sa sortie console pour référence.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.py" >}}

## **Sortie console**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
