---
title: Fusionner des fichiers
type: docs
weight: 10
url: /fr/java/merge-files/
---
## **Introduction**

 Aspose.Cells fournit différentes manières de fusionner des fichiers. Pour les fichiers simples contenant des données, une mise en forme et des formules, le[**Classeur.combine()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#combine(com.aspose.cells.Workbook) peut être utilisée pour combiner plusieurs classeurs, et la[**Feuille de calcul.copie(**)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)) peut être utilisée pour copier des feuilles de calcul dans un nouveau classeur. Ces méthodes sont faciles à utiliser et efficaces, mais si vous avez beaucoup de fichiers à fusionner, vous constaterez peut-être qu'elles consomment beaucoup de ressources système. Pour éviter cela, utilisez la méthode statique CellsHelper.mergeFiles, un moyen plus efficace de fusionner plusieurs fichiers.

## **Fusionner des fichiers à l'aide de Aspose.Cells**

L'exemple de code suivant illustre comment fusionner des fichiers volumineux à l'aide de la méthode CellsHelper.mergeFiles. Il faut deux fichiers simples mais volumineux, MyBook1.xls et MyBook2.xls. Les fichiers contiennent uniquement des données formatées et des formules.

{{% alert color="primary" %}}

La méthode CellsHelper.mergeFiles prend uniquement en charge la fusion de données, de styles, de mise en forme et de formules. Les objets tels que les graphiques, les images, les commentaires ou d'autres objets peuvent ne pas être fusionnés à l'aide de cette méthode. De plus, un fichier en cache est utilisé pour stocker des données temporaires pour le processus.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-MergeFiles-MergeFiles.java" >}}
