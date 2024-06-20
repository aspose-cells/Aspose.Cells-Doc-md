---
title: Il file di licenza non funziona più
type: docs
weight: 60
url: /it/net/license-file-not-working-anymore/
---

## **Sintomo**

A volte gli utenti si sentono frustrati perché i loro file di licenza non funzionano più quando spostano / pubblicano i loro progetti web su un nuovo server. Si sentono sconvolti perché i loro file di licenza funzionavano correttamente sul loro server precedente (vecchio), ma ora ottengono un **Evaluation Copyright Warning** aggiuntivo nel foglio di lavoro (ogni volta che generano report usando il componente) nell'ambiente del nuovo server.

### **Uno Scenario**

"Abbiamo usato Aspose.Cells nel nostro progetto web ASP.NET per generare/manipolare report di Excel, abbiamo ottenuto una licenza valida che stiamo utilizzando. Alcuni giorni fa, abbiamo spostato il sito web su un nuovo server; non ci sono state aggiornamenti o modifiche in alcun modo, ci siamo assicurati e abbiamo semplicemente spostato ogni singolo file sul nuovo server, inclusi i file Aspose.Cells.dll e lic correlati. Ora quando cerchiamo di generare report di Excel nell'ambiente del nuovo server, otteniamo un foglio con un watermark di **Avviso di Copyright di Valutazione** sui nostri report. Abbiamo provato a scaricare e installare un nuovo file di licenza dalla sezione I miei ordini del sito, ma non ha risolto il problema affatto. A proposito, abbiamo implementato la licenza inserendo il file Aspose.Cells.lic nella cartella bin del sito insieme al file del componente Aspose.Cells.dll, che, come ho menzionato, ha funzionato senza problemi sul vecchio server."

### **Soluzione**

Aspose ha un meccanismo di licenza pulito e affidabile. Generalmente, il problema dovrebbe essere correlato a un problema di distribuzione. Se un file di licenza funziona correttamente (su un server), dovrebbe funzionare altrettanto bene su altri server / ambienti. Normalmente gli utenti utilizzano eventi Application_Start o Session_Start ecc. nel file global.asax per inserire il codice di licenza lì. Quindi, è molto possibile che l'evento Application_Start / Session_Start non venga attivato per elaborare il codice di licenza nelle loro nuove posizioni. È da notare qui, Aspose.Cells genererà sempre un'eccezione se il componente non trova il file di licenza in un percorso. Gli utenti dovrebbero assicurarsi che il codice di licenza (ovunque lo collocano) venga elaborato e che gli eventi dovrebbero essere innescati in cui inseriscono il codice di licenza. L'utente può riavviare il servizio correlato cioè, "Pubblicazione nel Web" e provare a tracciare se gli eventi Application_Start / Session_Start vengono attivati quando visitano i loro progetti nell'ambiente del nuovo server.

### **Conferma**

Si prega inoltre di assicurarsi che…

- Stai utilizzando un file di licenza valido nel tuo progetto.
- Tu o qualcun altro non dovrebbe modificare il file di licenza altrimenti il file di licenza non funzionerà.
- Dovresti essere consapevole della scadenza della tua sottoscrizione alla licenza (puoi semplicemente aprire il file lic con il blocco note e controllare la data di scadenza).
- Non stai utilizzando una versione (Aspose.Cells.dll) rilasciata dopo la scadenza della tua sottoscrizione alla licenza. È da notare qui, un file di licenza non scade mai, ma se stai utilizzando la versione del componente rilasciata dopo la scadenza della tua sottoscrizione, otterrai un foglio con watermark di **Avviso di Copyright di Valutazione** aggiuntivo ogni volta che crei un file Excel.

### **Riferimenti**

<https://forum.aspose.com/t/license-file-not-working-on-new-server/83110>

<https://forum.aspose.com/t/license-not-being-detected/83516/4>
