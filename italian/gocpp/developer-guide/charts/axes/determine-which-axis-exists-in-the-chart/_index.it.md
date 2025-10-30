---
title: Determina quale asse esiste nel grafico con Golang tramite C++
description: Impara come determinare quale asse esiste in un grafico creato con Aspose.Cells for C++. La nostra guida ti aiuterà a capire come identificare e accedere ai diversi assi di un grafico, inclusi assi di categoria, valore, e secondari.
keywords: Aspose.Cells for C++, grafico, asse, esistenza, categoria, valore, secondario.
type: docs
weight: 140
url: /it/go-cpp/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

A volte, l'utente ha bisogno di sapere se un particolare asse esiste nel Grafico. Ad esempio, vuole sapere se esiste un Asse dei Valori Secondari all'interno del grafico o meno. Alcuni grafici come Diagramma a Torta, Torta Esplosa, TortaPie, TortaBarra, Torta3D, Torta3DEsplosa, Anello, Anello Esploso, ecc. non hanno un asse.

Aspose.Cells fornisce il metodo [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/go-cpp/chart/hasaxis/) per determinare se il grafico ha un particolare asse o meno.

{{% /alert %}}

Il seguente esempio di codice dimostra l'uso di [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/go-cpp/chart/hasaxis/) per determinare se il grafico di esempio ha assi di categoria e valore primari e secondari.

## Codice C++ per determinare quali assi esistono nel grafico

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetermineWhichAxisExistsInTheChart.go" >}}
## Output della console generato dall'esempio di codice

L'output della console del codice è stato mostrato di seguito che mostra true per la categoria primaria e l'asse dei valori e false per la categoria secondaria e l'asse dei valori.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
