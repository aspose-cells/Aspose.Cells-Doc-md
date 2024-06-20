---
title: Applica stile alla cella
type: docs
weight: 50
url: /it/net/aspose-cells-griddesktop/apply-style-on-cell/
keywords: GridDesktop,formato,stili,formati numerici,formato numerico,NumberFormat
description: Questo articolo presenta come ottenere o impostare il formato dello stile nella cella nel foglio di lavoro in GridDesktop.
---

{{% alert color="primary" %}} 

Questo argomento tratta dell'applicazione del formato dello stile su una cella, copriremo quasi tutte le proprietà correlate che possono essere utilizzate per applicare lo stile a una cella. Oltre a alcune impostazioni di formattazione di base, discuteremo anche del disegno dei bordi e dell'impostazione del formato numerico sulla cella in dettaglio.

{{% /alert %}} 
## **Applicare uno stile personalizzato a una cella - Un esempio**
Per cambiare il font e il colore di una cella utilizzando Aspose.Cells.GridDesktop, si prega di seguire i passaggi seguenti:

- Accedere a qualsiasi **Foglio di lavoro** desiderato
- Accedere a una **Cella** su cui vogliamo applicare uno **Stile**
- Ottenere **Stile** della **Cella**
- Impostare le proprietà dello **Stile** secondo le proprie esigenze personalizzate
- Infine, impostare lo **Stile** della **Cella** con quello aggiornato

Ci sono molte utili proprietà e metodi offerti dall'oggetto **Stile** che possono essere utilizzati dagli sviluppatori per personalizzare lo stile secondo le proprie esigenze. Nel codice seguente viene dimostrato come applicare uno stile personalizzato a una cella.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-ApplyStyle.cs" >}}
## **Disegnare i bordi delle celle**
Usando l'oggetto **Stile**, è possibile disegnare facilmente i bordi di una cella. I bordi possono essere disegnati in qualsiasi colore. Inoltre, gli sviluppatori hanno anche la flessibilità di scegliere un tipo specifico di linea che verrà utilizzata per disegnare i bordi intorno alla cella. Gli sviluppatori possono utilizzare i metodi **SetBorderLine** e **SetBorderColor** dell'oggetto **Stile** per disegnare bordi di qualsiasi tipo e colore. Allo stesso modo, per ottenere le informazioni sui bordi di qualsiasi cella, gli sviluppatori possono anche utilizzare i metodi **GetBorderLine** e **GetBorderColor** dell'oggetto **Stile**.
### **Tipi di bordi**
Ci sono sei tipi di bordi supportati da Aspose.Cells.GridDesktop come segue:

- **Sinistra** , rappresenta il bordo sinistro
- **Destra** , rappresenta il bordo destro
- **Superiore** , rappresenta il bordo superiore
- **Inferiore** , rappresenta il bordo inferiore
- **Diagonale in basso** , rappresenta il bordo diagonale in basso
- **Diagonale in alto** , rappresenta il bordo diagonale in alto
### **Tipi di linee di bordo**
Un bordo è composto da una linea. Cambiando il tipo di linea, cambia l'aspetto del bordo. Ci sono molti tipi di linee di bordo supportati da Aspose.Cells.GridDesktop, che sono anche elencati di seguito:

- **Nessuno** , rappresenta nessun bordo
- **Sottile** , rappresenta un bordo a linea continua
- **Medio** , rappresenta un bordo a linea continua con larghezza di linea uguale a 2f
- **Tratteggiato** , rappresenta un bordo a linea tratteggiata
- **Puntinato** , rappresenta un bordo a linea punteggiata
- **Spesso** , rappresenta un bordo a linea continua con larghezza di linea uguale a 3f
- **Medio trattato** , rappresenta un bordo a linea tratteggiata con larghezza di linea uguale a 2f
- **Sottile tratteggiato puntato** , rappresenta un bordo a linea a tratteggiata puntata
- **Medio trattato puntato** , rappresenta un bordo a linea a tratteggiata puntata con larghezza di linea uguale a 2f
- **Sottile trattato punto puntato** , rappresenta un bordo a linea a punto trattato puntato
- **MediumDashDotDotted**, rappresenta il bordo della linea tratteggiata di una linea con larghezza della linea uguale a 2f
## **Sommando Tutto Insieme - Esempio**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SummingUp.cs" >}}
## **Impostare i formati numerici**
Aspose.Cells.GridDesktop fornisce anche tipi di impostazioni di formati numerici. Ci sono 58 formati numerici integrati offerti da Aspose.Cells.GridDesktop. Per vedere l'elenco completo di tutti i formati numerici supportati, si prega di fare riferimento a [Elenco dei formati numerici supportati.](/cells/it/net/list-of-supported-number-formats/)

Tutti i formati numerici integrati hanno assegnato un numero di **Indice**. **Ad esempio**, il numero di **Indice** del formato numerico **0.00E+00** è **11**. Per utilizzare un formato numerico integrato in una qualsiasi cella, gli sviluppatori possono impostare la proprietà NumberFormat dell'oggetto **Style** al numero di **Indice** di quel formato numerico specifico. Tuttavia, se gli sviluppatori hanno bisogno di avere il proprio formato numerico personalizzato, allora possono anche utilizzare la proprietà Personalizzato dell'oggetto **Style**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SetNumberFormat.cs" >}}
