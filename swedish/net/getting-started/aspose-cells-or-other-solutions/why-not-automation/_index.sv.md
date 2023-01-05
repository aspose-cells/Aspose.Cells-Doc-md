---
title: Varför inte automatisering
type: docs
weight: 50
url: /sv/net/why-not-automation/
---
{{% alert color="primary" %}}

Varför är Aspose-komponenter ett mycket bättre alternativ än Microsoft Office Automation?*

{{% /alert %}}

## **Introduktion**

Det är två frågor som vi hör oftast här på Aspose:

1. **Kräver dina produkter att Microsoft Office är installerat för att de ska kunna köras?**
 Det enkla svaret är nej. Aspose komponenter är helt oberoende och är inte anslutna till, inte heller auktoriserade, sponsrade eller på annat sätt godkända av Microsoft Corporation.
1. **Varför ska vi använda Aspose-produkter istället för att använda Microsoft Office-automation?**
 Det kortaste svaret vi kan ge är att det finns många anledningar, där den främsta är att Microsoft själva starkt rekommenderar Office-automatisering från mjukvarulösningar:[Överväganden för automatisering av Office på serversidan](https://support.microsoft.com/en-us/topic/considerations-for-server-side-automation-of-office-48bcfe93-8a89-47f1-0bce-017433ad79e2).

Det finns flera anledningar till varför Aspose komponenter är ett bättre alternativ till automation. Några av de viktigaste skälen är:

- säkerhet
- Stabilitet
- Skalbarhet/hastighet
- Pris
- Funktioner

De viktigaste punkterna beskrivs nedan. Se också till att besöka länkarna i slutet av det här avsnittet.

### **säkerhet**

Följande är ett direkt citat från den ovan refererade artikeln Microsoft:

*"Office Applications var aldrig avsedda att användas på serversidan och tar därför inte hänsyn till säkerhetsproblemen som distribuerade komponenter möter. Office autentiserar inte inkommande förfrågningar och skyddar dig inte från att oavsiktligt köra makron eller starta en annan server som kan köra makron, från din kod på serversidan. Öppna inte filer som laddas upp till servern från en anonym webbsida! Baserat på säkerhetsinställningarna som sattes senast, kan servern köra makron under en administratörs- eller systemkontext med fulla privilegier och äventyra ditt nätverk! Dessutom använder Office många komponenter på klientsidan (som Simple MAPI, WinInet och MSDAIPP) som kan cachelagra klientautentiseringsinformation för att påskynda bearbetningen. Om Office automatiseras på serversidan , kan en instans betjäna mer än en klient, och eftersom autentiseringsinformation har cachelagrats för den sessionen är det möjligt att en klient kan använda cachen d autentiseringsuppgifter för en annan klient och därigenom få icke-beviljade åtkomstbehörigheter genom att utge sig för andra användare."*

Aspose produkter är mycket säkra. Aspose-komponenter körs i samma användarkontext som alla ASP.NET-applikationer, under ASPNET-användaren. Därför utgör Aspose komponenter inte en potentiell risk för viktiga systemresurser. Dessutom, när ett dokument öppnas av en Aspose-komponent, körs makron inte automatiskt. Aspose-komponenter byggdes med målet att tillåta utvecklare att skapa, manipulera och spara Office-filer. Ingen av riskerna med Microsoft Office-paketet är inneboende i Aspose komponenter.

### **Stabilitet**

Följande är ett direkt citat från den ovan refererade artikeln Microsoft:

*"Office 2000, Office XP och Office 2003 använder Microsoft Windows Installer-teknik (MSI) för att göra installation och självreparation enklare för en slutanvändare. MSI introducerar konceptet "installera vid första användning", vilket gör att funktionerna kan vara dynamiska installeras eller konfigureras under körning (för systemet, eller oftare för en viss användare). I en miljö på serversidan saktar detta både ned prestanda och ökar sannolikheten för att en dialogruta kan visas som ber användaren att godkänna installationen eller tillhandahålla en lämplig installationsskiva. Även om den är utformad för att öka kontorets motståndskraft som en slutanvändarprodukt, är kontorets implementering av MSI-funktioner kontraproduktiv i en miljö på serversidan. Dessutom är kontorets stabilitet i allmänhet , kan inte garanteras när du kör serversidan eftersom den inte har designats eller testats för denna typ av användning. Att använda Office som en tjänstkomponent på en nätverksserver kan minska stabiliteten för den maskinen och en är en följd av ditt nätverk som helhet. Om du planerar att automatisera Office-serversidan, försök att isolera programmet till en dedikerad dator som inte kan påverka viktiga funktioner och som kan startas om vid behov."*

Eftersom Aspose-komponenter är paketerade i en enda DLL, kommer det aldrig att finnas ett behov av att installera några ytterligare delar eller delar för att de ska fungera. Aspose-komponenter används endast av .NET-applikationer och det finns ingen del av komponentkoden utformad för att vänta på ett mänskligt svar. Aspose komponenter har testats noggrant. Aspose komponenter används av företag som IBM, Hilton, Reader's Digest, Bank of America och många fler.

### **Skalbarhet/hastighet**

Följande är ett direkt citat från den ovan refererade artikeln Microsoft:

*"Serversidans komponenter måste vara mycket återkommande, flertrådiga COM-komponenter med minimal overhead och hög genomströmning för flera klienter. Office-applikationer är i nästan alla avseenden raka motsatsen. De är icke-återkommande, STA-baserade automationsservrar som är designade för att tillhandahålla mångsidig men resurskrävande funktionalitet för en enskild klient. De erbjuder liten skalbarhet som en lösning på serversidan och har fasta gränser för viktiga element, som minne, som inte kan ändras genom konfiguration. Ännu viktigare är att de använder globala resurser (såsom minneskartade filer, globala tillägg eller mallar och delade automationsservrar), vilket kan begränsa antalet instanser som kan köras samtidigt och leda till tävlingsförhållanden om de är konfigurerade i en multiklientmiljö. planerar att köra mer än en instans av en Office-applikation samtidigt måste överväga att "poola" eller serialisera åtkomst till Office-applikationen för att undvika potentiella döda lås eller datakorruption."*

Aspose komponenter är mycket skalbara och blixtsnabba. Office-program var inte designade för att användas samtidigt av hundratals och tusentals användare; dock är Aspose komponenter designade för just detta. Våra komponenter är en äkta .NET-lösning och fungerar felfritt oavsett om det är på en enda server som driver en enda applikation eller på en belastningsbalanserad webbfarm som driver en företagsomfattande applikation.

### **Pris**

 När ett program använder Microsoft Office automation måste en kopia av Microsoft Office köpas för varje maskin som kör programmet. Det finns många gånger som ett program kan behöva skapa eller manipulera en Office-fil men kräver inte att användaren har Office. Aspose erbjuder en mycket[kostnadseffektiv](https://purchase.aspose.com/buy), royaltyfri, omfördelningslicens som tillåter distribution till ett obegränsat antal användare utan licensbekymmer.

När du skapar webbaserade applikationer är det viktigt att veta att Microsoft Office automation komponenter inte är prissatta eller licensierade för server-side lösningar ([Licensiering av Office 2000 Web Components och Office Server Extensions](#)); därför finns det ingen bra licenslösning för att distribuera webbapplikationer som använder Microsoft Office-komponenterna. Aspose erbjuder en mycket kostnadseffektiv lösning även för serverbaserade applikationer.

### **Funktioner**

 Aspose-komponenter tillhandahåller allt som behövs för att hantera Office-filer, plus mycket, mycket mer. De är designade med filosofin att tillåta utvecklare att uppnå de bästa resultaten med minsta möjliga arbete. Till skillnad från Office-automation ger Aspose-komponenter många kraftfulla, tidsbesparande funktioner. Till exempel,[Aspose.Cells](https://products.aspose.com/cells/) erbjuder utvecklare möjligheten att exportera från en**Datatabell** eller**DataView** direkt till en Excel-fil.[Aspose.Words](https://products.aspose.com/words/)erbjuder en liknande funktion som gör det möjligt för utvecklare att fylla i ett dokument för koppling av Word direkt från vilket .NET-dataobjekt som helst.[Varje komponent](https://products.aspose.com/total/) i Aspose-familjen erbjuder sin egen uppsättning unika, kraftfulla funktioner.

Det bästa med att köpa en Aspose-komponent eller en komponentsvit är att ha tillgång till våra utvecklingsteam. Våra utvecklingsteam inser att om det finns en funktion som ditt företag behöver, är det mer än troligt att andra företag kommer att behöva det också. Även om inte alla funktionsförfrågningar kan läggas till, försöker våra team att vara väldigt öppna och flexibla när de tillhandahåller hjälp. Det tänkesättet är det som har hjälpt Aspose komponenter att bli lika kraftfulla som de är. Om det finns ytterligare funktioner som du behöver från Office-automationsobjekt, är dina chanser att lägga till dem mycket, mycket låga.

## **Slutsats**

{{% alert color="primary" %}}

 Den här artikeln har tagit upp nyckelpunkterna om varför Aspose-komponenter är ett bättre val än Office-automation. Alla de olika Aspose komponenterna erbjuder en riskfri, ingen förpliktelse[utvärderingsversion](https://downloads.aspose.com/total). Vi uppmuntrar dig att dra nytta av den utvärderingen för att bättre se vad Aspose kan göra för dina ansökningar.


{{% /alert %}}
