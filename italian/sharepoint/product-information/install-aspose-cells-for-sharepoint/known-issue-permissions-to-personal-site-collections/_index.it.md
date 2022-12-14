---
title: "Problema noto: autorizzazioni per raccolte siti personali"
type: docs
weight: 40
url: /it/sharepoint/known-issue-permissions-to-personal-site-collections/
---
{{% alert color="primary" %}} 

Per impostazione predefinita, SharePoint non concede autorizzazioni complete per la gestione dei siti personali agli amministratori del portale. Ecco perché l'attivazione e la disattivazione in una raccolta siti personale potrebbe non riuscire quando viene eseguita dagli amministratori del portale. Ciò include l'attivazione e la disattivazione durante l'installazione.

{{% /alert %}} 
### **Concessione dell'autorizzazione ai siti personali**
Quando questo problema si verifica durante l'installazione, nel log di traccia di SharePoint viene registrata un'eccezione UnauthorizedAccessException in Microsoft.SharePoint.SPFeature.Activate(). Quando la disattivazione non riesce come parte della disinstallazione, viene visualizzata un'eccezione UnauthorizedAccessException nell'ultima schermata di configurazione per le disattivazioni non riuscite.

Per evitare questo problema, concedere agli amministratori del portale l'autorizzazione a gestire l'applicazione Web MySite:

1.  Vai a**Amministrazione centrale SharePoint** e selezionare il**Gestione delle candidature** scheda.
1.  Scegliere**Politica per l'applicazione Web** sotto il**Sicurezza delle applicazioni** gruppo.
1.  Assicurati di selezionare l'applicazione Web corretta per "Il mio sito" nel file**Applicazione web** elenco a destra.
1.  Selezionare**Aggiungi utenti** in alto a sinistra.
1.  Scegliere**Tutte le zone** di default sul**Aggiungi utenti** schermo e fare clic**Prossimo**.
1. Aggiungi l'utente o gli utenti appropriati o il gruppo di Active Directory di cui desideri avere il controllo sull'applicazione Web "Il mio sito".
1.  Seleziona il livello di controllo.

   **Aggiunta di utenti e impostazione del livello di controllo** 

![cose da fare:immagine_alt_testo](known-issue-permissions-to-personal-site-collections_1.png)




1.  Clic**Fine**.
