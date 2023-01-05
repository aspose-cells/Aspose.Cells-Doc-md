---
title: Fusionner des fichiers
type: docs
weight: 20
url: /fr/net/merge-files/
---
## **Introduction**

 Aspose.Cells fournit différentes manières de fusionner des fichiers. Pour les fichiers simples contenant des données, une mise en forme et des formules, le[**Classeur. Combiner ()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine) méthode peut être utilisée pour combiner plusieurs classeurs, et la[**Feuille de travail.Copier()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index)peut être utilisée pour copier des feuilles de calcul dans un nouveau classeur. Ces méthodes sont faciles à utiliser et efficaces, mais si vous avez beaucoup de fichiers à fusionner, vous constaterez peut-être qu'elles consomment beaucoup de ressources système. Pour éviter cela, utilisez le[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)méthode statique, un moyen plus efficace de fusionner plusieurs fichiers.

## **Fusionner des fichiers à l'aide de Aspose.Cells**

 L'exemple de code suivant illustre comment fusionner des fichiers volumineux à l'aide de[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)méthode. Il faut deux fichiers simples mais volumineux, Book1.xls et Book2.xls. Les fichiers contiennent uniquement des données formatées et des formules.

{{% alert color="primary" %}}

 Le[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles) prend uniquement en charge la fusion de données, de styles, de mise en forme et de formules. Les objets tels que les graphiques, les images, les commentaires ou d'autres objets peuvent ne pas être fusionnés à l'aide de cette méthode. De plus, un fichier en cache est utilisé pour stocker des données temporaires pour le processus.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-MergeFiles-1.cs" >}}
