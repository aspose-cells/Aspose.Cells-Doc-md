---
title: Geler les volets d'une feuille de calcul Excel
linktitle: Figer les volets
type: docs
weight: 190
url: /fr/net/how-to-freeze-panes-of-excel-worksheet
description: Dans cet article, vous apprendrez à geler des volets de feuilles de calcul Excel par programme à l'aide de la bibliothèque C# avec .NET API.
keywords: Freeze panes, Feeze window.
---
{{% alert color="primary" %}}

Dans cet article, nous apprendrons comment geler les volets.
Lorsque vous avez une énorme quantité de données sous un en-tête commun, vous ne pouvez pas voir l'en-tête lorsque vous faites défiler la feuille de calcul. Et chaque enregistrement contient de nombreuses données. Vous pouvez geler les volets afin de pouvoir voir cette partie gelée même lorsque le reste des données défile. Vous pouvez facilement voir les en-têtes dans les lignes supérieures ou les premières colonnes. Le gel et le dégel des volets modifient uniquement la vue des données sans modifier les données elles-mêmes.

{{% /alert %}}

##  **Dans Excel**

**![Figer les volets dans Excel](Freeze-panes.png)**


1. Si vous souhaitez geler des volets, geler des lignes et des colonnes, sélectionnez d'abord une cellule (telle que B2)
2. Cliquez sur Affichage > Figer les volets.
3. Dans le menu déroulant, cliquez sur Geler les volets.
4. Si vous faites défiler vers le bas ou vers la droite, la première ligne et la première colonne sont gelées.

**![Fonzen volets](Frozen-Panes.png)**

 Comme vous pouvez le voir, la 1ère ligne et la colonne A sont gelées, la deuxième ligne est 32 et la deuxième colonne visible est D.

Les volets gelés vous permettent d'afficher vos données volumineuses sans aucune trace de l'étiquette de ligne ou de colonne.




##  **Geler les volets avec Aspose.Cells pour .Net**
 Il est simple de geler les volets avec Aspose.Cells pour .Net. Veuillez utiliser le[**Feuille de travail.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)méthode pour figer les volets au Cell sélectionné.
1. Construisez un classeur pour ouvrir le fichier ou créez un fichier vide.
2. Gelez les volets avec la méthode Worksheet.FreezePanes().
3. Enregistrez le fichier.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Pane.cs" >}}

 Ci-joint[exemple de fichier Excel source](Freeze.xlsx).
