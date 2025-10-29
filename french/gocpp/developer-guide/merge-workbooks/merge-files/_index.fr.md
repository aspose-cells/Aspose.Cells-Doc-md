---
title: Fusionner des fichiers avec Golang via C++
linktitle: Fusionner des fichiers
type: docs
weight: 20
url: /fr/go-cpp/merge-files/
description: Découvrez comment fusionner efficacement des fichiers Excel en utilisant Aspose.Cells for C++.
---

## **Introduction**

Aspose.Cells offre plusieurs méthodes pour fusionner des fichiers. Pour des fichiers simples avec données, formatage, et formules, la méthode [**Workbook.Combine()**](https://reference.aspose.com/cells/go-cpp/workbook/combine/) peut être utilisée pour combiner plusieurs classeurs, et la méthode [**Worksheet.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/copy/) pour copier des feuilles de calcul dans un nouveau classeur. Ces méthodes sont faciles à utiliser et efficaces, mais si vous avez beaucoup de fichiers à fusionner, vous constaterez qu'elles consomment beaucoup de ressources système. Pour éviter cela, utilisez la méthode statique [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/), une façon plus efficace de fusionner plusieurs fichiers.

## **Fusionner des fichiers à l'aide d'Aspose.Cells**

Le code d'échantillon suivant illustre comment fusionner de grands fichiers en utilisant la méthode [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/go-cpp/cellshelper/mergefiles/). Il prend deux fichiers simples mais volumineux, Book1.xls et Book2.xls. Les fichiers contiennent uniquement des données formatées et des formules.

{{% alert color="primary" %}}

La méthode [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/go-cpp/cellshelper/mergefiles/) ne prend en charge que la fusion de données, styles, mise en forme, et formules. Des objets tels que des graphiques, images, commentaires ou autres objets pourraient ne pas être fusionnés avec cette méthode. De plus, un fichier en cache est utilisé pour stocker des données temporaires durant le processus.

{{% /alert %}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MergeFiles.go" >}}
