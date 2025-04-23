---
title: Installera Aspose.Cells på Windows
type: docs
weight: 20
url: /sv/net/installing-aspose-cells-on-windows/
---

{{% alert color="primary" %}} 

Ibland kan du stöta på problem med att installera **Aspose.Cells** med dess installationspaket (Aspose.Cells.msi ... Windows Installer Package) på **Windows Vista**. Det här dokumentet förklarar hur vi kan hantera det och implementera den framgångsrika installationen av komponenten. Faktum är att **Aspose.Cells**-installationspaketet behöver skapa en virtuell mapp på IIS för distribution av sina webbdemor (Asp.NET-Demor) på din maskin, så du behöver ha administratörsprivilegier innan du installerar **Aspose.Cells** med dess installationsprogram. Installationsprogrammet kräver administratörstillgång till systemet måste uttryckligen tillåtas att göra det.

{{% /alert %}} 
## **Möjliga faktorer**
Normalt implementeras produkter/komponenter som du installerar/använder i **Windows Vista** alltid under "normal användar"-behörigheter, även om du är **administratör**. Programmen har endast begränsad åtkomst till filsystemet, även om du är inloggad som **administratör**. Detta har vissa olyckliga bieffekter som du normalt inte skulle stöta på i Windows XP när du är inloggad som **administratör**.
## **UAC (User Account Control)**
**UAC** är en del av **Windows Vista** som frågar dig om tillstånd. **UAC**-läget (även känt som **Administratörsbehörighetsläge**) är ett driftläge som (främst) påverkar sättet som administratörskonton fungerar. När **UAC** är aktiverat (vilket det är som standard), måste du uttryckligen ge tillstånd till varje program som vill använda "administratörs"-behörigheter. Ett program som försöker använda administratörsbehörigheter utan ditt tillstånd kommer att nekas åtkomst. **UAC** krävs också för andra säkerhetsfunktioner i **Windows Vista**, inklusive **Skyddat läge** i Internet Explorer. Internet Explorer Skyddat läge skyddar din dator från skadliga webbsidor och andra webbrelaterade sårbarheter, inklusive okända.

När **UAC**-läget är aktiverat kommer varje program som du kör att ges endast "standardanvändar"-åtkomst till systemet, även när du är inloggad som administratör. **Windows Vista** har inbyggd förmåga att automatiskt minska potentiella säkerhetsluckor i systemet. Det gör det genom att automatiskt aktivera den här funktionen som kallas **User Account Control** (eller **UAC** för kort). **UAC** tvingar användare som är en del av den lokala administratörsgruppen att köra som om de vore vanliga användare utan administrativa privilegier. Även om **UAC** tydligt förbättrar säkerheten på **Windows Vista**, kanske du under vissa scenarier vill inaktivera det, till exempel när du ger demonstrationer inför en publik (demonstrationer som inte är säkerhetsrelaterade, till exempel). Vissa hemanvändare kan vara frestade att inaktivera **UAC** på grund av användningen av ytterligare resurser på deras system.
## **Steg som krävs för en framgångsrik installation av komponenten**
- Se till att IIS är installerat på din Vista innan du installerar **Aspose.Cells**. Det är obligatoriskt eftersom **Aspose.Cells** -installatören behöver skapa en virtuell mapp på IIS för distribution av webbdemon (Asp.NET-demonstrationer).
- Du måste inaktivera **UAC** (användarkontokontroll). Du måste se till att du har **Administratörsprivilegier** med full kontroll över systemet innan du installerar **Aspose.Cells**. Annars kan du få ett fel # 2869 medan du installerar **Aspose.Cells** med dess installerare.

Här är några sätt att uppnå detta.
### **Använda kommandoraden**
1. Sök efter cmd.exe i din Windows-katalog, högerklicka sedan på den och välj Kör som... **Administratör**
2. Now, Run the following command on command prompt: msiexec /i <your path>/Aspose.Cells.msi and Enter.
### **Använda Kontrollpanelen**
- Klicka på Start
- Klicka på Kontrollpanelen
- Klicka på Användarkonton och familjesäkerhet
- Klicka på Användarkonton
- Klicka på Vänd användarkontroll på eller av
- Avmarkera kryssrutan
- Klicka på OK

{{% alert color="primary" %}} 

Du behöver starta om din dator för att ändringen ska träda i kraft. Denna ändring påverkar alla konton på datorn, inte bara ditt.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
