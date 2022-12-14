---
title: Deinstallieren von Aspose.Cells für die SharePoint-Lizenz
type: docs
weight: 30
url: /de/sharepoint/uninstalling-aspose-cells-for-sharepoint-license/
---
{{% alert color="primary" %}} 

 Um die Lizenz Aspose.Cells für SharePoint zu deinstallieren, führen Sie bitte die folgenden Schritte von der Serverkonsole aus aus.

{{% /alert %}} 

1. Ziehen Sie die Lizenzlösung aus der Farm zurück:
stsadm.exe -o RetractSolution -Name Aspose.Cells.SharePoint.License.wsp -Immediate
1. Führen Sie administrative Zeitgeberaufträge aus, um das Zurückziehen sofort abzuschließen:
 stsadm.exe -o execadmsvcjobs
1. Warten Sie, bis das Zurückziehen abgeschlossen ist.
 Sie können die Zentraladministration verwenden, um zu überprüfen, ob der Widerruf abgeschlossen ist, indem Sie zu gehen**Zentrale Verwaltung** , dann**Operationen** und**Lösungsmanagement**.
1. Entfernen Sie die Lösung aus dem SharePoint-Lösungsspeicher:
 stsadm.exe -o deletesolution -name Aspose.Cells.SharePoint.License.wsp
