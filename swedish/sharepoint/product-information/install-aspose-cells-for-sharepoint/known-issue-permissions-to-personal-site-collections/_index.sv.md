---
title: Känd problem  Behörigheter för personliga webbplatssamlingar
type: docs
weight: 40
url: /sv/sharepoint/known-issue-permissions-to-personal-site-collections/
---

{{% alert color="primary" %}} 

SharePoint ger inte automatiskt fulla behörigheter att hantera personliga platser till portalkontoadministratörer. Därför kan aktivering och avaktivering av en personlig platssamling misslyckas när det utförs av portalkontoadministratörer. Detta inkluderar aktivering och avaktivering under installationen.

{{% /alert %}} 
### **Tilldela behörighet till personliga platser**
När detta problem uppstår under installationen loggas ett UnauthorizedAccessException på Microsoft.SharePoint.SPFeature.Activate() till SharePoint-spårloggen. När avaktivering misslyckas som en del av avinstallationen visas en UnauthorizedAccessException på den sista installationsbilden för de misslyckade avaktiveringarna.

För att förhindra detta problem, tilldela portalkontoadministratörer behörighet att hantera min webbplatsapp:

1. Gå till **SharePoint Centraladministration** och välj fliken **Programhantering**.
1. Välj **Policy för webbprogram** under gruppen **Programsäkerhet**.
1. Se till att du väljer rätt webbprogram för din "Min webbplats" i listan **Webbprogram** till höger.
1. Välj **Lägg till användare** längst upp till vänster.
1. Välj **Alla zoner** som standard på skärmen **Lägg till användare** och klicka på **Nästa**.
1. Lägg till lämpliga användare eller aktiva kataloggrupper som du vill ha kontroll över din "Min webbplats" webbapp.
1. Välj nivån för kontroll. 

   **Lägga till användare och ange kontrollnivån** 

![todo:image_alt_text](known-issue-permissions-to-personal-site-collections_1.png)




1. Klicka på **Slutför**.
