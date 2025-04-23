---
title: Créer des graphiques dynamiques
description: Apprenez à créer des graphiques dynamiques dans Aspose.Cells pour Python via .NET. Notre guide vous montrera comment mettre à jour dynamiquement les données du graphique, les séries et la mise en forme en fonction de vos besoins, vous permettant de présenter visuellement des données changeantes dans vos feuilles de calcul.
keywords: Aspose.Cells pour Python via .NET, création de graphiques, graphiques dynamiques, données, séries, mise en forme, feuilles de calcul, mise à jour.
type: docs
weight: 240
url: /fr/python-net/create-dynamic-charts/
---

{{% alert color="primary" %}}

Les graphiques dynamiques (ou interactifs) ont la capacité de changer lorsque vous modifiez la portée des données. En d'autres termes, les graphiques dynamiques peuvent refléter automatiquement les modifications lorsque la source de données est modifiée. Pour déclencher le changement de la source de données, on peut utiliser l'option de filtrage des tables Excel ou utiliser un contrôle tel qu'une liste déroulante ou une liste déroulante.

Cet article démontre l'utilisation des API Aspose.Cells pour Python via .NET pour créer des graphiques dynamiques en utilisant les deux approches mentionnées ci-dessus.

{{% /alert %}}

## **Utilisation des tables Excel**

{{% alert color="primary" %}}

Les tableaux Excel sont appelés ListObjects dans la perspective d'Aspose.Cells, donc nous utiliserons le terme "ListObject" au lieu de "Table" pour plus de clarté. Veuillez lire en détail comment [créer des ListObjects](/cells/fr/python-net/create-and-format-table/) avec l'API Aspose.Cells pour Python via .NET.

{{% /alert %}}

Les ListObjects offrent la fonctionnalité intégrée de tri et de filtrage des données sur interaction de l'utilisateur. Les options de tri et de filtrage sont fournies via des menus déroulants qui sont automatiquement ajoutés à la ligne d'en-tête de la . En raison de ces fonctionnalités (tri et filtrage), le [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) semble être le candidat idéal pour servir de source de données à un graphique dynamique, car lorsque le tri ou le filtrage est modifié, la représentation des données dans le graphique sera modifiée pour refléter l'état actuel de la .

Pour simplifier la démonstration et la rendre compréhensible, nous créerons le [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) à partir de zéro et avancerons pas à pas comme indiqué ci-dessous.

1. Créez un [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) vide.
1. Accédez au [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) du premier [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) dans le [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).
1. Insérez des données dans les cellules.
1. Créez [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) basé sur les données insérées.
1. Créez [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) basé sur la plage de données de [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject).
1. Enregistrez le résultat sur le disque.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateDynamicCharts.py" >}}

## **Utilisation de Formules Dynamiques**

Si vous ne souhaitez pas utiliser le [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) comme source de données pour le graphique dynamique, une autre option consiste à utiliser des fonctions Excel (ou des formules) pour créer une plage de données dynamique et un contrôle (tel qu'une zone de liste déroulante) pour déclencher le changement de données. Dans ce scénario, nous utiliserons la fonction VLOOKUP pour récupérer les valeurs appropriées en fonction de la sélection de la zone de liste déroulante. Lorsque la sélection est modifiée, la fonction VLOOKUP actualisera la valeur de la cellule. Si une plage de cellules utilise la fonction VLOOKUP, l'ensemble de la plage peut être actualisé lors de l'interaction de l'utilisateur, et peut donc être utilisée comme source pour le graphique dynamique.

Afin de simplifier la démonstration et de la rendre compréhensible, nous créerons le classeur à partir de zéro et avancerons étape par étape comme décrit ci-dessous.

1. Créez un [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) vide.
1. Accédez au [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) du premier [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) dans le [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).
1. Insérez des données dans les cellules en créant une plage nommée. Ces données serviront de série pour le graphique dynamique.
1. Créez [**ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox) basé sur la Plage nommée créée à l'étape précédente.
1. Insérez quelques autres données dans les cellules qui serviront de source à la fonction VLOOKUP.
1. Insérez la fonction VLOOKUP (avec les paramètres appropriés) dans une plage de cellules. Cette plage servira de source pour le graphique dynamique.
1. Créez [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) basé sur la plage créée à l'étape précédente.
1. Enregistrez le résultat sur le disque.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateDynamicChartsUsingDynamicFormula.py" >}}
