---
title: Comment et où utiliser les itérateurs
linktitle: Itérer les données
type: docs
weight: 640
url: /fr/java/how-and-where-to-use-iterators/
---
{{% alert color="primary" %}} 

Un objet d'une interface d'itérateur peut être utilisé pour parcourir tous les éléments d'une collection. Les itérateurs peuvent être utilisés pour inspecter les données d'une collection, mais ils ne peuvent pas être utilisés pour modifier la collection sous-jacente. En général, pour utiliser un itérateur pour parcourir le contenu d'une collection, les étapes suivantes doivent être suivies :

1. Obtenez un itérateur au début de la collection en appelant la méthode d'itérateur de la collection.
1. Configurez une boucle qui appelle la méthode hasNext. Faites itérer la boucle tant que la méthode hasNext renvoie true.
1. Dans la boucle, obtenez chaque élément en appelant la méthode suivante.

Aspose.Cells Les API fournissent un tas d'itérateurs, cependant, cet article traite principalement des trois types répertoriés ci-dessous.

1. Cells Itérateur
1. Itérateur de lignes
1. Itérateur de colonnes

{{% /alert %}} 
## **Comment utiliser les itérateurs**
### **Cells Itérateur**
Il existe différentes façons d'accéder à l'itérateur des cellules, et on peut utiliser n'importe laquelle de ces méthodes en fonction des exigences de l'application. Voici les méthodes qui renvoient l'itérateur des cellules.

1. Cells.iterator
1. Row.itérateur
1. Range.itérateur

Toutes les méthodes mentionnées ci-dessus renvoient l'itérateur qui permet de parcourir la collection de cellules qui ont été initialisées.

{{% alert color="primary" %}} 

Lors du parcours des cellules, la collection ne doit pas être modifiée (opérations qui entraîneront l'instanciation d'un nouveau Cell ou la suppression d'un Cell existant). Sinon, l'itérateur peut ne pas être en mesure de parcourir correctement toutes les cellules (certains éléments peuvent être parcourus à plusieurs reprises ou ignorés).

{{% /alert %}} 

L'exemple de code suivant illustre l'implémentation de la classe Iterator pour une collection de cellules.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CellsIterator-CellsIterator.java" >}}




##### **Itérateur de lignes**
L'itérateur de lignes est accessible lors de l'utilisation de la méthode RowCollection.iterator. L'exemple de code suivant illustre l'implémentation de la classe Iterator pour RowCollection.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RowsIterator-RowsIterator.java" >}}




##### **Itérateur de colonnes**
L'itérateur de colonnes est accessible lors de l'utilisation de la méthode ColumnCollection.iterator. L'exemple de code suivant illustre l'implémentation de la classe Iterator pour ColumnCollection.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ColumnsIterator-ColumnsIterator.java" >}}




#### **Où utiliser les itérateurs**
Afin de discuter des avantages de l'utilisation d'itérateurs, prenons un exemple en temps réel.
##### **Scénario**
Une exigence de l'application est de parcourir toutes les cellules d'une feuille de calcul donnée pour lire leurs valeurs. Il pourrait y avoir plusieurs façons de mettre en œuvre cet objectif. Quelques-uns sont illustrés ci-dessous.
###### **Utilisation de la plage d'affichage**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDisplayRange-UsingDisplayRange.java" >}}




###### **Utilisation de MaxDataRow et MaxDataColumn**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingMaxDataRowAndMaxDataColumn-UsingMaxDataRowAndMaxDataColumn.java" >}}





Comme vous pouvez le constater, les deux approches mentionnées ci-dessus utilisent une logique plus ou moins similaire, c'est-à-dire ; boucle sur toutes les cellules de la collection pour lire les valeurs des cellules. Cela pourrait être problématique pour un certain nombre de raisons, comme indiqué ci-dessous.

1. Les API telles que MaxRow, MaxDataRow, MaxColumn, MaxDataColumn & MaxDisplayRange nécessitent plus de temps pour rassembler les statistiques correspondantes. Dans le cas où la matrice de données (lignes x colonnes) est volumineuse, l'utilisation de ces API peut entraîner une baisse des performances.
1. Dans la plupart des cas, toutes les cellules d'une plage donnée ne sont pas instanciées. Dans de telles situations, vérifier chaque cellule de la matrice n'est pas aussi efficace que de vérifier uniquement les cellules initialisées.
1. L'accès à une cellule dans une boucle en tant que Cells.get(rowIndex, columnIndex) entraînera l'instanciation de tous les objets de cellule d'une plage, ce qui peut éventuellement provoquer une OutOfMemoryError.
##### **Conclusion**
Sur la base des faits mentionnés ci-dessus, voici les scénarios possibles dans lesquels les itérateurs doivent être utilisés.

1. Un accès en lecture seule à la collection de cellules est requis, c'est-à-dire ; l'exigence est d'inspecter uniquement les cellules.
1. Un grand nombre de cellules sont à traverser.
1. Seules les cellules/lignes/colonnes initialisées doivent être parcourues.
