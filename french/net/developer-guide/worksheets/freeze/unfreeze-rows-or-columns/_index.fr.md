---
title: Dégeler des lignes ou des colonnes
linktitle: Dégeler les volets
type: docs
weight: 190
url: /fr/net/unfreeze-rows-or-columns-of-excel-worksheet
description: Dans cet article, vous apprendrez comment débloquer des lignes, des colonnes ou des volets de feuilles de calcul Excel par programme à l'aide de la bibliothèque C# avec .NET API.
keywords: Unfreeze panes, Unfreeze rows, Unfreeze columns, unFreeze window.
---
{{% alert color="primary" %}}

Dans cet article, nous apprendrons comment dégeler les lignes, les colonnes et les volets.
Si les feuilles de calcul dans les fichiers Excel sont gelées, nous souhaitons parfois débloquer la feuille de calcul ou ajuster les lignes, colonnes ou volets gelés.

{{% /alert %}}

##  **Dans Excel**

1. Cliquez sur l'onglet Affichage > Geler les volets > Libérer les volets.

**![dégeler les volets dans Excel](Unfreeze-Panes.png)**




##  **Libérez les lignes, les colonnes ou les volets avec Aspose.Cells pour .Net**
 C'est simple de dégeler les volets avec Aspose.Cells pour .Net. Veuillez utiliser le[**Feuille de travail.UnFreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/unfreezepanes)méthode pour dégonfler les vitres.

1. Construisez un classeur pour ouvrir le fichier gelé.
2. Dégelez les volets avec la méthode Worksheet.UnFreezePanes().
3. Enregistrez le fichier.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Unfreeze-Pane.cs" >}}

 Ci-joint[exemple de fichier Excel source](Frozen.xlsx).
