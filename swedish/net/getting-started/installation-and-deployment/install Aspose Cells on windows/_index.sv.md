---
title: Installera Aspose.Cells på Windows
type: docs
weight: 20
url: /sv/net/installing-aspose-cells-on-windows/
---
{{% alert color="primary" %}} 

 Ibland kan du få problem med att installera**Aspose.Cells** med sitt installationspaket (Aspose.Cells.msi...Windows Installer Package) på**Windows Vista** . Detta dokument förklarar hur vi kan hantera det och implementera en framgångsrik installation av komponenten. Faktiskt**Aspose.Cells**installationsprogrammet måste skapa en virtuell mapp på IIS för distributionen av dess webbdemos (Asp.NET Demos) på din dator, så du måste ha administrationsrättigheter innan du installerar**Aspose.Cells** använder dess installationsprogram. Installationsprogrammet kräver åtkomst på administratörsnivå till systemet måste uttryckligen tillåtas att göra det.

{{% /alert %}} 
## **Möjliga faktorer**
 Normalt, i**Windows Vista** , de produkter/komponenter som du installerar/använder implementeras alltid under "normal användare"-behörighet, även om du är en**Administratör** . Programmen tillåts endast begränsad åtkomst till filsystemet, även om du är inloggad som en**Administratör** . Detta har några olyckliga biverkningar som du normalt inte skulle stöta på i Windows XP när du är inloggad som en**Administratör**.
## **UAC (User Account Control)**
**UAC** är en del av**Windows Vista** som ber dig om lov. De**UAC** läge (även känt som**Administratörsgodkännandeläge** ) är ett funktionssätt som (främst) påverkar hur administratörskonton fungerar. När**UAC**är aktiverat (vilket det är som standard), måste du uttryckligen ge tillstånd till alla program som vill använda "administratörsbefogenheter". Alla program som försöker använda administratörsbefogenheter utan din tillåtelse kommer att nekas åtkomst.**UAC** krävs också för andra säkerhetsfunktioner i**Windows Vista** , Inklusive**Skyddat läge** i Internet Explorer. Internet Explorer skyddat läge skyddar din dator från falska webbsidor och andra webbrelaterade sårbarheter, inklusive okända.

 När**UAC** läget är aktiverat, kommer varje program som du kör att ges endast "standardanvändare" åtkomst till systemet, även när du är inloggad som administratör.**Windows Vista** har den inbyggda förmågan att automatiskt minska risken för säkerhetsbrister i systemet. Det gör den genom att automatiskt aktivera den här funktionen som kallas**Användarkontokontroll** (eller**UAC** för korta). De**UAC**tvingar användare som är en del av den lokala administratörsgruppen att köra som om de vore vanliga användare utan administrativa rättigheter. Fastän**UAC** förbättrar tydligt säkerheten på**Windows Vista** , under vissa scenarier kanske du vill inaktivera det, till exempel när du ger demos inför en publik (demos som inte är säkerhetsrelaterade, till exempel). Vissa hemanvändare kan bli frestade att inaktivera**UAC** på grund av användningen av ytterligare resurser i deras system.
## **Involverade steg för framgångsrik installation av komponenten**
-  Se till att IIS är installerat på din Vista innan du installerar**Aspose.Cells** . Det är obligatoriskt pga**Aspose.Cells** installationsprogrammet måste skapa en virtuell mapp på IIS för distributionen av webbdemonerna (Asp.NET Demos).
-  Du måste inaktivera**UAC** (Kontroll av användarkonto). Du måste se till att du har en**Administratörsrättigheter** med full kontroll över systemet innan installation**Aspose.Cells** . Annars kan du få ett fel # 2869 när du installerar**Aspose.Cells**använder dess installationsprogram.

Följande är några sätt att uppnå detta.
### **Använder kommandoraden**
1.  Sök efter cmd.exe i din Windows-katalog, högerklicka sedan på den och välj Kör som...**Administratör**
 2. Kör nu följande kommando på kommandotolken: msiexec /i<your path>/Aspose.Cells.msi och Enter.
### **Använder kontrollpanelen**
- Klicka på Start
- Klicka på Kontrollpanelen
- Klicka på Användarkonton och familjesäkerhet
- Klicka på Användarkonton
- Klicka på Aktivera eller inaktivera kontroll av användarkonto
- Avmarkera kryssrutan
- Klicka på OK

{{% alert color="primary" %}} 

Du måste starta om datorn för att ändringen ska träda i kraft. Denna ändring påverkar alla konton på datorn, inte bara dina.

{{% /alert %}}
