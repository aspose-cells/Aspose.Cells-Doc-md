---
title: Fusionner des fichiers
type: docs
weight: 20
url: /fr/python-net/merge-files/
---

## **Introduction**

Aspose.Cells pour Python via .NET propose différentes méthodes pour fusionner des fichiers. Pour des fichiers simples avec des données, une mise en forme et des formules, la méthode [**Workbook.combine()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/combine) peut être utilisée pour combiner plusieurs classeurs, et la méthode [**Worksheet.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/copy) peut être utilisée pour copier des feuilles dans un nouveau classeur. Ces méthodes sont faciles à utiliser et efficaces, mais si vous avez beaucoup de fichiers à fusionner, vous pourriez constater qu'elles consomment beaucoup de ressources système. Pour éviter cela, utilisez la méthode statique [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files), une manière plus efficace de fusionner plusieurs fichiers.

## **Fusionner des fichiers avec Aspose.Cells pour Python via .NET**

Le code d'exemple suivant illustre comment fusionner des fichiers volumineux en utilisant la méthode [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files). Il prend deux fichiers simples mais volumineux, Book1.xls et Book2.xls. Les fichiers ne contiennent que des données mises en forme et des formules.

{{% alert color="primary" %}}

La méthode [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files) prend uniquement en charge la fusion de données, de styles, de mises en forme et de formules. Des objets comme les graphiques, les images, les commentaires ou autres objets pourraient ne pas être fusionnés en utilisant cette méthode. De plus, un fichier mis en cache est utilisé pour stocker des données temporaires pour le processus.

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Merge-Workbooks-CellsHelperClass-MergeFiles-1.py" >}}

