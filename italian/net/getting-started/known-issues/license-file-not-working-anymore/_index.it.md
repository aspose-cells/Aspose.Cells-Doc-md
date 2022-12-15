---
title: Il file di licenza non funziona più
type: docs
weight: 60
url: /it/net/license-file-not-working-anymore/
---
## **Sintomo**

 A volte, gli utenti si sentono frustrati perché i loro file di licenza non funzionano più quando spostano/pubblicano i loro progetti web su un nuovo server. Si sentono sconvolti perché i loro file di licenza funzionavano correttamente sul loro (vecchio) server precedente, ma ora ottengono un extra**Valutazione Avviso sul copyright** filigrana Foglio di lavoro (ogni volta che generano report utilizzando il componente) nel nuovo ambiente server.

### **Uno Scenario**

"Stiamo utilizzando Aspose.Cells sul nostro progetto web ASP.NET per generare/manipolare report Excel, abbiamo ottenuto una licenza valida che stiamo utilizzando. Alcuni giorni fa, abbiamo spostato il sito Web su un nuovo server; non ci sono stati aggiornamenti o modifiche di sorta , ci siamo assicurati e abbiamo semplicemente spostato tutti i file sul nuovo server, inclusi Aspose.Cells.dll e i relativi file .lic. Ora, quando proviamo a generare report Excel nel nuovo ambiente server, otteniamo un**Valutazione Avviso sul copyright** foglio di filigrana sui nostri rapporti. Abbiamo provato a scaricare e installare un nuovo file di licenza dalla sezione I miei ordini del sito, ma non ha risolto affatto il problema. Cordiali saluti, implementiamo la licenza inserendo il file Aspose.Cells.lic nella cartella bin del sito insieme al file del componente Aspose.Cells.dll, che, come ho detto, funzionava senza problemi sul vecchio server."

### **Soluzione**

Aspose ha un meccanismo di licenza pulito e affidabile. In generale, il problema dovrebbe essere correlato al problema di distribuzione. Se un file di licenza funziona bene (su un server), dovrebbe funzionare altrettanto bene anche su altri server/ambienti. Normalmente gli utenti utilizzano Application_Inizio o sessione_Avvia eventi ecc. nel file global.asax per inserire lì il codice di licenza. Quindi, è del tutto possibile che Application_Inizio / Sessione_Gli eventi di avvio non vengono attivati per elaborare il codice di licenza nelle nuove posizioni. Va notato qui che Aspose.Cells genererà sempre un'eccezione se il componente non riesce a trovare il file di licenza in un percorso. Gli utenti devono assicurarsi che il codice di licenza (ovunque lo posizionino) venga elaborato e che vengano attivati eventi in cui inserire il codice di licenza. L'utente può riavviare il servizio correlato, ad esempio "Pubblicazione sul World Wide Web" e provare a tracciare se Application_Inizio / Sessione_Gli eventi di avvio vengono attivati quando visitano i loro progetti nel nuovo ambiente server.

### **Conferma**

Assicurati anche che...

- Stai utilizzando un file di licenza valido nel tuo progetto.
- Tu o qualcun altro non dovreste modificare / modificare il file di licenza almeno il file di licenza non funzionerà.
- Dovresti essere a conoscenza della scadenza dell'abbonamento alla tua licenza (puoi semplicemente aprire il file lic nel blocco note e controllare la data di scadenza).
-  Non stai utilizzando una versione (Aspose.Cells.dll) rilasciata dopo la scadenza dell'abbonamento della licenza. Va notato qui che un file di licenza non scade mai, ma se stai utilizzando la versione del componente che viene rilasciata dopo la scadenza dell'abbonamento, otterrai un extra**Valutazione Avviso sul copyright** foglio di filigrana ogni volta che crei un file excel.

### **Riferimenti**

<https://forum.aspose.com/t/license-file-not-working-on-new-server/83110>

<https://forum.aspose.com/t/license-not-being-detected/83516/4>
