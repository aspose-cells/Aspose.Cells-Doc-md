---
title: Bereitstellung und Aktivierung
type: docs
weight: 20
url: /de/sharepoint/deployment-and-activation/
---
{{% alert color="primary" %}} 

[Installieren von Aspose.Cells for SharePoint](/cells/de/sharepoint/installing-aspose-cells-for-sharepoint/) führt Sie durch den Installationsprozess. In diesem Artikel wird erläutert, wie der Installationsprozess bereitgestellt und aktiviert wird.

{{% /alert %}} 
### **Einsatz**
Aspose.Cells for SharePoint führt die folgenden Aktionen während der Bereitstellung aus:

1.  Installiert**Aspose.Cells.SharePoint.dll** in den globalen Assemblycache und fügt einen SafeControl-Eintrag hinzu**web.config** Datei.
1. Installiert das Funktionsmanifest und andere erforderliche Dateien in den entsprechenden Verzeichnissen.
1. Registriert das Feature in der SharePoint-Datenbank und stellt es für die Aktivierung im Featurebereich zur Verfügung.
### **Aktivierung**
 Aspose.Cells for SharePoint ist als Funktion auf Websiteebene (Websitesammlung) gepackt und kann in Websitesammlungen aktiviert und deaktiviert werden.

Während der Aktivierung nimmt das Feature einige Änderungen am virtuellen Verzeichnis der übergeordneten Webanwendung der Websitesammlung vor:

1. Fügt der Sitemap-Datei eine Seite mit Konvertierungseinstellungen hinzu.
1. Kopiert die erforderlichen Ressourcendateien in den Ordner App_GlobalResources im virtuellen Verzeichnis.
