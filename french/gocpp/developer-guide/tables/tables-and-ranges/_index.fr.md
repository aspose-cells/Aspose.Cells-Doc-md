---
title: Tableaux et Plages
type: docs
weight: 30
url: /fr/go-cpp/tables-and-ranges/
---

## **Introduction**

Parfois, vous créez un tableau dans Microsoft Excel et ne souhaitez pas continuer à travailler avec la fonctionnalité de tableau qui l'accompagne. Au lieu de cela, vous voulez quelque chose qui ressemble à un tableau. Pour conserver des données dans un tableau sans perdre le formatage, convertissez le tableau en une plage de données classique. Aspose.Cells prend en charge cette fonctionnalité de Microsoft Excel pour les tableaux et les objets de liste.

## **Utilisation de Microsoft Excel**

Utilisez la fonctionnalité **Convertir en plage** pour convertir rapidement un tableau en une plage sans perdre le formatage. Dans Microsoft Excel 2007/2010 :

1. Cliquez n'importe où dans le tableau pour vous assurer que la cellule active se trouve dans une colonne de tableau.
1. Dans l'onglet **Création**, dans le groupe **Outils**, cliquez sur **Convertir en plage**.

{{% alert color="primary" %}}

Les fonctionnalités du tableau ne sont plus disponibles après sa conversion en plage. Par exemple, les en-têtes de ligne n'incluent plus les flèches de tri et de filtre, et les références structurées (références utilisant des noms de table) utilisées dans les formules se transforment en références de cellule classiques.

{{% /alert %}}

## **Utilisation d'Aspose.Cells**

Le code d'exemple suivant montre la même fonctionnalité en utilisant Aspose.Cells.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertTableToRange.go" >}}
