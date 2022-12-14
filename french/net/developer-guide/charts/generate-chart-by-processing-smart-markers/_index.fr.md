---
title: Générer un graphique en traitant des marqueurs intelligents
type: docs
weight: 2100
url: /fr/net/generate-chart-by-processing-smart-markers/
---
{{% alert color="primary" %}}

 Aspose.Cells Les API fournissent le[**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)classe pour travailler avec des marqueurs intelligents où la mise en forme et les formules sont placées dans les feuilles de calcul du concepteur, puis traitées avec[**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)classe pour remplir les données selon les marqueurs intelligents spécifiés. Il est également possible de créer des graphiques Excel en traitant des marqueurs intelligents, ce qui nécessitera les étapes suivantes.

- Création d'une feuille de calcul de concepteur
- Traitement de la feuille de calcul du concepteur par rapport à la source de données spécifiée
- Création de graphique basé sur des données peuplées

{{% /alert %}}

## Création d'une feuille de calcul Designer

Une feuille de calcul de concepteur est un simple fichier Excel créé avec l'application Excel Microsoft ou les API Aspose.Cells contenant le formatage visuel, les formules et les marqueurs intelligents, où le contenu peut être rempli au moment de l'exécution.

Par souci de simplicité, nous allons créer la feuille de calcul du concepteur à l'aide du Aspose.Cells for .NET API, puis la traiter par rapport à une source de données créée dynamiquement à des fins de démonstration.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

## Feuille de calcul du concepteur de traitement

Pour traiter la feuille de calcul du concepteur, il faut disposer d'une source de données correspondant aux marqueurs intelligents utilisés dans la feuille de calcul du concepteur. Par exemple, nous avons créé une entrée Smart Marker sous la forme &=Sales.Year, qui représente la colonne Year dans le DataTable Sales. Si une colonne correspondante n'est pas disponible dans la source de données, les API Aspose.Cells ignoreront le traitement pour ce marqueur intelligent particulier et, par conséquent, les données pour le marqueur intelligent particulier ne seront pas renseignées.

Afin de démontrer ce cas d'utilisation, nous allons créer la source de données à partir de zéro et la traiter par rapport à la feuille de calcul du concepteur créée à l'étape précédente. Cependant, dans un scénario en temps réel, les données peuvent déjà être disponibles pour un traitement ultérieur, vous pouvez donc ignorer la création de la source de données si les données sont déjà disponibles.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

Le traitement des marqueurs intelligents est assez simple, comme le montre l'extrait de code suivant.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

 L'extrait de code ci-dessus utilise l'instance existante de[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe créée à la première étape. Si vous disposez déjà du fichier de feuille de calcul du concepteur sur disque ou en mémoire, vous pouvez créer une instance de[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe en chargeant la feuille de calcul de concepteur existante.

{{% /alert %}}

## Création de graphique

 Une fois les données en place, tout ce que nous avons à faire est de créer un graphique basé sur la source de données. Afin de garder l'exemple simple, nous utiliserons le[**Chart.SetChartDataRangeChart.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange)afin que nous n'ayons pas à configurer davantage le graphique.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
