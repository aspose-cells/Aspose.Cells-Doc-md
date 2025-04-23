---
title: Varför inte automatisering
type: docs
weight: 20
url: /sv/java/why-not-automation/
---

{{% alert color="primary" %}}

Varför är Aspose-komponenter ett mycket bättre alternativ än Microsoft Office Automation?

Det finns två frågor som vi ofta hör här på Aspose:

1. **Kräver era produkter att Microsoft Office ska vara installerat för att de ska fungera?** 
   Det enkla svaret är nej. Aspose-komponenter är helt oberoende och är inte anslutna till, auktoriserade, sponsrade eller på annat sätt godkända av Microsoft Corporation.
1. **Varför ska vi använda Aspose-produkter istället för att använda Microsoft Office-automatisering?**
   Det kortaste svaret vi kunde ge är att det finns många skäl, och det främsta är att Microsoft själva starkt avråder från Office-automatisering från programvarulösningar: [Överväganden för serverbaserad automatisering av Office](https://support.microsoft.com/sv-se/topic/overvaganden-for-serverbaserad-automatisering-av-office-48bcfe93-8a89-47f1-0bce-017433ad79e2).

Det finns flera skäl till varför Aspose-komponenter är ett bättre alternativ till automatisering. Några av de viktigaste skälen är:

- [Säkerhet](/cells/sv/java/why-not-automation/#security)
- [Stabilitet](/cells/sv/java/why-not-automation/#security)
- [Skalbarhet/Hastighet](/cells/sv/java/why-not-automation/#security)
- [Pris](/cells/sv/java/why-not-automation/#security)
- [Funktioner](/cells/sv/java/why-not-automation/#security)

De viktigaste punkterna beskrivs nedan. Se även till att besöka länkarna längst ner i denna sektion.

{{% /alert %}}

## **Säkerhet**

Följande är en direkt citat från ovan nämnda Microsoft-artikel: *"Office-applikationer var aldrig avsedda att användas på serversidan och tar därför inte hänsyn till de säkerhetsproblem som distribuerade komponenter står inför. Office autentiserar inte inkommande förfrågningar och skyddar dig inte från att oavsiktligt köra makron eller starta en annan server som kan köra makron från din serversidkod. Öppna inte filer som laddas upp till servern från en anonym webbplats! Baserat på de senast inställda säkerhetsinställningarna kan servern köra makron under en administratörs- eller systemkontext med fulla privilegier och kompromettera ditt nätverk! Dessutom använder Office många klientbaserade komponenter (som Simple MAPI, WinInet och MSDAIPP) som kan cachas klientens autentiseringsinformation för att påskynda bearbetningen. Om Office automatiseras på serversidan kan en instans betjäna fler än en klient, och eftersom autentiseringsinformationen har cachats för den sessionen är det möjligt att en klient kan använda de cachade autentiseringsuppgifterna för en annan klient och därigenom få icke-beviljade åtkomstbehörigheter genom att utföra en imitation av andra användare."*

Aspose-produkter är mycket säkra. Aspose-komponenter körs i samma användarkontext som alla ASP.NET-applikationer, under användaren ASPNET. Därför utgör inte Aspose-komponenter någon potentiell risk för viktiga systemresurser. Dessutom körs inte makron automatiskt när en dokument öppnas med en Aspose-komponent. Aspose-komponenter har utvecklats med målet att låta utvecklare skapa, manipulera och spara Office-filer. Inga av de risker som är förknippade med Microsoft Office-paketet är inneboende i Aspose-komponenter.

## **Stabilitet**

Följande är en direkt citat från ovan nämnda Microsoft-artikel: *"Office 2000, Office XP och Office 2003 använder Microsoft Windows Installer (MSI) -teknik för att göra installation och självläkning enklare för en slutanvändare. MSI introducerar konceptet 'installera vid första användningen', vilket gör det möjligt att dynamiskt installera eller konfigurera funktioner vid körning (för systemet eller oftare för en särskild användare). I en serversidanmiljö fördröjer detta både prestandan och ökar sannolikheten för att en dialogruta kan dyka upp som begär att användaren ska godkänna installationen eller ange en lämplig installationsdisk. Även om det är utformat för att öka motståndskraften hos Office som slutanvändarprodukt, är implementationen av MSI-funktioner på serversidan kontraproduktiv. Dessutom kan stabiliteten hos Office i allmänhet inte garanteras när det körs på serversidan eftersom det inte har designats eller testats för denna typ av användning. Att använda Office som en tjänstekomponent på en nätverksserver kan minska stabiliteten hos den datorn och som en följd av detta hela ditt nätverk. Om du planerar att automatisera Office på serversidan ska du försöka isolera programmet till en dedikerad dator som inte kan påverka kritiska funktioner och som kan startas om det behövs."*

Eftersom Aspose-komponenter är packade i en enda DLL kommer det aldrig att finnas behov av att installera några ytterligare delar eller bitar för att de ska fungera. Aspose-komponenter används endast av .NET-applikationer och det finns ingen del av komponentkoden som är konstruerad för att vänta på ett mänskligt svar. Aspose-komponenter har noggrant testats. Aspose-komponenter används av företag som IBM, Hilton, Reader's Digest, Bank of America och många fler.

## **Skalbarhet/Hastighet**

Följande är en direkt citat från ovan nämnda Microsoft-artikel: *"Serversidekomponenter behöver vara höggradigt inmatningsbara, flertrådade COM-komponenter med minimal överhuvud och hög genomströmning för flera klienter. Office-applikationer är i nästan alla avseenden precis motsatsen. De är icke-inmatningsbara, STA-baserade automatiseringsservrar som är utformade för att tillhandahålla varierad men resursintensiv funktionalitet för en enda klient. De erbjuder liten skalbarhet som en serversidelösning och har fixa begränsningar för viktiga element, såsom minne, som inte kan ändras genom konfiguration. Ännu viktigare är att de använder globala resurser (såsom minneskartade filer, globala tillägg eller mallar och delade automatiseringsservrar), vilket kan begränsa antalet instanser som kan köras samtidigt och leda till kapplöpningssituationer om de konfigureras i en flerklientmiljö. Utvecklare som planerar att köra mer än en instans av vilken Office-applikation som helst samtidigt måste överväga att "poola" eller seriellera åtkomst till Office-applikationen för att undvika potentiella låsningar eller datorkorruption."*

Aspose-komponenter är mycket skalbara och blixtsnabba. Kontorsapplikationer var inte avsedda att användas samtidigt av hundratals och tusentals användare; men Aspose-komponenter är utformade just för det. Våra komponenter är en sann .NET-lösning och fungerar felfritt antingen på en enda server som driver en enskild applikation eller på en webbserverfarm med lastbalansering som driver en företagsomfattande applikation.

## **Pris**

När en applikation använder Microsoft Office-automatisering måste en kopia av Microsoft Office köpas för varje maskin som kör applikationen. Det finns många tillfällen då en applikation kanske behöver skapa eller manipulera en kontorsfil men inte kräver att användaren har Office. Aspose erbjuder en mycket kostnadseffektiv, royaltyfri och redistribueringslicens som tillåter distribution till ett obegränsat antal användare utan några licensproblem.

När du skapar webbaserade applikationer är det viktigt att veta att Microsoft Office-automatiseringskomponenter inte är prissatta eller licensierade för serversidans lösningar; därför finns ingen bra licensieringslösning för att distribuera webbapplikationer som använder Microsoft Office-komponenter. Aspose erbjuder en mycket kostnadseffektiv lösning även för serversidan.

## **Funktioner**

Aspose-komponenter ger allt som behövs för hantering av kontorsfiler, plus mycket mer. De är utformade med filosofin att tillåta utvecklare att uppnå de bästa resultaten med minsta möjliga arbete. Till skillnad från Office-automatisering erbjuder Aspose-komponenter många kraftfulla och tidsbesparande funktioner. Till exempel erbjuder [Aspose.Cells](https://products.aspose.com/cells/java/) utvecklare möjligheten att exportera från en **DataTable** eller **DataView** direkt till en Excelfil. [Varje komponent](https://products.aspose.com/total/) i Aspose-familjen erbjuder sina egna unika och kraftfulla funktioner.

Den bästa delen av att köpa en Aspose-komponent eller en komponentsvit är tillgången till våra utvecklingsteam. Våra utvecklingsteam inser att om det är en funktion som ditt företag behöver kommer med största sannolikhet andra företag att behöva det också. Även om inte varje funktionsbegäran kan läggas till, försöker våra team att vara mycket öppensinnade och flexibla när de ger assistans. Den tankegången är det som har hjälpt Aspose-komponenter att bli så kraftfulla som de är. Om det finns ytterligare funktioner som du behöver från Office-automatiseringsobjekt är dina chanser att få dem tillagda mycket, mycket låga.

## **Slutsats**

{{% alert color="primary" %}}

Den här artikeln har täckt de viktigaste punkterna om varför Aspose-komponenter är ett bättre val än Office-automatisering. Alla olika Aspose-komponenter erbjuder en riskfri, icke-bindande [utvärderingsversion](https://products.aspose.com/total/). Vi uppmanar dig att dra nytta av den utvärderingen för att bättre se vad Aspose kan göra för dina applikationer.

För mer information, se följande internetartiklar:

- [Överväganden för Serversidans Automatisering av Office](https://support.microsoft.com/en-us/topic/considerations-for-server-side-automation-of-office-48bcfe93-8a89-47f1-0bce-017433ad79e2)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
