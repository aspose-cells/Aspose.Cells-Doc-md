---
title: Formater le tableau croisé dynamique Cells
type: docs
weight: 20
url: /fr/python-java/format-pivot-table-cells/
---
{{% alert color="primary" %}}

 Parfois, vous souhaitez formater des cellules de tableau croisé dynamique. Par exemple, vous souhaitez appliquer une couleur d'arrière-plan aux cellules d'un tableau croisé dynamique. Aspose.Cells fournit deux méthodes[**Tableau croisé dynamique.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style) ) et[**Tableau croisé dynamique.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)), que vous pouvez utiliser à cette fin.

[**Tableau croisé dynamique.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style) ) applique le style à l'ensemble du tableau croisé dynamique tandis que[**Tableau croisé dynamique.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)) applique le style à une seule cellule du tableau croisé dynamique.

{{% /alert %}}

L'exemple de code suivant met en forme l'intégralité du tableau croisé dynamique avec une couleur bleu clair, puis met en forme la deuxième ligne du tableau en jaune.

**Le tableau croisé dynamique d'entrée, avant l'exécution du code**

![tâche : image_autre_texte](format-pivot-table-cells_1.png)

**Le tableau croisé dynamique de sortie, après l'exécution du code**

![tâche : image_autre_texte](format-pivot-table-cells_2.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-FormatCells.py" >}}
