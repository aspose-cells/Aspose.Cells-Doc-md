---
title: Licenza
type: docs
weight: 50
url: /it/python-java/licensing/
---
{{% alert color="primary" %}} 

 È possibile installare una versione di valutazione di**Aspose.Cells** for Python via Java con `pip install aspose-cells`. La versione di valutazione offre assolutamente le stesse funzionalità della versione con licenza del prodotto. Inoltre, la versione di valutazione diventa semplicemente concessa in licenza quando acquisti una licenza e aggiungi un paio di righe di codice per applicare la licenza.

 Una volta che sei soddisfatto della tua valutazione di**Aspose.Cells** , puoi[acquistare una licenza](https://purchase.aspose.com)sul sito Aspose. Acquisisci familiarità con i diversi tipi di abbonamento offerti. In caso di domande, non esitare a contattare il team di vendita Aspose.

Ogni licenza Aspose comporta un abbonamento di un anno per aggiornamenti gratuiti a eventuali nuove versioni o correzioni che escono durante questo periodo. Il supporto tecnico è gratuito e illimitato e viene fornito sia agli utenti con licenza che a quelli di valutazione.

{{% /alert %}} {{% alert color="primary" %}} 

 Se vuoi fare una prova**Aspose.Cells** senza limitazioni della versione di valutazione, richiedi una licenza temporanea di 30 giorni. Per favore riferisci a[Come ottenere una licenza temporanea?](https://purchase.aspose.com/temporary-license) per maggiori informazioni.

{{% /alert %}}

## **Limiti della versione di valutazione**

 Versione di valutazione di**Aspose.Cells** Il prodotto (senza una licenza specificata) fornisce funzionalità complete del prodotto, ma è limitato all'apertura di 100 file in un programma e un foglio di lavoro aggiuntivo con filigrana di valutazione.

Le limitazioni sono mostrate di seguito:

### **1a limitazione: numero di file aperti**

Quando esegui il tuo programma, puoi aprire solo 100 file Excel. Se la tua applicazione supera questo numero, verrà generata un'eccezione.

### **2a limitazione: foglio di lavoro con filigrana di valutazione**

![cose da fare:immagine_alt_testo](licensing_1.png)

Questo foglio di lavoro verrà sempre visualizzato come foglio di lavoro attivo. Solo nella versione con licenza, puoi impostare il foglio di lavoro attivo su altri fogli di lavoro.

## **Impostazione di una licenza**

La licenza è un file XML di testo semplice che contiene dettagli come il nome del prodotto, il numero di sviluppatori a cui è concesso in licenza, la data di scadenza dell'abbonamento e così via. Il file è firmato digitalmente, quindi non modificare il file; anche l'aggiunta involontaria di un'ulteriore interruzione di riga nel file lo invaliderà.

È necessario impostare una licenza prima di utilizzare Aspose.Cells se si desidera evitare i suoi limiti di valutazione. È necessario impostare una licenza solo una volta per applicazione o processo.

La licenza può essere caricata da un file nelle seguenti posizioni:

1. Percorso esplicito.
1. Cartella di lavoro.

 Usa il[Licenza.setLicenza](https://reference.aspose.com/cells/python-java/asposecells.api/License) metodo per concedere in licenza il componente. Spesso il modo più semplice per impostare una licenza consiste nell'inserire il file di licenza nella stessa cartella di Aspose.Cells.jar e specificare solo il nome del file senza percorso, come mostrato nell'esempio seguente:

### **Esempio**

 In questo esempio**Aspose.Cells** tenterà di trovare il file di licenza nella cartella di lavoro.

{{< highlight "python" >}}

from asposecells.api import License

lic = License()
lic.setLicense("Aspose.Cells.lic")

{{< /highlight >}}
