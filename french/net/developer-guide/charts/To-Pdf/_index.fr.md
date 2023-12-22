---
title:  Carte au PDF
description: Découvrez comment utiliser Aspose.Cells for .NET pour convertir un graphique en document PDF. Notre guide vous montrera comment exporter un graphique à partir d'Excel Microsoft et l'enregistrer sous le nom PDF pour une distribution et un archivage ultérieurs.
keywords: Aspose.Cells for .NET, Chart to PDF, Microsoft Excel, PDF Conversion, Export, Distribution, Archiving.
type: docs
weight: 47
url: /fr/net/chart-to-pdf/
---
##  **Tableau de rendu au PDF**

 Afin de restituer le graphique au format PDF, les API Aspose.Cells ont exposé le[**Chart.ToPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)méthode avec la possibilité de stocker le PDF résultant sur le chemin du disque ou sur Stream.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToPDF.cs" >}}

##  **Créer le graphique PDF avec la taille de page souhaitée**
Vous pouvez créer un graphique PDF avec la taille de page souhaitée en utilisant Aspose.Cells et spécifier comment vous souhaitez aligner le graphique à l'intérieur de la page : haut, bas, centre, gauche, droite, etc. En outre, le graphique de sortie peut être créé en flux ou sur disque. Veuillez consulter l'exemple de code suivant qui charge le[exemple de fichier Excel](64716906.xlsx) , accède au premier graphique de la feuille de calcul, puis le convertit en[sortie PDF](64716907.pdf) avec la taille de page souhaitée. La capture d'écran suivante montre que la taille de la page dans le PDF de sortie est de 7 x 7, comme spécifié dans le code, et que le graphique est aligné au centre à la fois horizontalement et verticalement.

![tâche : image_alt_text](create-chart-pdf-with-desired-page-size_1.png)
##  **Exemple de code**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-CreateChartPDFWithDesiredPageSize.cs" >}}

