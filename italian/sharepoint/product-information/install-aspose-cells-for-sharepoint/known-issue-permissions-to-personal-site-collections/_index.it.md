---
title: Problema noto  Autorizzazioni per le raccolte siti personali
type: docs
weight: 40
url: /it/sharepoint/known-issue-permissions-to-personal-site-collections/
---

{{% alert color="primary" %}} 

SharePoint di default non concede pieni permessi per gestire i siti personali agli amministratori del portale. Ecco perché l'attivazione e la disattivazione su una raccolta di siti personali potrebbero fallire quando vengono eseguite dagli amministratori del portale. Ciò include l'attivazione e la disattivazione durante l'installazione.

{{% /alert %}} 
### **Concessione di autorizzazioni ai siti personali**
Quando si verifica questo problema durante l'installazione, viene registrata una UnauthorizedAccessException in Microsoft.SharePoint.SPFeature.Activate() nel log di tracciamento di SharePoint. Quando la disattivazione fallisce come parte della disinstallazione, viene visualizzata una UnauthorizedAccessException sull'ultima schermata di installazione per le disattivazioni fallite.

Per evitare questo problema, concedere agli amministratori del portale il permesso di gestire l'applicazione Web del Mio Sito:

1. Vai a **Amministrazione centrale di SharePoint** e seleziona la scheda **Gestione Applicazioni**.
1. Scegli **Policy for Web Application** in **Gruppo di Sicurezza dell'Applicazione**.
1. Assicurati di selezionare l'Applicazione Web corretta per il tuo “Mio Sito” nella lista **Applicazioni Web** sulla destra.
1. Seleziona **Aggiungi Utenti** nell'angolo in alto a sinistra.
1. Scegli **Tutte le Zone** di default nella schermata **Aggiungi Utenti** e clicca su **Avanti**.
1. Aggiungi l'utente appropriato(i) o il gruppo di directory attivo che desideri controllare sulla tua Applicazione Web del “Mio Sito”.
1. Seleziona il livello di controllo. 

   **Aggiunta di utenti e impostazione del livello di controllo** 

![todo:image_alt_text](known-issue-permissions-to-personal-site-collections_1.png)




1. Fare clic su **Fine**.
