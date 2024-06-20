---
title: Creazione e personalizzazione di grafici
type: docs
weight: 10
url: /it/cpp/creating-and-customizing-charts/
---

## **Possibili Scenari di Utilizzo**

Un grafico è una visualizzazione visuale delle informazioni. Aspose.Cells consente agli sviluppatori di visualizzare le informazioni nei grafici proprio come fa Microsoft Excel. Presentare informazioni nei grafici è sempre utile per i decision maker per prendere decisioni rapide e tempestive. È più facile vedere rapidamente confronti, pattern e tendenze nei dati con i grafici piuttosto che con i numeri grezzi. La creazione di grafici a tempo di esecuzione, basati sui dati in un foglio di calcolo, è una delle utili funzionalità di Aspose.Cells. Aspose.Cells supporta la creazione di grafici standard e personalizzati. Di seguito, mostreremo alcuni esempi con file di esempio su come creare alcuni tipi comuni di grafici MS-Excel utilizzando l'API di Aspose.Cells.

## **Grafico a piramide**

Quando il codice di esempio viene eseguito, viene aggiunto un grafico a piramide al foglio di lavoro. Si prega di consultare il [file Excel di output](66519068.xlsx) del seguente codice di esempio.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_PyramidChart-new.cpp" >}}

## **Grafico a linee**

Nell'esempio precedente, cambiare semplicemente [**ChartType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/) in **`ChartType::Line`** crea un grafico a linee. Di seguito viene fornito il codice completo. Quando il codice viene eseguito, viene aggiunto un grafico a linee al foglio di lavoro. Si prega di consultare il [file Excel di output](66519069.xlsx) del seguente codice di esempio.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_LineChart-new.cpp" >}}

## **Grafico a bolle**

Per creare un grafico a bolle, [**ChartType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/) deve essere impostato su **`ChartType_Bubble`** e alcune proprietà aggiuntive come [**SetBubbleSizes**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setbubblesizes/) e [**SetXValues**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setxvalues/) devono essere impostate di conseguenza. Dopo aver eseguito il seguente codice, viene aggiunto un grafico a bolle al foglio di lavoro. Si prega di consultare il [file Excel di output](66519070.xlsx) del seguente codice di esempio.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_BubbleChart-new.cpp" >}}

## **Creazione di grafici personalizzati**

Finora, quando abbiamo discusso dei grafici, abbiamo esaminato grafici standard che hanno le proprie impostazioni di formattazione standard. Definiamo solo la fonte dei dati, impostiamo alcune proprietà e il grafico viene creato con le sue impostazioni di formato predefinite. Ma le API Aspose.Cells supportano anche la creazione di grafici personalizzati che consentono ai programmatori di creare grafici con le proprie impostazioni di formato. I programmatori possono creare grafici personalizzati durante l'esecuzione utilizzando Aspose.Cells.

Un grafico è composto da una serie di dati. Nella creazione di un grafico personalizzato, i programmatori hanno la libertà di utilizzare diversi tipi di grafici per diverse serie di dati.

Il seguente codice di esempio mostra come creare grafici personalizzati. In questo esempio, useremo un grafico a colonne per la prima serie di dati e un grafico a linee per la seconda serie. Il risultato è che aggiungiamo un grafico a colonne, combinato con un grafico a linee, al foglio di lavoro. Si prega di consultare il [file Excel di output](66519071.xlsx) del seguente codice di esempio.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_CustomChart-new.cpp" >}}
