---
title: Copier les paramètres de mise en page de la feuille de calcul source dans la feuille de calcul de destination
type: docs
weight: 80
url: /fr/python-net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Cet article explique comment utiliser le code d exemple Aspose.Cells pour Python via .NET pour copier les paramètres de la configuration de la page d une feuille source vers une feuille de destination de manière programmatique.
keywords: Bibliothèque Excel en Python, copie des paramètres de la configuration de la page, copie des paramètres de la configuration de la page vers la feuille cible en Python.
---

## **Scénarios d'utilisation possibles**

Lorsque vous ajoutez une nouvelle feuille à un classeur, elle contient les paramètres par défaut *Configuration de la page*. Il peut arriver que vous deviez transférer ces paramètres ([**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)) d'une feuille à une autre. Ce document explique comment copier les paramètres de la configuration de la page d'une feuille à une autre en utilisant les API Aspose.Cells pour Python via .NET.

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
{{< app/cells/assistant language="python-net" >}}
