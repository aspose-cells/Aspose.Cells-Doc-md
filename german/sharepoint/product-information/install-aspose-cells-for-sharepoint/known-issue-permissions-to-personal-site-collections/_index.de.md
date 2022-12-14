---
title: Bekanntes Problem – Berechtigungen für persönliche Websitesammlungen
type: docs
weight: 40
url: /de/sharepoint/known-issue-permissions-to-personal-site-collections/
---
{{% alert color="primary" %}} 

SharePoint gewährt Portaladministratoren standardmäßig keine vollständigen Berechtigungen zum Verwalten persönlicher Websites. Aus diesem Grund kann die Aktivierung und Deaktivierung einer persönlichen Websitesammlung fehlschlagen, wenn sie von Portaladministratoren durchgeführt wird. Dies umfasst die Aktivierung und Deaktivierung während des Setups.

{{% /alert %}} 
### **Erteilen von Berechtigungen für persönliche Websites**
Wenn dieses Problem während der Installation auftritt, wird eine UnauthorizedAccessException bei Microsoft.SharePoint.SPFeature.Activate() im SharePoint-Ablaufverfolgungsprotokoll protokolliert. Wenn die Deaktivierung im Rahmen der Deinstallation fehlschlägt, wird auf dem letzten Setup-Bildschirm eine UnauthorizedAccessException für die fehlgeschlagene(n) Deaktivierung(en) angezeigt.

Um dieses Problem zu vermeiden, erteilen Sie Portaladministratoren die Berechtigung zum Verwalten der MySite-Webanwendung:

1.  Gehe zu**SharePoint-Zentraladministration** und wählen Sie die aus**Bewerbungsmanagement** Tab.
1.  Wählen**Richtlinie für Webanwendung** unter dem**Anwendungssicherheit** Gruppe.
1.  Stellen Sie sicher, dass Sie die richtige Webanwendung für Ihre „Meine Website“ im auswählen**Internetanwendung** Liste rechts.
1.  Auswählen**Benutzer hinzufügen** oben links.
1.  Wählen**Alle Zonen** standardmäßig auf der**Benutzer hinzufügen** Bildschirm und klicken Sie auf**Nächste**.
1. Fügen Sie die entsprechenden Benutzer oder Active Directory-Gruppen hinzu, die Sie über Ihre Webanwendung „Meine Website“ steuern möchten.
1.  Wählen Sie die Kontrollebene aus.

   **Hinzufügen von Benutzern und Einstellen der Kontrollebene** 

![todo: Bild_alt_Text](known-issue-permissions-to-personal-site-collections_1.png)




1.  Klicken**Fertig**.
