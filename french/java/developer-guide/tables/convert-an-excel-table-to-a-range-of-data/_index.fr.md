---
title: Convertir un tableau Excel en une plage de données
type: docs
weight: 10
url: /fr/java/convert-an-excel-table-to-a-range-of-data/
---

{{% alert color="primary" %}}

Parfois, vous créez un tableau dans Microsoft Excel et ne voulez pas continuer à travailler avec la fonctionnalité de tableau qu'il propose. À la place, vous voulez quelque chose qui ressemble à un tableau. Pour conserver les données dans un tableau sans perdre la mise en forme, convertissez le tableau en une plage de données ordinaire.

Aspose.Cells prend en charge cette fonctionnalité de Microsoft Excel pour les tableaux et les objets de liste.

{{% /alert %}}

## **Utilisation de Microsoft Excel**

Utilisez la fonctionnalité **Convertir en plage** pour convertir rapidement un tableau en une plage sans perdre le formatage. Dans Microsoft Excel 2007/2010 :

1. Cliquez n'importe où dans le tableau pour vous assurer que la cellule active se trouve dans une colonne de tableau.

![todo:image_alt_text](convert-an-excel-table-to-a-range-of-data_1.gif)

1. Dans l'onglet **Création**, dans le groupe **Outils**, cliquez sur **Convertir en plage**.

![todo:image_alt_text](convert-an-excel-table-to-a-range-of-data_2.gif)

{{% alert color="primary" %}}

Les fonctionnalités du tableau ne sont plus disponibles après sa conversion en plage. Par exemple, les en-têtes de ligne n'incluent plus les flèches de tri et de filtre, et les références structurées (références utilisant des noms de table) utilisées dans les formules se transforment en références de cellule classiques.

{{% /alert %}}

## **Utilisation d'Aspose.Cells**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-ConvertTableToRange-ConvertTableToRange.java" >}}

## **Convertir un tableau en plage avec des options**

Aspose.Cells propose des options supplémentaires lors de la conversion d'un tableau en plage via la classe [**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions). La classe [**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions) fournit la propriété [**LastRow**](https://reference.aspose.com/cells/java/com.aspose.cells/tabletorangeoptions#LastRow) qui vous permet de définir le dernier index de la ligne du tableau. La mise en forme du tableau sera conservée jusqu'à l'index de ligne spécifié et le reste de la mise en forme sera supprimé.

Le code d'exemple ci-dessous démontre l'utilisation de la classe [**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Tables-ConvertTableToRangeWithOptions-1.java" >}}
{{< app/cells/assistant language="java" >}}
