---
title: Figer les volets de la feuille de calcul Excel
linktitle: Figer les volets
type: docs
weight: 190
url: /fr/net/how-to-freeze-panes-of-excel-worksheet
description: Dans cet article, vous apprendrez à figer des volets de feuilles de calcul Excel par programme à l'aide de la bibliothèque C# avec .NET API.
keywords: Freeze panes, Feeze window.
---
{{% alert color="primary" %}}

Dans cet article, nous allons apprendre à figer les volets.
Lorsque vous avez une énorme quantité de données sous un en-tête commun, vous ne pouvez pas voir l'en-tête lorsque vous faites défiler la feuille de calcul. Et chaque enregistrement contient de nombreuses données. Vous pouvez figer les volets afin de voir cette partie figée même lorsque le reste des données défile. Vous pouvez facilement voir les en-têtes dans les lignes supérieures ou les premières colonnes. Le gel et le dégel des volets ne modifient que la vue des données sans modifier les données elles-mêmes.

{{% /alert %}}

##  **Dans Excel**

**![figer les volets dans Excel](Freeze-panes.png)**


1. Si vous souhaitez figer les volets pour figer les lignes et les colonnes, sélectionnez d'abord une cellule (telle que B2)
2. Cliquez sur Affichage > Figer les volets.
3. Dans le menu déroulant, cliquez sur Figer les volets.
4. Si vous faites défiler vers le bas ou vers la droite, la première ligne et la première colonne sont figées.

**![Fonzen panges](Frozen-Panes.png)**

Comme vous pouvez le voir, la 1ère ligne et la colonne A sont gelées, la deuxième ligne son affichage est 32 et la deuxième colonne visible est D.

Les volets de gel vous permettent de visualiser vos données volumineuses sans suivre l'étiquette de la ligne ou de la colonne.




##  **Figer les volets avec Aspose.Cells pour .Net**
 Il est simple de geler les volets avec Aspose.Cells pour .Net. Veuillez utiliser le[**Feuille de calcul.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)méthode pour figer les vitres au Cell sélectionné.
1. Construire un classeur pour ouvrir le fichier ou créer un fichier vide.
2. Figer les volets avec la méthode Worksheet.FreezePanes().
3. Enregistrez le fichier.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Pane.cs" >}}

 Ci-joint[exemple de fichier Excel source](Freeze.xlsx).
