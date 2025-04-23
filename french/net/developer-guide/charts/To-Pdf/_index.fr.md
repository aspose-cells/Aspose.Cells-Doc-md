---
title: Graphique en PDF 
description: Apprenez comment utiliser Aspose.Cells for .NET pour convertir un graphique en document PDF. Notre guide vous montrera comment exporter un graphique depuis Microsoft Excel et le sauvegarder en tant que PDF pour une distribution et une archivage ultérieurs.
keywords: Aspose.Cells for .NET, Graphique en PDF, Microsoft Excel, Conversion PDF, Exportation, Distribution, Archivage.
type: docs
weight: 47
url: /fr/net/chart-to-pdf/
---

## **Rendu du graphique en PDF**

Pour rendre le graphique au format PDF, les API Aspose.Cells ont exposé la méthode [**Chart.ToPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index) avec la possibilité de stocker le PDF résultant sur le chemin du disque ou le flux.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToPDF.cs" >}}

## **Créer un PDF de graphique avec la taille de page souhaitée**
Vous pouvez créer un PDF de graphique avec votre taille de page souhaitée en utilisant Aspose.Cells et spécifier comment vous voulez aligner le graphique à l'intérieur de la page en haut, en bas, au centre, à gauche, à droite, etc. En outre, le graphique de sortie peut être créé en flux ou sur le disque. Veuillez consulter le code d'exemple suivant qui charge le [fichier Excel d'exemple](64716906.xlsx), accède au premier graphique à l'intérieur de la feuille de calcul, puis le convertit en [PDF de sortie](64716907.pdf) avec la taille de page souhaitée. La capture d'écran suivante montre que la taille de la page dans le PDF de sortie est 7x7 comme spécifié dans le code et que le graphique est aligné au centre à la fois horizontalement et verticalement. 

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)
## **Code d'exemple**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-CreateChartPDFWithDesiredPageSize.cs" >}}

{{< app/cells/assistant language="csharp" >}}
