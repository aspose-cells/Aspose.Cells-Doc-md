---
title: Ajouter des cellules à la fenêtre de surveillance des formules Microsoft Excel
type: docs
weight: 20
url: /fr/java/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Scénarios d'utilisation possibles**

La fenêtre de surveillance de Microsoft Excel est un outil utile pour surveiller les valeurs des cellules et leurs formules de manière pratique dans une fenêtre. Vous pouvez ouvrir la fenêtre de surveillance en cliquant sur *Formules > Surveiller*. Il a le bouton *Ajouter une surveillance* qui peut être utilisé pour ajouter les cellules à inspecter. De même, vous pouvez utiliser la méthode [**Worksheet.getCellWatches().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/cellwatchcollection#add(int,%20int)) pour ajouter des cellules à la fenêtre de surveillance à l'aide de l'API Aspose.Cells.

## **Ajouter des cellules à la fenêtre de surveillance des formules Microsoft Excel**

Le code d'exemple suivant définit la formule des cellules C1 et E1 et les ajoute toutes les deux à la *Watch Window*. Ensuite, il enregistre le classeur sous le nom de fichier Excel de sortie. Si vous ouvrez le fichier Excel de sortie et affichez la *Watch Window*, vous verrez les deux cellules comme indiqué dans cette capture d'écran.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.java" >}}
