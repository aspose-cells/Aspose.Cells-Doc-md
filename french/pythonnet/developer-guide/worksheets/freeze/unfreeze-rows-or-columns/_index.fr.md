---
title: Décongeler les lignes ou les colonnes
linktitle: Décongeler les volets
type: docs
weight: 190
url: /fr/python-net/unfreeze-rows-or-columns-of-excel-worksheet
description: Dans cet article, vous apprendrez comment déverrouiller les lignes, colonnes ou volets des feuilles de calcul Excel de manière programmée en utilisant les APIs Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Python Excel, Déverrouiller les volets en Python, Comment déverrouiller les lignes en Python, Comment déverrouiller les colonnes en Python, Comment déverrouiller la fenêtre en Python.
---

## **Introduction**

Dans cet article, nous allons apprendre comment dégeler les lignes, les colonnes et les volets. Si les feuilles de calcul des fichiers Excel sont figées, parfois nous voulons dégeler la feuille de calcul ou ajuster les lignes, les colonnes ou les volets figés.


## **Comment Déverrouiller les Lignes ou Colonnes dans Excel**

1. Cliquez sur l'onglet Affichage > Immobiliser les volets > Débloquer les volets.

**![débloquer les volets dans Excel](Unfreeze-Panes.png)**




## **Comment Déverrouiller les Lignes, Colonnes ou Volets avec la Bibliothèque Excel Aspose.Cells pour Python**
Il est simple de déverrouiller les volets avec Aspose.Cells pour Python via .NET. Veuillez utiliser la méthode [**Worksheet.un_freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/un_freeze_panes/) pour déverrouiller les volets .

1. Construisez le classeur pour ouvrir le fichier gelé.
2. Débloquez les volets avec la méthode Worksheet.UnFreezePanes().
3. Enregistrez le fichier.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Unfreeze-Pane.py" >}}

Fichier Excel source joint (Frozen.xlsx).
