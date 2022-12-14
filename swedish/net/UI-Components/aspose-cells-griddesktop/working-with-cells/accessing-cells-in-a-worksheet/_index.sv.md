---
title: Åtkomst till Cells i ett arbetsblad
type: docs
weight: 10
url: /sv/net/accessing-cells-in-a-worksheet/
---
{{% alert color="primary" %}} 

Vi har diskuterat om att arbeta med kalkylblad, rader och kolumner hittills men det är dags att gå djupare och prata om celler. Så i det här ämnet skulle vi börja vår diskussion om celler med en grundläggande funktion för att komma åt celler.

{{% /alert %}} 
## **Åtkomst till Cells i ett arbetsblad**
Vi kan komma åt vilken cell som helst i ett kalkylblad med API:et Aspose.Cells.GridDesktop. Det kan finnas tre möjliga sätt att komma åt celler enligt följande:

- **Använder Cell Namn**
- **Använder Cell:s rad- och kolumnindex**
- **Fokusera Cell**

Låt oss diskutera alla ovanstående tre tillvägagångssätt en efter en.
### **Använder Cell Namn**
 Alla celler i ett kalkylblad har ett unikt namn. Till exempel A1, A2, B1, B2 etc. Aspose.Cells.GridDesktop tillåter utvecklare att komma åt vilken cell som helst genom att använda dess cellnamn. Allt vi behöver göra är att bara skicka cellnamnet (som ett index) till**Cells** samling av**Arbetsblad**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByName.cs" >}}
### **Använder Cell:s rad- och kolumnindex**
 En cell i ett kalkylblad kan också kännas igen med hjälp av dess plats i termer av dess rad- och kolumnindex. Allt vi behöver göra är att bara skicka cellens rad- och kolumnindex till cellen**Cells** samling av**Arbetsblad**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByIndices.cs" >}}
### **Fokusera Cell**
 Om du inte vet exakt vad vilken cell ska nås. Då låter Aspose.Cells.GridDesktop dig också komma åt en cell som för närvarande är i fokus för en användare. Med den här funktionen kan du tillåta en användare att välja valfri cell och sedan kan du komma åt den cellen i backend. Det kan helt enkelt uppnås genom att använda**GetFocusedCell** metod för**Arbetsblad**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessFocusedCell.cs" >}}
