---
title: Fusionner des fichiers
type: docs
weight: 20
url: /fr/net/merge-files/
---

## **Introduction**

Aspose.Cells propose différentes façons de fusionner des fichiers. Pour des fichiers simples avec des données, des mises en forme et des formules, la méthode [**Workbook.Combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine) peut être utilisée pour combiner plusieurs classeurs, et la méthode [**Worksheet.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index) peut être utilisée pour copier des feuilles de calcul dans un nouveau classeur. Ces méthodes sont simples à utiliser et efficaces, mais si vous avez beaucoup de fichiers à fusionner, vous pourriez constater qu'elles consomment beaucoup de ressources système. Pour éviter cela, utilisez la méthode statique [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles), une façon plus efficace de fusionner plusieurs fichiers.

## **Fusionner des fichiers à l'aide d'Aspose.Cells**

Le code d'exemple suivant illustre comment fusionner des fichiers volumineux en utilisant la méthode [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles). Il prend deux fichiers simples mais volumineux, Book1.xls et Book2.xls. Les fichiers ne contiennent que des données mises en forme et des formules.

{{% alert color="primary" %}}

La méthode [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles) prend uniquement en charge la fusion de données, de styles, de mises en forme et de formules. Des objets comme les graphiques, les images, les commentaires ou autres objets pourraient ne pas être fusionnés en utilisant cette méthode. De plus, un fichier mis en cache est utilisé pour stocker des données temporaires pour le processus.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-MergeFiles-1.cs" >}}
