---
title: Apertura del file Excel senza la finestra di dialogo Apri Salva Annulla
type: docs
weight: 150
url: /it/net/opening-excel-file-without-open-save-cancel-dialog-box/
---
{{% alert color="primary" %}} 

Questo documento spiega come aprire un file Microsoft Excel in un browser senza visualizzare la finestra di dialogo Apri-Salva-Annulla.

 Va notato qui che la restrizione di sicurezza che non consente il download diretto di un file viene applicata da Microsoft (o altri fornitori di browser), non da Aspose. Viene imposta per bloccare e limitare il download di file potenzialmente dannosi su macchine locali .

È rischioso per il sistema locale del client consentire il download senza visualizzare la finestra di dialogo Apri-Salva-Annulla per richiedere il download. Non ci sono opzioni o soluzioni alternative disponibili da Aspose in quanto sarà un grosso rischio per la sicurezza.

{{% /alert %}} 
## **Perché un rischio per la sicurezza?**
L'immagine seguente mostra la finestra di dialogo Apri-Salva-Annulla mostrata da Internet Explorer durante il tentativo di scaricare un file.

|**La finestra di dialogo Apri-Salva-Annulla**|
|:- |
|![cose da fare:immagine_alt_testo](opening-excel-file-without-open-save-cancel-dialog-box_1.png)|
Come spiegato sopra, consentire l'apertura o l'esecuzione di un file sul proprio sistema senza la conferma che lo si desidera veramente è un rischio per la sicurezza. Alcuni file contengono virus e alcuni siti cercheranno di scaricare file dannosi sul tuo computer senza chiedere conferma. Pertanto, non è consigliabile consentire il download di file senza la richiesta di download in modo che gli utenti debbano verificare il file e la sua origine prima di scaricarlo o eseguirlo. La disattivazione della finestra di dialogo di download rende il sistema vulnerabile a virus, trojan e hacker che potrebbero intaccare silenziosamente il sistema.
## **Apertura di un file senza la finestra di dialogo Apri-Salva-Annulla**
 Sebbene sia un grosso problema di sicurezza, Microsoft fornisce ancora impostazioni di Internet Explorer che consentono agli utenti di disabilitare la richiesta Apri-Salva-Annulla per il download di file.

In Esplora risorse:

1.  Sul**Strumenti** menù, selezionare**Opzioni cartella**.
1. Fare clic sulla scheda Tipi di file nella finestra di dialogo Opzioni cartella.
1. Seleziona il tipo di file con estensione XLS.
1.  Clic**Avanzate**. 
Viene visualizzata una finestra di dialogo. Ha tre opzioni in basso.
1.  Deseleziona**Conferma l'apertura dopo il download**.
1.  Seleziona la terza opzione -**Sfoglia nella stessa finestra** - per visualizzare il file Excel in Internet Explorer senza avviare Microsoft Excel standalone.

|**Modifica delle opzioni del tipo di file**|
|:- |
|![cose da fare:immagine_alt_testo](opening-excel-file-without-open-save-cancel-dialog-box_2.png)|
Questa impostazione consente ai file di essere eseguiti direttamente nel browser Web, senza che venga visualizzata la finestra di dialogo Apri-Salva-Annulla durante il download o l'apertura del file.
