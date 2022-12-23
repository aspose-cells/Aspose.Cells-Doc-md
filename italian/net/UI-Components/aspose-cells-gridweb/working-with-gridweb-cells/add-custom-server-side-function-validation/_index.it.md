---
title: Aggiungi la convalida della funzione lato server personalizzata
type: docs
weight: 110
url: /it/net/add-custom-server-side-function-validation/
---
## **Possibili scenari di utilizzo**
A volte, potrebbe essere necessario implementare la convalida dei dati sul lato server. Aspose.Cells.GridWeb consente di aggiungere la convalida dei dati lato server personalizzata. Devi specificare l'intervallo di celle o l'area. È inoltre possibile impostare funzioni di convalida lato client per i callback con convalida lato server personalizzata.
## **Aggiungi la convalida della funzione lato server personalizzata**
 È necessario impostare la classe di convalida del server che implementa il**GridCustomServerValidation** interfaccia tramite**GridValidation.ServerValidation** attributo. È inoltre necessario impostare la funzione di convalida lato client (dovrebbe essere scritta in JavaScript sul lato client), questa funzione è obbligatoria per convalidare i dati sul client alla richiamata. È possibile impostare la stringa del messaggio di errore tramite**GridValidation.ErrorMessage** e titolo via**GridValidation.ErrorTitle**proprietà per le vostre esigenze. Si prega di vedere una serie di schermate che mostrano come funziona (passo dopo passo) in un dato scenario dopo aver eseguito il codice di esempio qui sotto. Nell'esempio non è possibile aggiornare i dati nelle celle B2:C3. Quando si tenta di modificare quelle celle nel foglio, verranno visualizzati alcuni messaggi di errore e il valore precedente verrà ripristinato. Puoi aprire la finestra della console (nel tuo browser) per stampare le informazioni/i dettagli della cella per determinati eventi.

![cose da fare:immagine_alt_testo](add-custom-server-side-function-validation_1.png)

![cose da fare:immagine_alt_testo](add-custom-server-side-function-validation_2.png)

![cose da fare:immagine_alt_testo](add-custom-server-side-function-validation_3.png)

![cose da fare:immagine_alt_testo](add-custom-server-side-function-validation_4.png)

![cose da fare:immagine_alt_testo](add-custom-server-side-function-validation_5.png)
## **Codice d'esempio**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Cells-AddCustomServerSideFunctionValidation.aspx.cs" >}}
