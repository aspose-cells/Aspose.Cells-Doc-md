---
title: Deinstallieren der Lizenz Aspose.Cells for SharePoint
type: docs
weight: 30
url: /de/sharepoint/uninstalling-aspose-cells-for-sharepoint-license/
---

{{% alert color="primary" %}} 

Um die Lizenz Aspose.Cells for SharePoint zu deinstallieren, verwenden Sie bitte die folgenden Schritte von der Serverkonsole. 

{{% /alert %}} 

1. Widerrufen Sie die Lizenzlösung aus dem Farm:
   stsadm.exe -o retractsolution -name Aspose.Cells.SharePoint.License.wsp -immediate
1. Führen Sie administrative Timerjobs aus, um den Widerruf unverzüglich abzuschließen:
   stsadm.exe -o execadmsvcjobs
1. Warten Sie, bis der Widerruf abgeschlossen ist.
   Sie können die Zentraladministration verwenden, um zu überprüfen, ob der Widerruf abgeschlossen ist, indem Sie zu **Zentraladministration**, dann **Betrieb** und **Lösungsverwaltung** gehen.
1. Entfernen Sie die Lösung aus dem SharePoint-Lösungsspeicher:
   stsadm.exe -o deletesolution -name Aspose.Cells.SharePoint.License.wsp
