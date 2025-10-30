---
title: Leggere le etichette dell asse dopo il calcolo del grafico
description: Impara come leggere le etichette degli assi in Aspose.Cells per Python via .NET dopo aver calcolato il grafico. La nostra guida ti mostrerà come accedere e recuperare le etichette degli assi, inclusi il loro formato e posizionamento.
keywords: Aspose.Cells per Python via .NET, grafico, etichette degli assi, calcolo, lettura, accesso, recupero, formattazione, posizionamento.
type: docs
weight: 90
url: /it/python-net/read-axis-labels-after-calculating-the-chart/
---

## **Possibili Scenari di Utilizzo**

È possibile leggere le etichette degli assi del grafico dopo aver calcolato i valori utilizzando il metodo [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/). Si prega di utilizzare il metodo [**Axis.get_axis_texts()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/axis/get_axis_texts) a tale scopo che restituirà l'elenco delle etichette degli assi.

## **Leggere le etichette dell'asse dopo il calcolo del grafico**

Si prega di vedere il seguente codice di esempio che carica il file Excel di esempio e legge le etichette dell'asse delle categorie del grafico nel primo foglio di lavoro. Stampa quindi i valori delle etichette degli assi sulla console. Si prega di vedere l'output della console del codice di esempio riportato di seguito per un riferimento.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ReadAxisLabelsAfterCalculatingTheChart.py" >}}

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
{{< app/cells/assistant language="python-net" >}}
