---
title: Varför inte automatisering
type: docs
weight: 50
url: /sv/net/why-not-automation/
---

{{% alert color="primary" %}}

Varför är Aspose-komponenter ett mycket bättre alternativ än Microsoft Office Automation?

{{% /alert %}}

## **Introduktion**

Det finns två frågor som vi ofta hör här på Aspose:

1. **Kräver era produkter att Microsoft Office ska vara installerat för att de ska fungera?**
   Det enkla svaret är nej. Aspose-komponenter är helt oberoende och är inte anslutna till, auktoriserade, sponsrade eller på annat sätt godkända av Microsoft Corporation.
1. **Varför ska vi använda Aspose-produkter istället för att använda Microsoft Office-automatisering?**
   Det kortaste svaret vi kunde ge är att det finns många skäl, och det främsta är att Microsoft själva starkt avråder från Office-automatisering från programvarulösningar: [Överväganden för serverbaserad automatisering av Office](https://support.microsoft.com/sv-se/topic/overvaganden-for-serverbaserad-automatisering-av-office-48bcfe93-8a89-47f1-0bce-017433ad79e2).

Det finns flera skäl till varför Aspose-komponenter är ett bättre alternativ till automatisering. Några av de viktigaste skälen är:

- Säkerhet
- Stabilitet
- Skalbarhet/Hastighet
- Pris
- Funktioner

De viktigaste punkterna beskrivs nedan. Se även till att besöka länkarna längst ner i denna sektion.

### **Säkerhet**

Följande är en direkt citat från ovan nämnda Microsoft-artikel:

*"Office-applikationer var aldrig avsedda för serverbaserad användning och tar därför inte hänsyn till de säkerhetsproblem som distribuerade komponenter står inför. Office autentiserar inte inkommande förfrågningar och skyddar dig inte från att oavsiktligt köra makron eller starta en annan server som kanske köra makron, från din serverside-kod. Öppna inte filer som laddas upp till servern från en anonym webb! Beroende på de senast inställda säkerhetsinställningar kan servern köra makron under en administratör eller systemkontext med fulla behörigheter och kompromissa ditt nätverk! Dessutom använder Office många klientkomponenter (som t.ex. Simple MAPI, WinInet och MSDAIPP) som kan cachea klientautentiseringsinformation för att snabba upp bearbetning. Om Office automatiseras serverbaserat kan en instans betjäna flera klienter, och eftersom autentiseringsinformationen har cachats för den sessionen är det möjligt att en klient kan använda de cachelagrade uppgifterna för en annan klient och på så sätt få obehörig åtkomst genom att utge sig för andra användare."*

Aspose-produkter är mycket säkra. Aspose-komponenter körs i samma användarkontext som alla ASP.NET-applikationer, under användaren ASPNET. Därför utgör inte Aspose-komponenter någon potentiell risk för viktiga systemresurser. Dessutom körs inte makron automatiskt när en dokument öppnas med en Aspose-komponent. Aspose-komponenter har utvecklats med målet att låta utvecklare skapa, manipulera och spara Office-filer. Inga av de risker som är förknippade med Microsoft Office-paketet är inneboende i Aspose-komponenter.

### **Stabilitet**

Följande är en direkt citat från den ovan nämnda Microsoft-artikeln:

*"Office 2000, Office XP och Office 2003 använder Microsoft Windows Installer (MSI)-teknik för att göra installation och självreparation enklare för en slutanvändare. MSI introducerar konceptet "installera vid första användning", vilket gör det möjligt att dynamiskt installera eller konfigurera funktioner vid körning (för systemet, eller oftare för en särskild användare). I en serversida miljö bromsar detta både ned prestanda och ökar sannolikheten att en dialogruta kan visas som begär att användaren godkänner installationen eller tillhandahåller en lämplig installationsdisk. Även om det är utformat för att öka tåligheten hos Office som en slutanvändarprodukt är Office-implementeringen av MSI-kapaciteter kontraproduktiv i en serversida miljö. Dessutom kan inte stabiliteten hos Office i allmänhet garanteras när den körs serverside eftersom den inte har utformats eller testats för den här typen av användning. Att använda Office som en tjänstekomponent på en nätverksserver kan minska stabiliteten hos den datorn och som en följd av det ditt nätverk som helhet. Om du planerar att automatisera Office-servern, försök att isolera programmet till en dedikerad dator som inte kan påverka kritiska funktioner och som kan startas om vid behov."*

Eftersom Aspose-komponenter är packade i en enda DLL kommer det aldrig att finnas behov av att installera några ytterligare delar eller bitar för att de ska fungera. Aspose-komponenter används endast av .NET-applikationer och det finns ingen del av komponentkoden som är konstruerad för att vänta på ett mänskligt svar. Aspose-komponenter har noggrant testats. Aspose-komponenter används av företag som IBM, Hilton, Reader's Digest, Bank of America och många fler.

### **Skalbarhet/Hastighet**

Följande är en direkt citat från den ovan nämnda Microsoft-artikeln:

*"Serversidans komponenter behöver vara mycket återinträdande, flertrådade COM-komponenter med minimal överhäng och hög genomströmning för flera klienter. Office-applikationer är nästan överallt det motsatta. De är icke-återinträdande, STA-baserade automatiseringsservrar som är utformade för att tillhandahålla varierande men resursintensiva funktioner för en enda klient. De erbjuder liten skalbarhet som en serverside-lösning och har fasta gränser för viktiga element, som minne, som inte kan ändras genom konfiguration. Ännu viktigare är att de använder globala resurser (som minnesmappade filer, globala tillägg eller mallar och delade automatiseringsservrar), vilket kan begränsa antalet instanser som kan köras samtidigt och leda till kapplöpningssituationer om de är konfigurerade i en flerklientmiljö. Utvecklare som planerar att köra mer än en instans av någon Office-applikation samtidigt behöver överväga att "poola" eller serialisera åtkomst till Office-applikationen för att undvika potentiella dödlägen eller datakorruption."*

Aspose-komponenter är mycket skalbara och blixtsnabba. Kontorsapplikationer var inte avsedda att användas samtidigt av hundratals och tusentals användare; men Aspose-komponenter är utformade just för det. Våra komponenter är en sann .NET-lösning och fungerar felfritt antingen på en enda server som driver en enskild applikation eller på en webbserverfarm med lastbalansering som driver en företagsomfattande applikation.

### **Pris**

När en applikation använder Microsoft Office-automatisering måste en kopia av Microsoft Office köpas för varje maskin som kör applikationen. Det finns många tillfällen då en applikation kanske behöver skapa eller manipulera en kontorsfil men inte kräver att användaren har Office. Aspose erbjuder en mycket kostnadseffektiv, royaltyfri och redistribueringslicens som tillåter distribution till ett obegränsat antal användare utan några licensproblem.

När du skapar webbaserade applikationer är det viktigt att veta att Microsoft Office-automatiseringskomponenter varken är prissatta eller licensierade för serversidelösningar ([Licensiering av Office 2000 Web Components och Office Server Extensions](#)); därför finns det ingen bra licensieringslösning för att distribuera webbapplikationer som utnyttjar Microsoft Office-komponenter. Aspose erbjuder en mycket kostnadseffektiv lösning för serverbaserade applikationer också.

### **Funktioner**

Aspose-komponenter tillhandahåller allt som behövs för att hantera kontorsfiler, plus mycket, mycket mer. De är utformade med filosofin att låta utvecklare uppnå de bästa resultaten med så lite arbete som möjligt. Till skillnad från Office-automatisering tillhandahåller Aspose-komponenter många kraftfulla, tidsbesparande funktioner. Till exempel erbjuder [Aspose.Cells](https://products.aspose.com/cells/) utvecklare möjligheten att exportera direkt från en **DataTable** eller **DataView** till en Excel-fil. [Aspose.Words](https://products.aspose.com/words/) erbjuder en liknande funktion som gör att utvecklare kan fylla i ett Word-sammanfogningsdokument direkt från vilket .NET-dataobjekt som helst. [Varje komponent](https://products.aspose.com/total/) i Aspose-familjen erbjuder sina egna unika, kraftfulla funktioner.

Den bästa delen av att köpa en Aspose-komponent eller en komponentsvit är tillgången till våra utvecklingsteam. Våra utvecklingsteam inser att om det är en funktion som ditt företag behöver kommer med största sannolikhet andra företag att behöva det också. Även om inte varje funktionsbegäran kan läggas till, försöker våra team att vara mycket öppensinnade och flexibla när de ger assistans. Den tankegången är det som har hjälpt Aspose-komponenter att bli så kraftfulla som de är. Om det finns ytterligare funktioner som du behöver från Office-automatiseringsobjekt är dina chanser att få dem tillagda mycket, mycket låga.

## **Slutsats**

{{% alert color="primary" %}}

Den här artikeln har täckt de viktigaste punkterna om varför Aspose-komponenter är ett bättre val än Office-automatisering. Alla olika Aspose-komponenter erbjuder en riskfri, icke-bindande [utvärderingsversion](https://downloads.aspose.com/total). Vi uppmuntrar dig att dra nytta av den utvärderingen för att bättre se vad Aspose kan göra för dina applikationer.


{{% /alert %}}
