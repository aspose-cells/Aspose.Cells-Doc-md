---
title: Formatter les cellules du tableau croisé dynamique
type: docs
weight: 20
url: /fr/python-java/format-pivot-table-cells/
---

{{% alert color="primary" %}}

Parfois, vous souhaitez formater les cellules de tableau croisé dynamique. Par exemple, vous souhaitez appliquer une couleur de fond aux cellules de tableau croisé dynamique. Aspose.Cells propose deux méthodes [**PivotTable.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style)) et [**PivotTable.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)), que vous pouvez utiliser à cet effet.

[**PivotTable.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style)) applique le style à l'ensemble du tableau croisé dynamique tandis que [**PivotTable.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)) applique le style à une seule cellule du tableau croisé dynamique.

{{% /alert %}}

Le code d'exemple suivant formate l'ensemble du tableau croisé dynamique avec une couleur bleu clair, puis formate la deuxième ligne du tableau en jaune.

**Le tableau croisé dynamique d'entrée, avant l'exécution du code**

![todo:image_alt_text](format-pivot-table-cells_1.png)

**Le tableau croisé dynamique de sortie, après l'exécution du code**

![todo:image_alt_text](format-pivot-table-cells_2.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-FormatCells.py" >}}
