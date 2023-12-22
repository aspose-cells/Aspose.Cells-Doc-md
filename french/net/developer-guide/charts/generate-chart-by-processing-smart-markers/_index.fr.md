---
title: Générer un graphique en traitant des marqueurs intelligents
description: Apprenez à générer des graphiques avec des marqueurs intelligents en utilisant le Aspose.Cells for .NET. Notre guide vous montrera comment traiter les marqueurs intelligents et leurs propriétés pour améliorer l'apparence et la convivialité de vos graphiques.
keywords: Aspose.Cells for .NET, chart generation, smart markers, appearance, usability, processing.
type: docs
weight: 2100
url: /fr/net/generate-chart-by-processing-smart-markers/
---
{{% alert color="primary" %}}

 Les API Aspose.Cells fournissent le[**Concepteur de classeur**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) classe pour travailler avec des marqueurs intelligents où le formatage et les formules sont placés dans les feuilles de calcul du concepteur, puis traités avec[**Concepteur de classeur**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)classe pour remplir les données selon les marqueurs intelligents spécifiés. Il est également possible de créer des graphiques Excel en traitant des Smart Markers, ce qui nécessitera les étapes suivantes.

- Création d'une feuille de calcul de concepteur
- Feuille de calcul du concepteur de traitement par rapport à la source de données spécifiée
- Création d'un graphique basé sur des données renseignées

{{% /alert %}}

##  Création d'une feuille de calcul de concepteur

Une feuille de calcul de concepteur est un simple fichier Excel créé avec l'application Excel Microsoft ou les API Aspose.Cells contenant le formatage visuel, les formules et les marqueurs intelligents, où le contenu peut être renseigné au moment de l'exécution.

Par souci de simplicité, nous créerons la feuille de calcul du concepteur à l'aide du Aspose.Cells for .NET API et la traiterons plus tard par rapport à une source de données créée dynamiquement à des fins de démonstration.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

##  Feuille de calcul du concepteur de traitement

Afin de traiter la feuille de calcul du concepteur, il faut disposer d'une source de données qui correspond aux marqueurs intelligents utilisés dans la feuille de calcul du concepteur. Par exemple, nous avons créé une entrée de marqueur intelligent sous la forme &=Sales.Year, qui représente la colonne Année dans le DataTable Sales. Si une colonne correspondante n'est pas disponible dans la source de données, les API Aspose.Cells ignoreront le traitement pour ce marqueur intelligent particulier et, par conséquent, les données de ce marqueur intelligent particulier ne seront pas renseignées.

Afin de démontrer ce cas d'utilisation, nous allons créer la source de données à partir de zéro et la traiter par rapport à la feuille de calcul du concepteur créée à l'étape précédente. Toutefois, dans un scénario en temps réel, les données peuvent déjà être disponibles pour un traitement ultérieur. Vous pouvez donc ignorer la création d'une source de données si les données sont déjà disponibles.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

Le traitement des marqueurs intelligents est assez simple, comme le démontre l'extrait de code suivant.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

 L'extrait de code ci-dessus utilise l'instance existante du[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe créée lors de la première étape. Si vous disposez déjà du fichier de feuille de calcul du concepteur sur le disque ou en mémoire, vous pouvez créer une instance de[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe en chargeant la feuille de calcul du concepteur existante.

{{% /alert %}}

##  Création de graphique

 Une fois les données en place, il ne nous reste plus qu'à créer un graphique basé sur la source de données. Afin de garder l'exemple simple, nous utiliserons le[**Chart.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange)méthode afin que nous n’ayons pas à configurer davantage le graphique.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
