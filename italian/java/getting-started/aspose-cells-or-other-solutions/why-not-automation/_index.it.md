---
title: Perché non Automazione
type: docs
weight: 20
url: /it/java/why-not-automation/
---

{{% alert color="primary" %}}

Perché i componenti Aspose sono una scelta molto migliore rispetto all'Automazione di Microsoft Office?*

Ci sono due domande che sentiamo più spesso qui in Aspose:

1. **I vostri prodotti richiedono l'installazione di Microsoft Office per funzionare?** 
   La risposta semplice è no. I componenti Aspose sono totalmente indipendenti e non sono affiliati, autorizzati, sponsorizzati o altrimenti approvati da Microsoft Corporation.
1. **Perché dovremmo utilizzare i prodotti Aspose invece di utilizzare l'automazione di Microsoft Office?**
   La risposta più breve che potremmo dare è che ci sono molte ragioni, la principale delle quali è che anche Microsoft sconsiglia fortemente l'automazione di Office dalle soluzioni software: [Considerazioni sull'automazione lato server di Office](https://support.microsoft.com/en-us/topic/considerations-for-server-side-automation-of-office-48bcfe93-8a89-47f1-0bce-017433ad79e2).

Ci sono diverse ragioni per cui i componenti Aspose sono un'alternativa migliore all'automazione. Alcune delle ragioni principali sono:

- [Sicurezza](/cells/it/java/why-not-automation/#security)
- [Stabilità](/cells/it/java/why-not-automation/#security)
- [Scalabilità/Velocità](/cells/it/java/why-not-automation/#security)
- [Prezzo](/cells/it/java/why-not-automation/#security)
- [Caratteristiche](/cells/it/java/why-not-automation/#security)

I punti chiave sono descritti di seguito. Assicurati inoltre di visitare i link alla fine di questa sezione.

{{% /alert %}}

## **Sicurezza**

La seguente è una citazione diretta dall'articolo di Microsoft sopra menzionato: *"Le Applicazioni di Office non sono mai state pensate per l'uso lato server e quindi non tengono conto dei problemi di sicurezza che devono affrontare i componenti distribuiti. Office non autentica le richieste in arrivo e non ti protegge dall'avviare involontariamente macro, o avviare un altro server che potrebbe eseguire macro, dal tuo codice lato server. Non aprire i file che vengono caricati sul server da un sito Web anonimo! In base alle impostazioni di sicurezza che sono state impostate per ultime, è possibile che il server possa eseguire macro con privilegi amministrativi o di sistema e compromettere la tua rete! Inoltre, Office utilizza molti componenti lato client (come Simple MAPI, WinInet e MSDAIPP) che possono memorizzare le informazioni di autenticazione del client per accelerare l'elaborazione. Se Office viene automatizzato lato server, un'istanza può servire più di un client e, poiché le informazioni di autenticazione sono state memorizzate per quella sessione, è possibile che un client possa utilizzare le credenziali memorizzate di un altro client e ottenere così permessi di accesso non concessi impersonando altri utenti."*

I prodotti Aspose sono molto sicuri. I componenti Aspose vengono eseguiti nello stesso contesto utente di tutte le applicazioni ASP.NET, sotto l'utente ASPNET. Di conseguenza, i componenti Aspose non costituiscono un potenziale rischio per le risorse di sistema vitali. Inoltre, quando un documento viene aperto da un componente Aspose, le macro non vengono eseguite automaticamente. I componenti Aspose sono stati progettati con l'obiettivo di consentire agli sviluppatori di creare, manipolare e salvare file Office. Nessuno dei rischi associati al pacchetto Microsoft Office è intrinseco ai componenti Aspose.

## **Stabilità**

La seguente è una citazione diretta dall'articolo di Microsoft sopra menzionato: *"Office 2000, Office XP e Office 2003 utilizzano la tecnologia di Microsoft Windows Installer (MSI) per semplificare l'installazione e l'autoriparazione per l'utente finale. MSI introduce il concetto di "installa al primo utilizzo", che consente di installare o configurare dinamicamente le funzionalità in fase di esecuzione (per il sistema, o più spesso per un utente particolare). In un ambiente server-side, questo rallenta le prestazioni e aumenta la probabilità che compaia una finestra di dialogo che chieda all'utente di approvare l'installazione o fornire un disco di installazione appropriato. Anche se è progettato per aumentare la resilienza di Office come prodotto per l'utente finale, l'implementazione di Office delle capacità di MSI è controproducente in un ambiente server-side. Inoltre, la stabilità di Office, in generale, non può essere garantita quando si esegue lato server perché non è stato progettato o testato per questo tipo di utilizzo. Utilizzare Office come componente di servizio su un server di rete può ridurre la stabilità di tale macchina e di conseguenza della tua rete nel suo complesso. Se prevedi di automatizzare Office lato server, cerca di isolare il programma su un computer dedicato che non può influire sulle funzioni critiche e che può essere riavviato secondo necessità."*

Poiché i componenti Aspose sono confezionati in un singolo DLL, non ci sarà mai bisogno di installare parti o componenti aggiuntivi per farli funzionare. I componenti Aspose sono utilizzati solo dalle applicazioni .NET e non c'è alcuna parte del codice del componente progettata per attendere una risposta umana. I componenti Aspose sono stati ampiamente testati. I componenti Aspose sono utilizzati da aziende come IBM, Hilton, Reader's Digest, Bank of America e molte altre.

## **Scalabilità/Velocità**

La seguente è una citazione diretta dall'articolo di Microsoft sopra menzionato: *"I componenti lato server devono essere componenti COM altamente rientranti, multi-threaded con un overhead minimo e un throughput elevato per client multipli. Le Applicazioni di Office sono in quasi tutti gli aspetti l'esatto opposto. Sono server di automazione basati su STA che sono progettati per fornire funzionalità diverse ma intensiva di risorse per un singolo client. Offrono una scalabilità limitata come soluzione lato server e hanno limiti fissi per elementi importanti, come la memoria, che non possono essere modificati tramite configurazione. Inoltre, utilizzano risorse globali (come file mappati in memoria, componenti aggiuntivi o modelli globali e server di automazione condivisi), che possono limitare il numero di istanze che possono essere eseguite contemporaneamente e portare a condizioni di gara se sono configurati in un ambiente multi-client. Gli sviluppatori che prevedono di eseguire più di un'istanza di qualsiasi Applicazione di Office contemporaneamente devono considerare il "pooling" o serializzare l'accesso all'Applicazione di Office per evitare potenziali deadlock o corruzione dei dati."*

I componenti Aspose sono altamente scalabili e estremamente veloci. Le applicazioni Office non sono state progettate per essere utilizzate contemporaneamente da centinaia e migliaia di utenti; tuttavia, i componenti Aspose sono stati progettati proprio per questo. I nostri componenti sono una vera soluzione .NET e funzionano alla perfezione sia su un singolo server che alimenta un'applicazione singola sia su un server web bilanciato che alimenta un'applicazione aziendale.

## **Prezzo**

Quando un'applicazione utilizza l'automazione Microsoft Office, è necessario acquistare una copia di Microsoft Office per ogni computer su cui viene eseguita l'applicazione. Molte volte un'applicazione potrebbe aver bisogno di creare o manipolare un file di Office senza richiedere all'utente di avere Office. Aspose offre una licenza di ridistribuzione molto [economica](https://purchase.aspose.com/buy), senza royalty, che consentirà la distribuzione a un numero illimitato di utenti senza preoccupazioni di licenza.

Nel creare applicazioni web, è importante sapere che i componenti di automazione di Microsoft Office non hanno un prezzo né una licenza per soluzioni lato server; quindi, non esiste una buona soluzione di licenza per distribuire applicazioni web che utilizzano i componenti di Microsoft Office. Aspose offre una soluzione molto conveniente per le applicazioni basate su server.

## **Caratteristiche**

I componenti di Aspose forniscono tutto ciò di cui hai bisogno per gestire i file di Office, e molto, molto altro. Sono progettati con la filosofia di consentire agli sviluppatori di ottenere i migliori risultati con il minor sforzo. A differenza dell'automazione di Office, i componenti di Aspose offrono molte funzioni potenti e risparmio di tempo. Ad esempio, [Aspose.Cells](https://products.aspose.com/cells/java/) offre agli sviluppatori la possibilità di esportare direttamente da un **DataTable** o da un **DataView** in un file Excel. [Ogni componente](https://products.aspose.com/total/) della famiglia Aspose offre il proprio set di funzionalità uniche e potenti.

Il miglior aspetto dell'acquisto di un componente Aspose o di un pacchetto di componenti è avere accesso ai nostri team di sviluppo. I nostri team di sviluppo comprendono che se c'è una funzionalità di cui la tua azienda ha bisogno, molto probabilmente anche altre aziende ne avranno bisogno. Anche se non tutte le richieste di funzionalità possono essere aggiunte, i nostri team cercano di essere molto aperti e flessibili nel fornire assistenza. Questo atteggiamento è ciò che ha aiutato i componenti Aspose a diventare così potenti come sono. Se ci sono funzionalità aggiuntive di cui hai bisogno dagli oggetti di automazione di Office, le probabilità che vengano aggiunte sono molto, molto basse.

## **Conclusioni**

{{% alert color="primary" %}}

Questo articolo ha trattato i punti chiave su perché i componenti di Aspose sono una scelta migliore rispetto all'automazione di Office. Tutti i diversi componenti Aspose offrono una versione di valutazione [senza rischi né obblighi](https://products.aspose.com/total/). Ti incoraggiamo a usufruire di tale valutazione per capire meglio cosa Aspose può fare per le tue applicazioni.

Per maggiori informazioni, consulta i seguenti articoli su Internet:

- [Considerazioni per l'Automazione Lato Server di Office](https://support.microsoft.com/en-us/topic/considerations-for-server-side-automation-of-office-48bcfe93-8a89-47f1-0bce-017433ad79e2)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
