---
title: Décongeler les lignes ou les colonnes
linktitle: Décongeler les volets
type: docs
weight: 190
url: /fr/net/unfreeze-rows-or-columns-of-excel-worksheet
description: Dans cet article, vous apprendrez comment débloquer les lignes, les colonnes ou les volets des feuilles de calcul Excel de manière programmatique en utilisant la bibliothèque C# avec l API .NET.
keywords: Débloquer les volets, Débloquer les lignes, Débloquer les colonnes, Débloquer la fenêtre.
---

## **Introduction**

Dans cet article, nous allons apprendre comment dégeler les lignes, les colonnes et les volets. Si les feuilles de calcul des fichiers Excel sont figées, parfois nous voulons dégeler la feuille de calcul ou ajuster les lignes, les colonnes ou les volets figés.


## **Dans Excel**

1. Cliquez sur l'onglet Affichage > Immobiliser les volets > Débloquer les volets.

**![débloquer les volets dans Excel](Unfreeze-Panes.png)**




## **Débloquer les lignes, les colonnes ou les volets avec Aspose.Cells pour .Net**
Il est simple de débloquer les volets avec Aspose.Cells pour .Net. Veuillez utiliser la méthode [**Worksheet.UnFreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/unfreezepanes) pour débloquer les volets.

1. Construisez le classeur pour ouvrir le fichier gelé.
2. Débloquez les volets avec la méthode Worksheet.UnFreezePanes().
3. Enregistrez le fichier.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Unfreeze-Pane.cs" >}}

Fichier Excel source joint (Frozen.xlsx).
{{< app/cells/assistant language="csharp" >}}
