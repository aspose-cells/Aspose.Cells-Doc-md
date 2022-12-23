---
title: Comment et où utiliser les énumérateurs
linktitle: Itérer les données
type: docs
weight: 55
url: /fr/net/how-and-where-to-use-enumerators/
---
{{% alert color="primary" %}}

Un énumérateur est un objet qui permet de parcourir un conteneur ou une collection. Les énumérateurs peuvent être utilisés pour lire les données de la collection, mais ils ne peuvent pas être utilisés pour modifier la collection sous-jacente, alors que IEnumerable est une interface qui définit une méthode GetEnumerator qui renvoie une interface IEnumerator, ce qui, à son tour, permet un accès en lecture seule à une collection.

Aspose.Cells Les API fournissent un tas d'énumérateurs cependant, cet article traite principalement des trois types répertoriés ci-dessous.

1. Cells Recenseur
1. Énumérateur de lignes
1. Énumérateur de colonnes

{{% /alert %}}

## **Comment utiliser les énumérateurs**

### **Cells Recenseur**

Il existe différentes façons d'accéder à l'énumérateur Cells, et on peut utiliser l'une de ces méthodes en fonction des exigences de l'application. Voici les méthodes qui renvoient l'énumérateur de cellules.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

Toutes les méthodes mentionnées ci-dessus retournent l'énumérateur qui permet de parcourir la collection de cellules qui ont été initialisées.

{{% alert color="primary" %}}

Lors du parcours des cellules, la collection ne doit pas être modifiée (opérations qui entraîneront l'instanciation d'un nouveau Cell ou la suppression d'un Cell existant). Sinon, l'énumérateur peut ne pas être en mesure de parcourir toutes les cellules correctement (certains éléments peuvent être parcourus à plusieurs reprises ou ignorés).

{{% /alert %}}

L'exemple de code suivant illustre l'implémentation de l'interface IEnumerator pour une collection Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

### **Énumérateur de lignes**

 L'énumérateur de lignes est accessible lors de l'utilisation de[**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator) méthode. L'exemple de code suivant illustre l'implémentation de l'interface IEnumerator pour[**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

### **Énumérateur de colonnes**

 L'énumérateur de colonnes est accessible lors de l'utilisation de[**ColumnCollection.GetEnumeratorColumnCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/columncollection) méthode. L'exemple de code suivant illustre l'implémentation de l'interface IEnumerator pour[**ColonneCollection**](https://reference.aspose.com/cells/net/aspose.cells/columncollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

## **Où utiliser les énumérateurs**

Afin de discuter des avantages de l'utilisation d'énumérateurs, prenons un exemple en temps réel.

**Scénario**

 Une exigence de l'application est de parcourir toutes les cellules d'un[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)pour lire leurs valeurs. Il pourrait y avoir plusieurs façons de mettre en œuvre cet objectif. Quelques-uns sont illustrés ci-dessous.

### **Utilisation de la plage d'affichage**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

### **Utilisation de MaxDataRow et MaxDataColumn**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

Comme vous pouvez le constater, les deux approches mentionnées ci-dessus utilisent une logique plus ou moins similaire, c'est-à-dire ; boucle sur toutes les cellules de la collection pour lire les valeurs des cellules. Cela pourrait être problématique pour un certain nombre de raisons, comme indiqué ci-dessous.

1.  API telles que[**MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow), [**MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow), [**MaxColonne**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn), [**MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) & [**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)besoin de temps supplémentaire pour rassembler les statistiques correspondantes. Dans le cas où la matrice de données (lignes x colonnes) est volumineuse, l'utilisation de ces API peut entraîner une baisse des performances.
1. Dans la plupart des cas, toutes les cellules d'une plage donnée ne sont pas instanciées. Dans de telles situations, vérifier chaque cellule de la matrice n'est pas aussi efficace que de vérifier uniquement les cellules initialisées.
1. L'accès à une cellule dans une boucle en tant que ligne Cells, colonne entraînera l'instanciation de tous les objets de cellule d'une plage, ce qui peut éventuellement provoquer OutOfMemoryException.

## **Conclusion**

Sur la base des faits mentionnés ci-dessus, voici les scénarios possibles dans lesquels les enquêteurs doivent être utilisés.

1. Un accès en lecture seule à la collection de cellules est requis, c'est-à-dire ; l'exigence est d'inspecter uniquement les cellules.
1. Un grand nombre de cellules sont à traverser.
1. Seules les cellules/lignes/colonnes initialisées doivent être traversées.
