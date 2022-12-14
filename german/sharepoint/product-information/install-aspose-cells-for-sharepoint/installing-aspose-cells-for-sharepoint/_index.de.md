---
title: Installieren von Aspose.Cells für SharePoint
type: docs
weight: 10
url: /de/sharepoint/installing-aspose-cells-for-sharepoint/
---
{{% alert color="primary" %}} 

 Aspose.Cells für SharePoint kann als Archiv Aspose.Cells.SharePoint.zip heruntergeladen werden.

{{% /alert %}} 
### **Inhalt archivieren**
Das Archiv Aspose.Cells.SharePoint.zip enthält:

- Aspose.Cells.SharePoint.wsp – SharePoint-Lösungsdatei. Aspose.Cells für SharePoint ist als SharePoint-Lösung verpackt, um die Bereitstellung/Rücknahme und die Aktivierung/Deaktivierung von Funktionen in der gesamten Serverfarm zu erleichtern.
- Aspose_LicenseAgreement.rtf – Endbenutzer-Lizenzvertrag
- Aspose.Cells für SharePoint.pdf – Benutzerdokumentation
- Aspose.Cells für SharePoint Documentation.chm – Benutzerdokumentation mit öffentlicher API-Referenz
- setup.exe – Setup-Programm
- setup.exe.config – Setup-Konfigurationsdatei

Das Setup-Programm überprüft die folgenden Bedingungen, bevor es mit der Installation fortfährt:

- WSS 3.0, MOSS 2007 oder SharePoint 2010 ist installiert.
- Der Benutzer hat die Berechtigung, SharePoint-Lösungen zu installieren.
- SharePoint-Datenbank ist online.
- Der WSS-Verwaltungsdienst wird gestartet.
- Der WSS-Timer-Dienst wird gestartet.

 Der WSS-Verwaltungsdienst und der Timer-Dienst sind erforderlich, da einige Setup-Aktionen auf einem Timer-Auftrag beruhen, der an alle Server in der Serverfarm weitergegeben wird.
#### **So installieren Sie Aspose.Cells für SharePoint**
1. Entpacken Sie die ZIP-Datei Aspose.Cells.SharePoint auf das lokale Laufwerk des MOSS 7.0- oder WSS 3.0-Servers.
1. Führen Sie setup.exe aus und folgen Sie den Anweisungen auf dem Bildschirm.

Das Setup-Programm führt die folgenden Aktionen aus:

1.  Überprüfen Sie die Installationsvoraussetzungen. Setup wird nicht fortgesetzt, wenn eine Überprüfung fehlschlägt.

   **Systemüberprüfung** 

![todo: Bild_alt_Text](installing-aspose-cells-for-sharepoint_1.png)




1.  Endbenutzer-Lizenzvereinbarung anzeigen. Der Benutzer muss die Vereinbarung akzeptieren, um fortzufahren.

   **Die EULA** 

![todo: Bild_alt_Text](installing-aspose-cells-for-sharepoint_2.png)




1. Dialogfeld zur Auswahl des Bereitstellungsziels anzeigen. Der Benutzer wählt Webanwendungen und Websitesammlungen aus, in denen die Funktion aktiviert werden soll. Siehe die Abbildung unten.

   **Bereitstellungsziele** 

![todo: Bild_alt_Text](installing-aspose-cells-for-sharepoint_3.png)




1.  Stellen Sie das Feature in der Serverfarm bereit.

   **Laufende Installation** 

![todo: Bild_alt_Text](installing-aspose-cells-for-sharepoint_4.png)




1. Aktivieren Sie die Funktion für die ausgewählten Websitesammlungen und konfigurieren Sie ihre übergeordneten Webanwendungen.
1.  Zeigen Sie eine Liste der Webanwendungen und Websitesammlungen an, in denen die Funktion bereitgestellt und aktiviert wurde.

   **Installation abgeschlossen** 

![todo: Bild_alt_Text](installing-aspose-cells-for-sharepoint_5.png)
