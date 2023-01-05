---
title: Licensfilen fungerar inte längre
type: docs
weight: 60
url: /sv/net/license-file-not-working-anymore/
---
## **Symptom**

 Ibland blir användarna frustrerade för att deras licensfiler inte fungerar längre när de flyttar/publicerar sina webbprojekt till en ny server. De känner sig upprörda eftersom deras licensfiler fungerade korrekt på deras tidigare (gamla) server men nu får de en extra**Utvärdering Copyright Varning** vattenstämpel arbetsblad (när de genererar rapporter med hjälp av komponenten) på den nya servermiljön.

### **Ett scenario**

"Vi har använt Aspose.Cells i vårt ASP.NET webbprojekt för att generera/manipulera Excel-rapporter, vi fick en giltig licens som vi använder. För några dagar sedan flyttade vi webbplatsen till en ny server; det gjordes inga som helst uppgraderingar eller ändringar, vi har sett till och helt enkelt flyttat varje fil till den nya servern, inklusive Aspose.Cells.dll och relaterade .lic-filer. Nu när vi försöker generera Excel-rapporter i den nya servermiljön får vi en**Utvärdering Copyright Varning** vattenstämpelblad på våra rapporter. Vi försökte ladda ner och installera en ny licensfil från avsnittet Mina beställningar på webbplatsen, men det löste inte problemet alls. FYI, vi implementerar licensen genom att placera filen Aspose.Cells.lic i webbplatsens bin-mapp tillsammans med komponentfilen Aspose.Cells.dll, som, som jag har nämnt, fungerade utan problem på den gamla servern."

### **Lösning**

Aspose har en ren och pålitlig licensmekanism. I allmänhet bör problemet vara relaterat till distributionsproblem. Om en licensfil fungerar bra (på en server) bör den fungera lika bra på andra servrar/miljöer. Normalt använder användarna Application_Start eller Session_Starta event etc. i global.asax-filen för att placera licenskoden där. Så det är mycket möjligt att applikationen_Start / Session_Starthändelser aktiveras inte för att bearbeta licenskoden på sina nya platser. Det bör noteras här att Aspose.Cells alltid ger ett undantag om komponenten inte kan hitta licensfilen i en sökväg. Användarna bör se till att licenskoden (var de än placeras) ska bearbetas och händelser ska utlösas där licenskoden placeras. Användaren kan starta om den relaterade tjänsten, dvs. "World Wide Web Publishing" och försöka spåra om Application_Start / Session_Starthändelser utlöses när de besöker sina projekt i den nya servermiljön.

### **Bekräftelse**

Se också till att…

- Du använder en giltig licensfil i ditt projekt.
- Du eller någon annan bör inte redigera/modifiera licensfilen, åtminstone fungerar inte licensfilen.
- Du bör vara medveten om att din licensprenumeration löper ut (du kan helt enkelt öppna lic-filen i anteckningsblocket och kontrollera utgångsdatumet).
-  Du använder inte en version (Aspose.Cells.dll) som släpps efter att din licensprenumeration löper ut. Det bör noteras här, en licensfil går aldrig ut, men om du använder komponentversionen som släpps efter att din prenumeration löper ut får du en extra**Utvärdering Copyright Varning** vattenstämpelblad när du skapar en excel-fil.

### **Referenser**

<https://forum.aspose.com/t/license-file-not-working-on-new-server/83110>

<https://forum.aspose.com/t/license-not-being-detected/83516/4>
