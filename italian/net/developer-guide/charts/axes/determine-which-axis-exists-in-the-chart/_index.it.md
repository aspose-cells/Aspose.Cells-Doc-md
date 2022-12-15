---
title: Determina quale asse esiste nel grafico
type: docs
weight: 140
url: /it/net/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

volte, l'utente deve sapere se esiste un particolare asse nel grafico. Ad esempio, vuole sapere se esiste o meno un asse del valore secondario all'interno del grafico. Alcuni grafici come Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded, ecc. non hanno un asse.

 Aspose.Cells fornisce[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) metodo per determinare se il grafico ha un asse particolare o meno.

{{% /alert %}}

 Il codice di esempio seguente illustra l'utilizzo di[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis)per determinare se il grafico di esempio ha la categoria primaria e secondaria e l'asse dei valori.

## Codice C# per determinare quale asse esiste nel grafico

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-DetermineAxisInChart-DetermineAxisInChart.cs" >}}

## Output della console generato dal codice di esempio

Di seguito è mostrato l'output della console del codice che mostra true per la categoria primaria e l'asse del valore e false per la categoria secondaria e l'asse del valore.

{{< highlight "java" >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
