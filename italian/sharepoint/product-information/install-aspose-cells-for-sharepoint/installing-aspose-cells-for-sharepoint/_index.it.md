---
title: Installazione Aspose.Cells for SharePoint
type: docs
weight: 10
url: /it/sharepoint/installing-aspose-cells-for-sharepoint/
---

{{% alert color="primary" %}} 

Aspose.Cells for SharePoint è scaricabile come archivio Aspose.Cells.SharePoint.zip. 

{{% /alert %}} 
### **Contenuti dell'archivio**
L'archivio Aspose.Cells.SharePoint.zip contiene:

- Aspose.Cells.SharePoint.wsp – File della soluzione SharePoint. Aspose.Cells for SharePoint è confezionato come una soluzione SharePoint per facilitare il deploy/retract e l'attivazione/disattivazione della funzionalità in tutto il server farm.
- Aspose_LicenseAgreement.rtf – Contratto di licenza per l'utente finale
- Aspose.Cells for SharePoint.pdf – Documentazione utente
- Aspose.Cells for SharePoint Documentation.chm – Documentazione utente con riferimento alla API pubblica
- setup.exe – Programma di installazione
- setup.exe.config – File di configurazione del programma di installazione

Il programma di installazione verifica le seguenti condizioni prima di procedere con l'installazione:

- WSS 3.0, MOSS 2007 o SharePoint 2010 è installato.
- L'utente ha il permesso di installare le soluzioni SharePoint.
- Il database di SharePoint è online.
- Il servizio di amministrazione di WSS è avviato.
- Il servizio Timer di WSS è avviato.

I servizi di amministrazione e Timer di WSS sono necessari poiché alcune azioni di configurazione si basano su un job del timer per propagarsi a tutti i server della farm. 
#### **Per installare Aspose.Cells for SharePoint**
1. Decomprimere Aspose.Cells.SharePoint zip sull'unità locale del server MOSS 7.0 o WSS 3.0.
1. Eseguire setup.exe e seguire le istruzioni visualizzate sullo schermo.

Il programma di installazione esegue le seguenti azioni:

1. Controllare i requisiti di installazione. L'installazione non continuerà se il controllo fallisce. 

   **Controllo del sistema** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_1.png)




1. Visualizzare il Contratto di Licenza per l'Utente Finale. L'utente deve accettare l'accordo per poter procedere. 

   **Il CLUF** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_2.png)




1. Visualizzare la finestra di selezione del target di distribuzione. L'utente seleziona le web application e le raccolte di siti in cui la funzionalità deve essere attivata. Vedere la figura qui sotto. 

   **Target di distribuzione** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_3.png)




1. Distribuire la funzionalità alla farm server. 

   **Installazione in corso** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_4.png)




1. Attivare la funzionalità per le raccolte di siti selezionate e configurare le web application padre.
1. Visualizzare un elenco di web application e raccolte di siti in cui la funzionalità è stata distribuita e attivata. 

   **Installazione completata** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_5.png)
