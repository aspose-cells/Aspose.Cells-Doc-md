---
title: Installation och aktivering
type: docs
weight: 20
url: /sv/sharepoint/deployment-and-activation/
---

{{% alert color="primary" %}} 

[Installation av Aspose.Cells for SharePoint](/cells/sv/sharepoint/installing-aspose-cells-for-sharepoint/) går igenom installationsprocessen. Den här artikeln förklarar hur installationsprocessen distribueras och aktiveras.

{{% /alert %}} 
### **Distribution**
Aspose.Cells for SharePoint utför följande åtgärder under distribution:

1. Installerar **Aspose.Cells.SharePoint.dll** i den globala samlingsplatsen och lägger till en SafeControl-post i filen **web.config**.
1. Installerar funktionmanifest och andra nödvändiga filer till lämpliga kataloger.
1. Registrerar funktionen i SharePoint-databasen och gör den tillgänglig för aktivering på funktionsomfånget.
### **Aktivering**
Aspose.Cells for SharePoint är paketerad som en funktionalitet på platssamlingsnivå och kan aktiveras och avaktiveras på webbplatssamlingar. 

Under aktivering gör funktionen vissa ändringar i virtuell katalog för webbapplikationen för webbplatsens samling:

1. Lägger till konverteringsinställningssida till webbplatskartan.
1. Kopierar nödvändiga resursfiler till mappen App_GlobalResources i den virtuella katalogen.
