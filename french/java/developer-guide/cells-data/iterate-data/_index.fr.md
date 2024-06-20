---
title: Comment et où utiliser les itérateurs
linktitle: Itérer les données
type: docs
weight: 640
url: /fr/java/how-and-where-to-use-iterators/
---

{{% alert color="primary" %}} 

Un objet d'une interface d'itérateur peut être utilisé pour traverser tous les éléments d'une collection. Les itérateurs peuvent être utilisés pour inspecter les données dans une collection, mais ils ne peuvent pas être utilisés pour modifier la collection sous-jacente. En général, pour utiliser un itérateur pour parcourir le contenu d'une collection, les étapes suivantes doivent être prises :

1. Obtenir un itérateur au début de la collection en appelant la méthode d'itérateur de la collection.
1. Mettre en place une boucle qui appelle la méthode hasNext. Faites en sorte que la boucle itère aussi longtemps que la méthode hasNext retourne vrai.
1. À l'intérieur de la boucle, obtenir chaque élément en appelant la méthode next.

Les API Aspose.Cells fournissent un tas d'itérateurs, cependant, cet article discute principalement des trois types énumérés ci-dessous.

1. Itérateur de cellules
1. Itérateur de lignes
1. Itérateur de colonnes

{{% /alert %}} 
## **Comment utiliser les itérateurs**
### **Itérateur de cellules**
Il existe diverses façons d'accéder à l'itérateur de cellules, et l'on peut utiliser l'une de ces méthodes en fonction des besoins de l'application. Voici les méthodes qui retournent l'itérateur de cellules.

1. Cells.iterator
1. Row.iterator
1. Range.iterator

Toutes les méthodes mentionnées ci-dessus renvoient l'itérateur qui permet de parcourir la collection de cellules qui ont été initialisées.

{{% alert color="primary" %}} 

Pendant le parcours des cellules, la collection ne doit pas être modifiée (opérations qui entraîneront une nouvelle cellule à être instanciée ou une cellule existante à être supprimée). Sinon, l'itérateur pourrait ne pas être en mesure de parcourir toutes les cellules correctement (certains éléments pourraient être parcourus à plusieurs reprises ou ignorés).

{{% /alert %}} 

L'exemple de code suivant démontre la mise en œuvre de la classe Iterator pour une collection de cellules.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CellsIterator-CellsIterator.java" >}}




##### **Itérateur de lignes**
L'itérateur de lignes peut être accédé tout en utilisant la méthode RowCollection.iterator. L'exemple de code suivant démontre la mise en œuvre de l'itérateur pour la classe RowCollection.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RowsIterator-RowsIterator.java" >}}




##### **Itérateur de colonnes**
L'itérateur de colonnes peut être accédé tout en utilisant la méthode ColumnCollection.iterator. L'exemple de code suivant démontre la mise en œuvre de l'itérateur pour la classe ColumnCollection.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ColumnsIterator-ColumnsIterator.java" >}}




#### **Où utiliser les itérateurs**
Pour discuter des avantages de l'utilisation des itérateurs, prenons un exemple concret.
##### **Scénario**
Une exigence de l'application est de parcourir toutes les cellules dans une feuille de calcul donnée pour lire leurs valeurs. Il pourrait y avoir plusieurs façons de mettre en œuvre cet objectif. Quelques-unes sont démontrées ci-dessous.
###### **Utilisation de la plage d'affichage**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDisplayRange-UsingDisplayRange.java" >}}




###### **Utilisation de MaxDataRow & MaxDataColumn**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingMaxDataRowAndMaxDataColumn-UsingMaxDataRowAndMaxDataColumn.java" >}}





Comme vous pouvez le constater, les deux approches mentionnées ci-dessus utilisent plus ou moins une logique similaire, c'est-à-dire; parcourir toutes les cellules de la collection pour lire les valeurs des cellules. Cela pourrait poser problème pour un certain nombre de raisons comme discuté ci-dessous.

1. Les API telles que MaxRow, MaxDataRow, MaxColumn, MaxDataColumn & MaxDisplayRange nécessitent du temps supplémentaire pour recueillir les statistiques correspondantes. Dans le cas où la matrice de données (ligne x colonnes) est grande, utiliser ces API pourrait entraîner une pénalité en termes de performances.
1. Dans la plupart des cas, toutes les cellules dans une plage donnée ne sont pas instanciées. Dans de telles situations, vérifier chaque cellule dans la matrice n'est pas aussi efficace que de vérifier uniquement les cellules initialisées.
1. Accéder à une cellule dans une boucle comme Cells.get(rowIndex, columnIndex) va provoquer l'instanciation de tous les objets de cellules dans une plage, ce qui pourrait éventuellement provoquer OutOfMemoryError.
##### **Conclusion**
Sur la base des faits mentionnés ci-dessus, voici les scénarios possibles où les itérateurs devraient être utilisés.

1. L'accès en lecture seule à la collection de cellules est requis, c'est-à-dire; la seule exigence est d'inspecter les cellules.
1. Un grand nombre de cellules doit être parcouru.
1. Seules les cellules/rangées/colonnes initialisées doivent être parcourues.
