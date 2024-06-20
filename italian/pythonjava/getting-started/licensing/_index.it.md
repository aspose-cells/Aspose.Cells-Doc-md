---
title: Licenza
type: docs
weight: 50
url: /it/python-java/licensing/
---

{{% alert color="primary" %}} 

È possibile installare una versione di valutazione di **Aspose.Cells** per Python via Java con `pip install aspose-cells`. La versione di valutazione fornisce esattamente le stesse funzionalità della versione con licenza del prodotto. Inoltre, la versione di valutazione diventa semplicemente con licenza quando si acquista una licenza e si aggiunge un paio di righe di codice per applicare la licenza.

Una volta soddisfatti della valutazione di Aspose.Cells, è possibile [acquistare una licenza](https://purchase.aspose.com) sul sito web di Aspose. Familiarizzati con i diversi tipi di abbonamento offerti. Se hai delle domande, non esitare a contattare il team vendite di Aspose.

Ogni licenza Aspose prevede un abbonamento annuale per aggiornamenti gratuiti a qualsiasi nuova versione o correzioni che verranno rilasciate durante questo periodo. Il supporto tecnico è gratuito e illimitato e fornito sia agli utenti con licenza che di valutazione.

{{% /alert %}} {{% alert color="primary" %}} 

Se vuoi testare Aspose.Cells senza limitazioni della versione di valutazione, richiedi una licenza temporanea di 30 giorni. Si prega di fare riferimento a [Come ottenere una licenza temporanea?](https://purchase.aspose.com/temporary-license) per ulteriori informazioni.

{{% /alert %}}

## **Limitazioni della Versione di Valutazione**

La versione di valutazione del prodotto Aspose.Cells (senza licenza specificata) fornisce la piena funzionalità del prodotto, ma è limitata ad aprire 100 file in un solo programma e un foglio di lavoro aggiuntivo con la filigrana di valutazione.

Le limitazioni sono indicate di seguito:

### **1ª Limitazione: Numero di File Aperti**

Al momento dell'esecuzione del programma, è possibile aprire solo 100 file Excel. Se la tua applicazione supera questo numero, verrà generata un'eccezione.

### **2ª Limitazione: Foglio di Lavoro con Filigrana di Valutazione**

![todo:image_alt_text](licensing_1.png)

Questo foglio di lavoro verrà sempre mostrato come il foglio di lavoro attivo. Solo nella versione con licenza, è possibile impostare il foglio di lavoro attivo su altri fogli di lavoro.

## **Impostare una licenza**

La licenza è un file XML in formato normale che contiene dettagli come il nome del prodotto, il numero di sviluppatori a cui è concessa la licenza, la data di scadenza della sottoscrizione e così via. Il file è firmato digitalmente, quindi non modificarlo; anche l'aggiunta involontaria di una riga vuota nel file lo renderà non valido.

È necessario impostare una licenza prima di utilizzare Aspose.Cells per evitare le limitazioni di valutazione. È necessario impostare una licenza solo una volta per applicazione o processo.

La licenza può essere caricata da un file nei seguenti percorsi:

1. Percorso esplicito.
1. Cartella di lavoro.

Usa il metodo [License.setLicense](https://reference.aspose.com/cells/python-java/asposecells.api/License) per concedere in licenza il componente. Spesso il modo più semplice per impostare una licenza è mettere il file di licenza nella stessa cartella di Aspose.Cells.jar e specificare solo il nome del file senza percorso come mostrato nell'esempio seguente:

### **Esempio**

In questo esempio **Aspose.Cells** cercherà di trovare il file di licenza nella tua cartella di lavoro.

{{< highlight python >}}

from asposecells.api import License

lic = License()
lic.setLicense("Aspose.Cells.lic")

{{< /highlight >}}
