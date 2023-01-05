---
title: Formattazione di un intervallo di Cells
type: docs
weight: 60
url: /it/net/formatting-a-range-of-cells/
---
{{% alert color="primary" %}} 

Questo argomento appartiene anche alla serie di argomenti relativi all'applicazione delle impostazioni dei caratteri e di altri stili di formattazione sulle celle. I nostri ultimi argomenti hanno trattato bene la gestione di tali funzionalità. Ad esempio, puoi fare riferimento a[Modifica del carattere e del colore di un Cell](/cells/it/net/changing-the-font-and-color-of-a-cell/) e[Applicazione di stili su Cells](/cells/it/net/applying-styles-on-cells/) argomenti per conoscere le stesse caratteristiche. Allora cosa c'è di nuovo in questo argomento se abbiamo già trattato questi concetti. Bene, l'unica differenza di questo argomento rispetto ai precedenti è che applicheremo le impostazioni di formattazione (relative a caratteri e altri stili) su un intervallo di celle invece che su una singola cella. Speriamo che troverai ancora questo argomento utile per te.

{{% /alert %}} 
## **Impostazione di carattere e stile di un intervallo di Cells**
 Prima di parlare delle impostazioni di formattazione (di cui abbiamo già parlato molto nei nostri argomenti precedenti), dovremmo sapere come creare un intervallo di celle. Bene, possiamo creare un intervallo di celle usando**CellRange** classe il cui costruttore accetta alcuni parametri per specificare l'intervallo di celle. Possiamo specificare l'intervallo di celle utilizzando il**Nomi** o**Indici di riga e colonna** delle celle di inizio e di fine.

 Una volta creato un file**CellRange** oggetto quindi possiamo usare le versioni sovraccaricate di**Imposta stile**, **ImpostaFont** & **ImpostaColoreFont** metodi di Foglio di lavoro che possono richiedere a**CellRange** oggetto per applicare le impostazioni di formattazione all'intervallo di celle specificato.

Diamo un'occhiata a un esempio per comprendere questo concetto di base.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FormattingCellRange-1.cs" >}}
