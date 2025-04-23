---
title: Come ridimensionare un foglio di lavoro
type: docs
weight: 130
url: /it/net/how-to-scale-a-worksheet/
description: Questo articolo mostra il codice che spiega come scalare un foglio di lavoro usando la libreria Aspose.Cells.
keywords: Scalare un foglio di lavoro in C#, Come scalare un foglio di lavoro usando C#, Scala un foglio di lavoro in C#.
---

## **Possibili Scenari di Utilizzo**
Ridimensionare un foglio di lavoro può essere utile per vari motivi, a seconda del contesto in cui si lavora. Ecco alcuni motivi comuni per ridimensionare un foglio di lavoro:
1. Adatta a pagina: assicurarsi che tutto il contenuto stia su una singola pagina o un numero specifico di pagine durante la stampa, rendendo più facile la lettura e la gestione senza dover sfogliare più pagine.

1. Presentazione: Per rendere il foglio di lavoro più organizzato e professionale, in particolare quando viene condiviso con altri in riunioni o report.

1. Leggibilità: Per regolare la dimensione del testo e degli altri elementi per una migliore leggibilità, soprattutto per le persone che potrebbero avere difficoltà a leggere caratteri più piccoli.

1. Gestione dello Spazio: Per ottimizzare l'uso dello spazio su un foglio di lavoro, assicurando che non ci siano spazi bianchi inutili e che tutte le informazioni importanti siano visibili senza scorrimenti eccessivi.

1. Visualizzazione dei Dati: Nel caso di grafici e diagrammi, la scala può aiutare a renderli più comprensibili regolando la dimensione per adattarsi correttamente allo spazio disponibile.

1. Coerenza: Per mantenere un aspetto uniforme in più fogli di lavoro o documenti, cosa particolarmente importante in ambienti professionali ed educativi.

## **Come scalare un foglio di lavoro in Excel**
La scalatura di un foglio di lavoro in Excel può aiutarti ad adattare i contenuti su una singola pagina o su un numero specificato di pagine durante la stampa. Ecco i passaggi per scalare un foglio di lavoro:

1. Apri il Tuo Foglio di Lavoro: Apri il foglio di lavoro Excel che desideri scalare.

1. Vai alla scheda Layout di Pagina: Clicca sulla scheda Layout di Pagina nella Barra multifunzione.

1. Gruppo Scala per Adatta: Nella scheda Layout di Pagina, trova il gruppo Scala per Adatta. Qui hai opzioni per regolare la scala. Larghezza: Questa opzione permette di specificare quante pagine di larghezza avrà il foglio stampato. Altezza: Questa opzione permette di specificare quante pagine di altezza avrà il foglio stampato. Scala: Puoi anche impostare una percentuale personalizzata di scalatura.
<br>
<img src="1.png" width=60% />

1. Regola Larghezza e Altezza: Imposta la Larghezza e l'Altezza al numero desiderato di pagine. Ad esempio, imposta entrambi a 1 pagina se vuoi che il foglio di lavoro si adatti su una pagina sola.

1. Regola la Percentuale di Scalatura (se necessario): Se preferisci impostare una percentuale di scalatura specifica, regola la casella Scala. Ad esempio, impostarla al 50% farà tutto la metà delle dimensioni originali.


## **Come scalare un foglio di lavoro usando C#**
Aspose.Cells è una libreria potente per lavorare con file Excel in modo programmatico. Per scalare un foglio di lavoro usando Aspose.Cells, devi seguire questi passaggi: carica [file di esempio](sample.xlsx) e regola le impostazioni di stampa affinché il contenuto si adatti al numero desiderato di pagine o a una percentuale specifica delle dimensioni originali.

### **Esempio: Adatta a una Pagina**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-scale-a-worksheet-fit-to-page.cs" >}}
<br>
<img src="3.png" width=60% />

### **Esempio: Scala alla Percentuale**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-scale-a-worksheet-scale-to-percentage.cs" >}}
<br>
<img src="2.png" width=60% />
{{< app/cells/assistant language="csharp" >}}
