---
title: Limitazioni della versione di valutazione
type: docs
weight: 110
url: /it/net/evaluation-version-limitations/
description: Aspose.Cells for .NET fornisce diversi piani di acquisto o offre una prova gratuita e una licenza temporanea di 30 giorni per la valutazione utilizzando le politiche di licenza e abbonamento in C#.
keywords: Evaluation Version Limitations, Number of Opened Files in Evaluation Version, Evaluation Watermark using Evaluation Version.
---
##  **Come ottenere la versione di valutazione di Aspose.Cells**

 È possibile scaricare una versione di valutazione di**Aspose.Cells** per NET da[la sua pagina di download](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) @ Maven repo. La versione di valutazione fornisce assolutamente le stesse funzionalità della versione con licenza del prodotto. Inoltre, la versione di valutazione diventa semplicemente concessa in licenza quando acquisti una licenza e aggiungi un paio di righe di codice per applicare la licenza.

 Una volta che sarai soddisfatto della tua valutazione di *Aspose.Cells**, potrai farlo[acquistare una licenza](https://purchase.aspose.com) al sito Aspose. Acquisisci familiarità con i diversi tipi di abbonamento offerti. In caso di domande, non esitate a contattare il team di vendita Aspose.

Ogni licenza Aspose prevede un abbonamento di un anno per aggiornamenti gratuiti a qualsiasi nuova versione o correzione rilasciata durante questo periodo. Il supporto tecnico è gratuito e illimitato e viene fornito sia agli utenti con licenza che a quelli in valutazione.

##  **Come testare Aspose.Cells senza limitazioni della versione di valutazione**

 Se vuoi fare una prova**Aspose.Cells** senza limitazioni della versione di valutazione, richiedi una licenza temporanea di 30 giorni. Per favore riferisci a[Come ottenere una licenza temporanea?](https://purchase.aspose.com/temporary-license) per maggiori informazioni.


##  **Limitazioni della versione di valutazione**

 Versione di valutazione di**Aspose.Cells** product (senza una licenza specificata) fornisce la funzionalità completa del prodotto, ma è limitato all'apertura di 100 file in un programma e un foglio di lavoro aggiuntivo con filigrana di valutazione.

Le limitazioni sono riportate di seguito:

###  **1a limitazione: numero di file aperti**

Quando esegui il programma, puoi aprire solo 100 file Excel. Se la tua domanda supera questo numero, verrà generata un'eccezione.

###  **2a limitazione: foglio di lavoro con filigrana di valutazione**
Questo foglio di lavoro verrà sempre visualizzato come foglio di lavoro attivo. Solo nella versione con licenza è possibile impostare il foglio di lavoro attivo su altri fogli di lavoro.
<br>
<image src="1.png" width="70%" />
<br>

###  **3a limitazione: testo semplice con informazioni sulla valutazione**
Nel file di testo normale di output di Aspose.Cells, un'informazione di valutazione verrà aggiunta alla fine del documento.
<br>
<image src="2.png" width="70%" />
<br>

###  **4° Limitazione: PDF e Immagine con Filigrana di Valutazione**
Nell'output PDF o nel file immagine di Aspose.Cells, una filigrana di valutazione verrebbe incollata nella parte superiore del documento/immagine. Non è possibile nascondere l'avviso sul copyright di valutazione (il foglio di lavoro aggiuntivo) anche nel controllo GridWeb, verrà sempre aggiunto (alla fine nelle schede del foglio di lavoro) nel controllo.
<br>
<image src="3.png" width="70%" />
<br>

###  **5a limitazione: impostazioni del file di configurazione (Aspose.Cells.GridWeb)**
Non è possibile specificare nuovamente il percorso dello script aggiungendo le seguenti righe di codice nella sezione di configurazione (ad esempio nel file web.config). acw_client è una cartella che contiene file e Aspose.Cells.GridWeb utilizza questa cartella per gestire la sua configurazione interna, ha file di script, file di immagine e altri file per specificare il comportamento di GridWeb e impostare altre operazioni. Il file di configurazione viene utilizzato per impedire al controllo di utilizzare le risorse client integrate (immagini, script e così via), il che è utile in alcuni casi/scenari. Inoltre, queste impostazioni di configurazione nel file web.config avranno effetto solo con la versione CON LICENZA del controllo.

**XML**
{{< highlight "csharp" >}}
<appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

Queste impostazioni potrebbero essere obbligatorie in alcuni casi/scenari se si utilizza il controllo Aspose.Cells.GridWeb in siti Web di file system o estensioni MS Ajax ecc.

{{% /alert %}}