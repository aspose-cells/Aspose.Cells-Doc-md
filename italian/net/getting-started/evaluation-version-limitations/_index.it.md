---
title: Limitazioni della Versione di Valutazione
type: docs
weight: 110
url: /it/net/evaluation-version-limitations/
description: Aspose.Cells for .NET fornisce diversi piani di acquisto o offre una prova gratuita e una licenza temporanea di 30 giorni per la valutazione utilizzando le politiche di licenza e abbonamento in C#.
keywords: Limitazioni della Versione di Valutazione, Numero di File Aperti nella Versione di Valutazione, Filigrana di Valutazione utilizzando la Versione di Valutazione.
---

## **Come Ottenere la Versione di Valutazione di Aspose.Cells**

È possibile scaricare una versione di valutazione di **Aspose.Cells** per .NET dalla [pagina di download](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) @ Maven repos. La versione di valutazione fornisce assolutamente le stesse capacità della versione con licenza del prodotto. Inoltre, la versione di valutazione diventa semplicemente con licenza quando si acquista una licenza e si aggiungono un paio di righe di codice per applicare la licenza.

Una volta soddisfatti della valutazione di Aspose.Cells, è possibile [acquistare una licenza](https://purchase.aspose.com) sul sito web di Aspose. Familiarizzati con i diversi tipi di abbonamento offerti. Se hai delle domande, non esitare a contattare il team vendite di Aspose.

Ogni licenza Aspose prevede un abbonamento annuale per aggiornamenti gratuiti a qualsiasi nuova versione o correzioni che verranno rilasciate durante questo periodo. Il supporto tecnico è gratuito e illimitato e fornito sia agli utenti con licenza che di valutazione.

## **Come Testare Aspose.Cells Senza Limitazioni della Versione di Valutazione**

Se vuoi testare Aspose.Cells senza limitazioni della versione di valutazione, richiedi una licenza temporanea di 30 giorni. Si prega di fare riferimento a [Come ottenere una licenza temporanea?](https://purchase.aspose.com/temporary-license) per ulteriori informazioni.


## **Limitazioni della Versione di Valutazione**

La versione di valutazione del prodotto Aspose.Cells (senza licenza specificata) fornisce la piena funzionalità del prodotto, ma è limitata ad aprire 100 file in un solo programma e un foglio di lavoro aggiuntivo con la filigrana di valutazione.

Le limitazioni sono indicate di seguito:

### **1ª Limitazione: Numero di File Aperti**

Al momento dell'esecuzione del programma, è possibile aprire solo 100 file Excel. Se la tua applicazione supera questo numero, verrà generata un'eccezione.

### **2ª Limitazione: Foglio di Lavoro con Filigrana di Valutazione**
Questo foglio di lavoro verrà sempre mostrato come il foglio di lavoro attivo. Solo nella versione con licenza, è possibile impostare il foglio di lavoro attivo su altri fogli di lavoro.
<br>
<image src="1.png" width="70%" />
<br>

### **3a Limitazione: Testo semplice con informazioni di valutazione**
Nel file di testo semplice in uscita di Aspose.Cells, delle informazioni di valutazione verranno aggiunte alla fine del documento.
<br>
<image src="2.png" width="70%" />
<br>

### **4a Limitazione: PDF e Immagine con Filigrana di valutazione**
Nel file PDF o immagine di output di Aspose.Cells, verrebbe incollato un watermark di valutazione in cima al documento/immagine. Non è possibile nascondere l'avviso di Copyright di valutazione (il foglio di lavoro aggiuntivo) nel controllo GridWeb, verrà sempre aggiunto (alla fine nelle schede dei fogli di lavoro) nel controllo.
<br>
<image src="3.png" width="70%" />
<br>

### **5ª Limitazione: Impostazioni del file di configurazione (Aspose.Cells.GridWeb)**
Non è possibile specificare nuovamente il percorso dello script aggiungendo le seguenti righe di codice nella sezione di configurazione (ad es. nel file web.config). Il acw_client è una cartella che contiene file e Aspose.Cells.GridWeb utilizza questa cartella per gestire la sua configurazione interna, ha file di script, file di immagini ed altri file per specificare il comportamento di GridWeb e impostare altre operazioni. Il file di configurazione serve per impedire al controllo di utilizzare le risorse client incorporate (immagini, script, ecc.) che è utile in alcuni casi / scenari. Inoltre, queste impostazioni di configurazione nel file web.config avranno effetto solo con la VERSIONE CON LICENZA del controllo.

**XML**
{{< highlight csharp >}}
<appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

Queste impostazioni potrebbero essere obbligatorie in alcuni casi / scenari se si utilizza il controllo Aspose.Cells.GridWeb in siti Web del File System o estensioni MS Ajax ecc.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
