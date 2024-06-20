---
title: Utilizzo di Sparklines e Impostazioni Formato 3D
type: docs
weight: 40
url: /it/java/using-sparklines-and-settings-3d-format/
---

## **Utilizzo delle Sparklines**
Microsoft Excel 2010 può analizzare le informazioni in modi più variati che mai. Consente agli utenti di monitorare ed evidenziare importanti tendenze dei dati con nuovi strumenti di analisi e visualizzazione dei dati. Le Sparklines sono mini-grafici che è possibile inserire all'interno delle celle, in modo da poter visualizzare dati e grafici sulla stessa tabella. Quando le sparklines vengono utilizzate correttamente, l'analisi dei dati è più rapida e diretta. Forniscono inoltre una visione semplice delle informazioni, evitando fogli di lavoro affollati con molti grafici elaborati.

Aspose.Cells fornisce un'API per manipolare le sparklines nei fogli di calcolo.
### **Le Sparklines in Microsoft Excel**
Per inserire sparklines in Microsoft Excel 2010:

1. Selezionare le celle in cui si desidera che compaiano le sparklines. Per renderle facili da visualizzare, selezionare le celle a lato dei dati.
1. Fare clic su **Inserisci** nella barra multifunzione e quindi scegliere **colonna** nel gruppo **Sparklines**.
1. Selezionare o inserire il intervallo di celle nel foglio di lavoro che contengono i dati di origine. I grafici compariranno.

Le Sparklines ti aiutano a visualizzare le tendenze, ad esempio, il record di vittorie o sconfitte per una lega di softball. Le Sparklines possono persino sommare l'intera stagione di ogni squadra nella lega.
### **Sparklines utilizzando Aspose.Cells**
I programmatori possono creare, eliminare o leggere Sparklines (nel file modello) utilizzando l'API fornita da Aspose.Cells. Le classi che gestiscono le Sparklines sono contenute nel namespace [Aspose.Cells.Charts](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) quindi è necessario importare questo namespace prima di utilizzare queste funzionalità.

Aggiungendo grafici personalizzati per un determinato intervallo di dati, i programmatori hanno la libertà di aggiungere diversi tipi di piccoli grafici alle aree di celle selezionate.

L'esempio di seguito mostra la funzione Sparklines. L'esempio mostra come:

1. Aprire un semplice file modello.
1. Leggere le informazioni delle sparklines per un foglio di lavoro.
1. Aggiungere nuove sparklines per un dato intervallo di dati in un'area di celle.
1. Salvare il file Excel su disco.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-UsingSparkLine.java" >}}
## **Impostazione del Formato 3D**
Potresti avere bisogno di stili di grafici 3D per ottenere solo i risultati per il tuo scenario. Aspose.Cells fornisce l'API pertinente per applicare la formattazione 3D di Microsoft Excel 2007.

Di seguito è riportato un esempio completo per dimostrare come creare un grafico e applicare la formattazione 3D di Microsoft Excel 2007. Dopo aver eseguito il codice di esempio, verrà aggiunto un grafico a colonne (con effetti 3D) al foglio di lavoro.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-Applying3DFormat.java" >}}
