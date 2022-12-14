---
title: Installazione di Aspose.Cells per SharePoint
type: docs
weight: 10
url: /it/sharepoint/installing-aspose-cells-for-sharepoint/
---
{{% alert color="primary" %}} 

 Aspose.Cells per SharePoint è scaricabile come archivio Aspose.Cells.SharePoint.zip.

{{% /alert %}} 
### **Archivio contenuti**
L'archivio Aspose.Cells.SharePoint.zip contiene:

- Aspose.Cells.SharePoint.wsp: file della soluzione SharePoint. Aspose.Cells per SharePoint è confezionato come soluzione SharePoint per facilitare la distribuzione/ritiro e l'attivazione/disattivazione delle funzionalità nella server farm.
- Aspose_LicenseAgreement.rtf – Contratto di licenza con l'utente finale
- Aspose.Cells per SharePoint.pdf – Documentazione utente
- Aspose.Cells per SharePoint Documentation.chm – Documentazione utente con riferimento API pubblico
- setup.exe – Programma di installazione
- setup.exe.config: file di configurazione dell'installazione

Il programma di installazione controlla le seguenti condizioni prima di procedere con l'installazione:

- WSS 3.0, MOSS 2007 o SharePoint 2010 è installato.
- L'utente dispone dell'autorizzazione per installare soluzioni SharePoint.
- Il database di SharePoint è online.
- Il servizio di amministrazione WSS viene avviato.
- Il servizio WSS Timer è stato avviato.

 Il servizio Amministrazione WSS e il servizio Timer sono necessari perché alcune azioni di configurazione si basano su un processo timer per la propagazione a tutti i server della server farm.
#### **Per installare Aspose.Cells per SharePoint**
1. Decomprimere Aspose.Cells.SharePoint zip nell'unità locale del server MOSS 7.0 o WSS 3.0.
1. Eseguire setup.exe e seguire le istruzioni sullo schermo.

Il programma di installazione esegue le seguenti azioni:

1.  Verificare i prerequisiti di installazione. L'installazione non continuerà se un controllo non riesce.

   **Controllo del sistema** 

![cose da fare:immagine_alt_testo](installing-aspose-cells-for-sharepoint_1.png)




1.  Visualizza il contratto di licenza con l'utente finale. L'utente deve accettare l'accordo per procedere.

   **L'EULA** 

![cose da fare:immagine_alt_testo](installing-aspose-cells-for-sharepoint_2.png)




1. Visualizza la finestra di dialogo per la selezione della destinazione della distribuzione. L'utente seleziona le applicazioni Web e le raccolte siti in cui deve essere attivata la funzionalità. Vedere la figura sottostante.

   **Obiettivi di distribuzione** 

![cose da fare:immagine_alt_testo](installing-aspose-cells-for-sharepoint_3.png)




1.  Distribuire la funzionalità alla server farm.

   **Installazione in corso** 

![cose da fare:immagine_alt_testo](installing-aspose-cells-for-sharepoint_4.png)




1. Attivare la funzionalità per le raccolte siti selezionate e configurare le relative applicazioni Web padre.
1.  Visualizza un elenco di applicazioni Web e raccolte siti in cui la funzionalità è stata distribuita e attivata.

   **Installazione completata** 

![cose da fare:immagine_alt_testo](installing-aspose-cells-for-sharepoint_5.png)
