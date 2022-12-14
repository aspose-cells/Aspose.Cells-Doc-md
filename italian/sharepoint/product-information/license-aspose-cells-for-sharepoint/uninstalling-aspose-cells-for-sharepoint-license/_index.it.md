---
title: Disinstallazione di Aspose.Cells per la licenza SharePoint
type: docs
weight: 30
url: /it/sharepoint/uninstalling-aspose-cells-for-sharepoint-license/
---
{{% alert color="primary" %}} 

 Per disinstallare Aspose.Cells per la licenza SharePoint, utilizzare i passaggi seguenti dalla console del server.

{{% /alert %}} 

1. Ritirare la soluzione di licenza dalla farm:
stsadm.exe -o retractsolution -name Aspose.Cells.SharePoint.License.wsp -immediato
1. Esegui processi timer amministrativi per completare immediatamente il ritiro:
 stsadm.exe -o execadmsvcjobs
1. Attendere il completamento del ritiro.
 Puoi utilizzare Amministrazione centrale per verificare se il ritiro è stato completato andando a**Amministrazione Centrale** , poi**Operazioni** e**Gestione della soluzione**.
1. Rimuovere la soluzione dall'archivio soluzioni di SharePoint:
 stsadm.exe -o deletesolution -name Aspose.Cells.SharePoint.License.wsp
