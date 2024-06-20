---
title: Lizenz Aspose.Cells for SharePoint installieren
type: docs
weight: 10
url: /de/sharepoint/installing-aspose-cells-for-sharepoint-license/
---

{{% alert color="primary" %}}

Sobald Sie mit Ihrer [Evaluation](/cells/de/sharepoint/evaluate-aspose-cells/) zufrieden sind, [erwerben Sie eine Lizenz](https://purchase.aspose.com/buy).

Bevor Sie kaufen, stellen Sie sicher, dass Sie die Lizenzabonnementbedingungen verstehen und zustimmen.

{{% /alert %}}

Die Lizenz wird per E-Mail an Sie gesendet, sobald die Bestellung bezahlt wurde. Die Lizenz ist ein ZIP-Archiv, das eine reguläre SharePoint-Lösungspaketdatei enthält.

Das Lizenz-ZIP enthält:

- **Aspose.Cells.SharePoint.License.wsp** – SharePoint-Lösungspaketdatei. Die Aspose.Cells for SharePoint-Lizenz ist als SharePoint-Lösungspaket verpackt, um die Bereitstellung und Rücknahme im gesamten Serverfarm zu erleichtern.
- **readme.txt** – Anweisungen zur Lizenzinstallation. Die Lizenzinstallation erfolgt über die Serverkonsole über **stsadm.exe**. Die erforderlichen Schritte zur Installation der Lizenz sind nachfolgend aufgeführt.

#### **Installation der Lizenz**

{{% alert color="primary" %}}

Pfade werden aus Gründen der Übersichtlichkeit weggelassen. Fügen Sie den tatsächlichen Pfad zur Datei **stsadm.exe** und/oder zur Lösungsdatei hinzu, wenn Sie die nachfolgenden Schritte ausführen.

{{% /alert %}}

1. Führen Sie stsadm aus, um die Lösung im SharePoint-Lösungsspeicher hinzuzufügen:
   stsadm.exe -o addsolution -filename Aspose.Cells.SharePoint.License.wsp
1. Bereitstellen der Lösung auf allen Servern in der Farm:
   stsadm.exe -o deploysolution -name Aspose.Cells.SharePoint.License.wsp -immediate -force
1. Ausführen administrativer Timerjobs, um die Bereitstellung sofort abzuschließen:
   stsadm.exe -o execadmsvcjobs

{{% alert color="primary" %}}

Beim Ausführen des Bereitstellungsschritts erhalten Sie eine Warnung, wenn der Windows SharePoint Services-Administrationsservice nicht gestartet wurde. **Stsadm.exe** ist auf diesen Dienst und den Windows SharePoint Timer-Dienst angewiesen, um Lösungsdaten über die Farm zu replizieren. Wenn diese Dienste auf Ihrer Serverfarm nicht ausgeführt werden, müssen Sie die Lizenz möglicherweise separat auf jedem Server bereitstellen.

{{% /alert %}}
