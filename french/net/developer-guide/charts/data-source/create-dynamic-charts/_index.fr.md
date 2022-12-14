---
title: Créer des graphiques dynamiques
type: docs
weight: 240
url: /fr/net/create-dynamic-charts/
---
{{% alert color="primary" %}}

Les graphiques dynamiques (ou interactifs) peuvent changer lorsque vous modifiez la portée des données. En d'autres termes, les graphiques dynamiques peuvent refléter automatiquement les modifications lorsque la source de données est modifiée. Afin de déclencher le changement dans la source de données, on peut utiliser l'option de filtrage des tableaux Excel ou utiliser un contrôle tel que ComboBox ou Liste déroulante.

Cet article illustre l'utilisation des API Aspose.Cells for .NET pour créer des graphiques dynamiques à l'aide des deux approches susmentionnées.

{{% /alert %}}

## **Utiliser des tableaux Excel**

{{% alert color="primary" %}}

 Les tableaux Excel sont appelés ListObjects dans la perspective Aspose.Cells, par conséquent, nous utiliserons le terme "ListObject" au lieu de "Table" pour plus de clarté. Veuillez lire en détail comment[créer des ListObjects](/cells/fr/net/create-and-format-table/) avec Aspose.Cells for .NET API.

{{% /alert %}}

 ListObjects fournit la fonctionnalité intégrée pour trier et filtrer les données lors de l'interaction de l'utilisateur. Les options de tri et de filtrage sont fournies via les listes déroulantes qui sont automatiquement ajoutées à la ligne d'en-tête du[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) . Grâce à ces fonctionnalités (tri et filtrage), les[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)semble être le candidat idéal pour servir de source de données à un graphique dynamique, car lorsque le tri ou le filtrage est modifié, la représentation des données dans le graphique sera modifiée pour refléter l'état actuel du[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).

 Afin de garder la démonstration simple à comprendre, nous allons créer le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook)partir de zéro et avancer étape par étape comme indiqué ci-dessous.

1.  Créer un vide[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1.  Accéder au[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) du premier[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) dans le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Insérez des données dans les cellules.
1.  Créer[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)sur la base des données insérées.
1.  Créer[**Graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) sur la base de la plage de données de[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).
1. Enregistrez le résultat sur le disque.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

## **Utilisation de formules dynamiques**

 Si vous ne souhaitez pas utiliser le[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)en tant que source de données pour le graphique dynamique, l'autre option consiste à utiliser des fonctions (ou formules) Excel pour créer une plage dynamique de données et un contrôle (tel que ComboBox) pour déclencher la modification des données. Dans ce scénario, nous utiliserons la fonction VLOOKUP pour récupérer les valeurs appropriées en fonction de la sélection de ComboBox. Lorsque la sélection est modifiée, la fonction VLOOKUP actualise la valeur de la cellule. Si une plage de cellules utilise la fonction VLOOKUP, toute la plage peut être actualisée lors de l'interaction de l'utilisateur, elle peut donc être utilisée comme source pour le graphique dynamique.

Afin de garder la démonstration simple à comprendre, nous allons créer le classeur à partir de zéro et avancer étape par étape comme indiqué ci-dessous.

1.  Créer un vide[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1.  Accéder au[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) du premier[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) dans le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Insérez des données dans les cellules en créant une plage nommée. Ces données serviront de série au graphique dynamique.
1.  Créer[**Boîte combo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox)en fonction de la plage nommée créée à l'étape précédente.
1. Insérez quelques données supplémentaires dans les cellules qui serviront de source à la fonction VLOOKUP.
1. Insérez la fonction VLOOKUP (avec les paramètres appropriés) dans une plage de cellules. Cette plage servira de source au graphique dynamique.
1.  Créer[**Graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)en fonction de la plage créée à l'étape précédente.
1. Enregistrez le résultat sur le disque.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
