---
title: Installazione di Aspose.Cells per la licenza SharePoint
type: docs
weight: 10
url: /it/sharepoint/installing-aspose-cells-for-sharepoint-license/
---
{{% alert color="primary" %}}

 Una volta che sei soddisfatto del tuo[valutazione](/cells/it/sharepoint/evaluate-aspose-cells/), [acquistare una licenza](https://purchase.aspose.com/buy).

Prima di acquistare, assicurati di aver compreso e accettato i termini di sottoscrizione della licenza.

{{% /alert %}}

La licenza ti viene inviata via email quando l'ordine è stato pagato. La licenza è un archivio ZIP contenente un normale pacchetto della soluzione SharePoint.

La licenza ZIP contiene:

- **Aspose.Cells.SharePoint.License.wsp** – File del pacchetto della soluzione SharePoint. La licenza Aspose.Cells per SharePoint è confezionata come soluzione SharePoint per facilitare la distribuzione e il ritiro nella server farm.
- **leggimi.txt** – Istruzioni per l'installazione della licenza. L'installazione della licenza viene eseguita dalla console del server tramite il file**stsadm.exe**. Di seguito sono riportati i passaggi necessari per installare la licenza.

#### **Installazione della licenza**

{{% alert color="primary" %}}

 I percorsi sono omessi per chiarezza. Aggiungi il percorso effettivo a**stsadm.exe** e/o il file della soluzione durante l'esecuzione dei passaggi seguenti.

{{% /alert %}}

1. Eseguire stsadm per aggiungere la soluzione all'archivio soluzioni di SharePoint:
 stsadm.exe -o addsolution -nomefile Aspose.Cells.SharePoint.License.wsp
1. Distribuisci la soluzione a tutti i server della farm:
stsadm.exe -o deploysolution -name Aspose.Cells.SharePoint.License.wsp -immediate -force
1. Esegui processi timer amministrativi per completare immediatamente la distribuzione:
 stsadm.exe -o execadmsvcjobs

{{% alert color="primary" %}}

 Si riceverà un avviso durante l'esecuzione della fase di distribuzione se il servizio di amministrazione di SharePoint Services Windows non è stato avviato.**Stsadm.exe** si basa su questo servizio e su Windows SharePoint Timer Service per replicare i dati della soluzione all'interno della farm. Se questi servizi non sono in esecuzione nella server farm, potrebbe essere necessario distribuire la licenza separatamente su ciascun server.

{{% /alert %}}
