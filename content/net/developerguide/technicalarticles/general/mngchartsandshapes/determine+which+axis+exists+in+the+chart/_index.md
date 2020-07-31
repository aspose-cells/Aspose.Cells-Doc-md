---
title : "Determine which Axis exists in the Chart" 
description : "" 
weight : 20511 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/mngchartsandshapes/determine+which+axis+exists+in+the+chart/
---

# Aspose.Cells for .NET : Determine which Axis exists in the Chart


Sometimes, the user needs to know if a particular axis exists in the Chart. For example, he wants to know if a Secondary Value Axis exists inside the chart or not. Some charts like Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded, etc do not have an axis.

Aspose.Cells provides [Chart.HasAxis(AxisType axisType, bool isPrimary)](https://apireference.aspose.com/net/cells/aspose.cells.charts/chart/methods/hasaxis) method to determine if the chart has a particular axis or not.

The following sample code demonstrates the use of [Chart.HasAxis(AxisType axisType, bool isPrimary)](https://apireference.aspose.com/net/cells/aspose.cells.charts/chart/methods/hasaxis) to determine if the sample chart has Primary and Secondary Category and Value Axis.

## Console Output

The console output of the code has been shown below which displays true for Primary Category and Value Axis and false for Secondary Category and Value Axis.

{{< code lang="cs" >}}
Has Primary Category Axis: True
Has Secondary Category Axis: False
Has Primary Value Axis: True
Has Seconary Value Axis: False
{{< /code >}}

