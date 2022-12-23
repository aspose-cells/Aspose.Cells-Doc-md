---
title: Utilizzo di sparkline e impostazioni Formato 3D
type: docs
weight: 40
url: /it/java/using-sparklines-and-settings-3d-format/
---
## **Utilizzo di sparkline**
Microsoft Excel 2010 può analizzare le informazioni in più modi che mai. Consente agli utenti di tracciare ed evidenziare importanti tendenze dei dati con nuovi strumenti di analisi e visualizzazione dei dati. I grafici sparkline sono mini-grafici che puoi posizionare all'interno delle celle in modo da poter visualizzare i dati e il grafico sulla stessa tabella. Quando i grafici sparkline vengono utilizzati correttamente, l'analisi dei dati è più rapida e mirata. Forniscono anche una semplice visualizzazione delle informazioni, evitando fogli di lavoro sovraffollati con molti grafici occupati.

Aspose.Cells fornisce un API per la manipolazione dei grafici sparkline nei fogli di calcolo.
### **Sparkline in Microsoft Excel**
Per inserire sparkline in Microsoft Excel 2010:

1. Seleziona le celle in cui vuoi che appaiano i grafici sparkline. Per facilitarne la visualizzazione, seleziona le celle a lato dei dati.
1.  Clic**Inserire** sul nastro e poi scegli**colonna** nel**Sparkline** gruppo.
1. Seleziona o immetti l'intervallo di celle nel foglio di lavoro che contiene i dati di origine. Appariranno i grafici.

I grafici sparkline ti aiutano a vedere le tendenze, ad esempio il record di vittorie o sconfitte per un campionato di softball. Gli sparkline possono anche riassumere l'intera stagione di ogni squadra del campionato.
### **Sparkline utilizzando Aspose.Cells**
 Gli sviluppatori possono creare, eliminare o leggere gli sparkline (nel file modello) utilizzando lo API fornito da Aspose.Cells. Le classi che gestiscono gli sparkline sono contenute nel[Aspose.Cells.Charts](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)spazio dei nomi, quindi è necessario importare questo spazio dei nomi prima di utilizzare queste funzionalità.

Aggiungendo grafici personalizzati per un determinato intervallo di dati, gli sviluppatori hanno la libertà di aggiungere diversi tipi di piccoli grafici ad aree di celle selezionate.

L'esempio seguente mostra la funzionalità Sparkline. L'esempio mostra come:

1. Apri un semplice file modello.
1. Leggi le informazioni sugli sparkline per un foglio di lavoro.
1. Aggiungi nuovi grafici sparkline per un determinato intervallo di dati a un'area della cella.
1. Salva il file Excel su disco.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-UsingSparkLine.java" >}}
## **Impostazione del formato 3D**
Potresti aver bisogno di stili di grafici 3D in modo da poter ottenere solo i risultati per il tuo scenario. Aspose.Cells fornisce il relativo API per applicare la formattazione 3D di Excel 2007 Microsoft.

Di seguito viene fornito un esempio completo per dimostrare come creare un grafico e applicare la formattazione 3D di Excel 2007 Microsoft. Dopo aver eseguito il codice di esempio, al foglio di lavoro verrà aggiunto un istogramma (con effetti 3D).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-Applying3DFormat.java" >}}
