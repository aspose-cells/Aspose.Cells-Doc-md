---
title: Tableaux et Plages
type: docs
weight: 50
url: /fr/python-net/tables-and-ranges/
---

## **Introduction**

Parfois, vous créez un tableau dans Microsoft Excel et ne voulez pas continuer à travailler avec la fonctionnalité de tableau qu'il propose. À la place, vous voulez quelque chose qui ressemble à un tableau. Pour conserver les données dans un tableau sans perdre la mise en forme, convertissez le tableau en une plage de données ordinaire.
Aspose.Cells pour Python via .NET supporte cette fonctionnalité des tableaux et objets de liste de Microsoft Excel.

## **Utilisation de Microsoft Excel**

Utilisez la fonctionnalité **Convertir en plage** pour convertir rapidement un tableau en une plage sans perdre le formatage. Dans Microsoft Excel 2007/2010 :

1. Cliquez n'importe où dans le tableau pour vous assurer que la cellule active se trouve dans une colonne de tableau.
1. Dans l'onglet **Création**, dans le groupe **Outils**, cliquez sur **Convertir en plage**.

## **Utiliser Aspose.Cells pour Python via .NET**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-ConvertTableToRange-1.py" >}}

{{% alert color="primary" %}}

Les fonctionnalités du tableau ne sont plus disponibles après sa conversion en plage. Par exemple, les en-têtes de ligne n'incluent plus les flèches de tri et de filtre, et les références structurées (références utilisant des noms de table) utilisées dans les formules se transforment en références de cellule classiques.

{{% /alert %}}

## **Convertir un tableau en plage avec des options**

Aspose.Cells pour Python via .NET offre des options supplémentaires lors de la conversion d’un tableau en plage via la classe [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions). La classe [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions) fournit la propriété [**last_row**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions/last_row/), qui permet de définir le dernier index de la ligne du tableau. La mise en forme du tableau sera conservée jusqu’au dernier index spécifié, le reste de la mise en forme sera supprimé.

Le code d'exemple ci-dessous démontre l'utilisation de la classe [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-ConvertTableToRangeWithOptions-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
