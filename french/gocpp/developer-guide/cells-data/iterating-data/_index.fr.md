---
title: Comment et où utiliser les énumérateurs avec Golang via C++
linktitle: Itérer les données
type: docs
weight: 55
url: /fr/go-cpp/how-and-where-to-use-enumerators/
description: Découvrez comment utiliser les énumérateurs via l’API Aspose.Cells for C++.
keywords: Comment utiliser des énumérateurs, énumérateur de cellules, énumérateur de lignes, énumérateur de colonnes
---

{{% alert color="primary" %}}

Un énumérateur est un objet qui permet de parcourir un conteneur ou une collection. Les énumérateurs peuvent être utilisés pour lire les données dans la collection, mais ils ne peuvent pas être utilisés pour modifier la collection sous-jacente, alors que IEnumerable est une interface qui définit une méthode GetEnumerator retournant une interface IEnumerator, ce qui permet un accès en lecture seule à une collection.

Les API Aspose.Cells fournissent une multitude d'énumérateurs, cependant, cet article traite principalement des trois types énumérés ci-dessous.

1. Énumérateur de cellules
1. Énumérateur de lignes
1. Énumérateur de colonnes

{{% /alert %}}

## **Comment utiliser des énumérateurs**

### **Énumérateur de cellules**

Il existe diverses façons d'accéder à l'énumérateur de cellules, et l'on peut utiliser l'une de ces méthodes en fonction des besoins de l'application. Voici les méthodes qui renvoient l'énumérateur de cellules.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/cells/getenumerator/)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/row/getenumerator/)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/range/getenumerator/)

Toutes les méthodes mentionnées ci-dessus renvoient l'énumérateur qui permet de parcourir la collection de cellules qui ont été initialisées.

{{% alert color="primary" %}}

En parcourant les cellules, la collection ne doit pas être modifiée (des opérations qui entraîneront l'instanciation d'une nouvelle cellule ou la suppression d'une cellule existante). Sinon, l'énumérateur risque de ne pas pouvoir parcourir toutes les cellules correctement (certains éléments peuvent être parcourus de manière répétitive ou sautés).

{{% /alert %}}

L'exemple de code suivant montre l'implémentation de l'interface IEnumerator pour une collection de cellules.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData.go" >}}
### **Itérateur de lignes**

L’énumérateur de lignes peut être accessible lors de l’utilisation de la méthode [**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/rowcollection/getenumerator/). L’exemple de code suivant démontre la mise en œuvre de l’interface IEnumerator pour [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-1.go" >}}
### **Colonnes Obtenir**

Les colonnes peuvent être accédées lors de l’utilisation de la méthode [**ColumnCollection.Get**](https://reference.aspose.com/cells/go-cpp/columncollection/get/). L’exemple de code suivant démontre la mise en œuvre de la méthode Get pour [**ColumnCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/columncollection/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-2.go" >}}
## **Où utiliser les énumérateurs**

Afin de discuter des avantages de l'utilisation des énumérateurs, prenons un exemple en temps réel.

**Scénario**

Une exigence d’application est de parcourir toutes les cellules dans une [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) donnée pour lire leurs valeurs. Il pourrait y avoir plusieurs façons de réaliser cet objectif. Quelques-unes sont démontrées ci-dessous.

### **Utilisation de la plage d'affichage**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-3.go" >}}
### **Utilisation de MaxDataRow & MaxDataColumn**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-4.go" >}}
Comme vous pouvez le constater, les deux approches ci-dessus utilisent plus ou moins une logique similaire, c'est-à-dire parcourir toutes les cellules de la collection pour lire les valeurs des cellules. Cela pourrait poser problème pour un certain nombre de raisons, comme discuté ci-dessous.

1. Des API telles que [**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/cells/getmaxrow/), [**GetMaxDataRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/), [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxcolumn/), [**GetMaxDataColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) et [**GetMaxDisplayRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) nécessitent du temps supplémentaire pour recueillir les statistiques correspondantes. Si la matrice de données (lignes x colonnes) est grande, l’utilisation de ces API pourrait entraîner une pénalité de performance.
1. Dans la plupart des cas, toutes les cellules dans une plage donnée ne sont pas instanciées. Dans de telles situations, vérifier chaque cellule dans la matrice n'est pas aussi efficace que de vérifier uniquement les cellules initialisées.
1. Accéder à une cellule dans une boucle en tant que Cells row, column entraînera l'instanciation de tous les objets de cellules dans une plage, ce qui pourrait finalement entraîner une OutOfMemoryException.

## **Conclusion**

Sur la base des faits mentionnés ci-dessus, voici les scénarios possibles où les énumérateurs doivent être utilisés.

1. Un accès en lecture seule de la collection de cellules est requis, c'est-à-dire; la nécessité est uniquement d'inspecter les cellules.
1. Un grand nombre de cellules doit être parcouru.
1. Seules les cellules/rangées/colonnes initialisées doivent être parcourues.
