---
title: Générer un graphique en traitant des marqueurs intelligents
description: Apprenez comment générer des graphiques avec des marqueurs intelligents en utilisant Aspose.Cells for .NET. Notre guide vous montrera comment traiter les marqueurs intelligents et leurs propriétés pour améliorer l apparence et l utilité de vos graphiques.
keywords: Aspose.Cells for .NET, génération de graphiques, marqueurs intelligents, apparence, utilité, traitement.
type: docs
weight: 2100
url: /fr/net/generate-chart-by-processing-smart-markers/
---

{{% alert color="primary" %}}

Les API Aspose.Cells fournissent la classe [**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) pour travailler avec les marqueurs intelligents, où la mise en forme et les formules sont placées dans les feuilles de calcul du concepteur, puis traitées avec la classe [**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) pour remplir les données selon les marqueurs intelligents spécifiés. Il est également possible de créer des graphiques Excel en traitant des marqueurs intelligents, ce qui nécessitera les étapes suivantes.

- Création de la feuille de calcul du concepteur
- Traitement de la feuille de calcul du concepteur par rapport à la source de données spécifiée
- Création d'un graphique basé sur des données populées

{{% /alert %}}

## Création d'une feuille Designer

Une feuille designer est un simple fichier Excel créé avec l'application Microsoft Excel ou les API Aspose.Cells contenant la mise en forme visuelle, des formules et des marqueurs intelligents, où le contenu peut être peuplé à l'exécution.

Pour des raisons de simplicité, nous créerons la feuille designer en utilisant l'API Aspose.Cells for .NET, puis nous la traiterons par rapport à une source de données créée dynamiquement à des fins de démonstration.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

## Traitement de la feuille Designer

Pour traiter la feuille designer, il faut disposer d'une source de données correspondant aux marqueurs intelligents utilisés dans la feuille designer. Par exemple, nous avons créé une entrée de marqueur intelligent comme &=Ventes.Annee, qui représente la colonne Année dans le DataTable des Ventes. Dans le cas où une colonne correspondante n'est pas disponible dans la source de données, les API Aspose.Cells sauteront le traitement pour ce marqueur intelligent particulier, et par conséquent, les données pour le marqueur intelligent particulier ne seront pas peuplées.

Afin de démontrer ce cas d'utilisation, nous créerons la source de données à partir de zéro et la traiterons par rapport à la feuille designer créée à l'étape précédente. Cependant, dans un scénario en temps réel, les données pourraient déjà être disponibles pour un traitement ultérieur, vous pouvez donc sauter la création de la source de données si les données sont déjà disponibles.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

Le traitement des marqueurs intelligents est assez simple comme le montre l'extrait de code suivant.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

L'extrait de code ci-dessus utilise l'instance existante de la classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) créée dans la première étape. Si vous avez déjà le fichier de feuille designer sur le disque ou en mémoire, vous pouvez créer une instance de la classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) en chargeant la feuille designer existante.

{{% /alert %}}

## Création d'un graphique

Une fois les données en place, il suffit de créer un graphique basé sur la source de données. Afin de garder l'exemple simple, nous utiliserons la méthode [**Chart.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange) afin de ne pas avoir à configurer davantage le graphique.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
