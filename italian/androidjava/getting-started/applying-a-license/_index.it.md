---
title: Applicazione di una licenza
type: docs
weight: 40
url: /it/java/applying-a-license/
---
{{% alert color="primary" %}}

 Una volta che sei soddisfatto della tua valutazione di Aspose.Cells,[acquistare una licenza](https://purchase.aspose.com/buy) sul sito Aspose. Acquisisci familiarità con il diverso[tipi di licenza](https://purchase.aspose.com/policies/license-types/) offerto. In caso di domande, non esitare a farlo[contattare il team commerciale Aspose](https://about.aspose.com/contact).

Ogni licenza Aspose comporta un abbonamento di un anno per aggiornamenti gratuiti a eventuali nuove versioni o correzioni che escono durante questo periodo. Il supporto tecnico è gratuito e illimitato e viene fornito sia agli utenti con licenza che a quelli di valutazione.

La licenza è un file XML di testo semplice che contiene dettagli come il nome del prodotto, il numero di sviluppatori con licenza, la data di scadenza dell'abbonamento e così via. Il file è firmato digitalmente, quindi non modificarlo: anche l'aggiunta di un'ulteriore interruzione di riga nel file lo invaliderà.

È necessario impostare una licenza prima di eseguire qualsiasi operazione con i documenti. Assicurati di farlo prima di creare un oggetto Document. È necessario impostare una licenza solo una volta per applicazione o processo.

{{% /alert %}}

## **Caricamento del file di licenza**

 In Aspose.Cells for Android via Java, la licenza può essere[incorporata come risorsa](/cells/it/java/applying-a-license/#applying-a-license-from-an-embedded-resource)o caricato da un flusso:

1.  Metti il file di licenza in qualsiasi posizione su**/mnt/sdcard/**.
1. Crea un flusso che faccia riferimento a file.
1. Passa il flusso (contenente il file di licenza) nel metodo SetLicense.

**Java**

{{< highlight "java" >}}

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

1.  Aggiungi il file di licenza come risorsa a quello della tua applicazione**res/grezzo** cartella.
 Il file di licenza dovrebbe essere visibile nel file**res/grezzo** cartella.
1. Accedi/carica la licenza dalla risorsa con il seguente esempio di codice.

**Java**

{{< highlight "java" >}}

 License license = new License();

InputStream inputStream = getResources().openRawResource(R.raw.license);

license.setLicense(inputStream);

{{< /highlight >}}
