---
title: Définir le type de forme des étiquettes de données du graphique
description: Découvrez comment définir le type de forme des étiquettes de données dans les graphiques en utilisant le Aspose.Cells for .NET. Notre guide vous expliquera les différents types de forme disponibles et vous montrera comment choisir la forme appropriée pour vos étiquettes de données afin d'améliorer la présentation et la convivialité de vos graphiques.
keywords: Aspose.Cells for .NET, charting, data labels, shape types, presentation, usability.
type: docs
weight: 110
url: /fr/net/set-the-shape-type-of-data-labels-of-chart/
---
##  **Scénarios d'utilisation possibles**
Vous pouvez modifier le type de forme des étiquettes de données du graphique à l'aide de la propriété DataLabels.ShapeType. Il prend la valeur de l'énumération DataLabelShapeType et modifie le type de forme des étiquettes de données en conséquence. Certaines de ses valeurs sont

{{< highlight "java" >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}
##  **Définir le type de forme des étiquettes de données du graphique**
 L’exemple de code suivant modifie le type de forme des étiquettes de données du graphique en DataLabelShapeType.WedgeEllipseCallout. Veuillez consulter le[exemple de fichier Excel](60489778.xlsx) utilisé dans ce code et le[sortie du fichier Excel](60489779.xlsx)généré par celui-ci. La capture d'écran montre l'effet du code sur un exemple de fichier Excel.

![tâche : image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
##  **Exemple de code**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetShapeTypeOfDataLabelsOfChart.cs" >}}
