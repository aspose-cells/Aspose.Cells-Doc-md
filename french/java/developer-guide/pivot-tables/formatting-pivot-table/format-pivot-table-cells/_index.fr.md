---
title: Formatter les cellules du tableau croisé dynamique
type: docs
weight: 20
url: /fr/java/format-pivot-table-cells/
---

{{% alert color="primary" %}}

Parfois, vous souhaitez formater les cellules de tableau croisé dynamique. Par exemple, vous souhaitez appliquer une couleur de fond aux cellules de tableau croisé dynamique. Aspose.Cells propose deux méthodes [**PivotTable.formatAll()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#formatAll(com.aspose.cells.Style)) et [**PivotTable.format()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#format(int,%20int,%20com.aspose.cells.Style)), que vous pouvez utiliser à cet effet.

[**PivotTable.formatAll()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#formatAll(com.aspose.cells.Style)) applique le style à l'ensemble du tableau croisé dynamique tandis que [**PivotTable.format()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#format(int,%20int,%20com.aspose.cells.Style)) applique le style à une seule cellule du tableau croisé dynamique.

{{% /alert %}}

Le code d'exemple suivant formate l'ensemble du tableau croisé dynamique avec une couleur bleu clair, puis formate la deuxième ligne du tableau en jaune.

**Le tableau croisé dynamique d'entrée, avant l'exécution du code**

![todo:image_alt_text](format-pivot-table-cells_1.png)

**Le tableau croisé dynamique de sortie, après l'exécution du code**

![todo:image_alt_text](format-pivot-table-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FormatPivotTableCells-FormatPivotTableCells.java" >}}
