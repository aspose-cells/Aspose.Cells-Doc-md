---
title: Installation von Aspose.Cells for SharePoint
type: docs
weight: 10
url: /de/sharepoint/installing-aspose-cells-for-sharepoint/
---

{{% alert color="primary" %}} 

Aspose.Cells for SharePoint ist als Archiv Aspose.Cells.SharePoint.zip herunterladbar. 

{{% /alert %}} 
### **Archivinhalt**
Das Archiv Aspose.Cells.SharePoint.zip enthält:

- Aspose.Cells.SharePoint.wsp – SharePoint-Lösungsdatei. Aspose.Cells for SharePoint ist als SharePoint-Lösung verpackt, um Bereitstellung/Rücknahme und Feature-Aktivierung/Deaktivierung über den Serverfarm hinweg zu erleichtern.
- Aspose_LicenseAgreement.rtf – Endbenutzer-Lizenzvereinbarung
- Aspose.Cells for SharePoint.pdf – Benutzerdokumentation
- Aspose.Cells for SharePoint Dokumentation.chm – Benutzerdokumentation mit öffentlicher API-Referenz
- setup.exe – Setup-Programm
- setup.exe.config – Setup-Konfigurationsdatei

Das Setup-Programm überprüft die folgenden Bedingungen, bevor es mit der Installation fortsetzt:

- WSS 3.0, MOSS 2007 oder SharePoint 2010 ist installiert.
- Der Benutzer hat die Berechtigung, SharePoint-Lösungen zu installieren.
- Die SharePoint-Datenbank ist online.
- Der WSS-Verwaltungsdienst ist gestartet.
- Der WSS-Zeitgeberdienst ist gestartet.

Der WSS-Verwaltungsdienst und der Zeitgeberdienst sind erforderlich, da einige Einrichtungsaktionen von einem Zeitgesteuerten Job abhängen, der auf alle Server im Serverfarm verteilt wird. 
#### **Um Aspose.Cells for SharePoint zu installieren**
1. Entpacken Sie Aspose.Cells.SharePoint zip auf dem lokalen Laufwerk des MOSS 7.0- oder WSS 3.0-Servers.
1. Führen Sie setup.exe aus und befolgen Sie die Anweisungen auf dem Bildschirm.

Das Setup-Programm führt die folgenden Aktionen aus:

1. Überprüfen Sie die Installationsvoraussetzungen. Das Setup wird nicht fortgesetzt, wenn eine Überprüfung fehlschlägt. 

   **Systemprüfung** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_1.png)




1. Anzeigen der Endbenutzer-Lizenzvereinbarung. Der Benutzer muss der Vereinbarung zustimmen, um fortzufahren. 

   **Die EULA** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_2.png)




1. Dialogfeld zur Auswahl des Bereitstellungsziels anzeigen. Der Benutzer wählt Webanwendungen und Website-Sammlungen aus, in denen das Feature aktiviert werden soll. Siehe die Abbildung unten. 

   **Bereitstellungsziele** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_3.png)




1. Das Feature in der Serverfarm bereitstellen. 

   **Installation läuft** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_4.png)




1. Das Feature für die ausgewählten Website-Sammlungen aktivieren und deren übergeordnete Webanwendungen konfigurieren.
1. Eine Liste der Webanwendungen und Website-Sammlungen anzeigen, in denen das Feature bereitgestellt und aktiviert wurde. 

   **Installation abgeschlossen** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_5.png)
