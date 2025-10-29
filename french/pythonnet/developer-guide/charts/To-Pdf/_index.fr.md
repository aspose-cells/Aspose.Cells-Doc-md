---
title: Graphique en PDF 
description: Découvrez comment utiliser Aspose.Cells pour Python via .NET pour convertir un graphique en un document PDF. Notre guide montrera comment exporter un graphique depuis Microsoft Excel et le sauvegarder en tant que PDF pour une distribution et une archivage ultérieurs.
keywords: Aspose.Cells pour Python via .NET, Graphique en PDF, Microsoft Excel, Conversion en PDF, Exportation, Distribution, Archivage.
type: docs
weight: 47
url: /fr/python-net/chart-to-pdf/
---

## **Rendu du graphique en PDF**

Pour rendre le graphique au format PDF, les API Aspose.Cells pour Python via .NET ont exposé la méthode [**Chart.to_pdf**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_pdf) avec la capacité de stocker le PDF résultant sur le chemin du disque ou en Stream.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChartRenderingChartToPDF.py" >}}

## **Créer un PDF de graphique avec la taille de page souhaitée**
Vous pouvez créer un PDF de graphique avec la taille de page souhaitée en utilisant Aspose.Cells pour Python via .NET et spécifier la façon dont vous souhaitez aligner le graphique à l’intérieur de la page, comme en haut, en bas, au centre, à gauche, à droite, etc. De plus, le graphique de sortie peut être créé dans un flux ou sur le disque. Voici un exemple de code qui charge le fichier Excel [exemple](64716906.xlsx), accède au premier graphique dans la feuille de calcul, puis le convertit en [PDF de sortie](64716907.pdf) avec la taille de page souhaitée. La capture d'écran suivante montre que la taille de la page dans le PDF de sortie est de 7x7 comme spécifié dans le code et que le graphique est aligné au centre à la fois horizontalement et verticalement. 

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)
## **Code d'exemple**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateChartPDFWithDesiredPageSize.py" >}}

{{< app/cells/assistant language="python-net" >}}
