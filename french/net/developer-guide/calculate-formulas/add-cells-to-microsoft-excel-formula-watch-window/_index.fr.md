---
title: Ajouter des cellules à la fenêtre de surveillance des formules Microsoft Excel
description: Comment utiliser la bibliothèque Aspose.Cells pour ajouter des cellules à la fenêtre de surveillance des formules dans Excel. En chargeant un fichier Excel existant ou en en créant un nouveau, nous pouvons manipuler les cellules et définir des formules. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, Fenêtre de surveillance des formules, Cellules, Ajout
type: docs
weight: 60
url: /fr/net/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Scénarios d'utilisation possibles**

La fenêtre de surveillance Microsoft Excel est un outil utile pour visualiser facilement les valeurs de cellules et ses formules dans une fenêtre. Vous pouvez ouvrir la *Fenêtre de surveillance* en cliquant sur *Formules > Surveiller Fenêtre*. Elle possède le bouton *Nouvelle montre* qui peut être utilisé pour ajouter les cellules à inspecter. De même, vous pouvez utiliser la méthode [**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/net/aspose.cells/cellwatchcollection/methods/add/index) pour ajouter des cellules à la *Fenêtre de surveillance* à l'aide de l'API Aspose.Cells.

## **Ajouter des cellules à la fenêtre de surveillance des formules Microsoft Excel**

Le code d'exemple suivant définit la formule des cellules C1 et E1 et les ajoute toutes les deux à la fenêtre de surveillance. Ensuite, il enregistre le classeur sous forme de [fichier Excel de sortie](67338481.xlsx). Si vous ouvrez le fichier Excel de sortie et affichez la *Fenêtre de surveillance*, vous verrez les deux cellules comme indiqué dans cette capture d'écran.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.cs" >}}
{{< app/cells/assistant language="csharp" >}}
