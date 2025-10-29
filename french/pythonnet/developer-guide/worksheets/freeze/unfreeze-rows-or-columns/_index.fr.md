---
title: Décongeler les lignes ou les colonnes
linktitle: Décongeler les volets
type: docs
weight: 190
url: /fr/python-net/unfreeze-rows-or-columns-of-excel-worksheet
description: Dans cet article, vous apprendrez comment déverrouiller les lignes, colonnes ou volets des feuilles Excel de manière programmatique en utilisant Aspose.Cells pour Python via .NET APIs.
keywords: Bibliothèque Excel Python, Déverrouiller les volets, Comment déverrouiller les lignes, Comment déverrouiller les colonnes, Comment déverrouiller la fenêtre.
---

## **Introduction**

Dans cet article, nous allons apprendre comment dégeler les lignes, les colonnes et les volets. Si les feuilles de calcul des fichiers Excel sont figées, parfois nous voulons dégeler la feuille de calcul ou ajuster les lignes, les colonnes ou les volets figés.


## **Comment déverrouiller les lignes ou colonnes dans Excel**

1. Cliquez sur l'onglet Affichage > Immobiliser les volets > Débloquer les volets.

**![débloquer les volets dans Excel](Unfreeze-Panes.png)**




## **Comment déverrouiller les lignes, colonnes ou volets avec Aspose.Cells pour la bibliothèque Excel Python**
Il est simple de désépingler les volets avec Aspose.Cells pour Python via .NET. Veuillez utiliser la méthode [**Worksheet.un_freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/un_freeze_panes/) pour désépingler les volets.

1. Construisez le classeur pour ouvrir le fichier gelé.
2. Débloquez les volets avec la méthode Worksheet.UnFreezePanes().
3. Enregistrez le fichier.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Unfreeze-Pane.py" >}}

Fichier Excel source joint (Frozen.xlsx).
{{< app/cells/assistant language="python-net" >}}
