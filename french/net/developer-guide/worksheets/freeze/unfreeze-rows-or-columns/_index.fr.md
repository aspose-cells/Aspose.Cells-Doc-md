---
title: Dégeler des lignes ou des colonnes
linktitle: Dégeler les volets
type: docs
weight: 190
url: /fr/net/unfreeze-rows-or-columns-of-excel-worksheet
description: Dans cet article, vous apprendrez à dégeler des lignes, des colonnes ou des volets de feuilles de calcul Excel par programmation à l'aide de la bibliothèque C# avec .NET API.
keywords: Unfreeze panes, Unfreeze rows, Unfreeze columns, unFreeze window.
---
{{% alert color="primary" %}}

Dans cet article, nous apprendrons comment dégeler des lignes, des colonnes et des volets.
Si les feuilles de calcul dans les fichiers Excel sont gelées, nous souhaitons parfois les dégeler ou ajuster les lignes, colonnes ou volets gelés.

{{% /alert %}}

##  **Dans Excel**

1. Cliquez sur l'onglet Affichage > Figer les volets > Libérer les volets.

**![dégeler les volets dans Excel](Unfreeze-Panes.png)**




##  **Dégelez les lignes, les colonnes ou les volets avec Aspose.Cells pour .Net**
 Il est simple de dégeler les volets avec Aspose.Cells pour .Net. Veuillez utiliser le[**Feuille de calcul.UnFreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/unfreezepanes)méthode pour dégonfler les volets.

1. Construire un classeur pour ouvrir le fichier gelé.
2. Libérez les volets avec la méthode Worksheet.UnFreezePanes().
3. Enregistrez le fichier.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Unfreeze-Pane.cs" >}}

 Ci-joint[exemple de fichier Excel source](Frozen.xlsx).
