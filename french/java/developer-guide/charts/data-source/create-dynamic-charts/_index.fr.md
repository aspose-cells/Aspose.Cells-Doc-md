---
title: Créer des graphiques dynamiques
type: docs
weight: 200
url: /fr/java/create-dynamic-charts/
---
{{% alert color="primary" %}}

Les graphiques dynamiques (ou interactifs) peuvent changer lorsque vous modifiez la portée des données. En d'autres termes, les graphiques dynamiques peuvent refléter automatiquement les modifications lorsque la source de données est modifiée. Afin de déclencher le changement de source de données, on peut utiliser l'option de filtrage des tableaux Excel ou utiliser un contrôle tel que ComboBox ou Liste déroulante.

Cet article illustre l'utilisation des API Aspose.Cells for Java pour créer des graphiques dynamiques à l'aide des deux approches susmentionnées.

{{% /alert %}}

## **Utiliser des tableaux Excel**

{{% alert color="primary" %}}

 Les tableaux Excel sont appelés ListObjects dans la perspective Aspose.Cells, nous utiliserons donc le terme "ListObject" au lieu de "Table" pour plus de clarté. Veuillez lire en détail comment[créer des ListObjects](/cells/fr/java/creating-a-list-object/) avec Aspose.Cells for .NET API.

{{% /alert %}}

ListObjects fournit la fonctionnalité intégrée pour trier et filtrer les données lors de l'interaction de l'utilisateur. Les options de tri et de filtrage sont fournies via les listes déroulantes qui sont automatiquement ajoutées à la ligne d'en-tête du ListObject. En raison de ces fonctionnalités (tri et filtrage), le ListObject semble être le candidat idéal pour servir de source de données à un graphique dynamique, car lorsque le tri ou le filtrage est modifié, la représentation des données dans le graphique sera modifiée pour refléter le courant. état du ListObject.

Afin de garder la démonstration simple à comprendre, nous allons créer le classeur à partir de zéro et avancer étape par étape comme indiqué ci-dessous.

1. Créez un classeur vide.
1. Accédez au Cells de la première feuille de calcul du classeur.
1. Insérez des données dans les cellules.
1. Créez ListObject en fonction des données insérées.
1. Créer un graphique basé sur la plage de données de ListObject.
1. Enregistrer le résultat sur disque.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingExcelTables-UsingExcelTables.java" >}}

## **Utilisation de formules dynamiques**

Si vous ne souhaitez pas utiliser les ListObjects comme source de données pour le graphique dynamique, l'autre option consiste à utiliser les fonctions Excel (ou formules) pour créer une plage dynamique de données et un contrôle (tel que ComboBox) pour déclencher le changement. dans les données. Dans ce scénario, nous utiliserons la fonction VLOOKUP pour récupérer les valeurs appropriées en fonction de la sélection de ComboBox. Lorsque la sélection est modifiée, la fonction VLOOKUP actualise la valeur de la cellule. Si une plage de cellules utilise la fonction VLOOKUP, toute la plage peut être actualisée lors de l'interaction de l'utilisateur et peut donc être utilisée comme source du graphique dynamique.

Afin de garder la démonstration simple à comprendre, nous allons créer le classeur à partir de zéro et avancer étape par étape comme indiqué ci-dessous.

1. Créez un classeur vide.
1. Accédez au Cells de la première feuille de calcul du classeur.
1. Insérez des données dans les cellules en créant une plage nommée. Ces données serviront de séries au graphique dynamique.
1. Créez ComboBox en fonction de la plage nommée créée à l'étape précédente.
1. Insérez quelques données supplémentaires dans les cellules qui serviront de source à la fonction VLOOKUP.
1. Insérez la fonction VLOOKUP (avec les paramètres appropriés) dans une plage de cellules. Cette plage servira de source au graphique dynamique.
1. Créer un graphique basé sur la plage créée à l'étape précédente.
1. Enregistrer le résultat sur disque.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDynamicFormulas-UsingDynamicFormulas.java" >}}
