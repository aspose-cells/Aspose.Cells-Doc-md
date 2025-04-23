---
title: Leggere le etichette dell asse dopo il calcolo del grafico
description: Scopri come leggere le etichette degli assi in Aspose.Cells for Java dopo aver calcolato il grafico. La nostra guida ti mostrerà come accedere e recuperare le etichette degli assi, inclusa la loro formattazione e posizionamento.
keywords: Aspose.Cells for Java, grafico, etichette degli assi, calcolo, lettura, accesso, recupero, formattazione, posizionamento.
type: docs
weight: 90
url: /it/java/read-axis-labels-after-calculating-the-chart/
---

## **Possibili Scenari di Utilizzo**

Puoi leggere le etichette degli assi del tuo grafico dopo aver calcolato i suoi valori utilizzando il metodo [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart/#calculate--). Si prega di utilizzare il metodo [**Axis.getAxisTexts()**](https://reference.aspose.com/cells/java/com.aspose.cells/axis/#getAxisTexts--) per questo scopo che restituirà l'elenco delle etichette degli assi.

## **Leggere le etichette dell'asse dopo il calcolo del grafico**

Si prega di consultare il codice di esempio seguente che carica il [file di Excel di esempio](64716829.xlsx) e legge le etichette dell'asse delle categorie del grafico nel primo foglio di lavoro. Quindi stampa i valori delle etichette degli assi sulla console. Si prega di consultare l'output della console del codice di esempio sottostante per un riferimento.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-ReadAxisLabelsAfterCalculatingTheChart.java" >}}

## **Output della console**

{{< highlight java >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
