---
title: Fusionner des fichiers
type: docs
weight: 10
url: /fr/java/merge-files/
---

## **Introduction**

Aspose.Cells propose différentes façons de fusionner des fichiers. Pour des fichiers simples avec des données, une mise en forme et des formules, la méthode [**Workbook.combine()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#combine-com.aspose.cells.Workbook-) peut être utilisée pour combiner plusieurs classeurs, et la méthode [**Worksheet.copy(**)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy-com.aspose.cells.Worksheet-) peut être utilisée pour copier des feuilles de calcul dans un nouveau classeur. Ces méthodes sont faciles à utiliser et efficaces, mais si vous avez de nombreux fichiers à fusionner, vous constaterez qu'elles consomment beaucoup de ressources système. Pour éviter cela, utilisez la méthode statique CellsHelper.mergeFiles, une manière plus efficace de fusionner plusieurs fichiers.

## **Fusionner des fichiers à l'aide d'Aspose.Cells**

Le code d'exemple suivant illustre comment fusionner de grands fichiers à l'aide de la méthode CellsHelper.mergeFiles. Il prend deux fichiers simples mais volumineux, MyBook1.xls et MyBook2.xls. Les fichiers contiennent uniquement des données formatées et des formules.

{{% alert color="primary" %}}

La méthode CellsHelper.mergeFiles prend en charge uniquement la fusion de données, de styles, de mise en forme et de formules. Des objets tels que des graphiques, des images, des commentaires ou d'autres objets pourraient ne pas être fusionnés à l'aide de cette méthode. De plus, un fichier mis en cache est utilisé pour stocker les données temporaires pour le processus.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-MergeFiles-MergeFiles.java" >}}
{{< app/cells/assistant language="java" >}}
