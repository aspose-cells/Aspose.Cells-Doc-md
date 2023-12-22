---
title: Creazione e personalizzazione di grafici
type: docs
weight: 10
url: /it/cpp/creating-and-customizing-charts/
---
##  **Possibili scenari di utilizzo**

Un grafico è una visualizzazione visiva di informazioni. Aspose.Cells consente agli sviluppatori di visualizzare le informazioni nei grafici proprio come fa Microsoft Excel. Presentare le informazioni nei grafici è sempre utile ai decisori per prendere decisioni rapide e tempestive. È più facile vedere rapidamente confronti, modelli e tendenze nei dati con i grafici piuttosto che con i numeri grezzi. La creazione di grafici in fase di esecuzione, sulla base dei dati in un foglio di calcolo, è una delle funzionalità utili di Aspose.Cells. Aspose.Cells supporta la creazione di grafici sia standard che personalizzati. Di seguito, mostreremo alcuni esempi con file di esempio su come creare alcuni tipi comuni di grafici MS-Excel utilizzando Aspose.Cells API.

##  **Grafico piramidale**

 Quando viene eseguito il codice di esempio, al foglio di lavoro viene aggiunto un grafico a piramide. Si prega di consultare il[file Excel di output](66519068.xlsx) del seguente codice di esempio.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_PyramidChart-new.cpp" >}}

##  **Grafico a linee**

Nell'esempio sopra, semplicemente cambiando il file[**ChartType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/)A**"TipoGrafico::Linea".**crea un grafico a linee. La fonte completa è fornita di seguito. quando il codice viene eseguito, al foglio di lavoro viene aggiunto un grafico a linee. Si prega di consultare il[file Excel di output](66519069.xlsx) del seguente codice di esempio.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_LineChart-new.cpp" >}}

##  **Grafico a bolle**

Per creare un grafico a bolle, il[**ChartType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/) deve essere impostato su**"ChartType_Bubble".** e alcune proprietà extra come[**Imposta dimensioni bolla**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setbubblesizes/) & [**ImpostaXValori**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setxvalues/) devono essere impostati di conseguenza. Dopo aver eseguito il codice seguente, al foglio di lavoro viene aggiunto un grafico a bolle. Si prega di consultare il[file Excel di output](66519070.xlsx) del seguente codice di esempio.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_BubbleChart-new.cpp" >}}

##  **Creazione di grafici personalizzati**

Finora, quando abbiamo parlato dei grafici, abbiamo esaminato i grafici standard che hanno le proprie impostazioni di formattazione standard. Definiamo solo l'origine dati, impostiamo alcune proprietà e il grafico viene creato con le sue impostazioni di formato predefinite. Ma le API Aspose.Cells supportano anche la creazione di grafici personalizzati che consentono agli sviluppatori di creare grafici con le proprie impostazioni di formato. Gli sviluppatori possono creare grafici personalizzati in fase di esecuzione utilizzando Aspose.Cells.

Un grafico è composto da una serie di dati. Quando creano un grafico personalizzato, gli sviluppatori hanno la libertà di utilizzare diversi tipi di grafici per diverse serie di dati.

 Il codice di esempio seguente mostra come creare grafici personalizzati. In questo esempio utilizzeremo un grafico a colonne per la prima serie di dati e un grafico a linee per la seconda serie. Il risultato è che aggiungiamo un grafico a colonne, combinato con un grafico a linee, al foglio di lavoro. Si prega di consultare il[file Excel di output](66519071.xlsx) del seguente codice di esempio.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_CustomChart-new.cpp" >}}
