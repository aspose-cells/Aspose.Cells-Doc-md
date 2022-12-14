---
title: Känt problem - Behörigheter till personliga webbplatssamlingar
type: docs
weight: 40
url: /sv/sharepoint/known-issue-permissions-to-personal-site-collections/
---
{{% alert color="primary" %}} 

SharePoint ger som standard inte fullständiga behörigheter att hantera personliga webbplatser till portaladministratörer. Det är därför aktivering och avaktivering på en personlig webbplatssamling kan misslyckas när den utförs av portaladministratörer. Detta inkluderar aktivering och avaktivering under installationen.

{{% /alert %}} 
### **Bevilja tillstånd till personliga webbplatser**
När det här problemet uppstår under installationen loggas ett UnauthorizedAccessException på Microsoft.SharePoint.SPFeature.Activate() till SharePoint-spårningsloggen. När avaktiveringen misslyckas som en del av avinstallationen, visas ett UnauthorizedAccessException på den senaste inställningsskärmen för den eller de misslyckade inaktiveringen.

För att förhindra detta problem, ge portaladministratörer behörighet att hantera MySite-webbapplikationen:

1.  Gå till**SharePoint central administration** och välj**Applikationshantering** flik.
1.  Välja**Policy för webbapplikation** under**Applikationssäkerhet** grupp.
1.  Se till att du väljer rätt webbapplikation för din "Min webbplats" i**Webbapplikation** lista till höger.
1.  Välj**Lägg till användare** uppe till vänster.
1.  Välja**Alla zoner** som standard på**Lägg till användare** skärmen och klicka**Nästa**.
1. Lägg till lämplig användare eller aktiv kataloggrupp som du vill ha kontroll över din "Min webbplats"-webbapplikation.
1.  Välj kontrollnivå.

   **Lägga till användare och ställa in kontrollnivån** 

![todo:image_alt_text](known-issue-permissions-to-personal-site-collections_1.png)




1.  Klick**Avsluta**.
