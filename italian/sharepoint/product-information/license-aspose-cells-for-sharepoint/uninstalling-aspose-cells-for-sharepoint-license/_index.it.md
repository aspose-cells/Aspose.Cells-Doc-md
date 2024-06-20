---
title: Disinstallazione della Licenza Aspose.Cells for SharePoint
type: docs
weight: 30
url: /it/sharepoint/uninstalling-aspose-cells-for-sharepoint-license/
---

{{% alert color="primary" %}} 

Per disinstallare la licenza Aspose.Cells for SharePoint, utilizza le operazioni seguenti dalla console del server. 

{{% /alert %}} 

1. Ritirare la soluzione della licenza dalla farm:
   stsadm.exe -o retractsolution -name Aspose.Cells.SharePoint.License.wsp -immediate
1. Eseguire i lavori di amministrazione temporizzati per completare immediatamente la retrazione:
   stsadm.exe -o execadmsvcjobs
1. Attendere il completamento della retrazione.
   È possibile utilizzare l'Amministrazione centrale per verificare se la retrazione è stata completata andando su **Amministrazione centrale**, quindi su **Operazioni** e **Gestione soluzioni**.
1. Rimuovere la soluzione dal deposito delle soluzioni di SharePoint:
   stsadm.exe -o deletesolution -name Aspose.Cells.SharePoint.License.wsp
