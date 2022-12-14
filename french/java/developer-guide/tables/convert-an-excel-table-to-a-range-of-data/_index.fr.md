---
title: Convertir un tableau Excel en une plage de données
type: docs
weight: 10
url: /fr/java/convert-an-excel-table-to-a-range-of-data/
---
{{% alert color="primary" %}}

Parfois, vous créez un tableau dans Microsoft Excel et ne souhaitez pas continuer à travailler avec la fonctionnalité de tableau qui l'accompagne. Au lieu de cela, vous voulez quelque chose qui ressemble à une table. Pour conserver les données dans un tableau sans perdre la mise en forme, convertissez le tableau en une plage de données normale.

Aspose.Cells prend en charge cette fonctionnalité de Microsoft Excel pour les tableaux et les objets de liste.

{{% /alert %}}

## **Utilisation d'Excel Microsoft**

 Utilisez le**Convertir en plage** fonctionnalité pour convertir rapidement un tableau en plage sans perdre la mise en forme. Dans Excel Microsoft 2007/2010 :

1. Cliquez n'importe où dans le tableau pour vous assurer que la cellule active se trouve dans une colonne du tableau.

![tâche : image_autre_texte](convert-an-excel-table-to-a-range-of-data_1.gif)

1.  Sur le**Concevoir** onglet, dans l'onglet**Outils** groupe, cliquez**Convertir en plage**.

![tâche : image_autre_texte](convert-an-excel-table-to-a-range-of-data_2.gif)

{{% alert color="primary" %}}

Les fonctionnalités du tableau ne sont plus disponibles une fois le tableau converti en plage. Par exemple, les en-têtes de ligne n'incluent plus les flèches de tri et de filtrage, et les références structurées (références qui utilisent des noms de table) qui étaient utilisées dans les formules se transforment en références de cellule normales.

{{% /alert %}}

## **En utilisant Aspose.Cells**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-ConvertTableToRange-ConvertTableToRange.java" >}}

## **Convertir une table en plage avec des options**

Aspose.Cells fournit des options supplémentaires lors de la conversion de la table en plage via le[**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)classer. La[**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)la classe fournit[**Dernière rangée**](https://reference.aspose.com/cells/java/com.aspose.cells/tabletorangeoptions#LastRow)propriété qui vous permet de définir le dernier index de la ligne du tableau. La mise en forme du tableau sera conservée jusqu'à l'index de ligne spécifié et le reste de la mise en forme sera supprimé.

L'exemple de code ci-dessous illustre l'utilisation de[**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)classer.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Tables-ConvertTableToRangeWithOptions-1.java" >}}
