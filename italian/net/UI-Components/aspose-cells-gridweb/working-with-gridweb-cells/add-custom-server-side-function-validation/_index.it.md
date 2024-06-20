---
title: Aggiungi convalida della funzione lato server personalizzata
type: docs
weight: 110
url: /it/net/aspose-cells-gridweb/add-custom-server-side-function-validation/
keywords: GridWeb, convalida lato server
description: Questo articolo presenta come lavorare con la convalida lato server in GridWeb.
---

## **Possibili Scenari di Utilizzo**
A volte potresti dover implementare la convalida dei dati lato server. Aspose.Cells.GridWeb ti consente di aggiungere una convalida personalizzata lato server. Devi specificare l'intervallo o l'area della cella. Puoi anche impostare funzioni di convalida lato client per callback con la convalida personalizzata lato server.
## **Aggiungi convalida della funzione personalizzata lato server**
È necessario impostare la classe di convalida server che implementa l'interfaccia **GridCustomServerValidation** tramite l'attributo **GridValidation.ServerValidation**. È anche necessario impostare la funzione di convalida lato client (deve essere scritta in JavaScript lato client), questa funzione è obbligatoria per convalidare i dati lato client in callback. Puoi impostare la stringa del messaggio di errore tramite le proprietà **GridValidation.ErrorMessage** e il titolo tramite le proprietà **GridValidation.ErrorTitle** per le tue esigenze. Si prega di consultare una serie di screenshot che mostrano come funziona (passo dopo passo) in uno scenario specifico dopo aver eseguito il codice di esempio di seguito. Nell'esempio, non è possibile aggiornare i dati nelle celle B2:C3. Quando si cerca di modificare tali celle nel foglio, verranno visualizzati alcuni messaggi di errore e il valore precedente verrà ripristinato. È possibile aprire la finestra Console (nel tuo browser) per stampare le informazioni/dettagli della cella per determinati eventi. 

![todo:image_alt_text](add-custom-server-side-function-validation_1.png)

![todo:image_alt_text](add-custom-server-side-function-validation_2.png)

![todo:image_alt_text](add-custom-server-side-function-validation_3.png)

![todo:image_alt_text](add-custom-server-side-function-validation_4.png)

![todo:image_alt_text](add-custom-server-side-function-validation_5.png)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Cells-AddCustomServerSideFunctionValidation.aspx.cs" >}}
