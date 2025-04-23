---
title: Determinare quale Asse esiste nel Grafico
description: Impara come determinare quale asse esiste in un grafico creato con Aspose.Cells per Python via .NET. La nostra guida ti aiuterà a capire come identificare e accedere ai vari assi in un grafico, inclusi gli assi di categoria, valore e secondari.
keywords: Aspose.Cells per Python via .NET, grafico, asse, esistenza, categoria, valore, secondario.
type: docs
weight: 140
url: /it/python-net/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

A volte, l'utente ha bisogno di sapere se un particolare asse esiste nel Grafico. Ad esempio, vuole sapere se esiste un Asse dei Valori Secondari all'interno del grafico o meno. Alcuni grafici come Diagramma a Torta, Torta Esplosa, TortaPie, TortaBarra, Torta3D, Torta3DEsplosa, Anello, Anello Esploso, ecc. non hanno un asse.

Aspose.Cells per Python via .NET fornisce il metodo [**Chart.has_axis(AxisType axis_type, bool is_primary)**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/has_axis) per determinare se un grafico ha un asse particolare o no.

{{% /alert %}}

Il seguente codice di esempio dimostra l'uso di [**Chart.has_axis(AxisType axis_type, bool is_primary)**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/has_axis) per determinare se il grafico di esempio ha assi di categoria e valore primari e secondari.

## Codice C# per determinare quali assi esistono nel grafico

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-DetermineAxisInChart.py" >}}

## Output della console generato dall'esempio di codice

L'output della console del codice è stato mostrato di seguito che mostra true per la categoria primaria e l'asse dei valori e false per la categoria secondaria e l'asse dei valori.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
