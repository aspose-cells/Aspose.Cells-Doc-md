---
title: Determina quale asse esiste nel grafico
type: docs
weight: 130
url: /it/java/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

A volte, l'utente deve sapere se esiste un particolare asse nel grafico. Ad esempio, vuole sapere se esiste o meno un asse del valore secondario all'interno del grafico. Alcuni grafici come Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded ecc. non hanno un asse.

 Aspose.Cells fornisce[**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis(int,%20boolean)) metodo per determinare se il grafico ha un asse particolare o meno.

{{% /alert %}}

## Determina quale asse esiste nel grafico

Lo screenshot seguente mostra un grafico con solo la categoria primaria e l'asse del valore. Non ha alcuna categoria secondaria e asse del valore.

![cose da fare:immagine_alt_testo](determine-which-axis-exists-in-the-chart_1.png)

 Il codice di esempio seguente illustra l'utilizzo di[**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis(int,%20boolean)per determinare se il grafico di esempio ha la categoria primaria e secondaria e l'asse dei valori. Di seguito è mostrato l'output della console del codice che mostra true per la categoria primaria e l'asse del valore e false per la categoria secondaria e l'asse del valore.

### Codice Java per determinare quale asse esiste nel grafico

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetermineWhichAxisExistsInChart-DetermineWhichAxisExistsInChart.java" >}}

### Output della console generato dal codice di esempio

Ecco l'output della console del codice di esempio sopra.

{{< highlight "java" >}}

Has Primary Category Axis: true

Has Secondary Category Axis: false

Has Primary Value Axis: true

Has Secondary Value Axis: false

{{< /highlight >}}
