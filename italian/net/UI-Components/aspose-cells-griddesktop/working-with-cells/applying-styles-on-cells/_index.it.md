---
title: Applicazione di stili su Cells
type: docs
weight: 50
url: /it/net/applying-styles-on-cells/
---
{{% alert color="primary" %}} 

Questo argomento riguarda l'applicazione degli stili alle celle, quindi cercheremo di coprire quasi tutto ciò che può essere utilizzato per applicare lo stile a una cella. Oltre ad alcune impostazioni di formattazione di base, discuteremo anche del disegno dei bordi e dell'impostazione del formato numerico delle celle in dettaglio.

{{% /alert %}} 
## **Applicazione di uno stile personalizzato su un Cell - Un esempio**
Per modificare il carattere e il colore di una cella utilizzando Aspose.Cells.GridDesktop, procedi nel seguente modo:

-  Accedi a qualsiasi desiderato**Foglio di lavoro**
-  Accedi a**Cell** su cui vogliamo applicare a**Stile**
-  Ottenere**Stile** del**Cell**
-  Impostare**Stile** proprietà in base alle vostre esigenze personalizzate
-  Finalmente, set**Stile** del**Cell** con quello aggiornato

 Ci sono molte proprietà e metodi utili offerti da**Stile** oggetto che può essere utilizzato dagli sviluppatori per personalizzare lo stile in base alle proprie esigenze. Nel codice seguente viene dimostrato come applicare lo stile personalizzato sulla cella.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-ApplyStyle.cs" >}}
## **Bordi di disegno di Cells**
 Usando**Stile**oggetto, possiamo disegnare i bordi di una cella molto facilmente. I bordi possono essere disegnati in qualsiasi colore. Inoltre, gli sviluppatori hanno anche la flessibilità di scegliere un tipo specifico di linea che verrà utilizzato per tracciare i bordi attorno alla cella. Gli sviluppatori possono utilizzare**SetBorderLine** e**ImpostaBorderColor** metodi di**Stile** oggetto per disegnare bordi di qualsiasi tipo e colore. Allo stesso modo, per ottenere informazioni sul confine di qualsiasi cella, gli sviluppatori possono anche utilizzare**GetBorderLine** e**OttieniBorderColor** metodi di**Stile** oggetto.
### **Tipi di confini**
Ci sono sei tipi di bordi supportati da Aspose.Cells.GridDesktop come segue:

- **Sono partiti** , rappresenta il bordo sinistro
- **Destra** , rappresenta il bordo destro
- **Superiore** , rappresenta il bordo superiore
- **Parte inferiore** , rappresenta il bordo inferiore
- **Diagonale giù** , rappresenta il bordo inferiore diagonale
- **DiagonalUp** , rappresenta il bordo superiore diagonale
### **Tipi di linee di confine**
Un bordo è composto da una linea. Modificando il tipo di linea, cambia l'aspetto di un bordo. Esistono molti tipi di linee di confine supportate da Aspose.Cells.GridDesktop, anch'esse elencate di seguito:

- **Nessuno** , non rappresenta alcun confine
- **Sottile** , rappresenta il bordo a linea continua
- **medio** , rappresenta il bordo della linea continua con larghezza della linea pari a 2f
- **Tratteggiato** , rappresenta il bordo della linea tratteggiata
- **Punteggiato** , rappresenta il bordo della linea tratteggiata
- **Spesso** , rappresenta il bordo della linea continua con larghezza della linea uguale a 3f
- **MedioTratteggiato** , rappresenta il bordo della linea tratteggiata con larghezza della linea pari a 2f
- **ThinDashDotted** , rappresenta il bordo della linea tratteggiata
- **MediumDashDotted** , rappresenta il bordo della linea tratteggiata tratteggiata con larghezza della linea pari a 2f
- **ThinDashDotDotted** , rappresenta il bordo della linea tratteggiata punto punto
- **MedioTrattinoPuntoPunteggiato** , rappresenta il bordo tratteggiato punto punto con larghezza della linea pari a 2f
## **Riassumendo tutti insieme - Esempio**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SummingUp.cs" >}}
## **Impostazione dei formati numerici**
Aspose.Cells.GridDesktop fornisce anche una forte funzionalità di impostazione dei formati numerici per i valori inseriti nelle celle. Ci sono 58 formati numerici incorporati offerti da Aspose.Cells.GridDesktop. Per visualizzare un elenco completo di tutti i formati numerici supportati, fare riferimento a[Formati numerici supportati.](/cells/it/net/list-of-supported-number-formats/)

 A tutti i formati numerici incorporati viene assegnato un**Indice** numero.**Per esempio** il**Indice** numero di**0.00E+00** il formato numerico è**11** . Per utilizzare un formato numerico predefinito in qualsiasi cella, gli sviluppatori possono impostare la proprietà NumberFormat di**Stile** opporsi al**Indice** numero di quel formato numerico specifico. Tuttavia, se gli sviluppatori devono avere il proprio formato numerico personalizzato, possono anche utilizzare la proprietà personalizzata di**Stile** oggetto.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SetNumberFormat.cs" >}}
