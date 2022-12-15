---
title: Creazione e personalizzazione di grafici
type: docs
weight: 10
url: /it/cpp/creating-and-customizing-charts/
---
## **Possibili scenari di utilizzo**

Un grafico è una visualizzazione visiva di informazioni. Aspose.Cells consente agli sviluppatori di visualizzare le informazioni nei grafici proprio come fa Microsoft Excel. La presentazione delle informazioni nei grafici è sempre utile ai decisori per prendere decisioni rapide e tempestive. È più facile vedere rapidamente confronti, modelli e tendenze nei dati con grafici piuttosto che numeri grezzi. La creazione di grafici in fase di esecuzione, basati sui dati in un foglio di calcolo, è una delle funzionalità utili di Aspose.Cells. Aspose.Cells supporta la creazione di grafici standard e personalizzati. Di seguito, mostreremo alcuni esempi con file di esempio su come creare alcuni tipi di grafici MS-Excel comuni utilizzando l'API Aspose.Cells.

## **Grafico a piramide**

 Quando viene eseguito il codice di esempio, al foglio di lavoro viene aggiunto un grafico a piramide. Si prega di consultare il[file Excel di output](66519068.xlsx) del seguente codice di esempio.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_PyramidChart.cpp" >}}

## **Grafico a linee**

Nell'esempio sopra, semplicemente cambiando il file[**Tipo di grafico**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70)a[**GraficoTipo_Linea**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70ad12ff1561ab1424a0c3095b6dc07ac25)crea un grafico a linee. La fonte completa è fornita di seguito. quando il codice viene eseguito, al foglio di lavoro viene aggiunto un grafico a linee. Si prega di consultare il[file Excel di output](66519069.xlsx) del seguente codice di esempio.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_LineChart.cpp" >}}

## **Grafico a bolle**

Per creare un grafico a bolle, il[**Tipo di grafico**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70) deve essere impostato su[**ChartType_Bolla**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70a5efa533b454f9415e4497dbb2ab28b3d) e poche proprietà extra come[**Imposta dimensioni bolla**](https://reference.aspose.com/cells/cpp/class/aspose.cells.charts.i_series#a00cf890ba7ab419d31a522ab52b02e9d) & [**ImpostaXValori**](https://reference.aspose.com/cells/cpp/class/aspose.cells.charts.i_series#a788ff4aa51dbf9bed5327298af93a6db) devono essere impostati di conseguenza. Dopo aver eseguito il codice seguente, al foglio di lavoro viene aggiunto un grafico a bolle. Si prega di consultare il[file Excel di output](66519070.xlsx) del seguente codice di esempio.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_BubbleChart.cpp" >}}

## **Creazione di grafici personalizzati**

Finora, quando abbiamo discusso dei grafici, abbiamo esaminato i grafici standard che hanno le proprie impostazioni di formattazione standard. Definiamo solo l'origine dati, impostiamo alcune proprietà e il grafico viene creato con le impostazioni di formato predefinite. Ma le API Aspose.Cells supportano anche la creazione di grafici personalizzati che consentono agli sviluppatori di creare grafici con le proprie impostazioni di formato. Gli sviluppatori possono creare grafici personalizzati in fase di esecuzione utilizzando Aspose.Cells.

Un grafico è composto da una serie di dati. Durante la creazione di un grafico personalizzato, gli sviluppatori hanno la libertà di utilizzare diversi tipi di grafici per diverse serie di dati.

 Il codice di esempio riportato di seguito mostra come creare grafici personalizzati. In questo esempio, utilizzeremo un istogramma per la prima serie di dati e un grafico a linee per la seconda serie. Il risultato è che aggiungiamo un istogramma, combinato con un grafico a linee, al foglio di lavoro. Si prega di consultare il[file Excel di output](66519071.xlsx) del seguente codice di esempio.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_CustomChart.cpp" >}}
