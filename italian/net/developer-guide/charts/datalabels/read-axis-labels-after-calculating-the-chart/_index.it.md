---
title: Leggi le etichette degli assi dopo aver calcolato il grafico
description: Scopri come leggere le etichette degli assi in Aspose.Cells for .NET dopo aver calcolato il grafico. La nostra guida ti mostrerà come accedere e recuperare le etichette degli assi, inclusi la loro formattazione e posizionamento.
keywords: Aspose.Cells for .NET, chart, axis labels, calculation, reading, accessing, retrieving, formatting, positioning.
type: docs
weight: 90
url: /it/net/read-axis-labels-after-calculating-the-chart/
---
##  **Possibili scenari di utilizzo**

Puoi leggere le etichette degli assi del tuo grafico dopo aver calcolato i suoi valori utilizzando[**Grafico.Calcola()**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/calculate/)metodo. Si prega di utilizzare il[**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/getaxistexts/) metodo a questo scopo che restituirà l'elenco delle etichette degli assi.

##  **Leggi le etichette degli assi dopo aver calcolato il grafico**

Consulta il seguente codice di esempio che carica il file[file Excel di esempio](ReadAxisLabels.xlsx)e legge le etichette degli assi delle categorie del grafico nel primo foglio di lavoro. Quindi stampa i valori delle etichette degli assi sulla console. Per riferimento, vedere l'output della console del codice di esempio fornito di seguito.

##  **Codice d'esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Charts-ReadAxisLabelsAfterCalculatingTheChart.cs" >}}

##  **Uscita della console**

{{< highlight "csharp" >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
