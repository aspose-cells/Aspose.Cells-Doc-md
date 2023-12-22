---
title: Determina quale asse esiste nel grafico
description: Scopri come determinare quale asse esiste in un grafico creato utilizzando Aspose.Cells for .NET. La nostra guida ti aiuterà a capire come identificare e accedere ai diversi assi in un grafico, inclusi categoria, valore e assi secondari.
keywords: Aspose.Cells for .NET, chart, axis, existence, category, value, secondary.
type: docs
weight: 140
url: /it/net/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

A volte, l'utente ha bisogno di sapere se un particolare asse esiste nel grafico. Ad esempio, vuole sapere se esiste o meno un asse dei valori secondario all'interno del grafico. Alcuni grafici come Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded, ecc. non hanno un asse.

 Aspose.Cells fornisce[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) metodo per determinare se il grafico ha un asse particolare o meno.

{{% /alert %}}

 Il codice di esempio seguente illustra l'utilizzo di[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis)per determinare se il grafico di esempio ha una categoria primaria e secondaria e un asse dei valori.

##  Codice C# per determinare quale asse esiste nel grafico

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-DetermineAxisInChart-DetermineAxisInChart.cs" >}}

## Output della console generato dal codice di esempio

Di seguito è stato mostrato l'output della console del codice che visualizza true per la categoria primaria e l'asse dei valori e false per la categoria secondaria e l'asse dei valori.

{{< highlight "java" >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
