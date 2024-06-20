---
title: Installazione della licenza Aspose.Cells for SharePoint
type: docs
weight: 10
url: /it/sharepoint/installing-aspose-cells-for-sharepoint-license/
---

{{% alert color="primary" %}}

Una volta soddisfatto della tua [valutazione](/cells/it/sharepoint/evaluate-aspose-cells/), [acquista una licenza](https://purchase.aspose.com/buy).

Prima di acquistare, assicurati di comprendere e accettare i termini di abbonamento della licenza.

{{% /alert %}}

La licenza ti verrà inviata via email quando l'ordine sarà stato pagato. La licenza è un file ZIP che contiene un normale pacchetto di soluzioni SharePoint.

Il file ZIP della licenza contiene:

- **Aspose.Cells.SharePoint.License.wsp** – File del pacchetto di soluzioni SharePoint. La licenza Aspose.Cells for SharePoint è confezionata come soluzione SharePoint per facilitare il rilascio e il ritiro nell'intera farm del server.
- **readme.txt** – Istruzioni per l'installazione della licenza. L'installazione della licenza viene eseguita dalla console del server tramite **stsadm.exe**. Di seguito sono indicate le operazioni necessarie per installare la licenza.

#### **Installazione della Licenza**

{{% alert color="primary" %}}

I percorsi sono omessi per chiarezza. Aggiungi il percorso effettivo del file **stsadm.exe** e/o della soluzione quando esegui le operazioni seguenti.

{{% /alert %}}

1. Esegui stsadm per aggiungere la soluzione all'archivio delle soluzioni SharePoint:
   stsadm.exe -o addsolution -filename Aspose.Cells.SharePoint.License.wsp
1. Distribuisci la soluzione su tutti i server della farm:
   stsadm.exe -o deploysolution -name Aspose.Cells.SharePoint.License.wsp -immediate -force
1. Esegui le operazioni amministrative programmate per completare immediatamente il rilascio:
   stsadm.exe -o execadmsvcjobs

{{% alert color="primary" %}}

Riceverai un avviso durante l'esecuzione del passaggio di rilascio se il servizio di amministrazione di Windows SharePoint Services non è stato avviato. **Stsadm.exe** si basa su questo servizio e sul servizio Windows SharePoint Timer per replicare i dati della soluzione nell'intera farm. Se questi servizi non sono in esecuzione nella tua farm di server, potresti dover distribuire la licenza separatamente su ciascun server.

{{% /alert %}}
