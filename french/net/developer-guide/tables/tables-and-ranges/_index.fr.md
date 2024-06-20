---
title: Tableaux et Plages
type: docs
weight: 50
url: /fr/net/tables-and-ranges/
---

## **Introduction**

Parfois, vous créez un tableau dans Microsoft Excel et ne voulez pas continuer à travailler avec la fonctionnalité de tableau qu'il propose. À la place, vous voulez quelque chose qui ressemble à un tableau. Pour conserver les données dans un tableau sans perdre la mise en forme, convertissez le tableau en une plage de données ordinaire.
Aspose.Cells prend en charge cette fonctionnalité de Microsoft Excel pour les tableaux et les objets liste.

## **Utilisation de Microsoft Excel**

Utilisez la fonctionnalité **Convertir en plage** pour convertir rapidement un tableau en une plage sans perdre le formatage. Dans Microsoft Excel 2007/2010 :

1. Cliquez n'importe où dans le tableau pour vous assurer que la cellule active se trouve dans une colonne de tableau.
1. Dans l'onglet **Création**, dans le groupe **Outils**, cliquez sur **Convertir en plage**.

## **Utilisation d'Aspose.Cells**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRange-1.cs" >}}

{{% alert color="primary" %}}

Les fonctionnalités du tableau ne sont plus disponibles après sa conversion en plage. Par exemple, les en-têtes de ligne n'incluent plus les flèches de tri et de filtre, et les références structurées (références utilisant des noms de table) utilisées dans les formules se transforment en références de cellule classiques.

{{% /alert %}}

## **Convertir un tableau en plage avec des options**

Aspose.Cells propose des options supplémentaires lors de la conversion d'une table en plage via la classe [**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions). La classe [**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions) fournit la propriété [**LastRow**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions/properties/lastrow) qui vous permet de définir le dernier index de la ligne de table. La mise en forme du tableau sera conservée jusqu'à l'index de ligne spécifié et le reste de la mise en forme sera supprimé.

Le code d'exemple ci-dessous démontre l'utilisation de la classe [**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRangeWithOptions-1.cs" >}}
