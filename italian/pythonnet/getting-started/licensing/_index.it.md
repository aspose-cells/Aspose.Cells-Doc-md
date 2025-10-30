---
title: Licenza
type: docs
weight: 21
url: /it/python-net/licensing/
---

{{% alert color="primary" %}}

È possibile scaricare facilmente una versione di valutazione di Aspose.Cells Python tramite .Net dalla sua [pagina di download](https://pypi.org/project/aspose-cells-python/) @ Repos di Pypi. La versione di valutazione fornisce assolutamente le stesse funzionalità della versione con licenza del componente. Inoltre, la versione di valutazione diventa semplicemente con licenza quando si acquista una licenza e si aggiungono un paio di righe di codice per applicare la licenza.

{{% /alert %}}

## **Limitazioni della Versione di Valutazione**

La versione di valutazione del prodotto Aspose.Cells Python tramite .Net (senza una licenza specificata) fornisce piena funzionalità del prodotto, ma è limitata nell'aprire 100 file in un solo programma e un foglio di lavoro extra con il watermark di valutazione.

Le limitazioni sono indicate di seguito:

- **Numero di File Aperti** (Aspose.Cells Python tramite .Net)
  Quando esegui il tuo programma, puoi aprire solo 100 file Excel utilizzando la libreria Aspose.Cells Python tramite .Net. Se la tua applicazione supera questo numero, verrà generata un'eccezione.


Inoltre, un foglio di lavoro con il watermark di valutazione comparirà sempre come foglio di lavoro attivo nel file Excel generato utilizzando la libreria Aspose.Cells Python. Solo nella versione con licenza, puoi impostare il foglio di lavoro attivo su altri fogli di lavoro. Nell'output del file PDF o immagine tramite Aspose.Cells Python, un watermark di valutazione verrà incollato nella parte superiore del documento/immagine.

{{% alert color="primary" %}}

Se desideri testare Aspose.Cells Python senza limitazioni della versione di valutazione, puoi anche richiedere una [Licenza Temporanea di 30 Giorni](https://purchase.aspose.com/temporary-license).

{{% /alert %}}

## **Applicare una Licenza in Aspose.Cells Python tramite Componente**

La licenza è un file XML di testo semplice che contiene dettagli come il nome del prodotto, il numero di sviluppatori a cui è concessa la licenza, la data di scadenza della sottoscrizione e così via. Il file è firmato digitalmente, quindi non modificarlo. Anche l'aggiunta involontaria di un'interruzione di riga extra nel file lo renderà non valido. È necessario impostare una licenza prima di utilizzare Aspose.Cells Python se si desidera evitare le limitazioni della valutazione. È necessario impostare una licenza una sola volta per ogni applicazione (o processo). La licenza può essere caricata da un file.

Aspose.Cells Python cerca di trovare la licenza in posizioni di percorso esplicite.

Ci sono due metodi comuni per applicare una licenza da file.

### **Applicare una Licenza da Disco**

Il modo più semplice per impostare una licenza è mettere il file di licenza nel percorso esplicito.

{{< highlight csharp >}}

# Instantiate an instance of license and set the license file through its path

license = License();
# For Windows
license.set_license("D:\Aspose.Cells.lic");
# For Linux or MacOS
license.set_license("/home/yourusername/Aspose.Cells.lic"); 
{{< /highlight >}}

{{% alert color="primary" %}}

Quando chiami il metodo set_license, il nome della licenza deve essere lo stesso del nome del tuo file di licenza. Per esempio,è possibile cambiare il nome del file di licenza in **Aspose.Cells.lic.xml**. Quindi nel tuo codice, dovresti utilizzare il nome della licenza modificato (**Aspose.Cells.lic.xml**) per il metodo set_license.

{{% /alert %}}


{{< app/cells/assistant language="python-net" >}}
