---
title: Déterminez quel axe existe dans le graphique
description: Apprenez comment déterminer quel axe existe dans un graphique créé à l aide d Aspose.Cells pour Python via .NET. Notre guide vous aidera à comprendre comment identifier et accéder aux différents axes dans un graphique, y compris les axes de catégorie, de valeur et secondaires.
keywords: Aspose.Cells pour Python via .NET, graphique, axe, existence, catégorie, valeur, secondaire.
type: docs
weight: 140
url: /fr/python-net/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

Parfois, l'utilisateur a besoin de savoir si un axe particulier existe dans le graphique. Par exemple, il veut savoir si un axe de valeurs secondaires existe à l'intérieur du graphique ou non. Certains graphiques comme Camembert, CamembertExploded, CamembertCamembert, CamembertBarre, Camembert3D, Camembert3DExploded, Anneau, AnneauExploded, etc. n'ont pas d'axe.

Aspose.Cells pour Python via .NET fournit la méthode [**Chart.has_axis(AxisType axis_type, bool is_primary)**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/has_axis) pour déterminer si le graphique possède un axe particulier ou non.

{{% /alert %}}

Le code d'exemple suivant démontre l'utilisation de [**Chart.has_axis(AxisType axis_type, bool is_primary)**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/has_axis) pour déterminer si le graphique d'exemple possède des axes de catégorie et de valeurs primaires et secondaires.

## Code C# pour déterminer quels axes existent dans le graphique

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-DetermineAxisInChart.py" >}}

## Sortie console générée par le code d'exemple

La sortie de la console du code est affichée ci-dessous, affichant true pour la Catégorie Principale et Axe de Valeur, et false pour la Catégorie Secondaire et Axe de Valeur.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
