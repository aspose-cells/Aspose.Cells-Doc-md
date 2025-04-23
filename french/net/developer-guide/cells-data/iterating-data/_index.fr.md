---
title: Comment et où utiliser les énumérateurs
linktitle: Itérer les données
type: docs
weight: 55
url: /fr/net/how-and-where-to-use-enumerators/
description: Apprenez comment et où utiliser des énumérateurs via l API Aspose.Cells for .NET.
keywords: Comment utiliser des énumérateurs, énumérateur de cellules, énumérateur de lignes, énumérateur de colonnes
---

{{% alert color="primary" %}}

Un énumérateur est un objet qui fournit la capacité de parcourir un conteneur ou une collection. Les énumérateurs peuvent être utilisés pour lire les données dans la collection, mais ils ne peuvent pas être utilisés pour modifier la collection sous-jacente, tandis que IEnumerable est une interface qui définit une méthode GetEnumerator qui renvoie une interface IEnumerator, ce qui permet un accès en lecture seule à une collection.

Les API Aspose.Cells fournissent une multitude d'énumérateurs, cependant, cet article traite principalement des trois types énumérés ci-dessous.

1. Énumérateur de cellules
1. Énumérateur de lignes
1. Énumérateur de colonnes

{{% /alert %}}

## **Comment utiliser des énumérateurs**

### **Énumérateur de cellules**

Il existe diverses façons d'accéder à l'énumérateur de cellules, et l'on peut utiliser l'une de ces méthodes en fonction des besoins de l'application. Voici les méthodes qui renvoient l'énumérateur de cellules.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

Toutes les méthodes mentionnées ci-dessus renvoient l'énumérateur qui permet de parcourir la collection de cellules qui ont été initialisées.

{{% alert color="primary" %}}

En parcourant les cellules, la collection ne doit pas être modifiée (des opérations qui entraîneront l'instanciation d'une nouvelle cellule ou la suppression d'une cellule existante). Sinon, l'énumérateur risque de ne pas pouvoir parcourir toutes les cellules correctement (certains éléments peuvent être parcourus de manière répétitive ou sautés).

{{% /alert %}}

L'exemple de code suivant montre l'implémentation de l'interface IEnumerator pour une collection de cellules.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

### **Itérateur de lignes**

L'itérateur de lignes peut être accédé lors de l'utilisation de la méthode [**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator). L'exemple de code suivant montre l'implémentation de l'interface IEnumerator pour [**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

### **Itérateur de colonnes**

L'itérateur de colonnes peut être accédé lors de l'utilisation de la méthode [**ColumnCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/columncollection). L'exemple de code suivant montre l'implémentation de l'interface IEnumerator pour [**ColumnCollection**](https://reference.aspose.com/cells/net/aspose.cells/columncollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

## **Où utiliser les énumérateurs**

Afin de discuter des avantages de l'utilisation des énumérateurs, prenons un exemple en temps réel.

**Scénario**

Une exigence de l'application est de parcourir toutes les cellules dans un [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) donné pour lire leurs valeurs. Il pourrait y avoir plusieurs façons de mettre en œuvre cet objectif. Quelques exemples sont indiqués ci-dessous.

### **Utilisation de la plage d'affichage**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

### **Utilisation de MaxDataRow & MaxDataColumn**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

Comme vous pouvez le constater, les deux approches ci-dessus utilisent plus ou moins une logique similaire, c'est-à-dire parcourir toutes les cellules de la collection pour lire les valeurs des cellules. Cela pourrait poser problème pour un certain nombre de raisons, comme discuté ci-dessous.

1. Les API telles que [**MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow), [**MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow), [**MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn), [**MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) & [**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) nécessitent du temps supplémentaire pour rassembler les statistiques correspondantes. Dans le cas où la matrice de données (lignes x colonnes) est grande, l'utilisation de ces API pourrait entraîner une pénalité de performance.
1. Dans la plupart des cas, toutes les cellules dans une plage donnée ne sont pas instanciées. Dans de telles situations, vérifier chaque cellule dans la matrice n'est pas aussi efficace que de vérifier uniquement les cellules initialisées.
1. Accéder à une cellule dans une boucle en tant que Cells row, column entraînera l'instanciation de tous les objets de cellules dans une plage, ce qui pourrait finalement entraîner une OutOfMemoryException.

## **Conclusion**

Sur la base des faits mentionnés ci-dessus, voici les scénarios possibles où les énumérateurs doivent être utilisés.

1. Un accès en lecture seule de la collection de cellules est requis, c'est-à-dire; la nécessité est uniquement d'inspecter les cellules.
1. Un grand nombre de cellules doit être parcouru.
1. Seules les cellules/rangées/colonnes initialisées doivent être parcourues.
{{< app/cells/assistant language="csharp" >}}
