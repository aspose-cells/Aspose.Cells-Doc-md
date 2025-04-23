---
title: Leggere le etichette dell asse dopo il calcolo del grafico
description: Scopri come leggere le etichette dell asse in Aspose.Cells for .NET dopo il calcolo del grafico. La nostra guida ti mostrerà come accedere e recuperare le etichette dell asse, inclusa la loro formattazione e posizionamento.
keywords: Aspose.Cells for .NET, grafico, etichette degli assi, calcolo, lettura, accesso, recupero, formattazione, posizionamento.
type: docs
weight: 90
url: /it/net/read-axis-labels-after-calculating-the-chart/
---

## **Possibili Scenari di Utilizzo**

È possibile leggere le etichette degli assi del grafico dopo aver calcolato i valori utilizzando il metodo [**Chart.Calculate()**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/calculate/). Si prega di utilizzare il metodo [**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/getaxistexts/) a tale scopo che restituirà l'elenco delle etichette degli assi.

## **Leggere le etichette dell'asse dopo il calcolo del grafico**

Si prega di vedere il seguente codice di esempio che carica il file Excel di esempio e legge le etichette dell'asse delle categorie del grafico nel primo foglio di lavoro. Stampa quindi i valori delle etichette degli assi sulla console. Si prega di vedere l'output della console del codice di esempio riportato di seguito per un riferimento.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Charts-ReadAxisLabelsAfterCalculatingTheChart.cs" >}}

## **Output della console**

{{< highlight csharp >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
