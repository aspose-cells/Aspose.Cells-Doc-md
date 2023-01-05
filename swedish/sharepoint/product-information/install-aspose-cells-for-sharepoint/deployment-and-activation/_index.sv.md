---
title: Implementering och aktivering
type: docs
weight: 20
url: /sv/sharepoint/deployment-and-activation/
---
{{% alert color="primary" %}} 

[Installerar Aspose.Cells for SharePoint](/cells/sv/sharepoint/installing-aspose-cells-for-sharepoint/) vägleder dig genom installationsprocessen. Den här artikeln förklarar hur installationsprocessen distribueras och aktiveras.

{{% /alert %}} 
### **Spridning**
Aspose.Cells for SharePoint utför följande åtgärder under driftsättning:

1.  Installerar**Aspose.Cells.SharePoint.dll** i Global Assembly Cache och lägger till en SafeControl-post till**web.config** fil.
1. Installationsfunktioner manifest och andra nödvändiga filer till lämpliga kataloger.
1. Registrerar funktionen i SharePoint-databasen och gör den tillgänglig för aktivering i funktionsomfånget.
### **Aktivering**
 Aspose.Cells for SharePoint är förpackad som en funktion på webbplatsen (webbplatssamling) och kan aktiveras och inaktiveras på webbplatssamlingar.

Under aktiveringen gör funktionen några ändringar i den virtuella katalogen för webbplatssamlingens överordnade webbapplikation:

1. Lägger till sidan med konverteringsinställningar i webbplatskartfilen.
1. Kopierar nödvändiga resursfiler till mappen App_GlobalResources i den virtuella katalogen.
