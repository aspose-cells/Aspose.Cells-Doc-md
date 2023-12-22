---
title: Geler la ou les lignes supérieures de la feuille de calcul Excel
linktitle: Geler les lignes
type: docs
weight: 190
url: /fr/net/how-to-freeze-rows-of-excel-worksheet
description: Dans cet article, vous apprendrez à geler les lignes supérieures des feuilles de calcul Excel par programme à l'aide de la bibliothèque C# avec .NET API.
keywords: Freeze top rows, Feeze top row.
---
{{% alert color="primary" %}}

Dans cet article, nous apprendrons comment figer la ou les rangées supérieures.
Lorsque vous avez une énorme quantité de données sous un en-tête commun, vous ne pouvez pas voir l'en-tête lorsque vous faites défiler la feuille de calcul. Vous pouvez geler la ou les lignes supérieures afin de pouvoir voir cette partie gelée même lorsque le reste des données défile. Vous pouvez facilement voir les en-têtes dans les rangées supérieures.

{{% /alert %}}

##  **Geler les lignes dans Excel**

**![Geler la ou les lignes supérieures dans Excel](Freeze-Rows.png)**


1. Si vous souhaitez geler la ou les lignes supérieures, sélectionnez d'abord la ligne située sous la ligne qui doit être gelée.
2. Cliquez sur Affichage > Figer les volets.
3. Dans le menu déroulant, cliquez sur Geler la ligne supérieure.
4. Si vous faites défiler vers le bas, la première ligne est toujours en vue de dessus.

**![Ligne Fonzen](Frozen-Row.png)**

Comme vous pouvez le voir, la 1ère ligne est gelée, la première ligne reste toujours en haut de la vue lorsque vous faites défiler vers le bas.

Geler les lignes vous permet de visualiser vos données volumineuses sans aucune trace de l'étiquette de la ligne.




##  **Geler les lignes avec Aspose.Cells pour .Net**
 Il est simple de geler les lignes avec Aspose.Cells pour .Net.
 Veuillez utiliser le[**Feuille de travail.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)méthode pour figer les lignes sur la ligne sélectionnée.
1. Construisez un classeur pour ouvrir le fichier ou créez un fichier vide.
2. Gelez la première ligne avec la méthode Worksheet.FreezePanes().
3. Enregistrez le fichier.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Row.cs" >}}

 Ci-joint[exemple de fichier Excel source](../Freeze.xlsx).
