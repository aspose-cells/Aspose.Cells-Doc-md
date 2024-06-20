---
title: Bekanntes Problem  Berechtigungen für persönliche Website Sammlungen
type: docs
weight: 40
url: /de/sharepoint/known-issue-permissions-to-personal-site-collections/
---

{{% alert color="primary" %}} 

SharePoint gewährt standardmäßig keine vollen Berechtigungen zur Verwaltung von persönlichen Websites an Portaladministratoren. Deshalb kann die Aktivierung und Deaktivierung einer persönlichen Website-Sammlung durch Portaladministratoren fehlschlagen. Dies umfasst die Aktivierung und Deaktivierung während der Einrichtung.

{{% /alert %}} 
### **Berechtigung für persönliche Websites gewähren**
Wenn dieses Problem während der Installation auftritt, wird eine UnauthorizedAccessException bei Microsoft.SharePoint.SPFeature.Activate() im SharePoint-Traceprotokoll protokolliert. Wenn die Deaktivierung als Teil der Deinstallation fehlschlägt, wird eine UnauthorizedAccessException auf dem letzten Einrichtungsbildschirm für die fehlgeschlagenen Deaktivierungen angezeigt.

Um dieses Problem zu verhindern, gewähren Sie Portaladministratoren die Berechtigung zur Verwaltung der MySite-Webanwendung:

1. Gehen Sie zu **SharePoint-Centraladministration** und wählen Sie den **Anwendungsverwaltung**-Tab aus.
1. Wählen Sie **Richtlinie für Webanwendung** in der Gruppe **Anwendungssicherheit** aus.
1. Stellen Sie sicher, dass Sie die richtige Webanwendung für Ihre „Meine Website“ in der Liste **Webanwendung** rechts auswählen.
1. Wählen Sie **Benutzer hinzufügen** oben links aus.
1. Wählen Sie standardmäßig **Alle Zonen** auf dem Bildschirm **Benutzer hinzufügen** aus und klicken Sie auf **Weiter**.
1. Fügen Sie den entsprechenden Benutzer bzw. die aktive Verzeichnisgruppe hinzu, die die Kontrolle über Ihre „Meine Website“-Webanwendung haben soll.
1. Wählen Sie das Kontrollniveau aus. 

   **Benutzer hinzufügen und Kontrollniveau einstellen** 

![todo:image_alt_text](known-issue-permissions-to-personal-site-collections_1.png)




1. Klicken Sie auf **Fertig stellen**.
