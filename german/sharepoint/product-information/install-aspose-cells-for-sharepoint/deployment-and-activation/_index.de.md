---
title: Bereitstellung und Aktivierung
type: docs
weight: 20
url: /de/sharepoint/deployment-and-activation/
---

{{% alert color="primary" %}} 

[Die Installation von Aspose.Cells for SharePoint](/cells/de/sharepoint/installing-aspose-cells-for-sharepoint/) führt Sie durch den Installationsprozess. Dieser Artikel erläutert, wie der Installationsprozess bereitgestellt und aktiviert wird.

{{% /alert %}} 
### **Bereitstellung**
Aspose.Cells for SharePoint führt während der Bereitstellung folgende Aktionen aus:

1. Installiert **Aspose.Cells.SharePoint.dll** in den Global Assembly Cache und fügt einen SafeControl-Eintrag zur Datei **web.config** hinzu.
1. Installiert das Feature-Manifest und andere erforderliche Dateien in die entsprechenden Verzeichnisse.
1. Registriert das Feature in der SharePoint-Datenbank und macht es auf Feature-Ebene zur Aktivierung verfügbar.
### **Aktivierung**
Aspose.Cells for SharePoint ist als Site- (Site Collection-)Ebene Feature verpackt und kann auf Site Collections aktiviert und deaktiviert werden. 

Während der Aktivierung nimmt das Feature einige Änderungen am virtuellen Verzeichnis der übergeordneten Webanwendung der Site Collection vor:

1. Fügt eine Konvertierungseinstellungen-Seite zur Sitemap-Datei hinzu.
1. Kopiert erforderliche Ressourcendateien in den App_GlobalResources-Ordner im virtuellen Verzeichnis.
