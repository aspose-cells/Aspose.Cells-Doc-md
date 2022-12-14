---
title: Licenza
type: docs
weight: 21
url: /it/python-net/licensing/
---
{{% alert color="primary" %}}

 Puoi facilmente scaricare una versione di valutazione di Aspose.Cells Python tramite .Net dal suo[pagina di download](https://pypi.org/project/aspose-cells-python/) @ Pypi repository. La versione di valutazione offre assolutamente le stesse funzionalità della versione con licenza del componente. Inoltre, la versione di valutazione diventa semplicemente concessa in licenza quando acquisti una licenza e aggiungi un paio di righe di codice per applicare la licenza.

{{% /alert %}}

## **Limiti della versione di valutazione**

La versione di valutazione di Aspose.Cells Python tramite il prodotto .Net (senza una licenza specificata) fornisce funzionalità complete del prodotto, ma è limitata all'apertura di 100 file in un programma e un foglio di lavoro aggiuntivo con filigrana di valutazione.

Le limitazioni sono mostrate di seguito:

- **Numero di file aperti** (Aspose.Cells Python tramite .Net)
Quando si esegue il programma, è possibile aprire solo 100 file Excel utilizzando Aspose.Cells Python tramite la libreria .Net. Se la tua applicazione supera questo numero, verrà generata un'eccezione.


Inoltre, un foglio di lavoro con filigrana di valutazione verrà sempre visualizzato come foglio di lavoro attivo nel file excel generato utilizzando Aspose.Cells Python tramite libreria. Solo nella versione con licenza, puoi impostare il foglio di lavoro attivo su altri fogli di lavoro. Nel file PDF o immagine di output di Aspose.Cells Python tramite, una filigrana di valutazione verrebbe incollata nella parte superiore del documento/immagine.

{{% alert color="primary" %}}

 Se vuoi testare Aspose.Cells Python tramite senza limitazioni della versione di valutazione, puoi anche richiedere un[Licenza temporanea di 30 giorni](https://purchase.aspose.com/temporary-license).

{{% /alert %}}

## **Applicazione di una licenza in Aspose.Cells Python tramite componente**

La licenza è un file XML di testo semplice che contiene dettagli come il nome del prodotto, il numero di sviluppatori a cui è concesso in licenza, la data di scadenza dell'abbonamento e così via. Il file è firmato digitalmente, quindi non modificarlo. Anche l'aggiunta involontaria di un'ulteriore interruzione di riga nel file lo invaliderà. È necessario impostare una licenza prima di utilizzare Aspose.Cells Python tramite se si desidera evitare la sua limitazione di valutazione. È necessario impostare una licenza solo una volta per applicazione (o processo). La licenza può essere caricata da un file.

Aspose.Cells Python tramite tenta di trovare la licenza in percorsi espliciti.

Esistono due metodi comuni per applicare una licenza da file.

### **Applicazione di una licenza da disco**

Il modo più semplice per impostare una licenza è inserire il file di licenza nel percorso esplicito.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license file through its path

license = License();
 //For Windows
license.set_license("D:\Aspose.Cells.lic");
 //For Linux or MacOS
license.set_license("/home/yourusername/Aspose.Cells.lic"); 
{{< /highlight >}}

{{% alert color="primary" %}}

Quando chiami il set_metodo di licenza, il nome della licenza deve essere uguale a quello del nome del file di licenza. Ad esempio, puoi modificare il nome del file di licenza in **Aspose.Cells.lic.xml**. Quindi, nel tuo codice, dovresti usare il nome della licenza modificata (**Aspose.Cells.lic.xml**) per il set_metodo di licenza.

{{% /alert %}}


