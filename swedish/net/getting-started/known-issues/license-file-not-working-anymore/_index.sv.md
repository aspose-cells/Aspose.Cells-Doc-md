---
title: Licensfilen fungerar inte längre
type: docs
weight: 60
url: /sv/net/license-file-not-working-anymore/
---

## **Symptom**

Ibland blir användarna frustrerade eftersom deras licensfiler inte längre fungerar när de flyttar/publicerar sina webbprojekt till en ny server. De är besvikna eftersom deras licensfiler fungerade korrekt på deras tidigare (gamla) server men nu får de en extra **Evaluering Copyright Varning**-vattenstämpel på arbetsbladet (när de genererar rapporter med komponenten) i den nya serversmiljön.

### **En scen**

"Vi har använt Aspose.Cells i vårt ASP.NET-webbprojekt för att generera/manipulera Excel-rapporter, vi har en giltig licens som vi använder. För några dagar sedan flyttade vi webbplatsen till en ny server; det fanns inga uppgraderingar eller ändringar alls, vi har sett till och helt enkelt flyttat alla filer till den nya servern, inklusive Aspose.Cells.dll och relaterade .lic-filer. Nu när vi försöker generera Excel-rapporter i den nya serversmiljön får vi en **Evaluering Copyright Varning**-vattenstämpel på våra rapporter. Vi försökte ladda ner och installera en ny licensfil från avdelningen Mina beställningar på webbplatsen, men det löste inte problemet alls. För din information, implementerar vi licensen genom att placera filen Aspose.Cells.lic i webbplatsens bin-mapp tillsammans med komponentfilen Aspose.Cells.dll, vilket, som jag har nämnt, fungerade utan problem på den gamla servern."

### **Lösning**

Aspose har en ren och pålitlig licensieringsmekanism. Generellt sett borde problemet vara relaterat till distributionsproblem. Om en licensfil fungerar bra (på en server) bör den fungera lika bra på andra servrar/miljöer också. Normalt sett använder användarna Application_Start eller Session_Start händelser osv. i filen global.asax för att placera licensieringskoden där. Så det är ganska möjligt att Application_Start / Session_Start händelse(r) inte aktiveras för att bearbeta licensieringskoden på deras nya platser. Det bör noteras här att Aspose.Cells alltid kastar ett undantag om komponenten inte kan hitta licensfilen i en sökväg. Användarna bör se till att licensieringskoden (var de än placerar den) bör bearbetas och att händelser bör aktiveras där licensieringskoden är placerad. Användaren kan starta om den relaterade tjänsten, dvs. "World Wide Web Publishing", och försöka spåra om Application_Start / Session_Start händelser aktiveras när de besöker sina projekt i den nya serversmiljön.

### **Bekräftelse**

Se också till att…

- Du använder en giltig licensfil i ditt projekt.
- Du eller någon annan inte bör redigera/ändra licensfilen minst så att licensfilen inte fungerar.
- Du bör vara medveten om att din licensprenumeration går ut (du kan enkelt öppna filen med .lic i anteckningar och kontrollera utgångsdatumet).
- Du använder inte en version (Aspose.Cells.dll) som släpps efter att din licensprenumeration gått ut. Det bör noteras här att en licensfil aldrig går ut, men om du använder komponentversioner som släpps efter att din prenumeration gått ut, får du en extra **Evaluering Copyright Varning**-vattenstämpel när du skapar en Excel-fil.

### **Referenser**

<https://forum.aspose.com/t/license-file-not-working-on-new-server/83110>

<https://forum.aspose.com/t/license-not-being-detected/83516/4>
{{< app/cells/assistant language="csharp" >}}
