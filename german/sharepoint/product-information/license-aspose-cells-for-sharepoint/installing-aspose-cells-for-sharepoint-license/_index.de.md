---
title: Aspose.Cells for SharePoint Lizenz installieren
type: docs
weight: 10
url: /de/sharepoint/installing-aspose-cells-for-sharepoint-license/
---
{{% alert color="primary" %}}

 Sobald Sie mit Ihrem zufrieden sind[Auswertung](/cells/de/sharepoint/evaluate-aspose-cells/), [eine Lizenz kaufen](https://purchase.aspose.com/buy).

Stellen Sie vor dem Kauf sicher, dass Sie die Lizenzabonnementbedingungen verstanden haben und ihnen zustimmen.

{{% /alert %}}

Die Lizenz wird Ihnen per E-Mail zugeschickt, wenn die Bestellung bezahlt wurde. Die Lizenz ist ein ZIP-Archiv, das ein reguläres SharePoint-Lösungspaket enthält.

Die Lizenz-ZIP enthält:

- **Aspose.Cells.SharePoint.License.wsp** – SharePoint-Lösungspaketdatei. Die Aspose.Cells for SharePoint-Lizenz ist als SharePoint-Lösung verpackt, um die Bereitstellung und das Zurückziehen in der gesamten Serverfarm zu erleichtern.
- **readme.txt**– Anweisungen zur Lizenzinstallation. Die Lizenzinstallation wird von der Serverkonsole aus über die durchgeführt**stsadm.exe**. Die zur Installation der Lizenz erforderlichen Schritte sind unten aufgeführt.

#### **Installieren der Lizenz**

{{% alert color="primary" %}}

 Pfade sind der Übersichtlichkeit halber weggelassen. Fügen Sie den tatsächlichen Pfad hinzu**stsadm.exe** und/oder Lösungsdatei, wenn Sie die folgenden Schritte ausführen.

{{% /alert %}}

1. Führen Sie stsadm aus, um die Lösung zum SharePoint-Lösungsspeicher hinzuzufügen:
 stsadm.exe -o addsolution -filename Aspose.Cells.SharePoint.License.wsp
1. Stellen Sie die Lösung auf allen Servern in der Farm bereit:
 stsadm.exe -o deploysolution -name Aspose.Cells.SharePoint.License.wsp -immediate -force
1. Führen Sie administrative Zeitgeberaufträge aus, um die Bereitstellung sofort abzuschließen:
 stsadm.exe -o execadmsvcjobs

{{% alert color="primary" %}}

 Sie erhalten beim Ausführen des Bereitstellungsschritts eine Warnung, wenn der Windows SharePoint Services-Verwaltungsdienst nicht gestartet wurde.**Stsadm.exe**verlässt sich auf diesen Dienst und Windows SharePoint Timer Service, um Lösungsdaten in der gesamten Farm zu replizieren. Wenn diese Dienste nicht auf Ihrer Serverfarm ausgeführt werden, müssen Sie die Lizenz möglicherweise auf jedem Server separat bereitstellen.

{{% /alert %}}
