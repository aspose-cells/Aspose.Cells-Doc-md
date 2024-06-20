---
title: Applicazione di una licenza
type: docs
weight: 40
url: /it/java/applying-a-license/
---

{{% alert color="primary" %}}

Una volta soddisfatti della valutazione di Aspose.Cells, [acquistare una licenza](https://purchase.aspose.com/buy) sul sito web di Aspose. Prenditi confidenza con i diversi [tipi di licenze](https://purchase.aspose.com/policies/license-types/) offerti. Se hai domande, non esitare a [contattare il team di vendita di Aspose](https://about.aspose.com/contact).

Ogni licenza Aspose prevede un abbonamento annuale per aggiornamenti gratuiti a qualsiasi nuova versione o correzioni che verranno rilasciate durante questo periodo. Il supporto tecnico è gratuito e illimitato e fornito sia agli utenti con licenza che di valutazione.

La licenza è un file XML in testo semplice che contiene dettagli come il nome del prodotto, il numero di sviluppatori con licenza, la data di scadenza dell'abbonamento e così via. Il file è firmato digitalmente, quindi non modificarlo: anche aggiungere una riga extra nel file lo renderà non valido.

È necessario impostare una licenza prima di eseguire qualsiasi operazione con i documenti. Assicurati di farlo prima di creare un oggetto Document. È necessario impostare una licenza solo una volta per applicazione o processo.

{{% /alert %}}

## **Caricamento del file di licenza**

In Aspose.Cells per Android via Java, la licenza può essere [incorporata come risorsa](/cells/it/java/applying-a-license/#applying-a-license-from-an-embedded-resource) o caricata da uno stream:

1. Metti il file di licenza in qualsiasi posizione su **/mnt/sdcard/**.
1. Crea uno stream che fa riferimento al file.
1. Passa lo stream (contenente il file di licenza) al metodo SetLicense.

**Java**

{{< highlight java >}}

 String dataDir = Environment.getExternalStorageDirectory().getPath() + "/";

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream(dataDir + "Aspose.Cells.Android.lic");

// Instantiate the License class

License license = new License();

//Set the license through the stream object

license.setLicense(fstream);

{{< /highlight >}}

### **Applicazione di una licenza da una risorsa incorporata**

Per accedere alla licenza come risorsa per nome da un file di pacchetto Android:

1. Aggiungi il file di licenza come risorsa alla cartella **res/raw** della tua applicazione.
   Il file di licenza dovrebbe essere visibile nella cartella **res/raw**.
1. Accedi/carica la licenza dalla risorsa con il seguente esempio di codice.

**Java**

{{< highlight java >}}

 License license = new License();

InputStream inputStream = getResources().openRawResource(R.raw.license);

license.setLicense(inputStream);

{{< /highlight >}}
