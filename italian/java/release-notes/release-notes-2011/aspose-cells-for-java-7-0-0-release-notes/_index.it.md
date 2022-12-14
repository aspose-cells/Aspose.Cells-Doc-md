---
title: Aspose.Cells for Java 7.0.0 Note di rilascio
type: docs
weight: 40
url: /it/java/aspose-cells-for-java-7-0-0-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 7.0.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.0.0/)

{{% /alert %}} 

 introduzione

Siamo lieti di annunciare Aspose.Cells for Java v7.0.0 per gli utenti. Questa è la prima versione in cui abbiamo portato automaticamente dal nostro codice .NET e quindi potrebbe contenere molte funzionalità che mancavano nelle precedenti versioni Aspose.Cells for Java. Questa versione è una pietra miliare perché d'ora in poi possiamo lavorare in modo più efficiente e significa semplicemente un Aspose.Cells for Java molto migliore per te. La ragione di ciò è che ora possiamo mantenere due prodotti Aspose.Cells for Java e Aspose.Cells for .NET da un'unica base di codice sorgente. D'ora in poi i due prodotti includono quasi lo stesso set di funzionalità, correzioni e vengono rilasciati anche lo stesso giorno.

 Panoramica delle modifiche

 Non è pratica comune per noi apportare modifiche sostanziali allo API e cerchiamo sempre di evitarlo quando possibile, ma a volte è necessario. In questo caso le modifiche nella nuova versione si verificano perché:

- Un passaggio verso l'utilizzo del framework unificato Aspose che impone un API migliorato per il caricamento e il salvataggio. Ciò consente di utilizzare uno API più organizzato e coerente in tutti i prodotti Aspose.
- Il codice sorgente dalla piattaforma .NET verrà ora portato automaticamente sulla piattaforma Java. Ciò consentirà a Aspose.Cells for Java di corrispondere a Aspose.Cells for .NET funzione per funzione.

 Nuove funzionalità/miglioramenti



 Ci sono alcune funzionalità che sono ora incluse/migliorate.

-  Versioni compilate separate del prodotto per diversi JDK, ad esempio 1.4, 1.5, 1.6
 Imposta formule con riferimenti esterni
 Supporto ListObjects / Tabelle
 Supporta oggetti AutoShapes
 Sono stati apportati miglioramenti alla funzione Shape-to-Image
 Sono stati apportati miglioramenti alla funzione Chart-to-Image
 Sono stati apportati miglioramenti alla funzione Foglio-immagine
 Sono stati apportati miglioramenti per la funzionalità da Excel a PDF
 Sono stati apportati miglioramenti alla funzione Adatta righe/colonne

Problemi noti/limitazioni



 Ci sono una serie di limitazioni note in questa versione. Ci sono alcune funzionalità che potrebbero non essere supportate nella v7.0.0 che erano effettivamente supportate nelle versioni precedenti:

- Utilizzo delle API LightCells
 Lettura di file HTML
 Lettura/salvataggio di grafici/forme per file ODS
 Conservazione delle macro durante la lettura del file ODS e salvataggio delle macro nel file ODS



 Notevoli modifiche per gli utenti esistenti



In questa versione (Aspose.Cells for Java v7.0.0), abbiamo rinominato alcune API impostate per pulire la struttura API per abbinarla a Aspose.Cells for .NET. Abbiamo alcune classi di raccolta ma i loro nomi non le giustificano secondo gli standard .NET. Quindi, abbiamo deciso di cambiare di conseguenza i nomi di alcune classi e di altri membri. A causa di queste modifiche, potrebbe essere necessario correggere alcune parti dei segmenti di codice esistenti durante l'aggiornamento dalla versione precedente di Aspose.Cells for Java. Se non si utilizza nessuno dei membri elencati di seguito, molto probabilmente non sarà necessario apportare modifiche poiché il tuo codice verrà già compilato correttamente con la nuova versione. Tutte le stesse funzionalità rimangono intatte, solo l'accesso ad alcuni membri è stato spostato, rinominato o unito ad altri metodi.

Nota: abbiamo fatto del nostro meglio per non perdere alcuna funzionalità rispetto alle versioni/correzioni precedenti attraverso il refactoring di API, ma, temo, potresti riscontrare alcuni problemi e questa versione potrebbe non superare tutti i casi di test. Lavoriamo continuamente per migliorarlo per assicurarci che la nuova versione funzioni al 100% con tutti i problemi precedenti (risolti nelle versioni/correzioni precedenti del prodotto). Abbiamo bisogno di più tempo per valutarli tutti e rendere il prodotto più robusto. Incoraggiamo inoltre tutti voi a valutare i vostri precedenti problemi con questa nuova versione nei vostri diversi ambienti. Non esitate a segnalarci qualsiasi problema utilizzando il forum Aspose.Cells. La vostra collaborazione in questo senso è molto apprezzata.
