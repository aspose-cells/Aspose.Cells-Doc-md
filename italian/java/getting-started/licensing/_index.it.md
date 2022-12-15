---
title: Licenza
type: docs
weight: 50
url: /it/java/licensing/
---
{{% alert color="primary" %}} 

 È possibile scaricare una versione di valutazione di**Aspose.Cells** for Java da[la sua pagina di download](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) @ Repository Maven. La versione di valutazione offre assolutamente le stesse funzionalità della versione con licenza del prodotto. Inoltre, la versione di valutazione diventa semplicemente concessa in licenza quando acquisti una licenza e aggiungi un paio di righe di codice per applicare la licenza.

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

La licenza può essere caricata da un flusso o da un file nelle seguenti posizioni:

1. Percorso esplicito.
1. La cartella che contiene Aspose.Cells.jar.

 Utilizzare il[Licenza.setLicenza](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense(java.io.InputStream)) metodo per concedere in licenza il componente. Spesso il modo più semplice per impostare una licenza consiste nell'inserire il file di licenza nella stessa cartella di Aspose.Cells.jar e specificare solo il nome del file senza percorso, come mostrato nell'esempio seguente:

### **Esempio 1**

 In questo esempio**Aspose.Cells** tenterà di trovare il file di licenza nella cartella che contiene i JAR della tua applicazione.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

### **Esempio 2**

Inizializza una licenza da un flusso.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

### **Note sull'applicazione di una licenza in Aspose.Cells.GridWeb**

Si consiglia di inserire il codice di licenza in un punto dell'applicazione Web in cui deve essere elaborato per primo.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **Applicazione della licenza misurata**

Aspose.Cells consente agli sviluppatori di applicare la chiave misurata. È un nuovo meccanismo di licenza. Il nuovo meccanismo di licenza verrà utilizzato insieme al metodo di licenza esistente. I clienti che desiderano essere fatturati in base all'utilizzo delle funzionalità API possono utilizzare la licenza misurata. Per maggiori dettagli, fare riferimento a[Domande frequenti sulle licenze misurate](https://purchase.aspose.com/faqs/licensing/metered)sezione.

Una nuova classe[Misurato](https://reference.aspose.com/cells/java/com.aspose.cells/Metered)è stato introdotto per applicare la chiave misurata. Di seguito è riportato il codice di esempio che illustra come impostare la chiave pubblica e privata misurata.

{{< highlight "java" >}}

//Set metered public and private keys

Metered metered = new Metered();

//Access the setMeteredKey property and pass public and private keys as parameters

metered.setMeteredKey("************", "************");

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Check if the license is set

System.out.println(workbook.isLicensed());

//Get the Consumption quantity

double amountBefore = Metered.getConsumptionQuantity();

System.out.println(amountBefore);

Workbook workbook2 = new Workbook("Book1.xlsx");

workbook2.save("out1.xlsx");

//Get the Consumption quantity again which should be greater a bit

double amountAfter = Metered.getConsumptionQuantity();

System.out.println(amountAfter);

{{< /highlight >}}
