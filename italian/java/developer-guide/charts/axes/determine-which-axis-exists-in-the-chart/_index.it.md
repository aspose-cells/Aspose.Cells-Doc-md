---
title: Determinare quale Asse esiste nel Grafico
type: docs
weight: 130
url: /it/java/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

A volte, l'utente ha bisogno di sapere se un particolare asse esiste nel grafico. Ad esempio, vuole sapere se esiste un asse dei valori secondari all'interno del grafico o meno. Alcuni grafici come Torta, TortaEsplosa, TortaTorta, TortaBarra, Torta3D, Torta3DEsplosa, Anello, AnelloEsploso, ecc. non hanno un asse.

Aspose.Cells fornisce il metodo [**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis-int-boolean-) per determinare se il grafico ha un particolare asse o meno.

{{% /alert %}}

## Determinare quali assi esistono nel grafico

La seguente schermata mostra un grafico che ha solo l'asse della categoria primaria e dei valori. Non ha alcun asse della categoria e dei valori secondari.

![todo:image_alt_text](determine-which-axis-exists-in-the-chart_1.png)

Il seguente codice di esempio dimostra l'uso di [**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis-int-boolean-) per determinare se il grafico di esempio ha assi della categoria primaria e secondaria e assi dei valori. L'output della console del codice è mostrato di seguito e visualizza true per l'asse della categoria e dei valori primari e false per l'asse della categoria e dei valori secondari.

### Codice Java per determinare quali assi esistono nel grafico

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetermineWhichAxisExistsInChart-DetermineWhichAxisExistsInChart.java" >}}

### Uscita della console generata dal codice di esempio

Ecco l'Output della Console del codice di esempio sopra.

{{< highlight java >}}

Has Primary Category Axis: true

Has Secondary Category Axis: false

Has Primary Value Axis: true

Has Secondary Value Axis: false

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
