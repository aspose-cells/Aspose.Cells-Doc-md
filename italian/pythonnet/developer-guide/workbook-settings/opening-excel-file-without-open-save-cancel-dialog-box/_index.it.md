---
title: Apertura file Excel senza finestra di dialogo Apri Salva Annulla
type: docs
weight: 150
url: /it/python-net/opening-excel-file-without-open-save-cancel-dialog-box/
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
Come spiegato in precedenza, consentire a un file di aprirsi o eseguirsi sul sistema senza conferma che si desideri davvero è un rischio di sicurezza. Alcuni file contengono virus e alcuni siti cercheranno di scaricare file dannosi sulla tua macchina senza avvisarti. Pertanto, non è consigliabile consentire il download di file senza il prompt di download in modo che gli utenti debbano verificare che il file e la sua origine possano essere verificati prima di scaricarlo o eseguirlo. Disabilitare la finestra di dialogo di download rende il sistema vulnerabile a virus, trojan e hacker che potrebbero influenzare silenziosamente il sistema. 
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

