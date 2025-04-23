---
title: Determinare quale Asse esiste nel Grafico
description: Scopri come determinare quale asse esiste in un grafico creato utilizzando Aspose.Cells for .NET. La nostra guida ti aiuterà a capire come identificare e accedere ai diversi assi in un grafico, inclusi categorie, valori e assi secondari.
keywords: Aspose.Cells for .NET, grafico, asse, esistenza, categoria, valore, secondario.
type: docs
weight: 140
url: /it/net/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

A volte, l'utente ha bisogno di sapere se un particolare asse esiste nel Grafico. Ad esempio, vuole sapere se esiste un Asse dei Valori Secondari all'interno del grafico o meno. Alcuni grafici come Diagramma a Torta, Torta Esplosa, TortaPie, TortaBarra, Torta3D, Torta3DEsplosa, Anello, Anello Esploso, ecc. non hanno un asse.

Aspose.Cells fornisce il metodo [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) per determinare se il grafico ha un particolare asse o meno.

{{% /alert %}}

Il seguente codice di esempio dimostra l'uso di [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) per determinare se il grafico di esempio ha assi di categoria e valore primari e secondari.

## Codice C# per determinare quali assi esistono nel grafico

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-DetermineAxisInChart-DetermineAxisInChart.cs" >}}

## Output della console generato dall'esempio di codice

L'output della console del codice è stato mostrato di seguito che mostra true per la categoria primaria e l'asse dei valori e false per la categoria secondaria e l'asse dei valori.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
