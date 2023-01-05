---
title: Tableaux et plages
type: docs
weight: 30
url: /fr/cpp/tables-and-ranges/
---
## **Introduction**
Parfois, vous créez un tableau dans Microsoft Excel et ne souhaitez pas continuer à travailler avec la fonctionnalité de tableau qui l'accompagne. Au lieu de cela, vous voulez quelque chose qui ressemble à une table. Pour conserver les données dans un tableau sans perdre la mise en forme, convertissez le tableau en une plage de données normale. Aspose.Cells prend en charge cette fonctionnalité de Microsoft Excel pour les tableaux et les objets de liste.
## **Utilisation d'Excel Microsoft**
 Utilisez le**Convertir en plage** fonctionnalité pour convertir rapidement un tableau en plage sans perdre la mise en forme. Dans Excel Microsoft 2007/2010 :

1. Cliquez n'importe où dans le tableau pour vous assurer que la cellule active se trouve dans une colonne du tableau.
1.  Sur le**Concevoir** onglet, dans l'onglet**Outils** groupe, cliquez**Convertir en plage**.

{{% alert color="primary" %}} 

Les fonctionnalités du tableau ne sont plus disponibles une fois le tableau converti en plage. Par exemple, les en-têtes de ligne n'incluent plus les flèches de tri et de filtrage, et les références structurées (références qui utilisent des noms de table) qui étaient utilisées dans les formules se transforment en références de cellule normales.

{{% /alert %}} 
## **En utilisant Aspose.Cells**
L'extrait de code suivant illustre la même fonctionnalité en utilisant Aspose.Cells.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-ConvertTableToRange.cpp" >}}
