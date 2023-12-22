---
title: Créer des graphiques dynamiques
description: Apprenez à créer des graphiques dynamiques au Aspose.Cells for .NET. Notre guide vous montrera comment mettre à jour dynamiquement les données, les séries et le formatage des graphiques en fonction de vos besoins, vous permettant de présenter visuellement les données changeantes dans vos feuilles de calcul.
keywords: Aspose.Cells for .NET, charting, dynamic charts, data, series, formatting, worksheets, updating.
type: docs
weight: 240
url: /fr/net/create-dynamic-charts/
---
{{% alert color="primary" %}}

Les graphiques dynamiques (ou interactifs) ont la possibilité de changer lorsque vous modifiez la portée des données. En d'autres termes, les graphiques dynamiques peuvent refléter automatiquement les changements lorsque la source de données est modifiée. Afin de déclencher le changement de source de données, on peut utiliser l'option de filtrage des tableaux Excel ou utiliser un contrôle tel que ComboBox ou Dropdown list.

Cet article montre l'utilisation des API Aspose.Cells for .NET pour créer des graphiques dynamiques à l'aide des deux approches susmentionnées.

{{% /alert %}}

##  **Utiliser des tableaux Excel**

{{% alert color="primary" %}}

 Les tableaux Excel sont appelés ListObjects dans la perspective Aspose.Cells. Par conséquent, nous utiliserons le terme « ListObject » au lieu de « Table » pour plus de clarté. Veuillez lire en détail comment[créer des objets de liste](/cells/fr/net/create-and-format-table/)avec Aspose.Cells for .NET API.

{{% /alert %}}

 ListObjects fournit la fonctionnalité intégrée pour trier et filtrer les données lors de l'interaction de l'utilisateur. Les options de tri et de filtrage sont fournies via les listes déroulantes qui sont automatiquement ajoutées à la ligne d'en-tête du[**ObjetListe**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) . Grâce à ces fonctionnalités (tri et filtrage), le[**ObjetListe**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) semble être le candidat idéal pour servir de source de données à un graphique dynamique, car lorsque le tri ou le filtrage est modifié, la représentation des données dans le graphique sera modifiée pour refléter l'état actuel du graphique.[**ObjetListe**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).

 Afin de garder la démonstration simple à comprendre, nous allons créer le[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook)à partir de zéro et avancez étape par étape comme indiqué ci-dessous.

1.  Créer un vide[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1.  Accéder au[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) du premier[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) dans le[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Insérez des données dans les cellules.
1.  Créer[**ObjetListe**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)en fonction des données insérées.
1.  Créer[**Graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) basé sur la plage de données de[**ObjetListe**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).
1. Enregistrez le résultat sur le disque.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

##  **Utiliser des formules dynamiques**

Si vous ne souhaitez pas utiliser le[**ObjetListe**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)en tant que source de données pour le graphique dynamique, l'autre option consiste à utiliser des fonctions (ou formules) Excel pour créer une plage dynamique de données et un contrôle (tel que ComboBox) pour déclencher la modification des données. Dans ce scénario, nous utiliserons la fonction RECHERCHEV pour récupérer les valeurs appropriées en fonction de la sélection de ComboBox. Lorsque la sélection est modifiée, la fonction RECHERCHEV actualisera la valeur de la cellule. Si une plage de cellules utilise la fonction RECHERCHEV, la plage entière peut être actualisée lors de l'interaction de l'utilisateur, elle peut donc être utilisée comme source du graphique dynamique.

Afin de garder la démonstration simple à comprendre, nous allons créer le classeur à partir de zéro et avancer étape par étape comme indiqué ci-dessous.

1.  Créer un vide[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1.  Accéder au[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) du premier[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) dans le[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Insérez des données dans les cellules en créant une plage nommée. Ces données serviront de série au graphique dynamique.
1.  Créer[**Boîte combo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox)en fonction de la plage nommée créée à l’étape précédente.
1. Insérez quelques données supplémentaires dans les cellules qui serviront de source à la fonction RECHERCHEV.
1. Insérez la fonction RECHERCHEV (avec les paramètres appropriés) dans une plage de cellules. Cette plage servira de source au graphique dynamique.
1.  Créer[**Graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)en fonction de la plage créée à l’étape précédente.
1. Enregistrez le résultat sur le disque.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
