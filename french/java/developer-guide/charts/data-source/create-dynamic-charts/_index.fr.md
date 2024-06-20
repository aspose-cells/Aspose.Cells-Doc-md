---
title: Créer des graphiques dynamiques
type: docs
weight: 200
url: /fr/java/create-dynamic-charts/
---

{{% alert color="primary" %}}

Les graphiques dynamiques (ou interactifs) ont la capacité de changer lorsque vous modifiez la portée des données. En d'autres termes, les graphiques dynamiques peuvent refléter automatiquement les modifications lorsque la source de données est modifiée. Pour déclencher le changement de source de données, on peut utiliser l'option de filtrage des tableaux Excel ou utiliser un contrôle tel qu'une liste déroulante ou une liste déroulante.

Cet article démontre l'utilisation des API Aspose.Cells for Java pour créer des graphiques dynamiques en utilisant les deux approches mentionnées ci-dessus.

{{% /alert %}}

## **Utilisation des tables Excel**

{{% alert color="primary" %}}

Les tableaux Excel sont appelés ListObjects du point de vue d'Aspose.Cells, c'est pourquoi nous utiliserons le terme "ListObject" au lieu de "Table" pour plus de clarté. Veuillez lire en détail comment [créer des ListObjects](/cells/fr/java/creating-a-list-object/) avec l'API Aspose.Cells for .NET.

{{% /alert %}}

Les ListObjects fournissent la fonctionnalité intégrée de tri et de filtrage des données lors de l'interaction de l'utilisateur. Les options de tri et de filtrage sont fournies via les listes déroulantes ajoutées automatiquement à la ligne d'en-tête du ListObject. En raison de ces fonctionnalités (tri et filtrage), le ListObject semble être le candidat parfait pour servir de source de données à un graphique dynamique car lorsque le tri ou le filtrage est modifié, la représentation des données dans le graphique sera modifiée pour refléter l'état actuel du ListObject.

Afin de simplifier la démonstration et de la rendre compréhensible, nous créerons le classeur à partir de zéro et avancerons étape par étape comme décrit ci-dessous.

1. Créer un classeur vide.
1. Accéder aux cellules de la première feuille de calcul dans le classeur.
1. Insérez des données dans les cellules.
1. Créer un ListObject basé sur les données insérées.
1. Créer un graphique basé sur la plage de données du ListObject.
1. Enregistrer le résultat sur le disque.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingExcelTables-UsingExcelTables.java" >}}

## **Utilisation de Formules Dynamiques**

Si vous ne souhaitez pas utiliser les ListObjects comme source de données pour le graphique dynamique, l'autre option est d'utiliser des fonctions Excel (ou des formules) pour créer une plage de données dynamique, et un contrôle (tel qu'une liste déroulante) pour déclencher le changement de données. Dans ce scénario, nous utiliserons la fonction VLOOKUP pour récupérer les valeurs appropriées en fonction de la sélection de la liste déroulante. Lorsque la sélection est modifiée, la fonction VLOOKUP rafraîchira la valeur de la cellule. Si une plage de cellules utilise la fonction VLOOKUP, toute la plage peut être rafraîchie lors de l'interaction de l'utilisateur, et peut donc être utilisée comme source du graphique dynamique.

Afin de simplifier la démonstration et de la rendre compréhensible, nous créerons le classeur à partir de zéro et avancerons étape par étape comme décrit ci-dessous.

1. Créer un classeur vide.
1. Accéder aux cellules de la première feuille de calcul dans le classeur.
1. Insérer des données dans les cellules en créant une plage nommée. Ces données serviront de séries pour le graphique dynamique.
1. Créer une zone de liste déroulante basée sur la plage nommée créée à l'étape précédente.
1. Insérer davantage de données dans les cellules qui serviront de source à la fonction VLOOKUP.
1. Insérez la fonction VLOOKUP (avec les paramètres appropriés) dans une plage de cellules. Cette plage servira de source au graphique dynamique.
1. Créer un graphique basé sur la plage créée à l'étape précédente.
1. Enregistrer le résultat sur le disque.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDynamicFormulas-UsingDynamicFormulas.java" >}}
