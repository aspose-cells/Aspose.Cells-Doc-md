---
title: Aprire un file Excel senza la finestra di dialogo di Salvataggio Annulla tramite Node.js con C++
linktitle: Apertura file Excel senza finestra di dialogo Apri Salva Annulla
type: docs
weight: 150
url: /it/nodejs-cpp/opening-excel-file-without-open-save-cancel-dialog-box/
--- 

{{% alert color="primary" %}} 

Questo documento spiega come aprire un file Microsoft Excel in un browser senza mostrare la finestra di dialogo Apri-Salva-Annulla. 

Si noti che la restrizione di sicurezza che non consente il download diretto di un file è imposta da Microsoft (o altri fornitori di browser), non da Aspose. È imposto per bloccare e limitare il download di file potenzialmente dannosi alle macchine locali. 

È rischioso per il sistema locale del cliente consentire il download senza mostrare la finestra di dialogo Apri-Salva-Annulla per avviare il download. Non c'è alcuna opzione o soluzione disponibile da Aspose in quanto rappresenterebbe un rischio di sicurezza molto elevato.

{{% /alert %}} 

## **Perché un rischio di sicurezza?**
L'immagine seguente mostra la finestra di dialogo Apri-Salva-Annulla visualizzata da Internet Explorer quando si cerca di scaricare un file.

|**La finestra di dialogo Apri-Salva-Annulla**| 
| :- | 
|![todo:image_alt_text](opening-excel-file-without-open-save-cancel-dialog-box_1.png)| 
Come spiegato sopra, permettere l'apertura o l'esecuzione di un file sul sistema senza conferma che lo si desideri davvero rappresenta un rischio per la sicurezza. Alcuni file contengono virus, e alcuni siti tentano di scaricare file dannosi sul tuo computer senza chiedere. Pertanto, non è consigliabile consentire il download di files senza la finestra di dialogo di download, in modo che gli utenti debbano verificare il file e la sua fonte prima di scaricarlo o eseguirlo. Disattivare la finestra di dialogo di download rende il sistema vulnerabile a virus, Trojan e hacker che possono influenzare silenziosamente il sistema. 

## **Apertura di un file senza la finestra di dialogo Apri-Salva-Annulla**
Anche se è una grande preoccupazione per la sicurezza, Microsoft fornisce comunque impostazioni di Internet Explorer che consentono agli utenti di disabilitare il prompt Apri-Salva-Annulla per il download di file. 

In Esplora risorse di Windows:

1. Nel menu **Strumenti**, seleziona **Opzioni cartella**.
1. Fai clic sulla scheda Tipi file nella finestra di dialogo Opzioni cartella.
1. Seleziona il tipo di file con estensione XLS.
1. Fare clic su **Avanzate**. 
   Viene visualizzata una finestra di dialogo. Ha tre opzioni in fondo.
1. Deseleziona **Conferma apertura dopo il download**.
1. Seleziona la terza opzione - **Sfoglia nella stessa finestra** - per visualizzare il file Excel in Internet Explorer senza avviare Microsoft Excel in modalità stand-alone. 

|**Modifica delle opzioni del tipo di file**| 
| :- | 
|![todo:image_alt_text](opening-excel-file-without-open-save-cancel-dialog-box_2.png)| 
Questa impostazione consente ai file di essere eseguiti direttamente nel browser web, senza che venga mostrata la finestra di dialogo Apri-Salva-Annulla durante il download o l'apertura del file. 
