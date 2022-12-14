---
title: Applicera stilar på Cells
type: docs
weight: 50
url: /sv/net/applying-styles-on-cells/
---
{{% alert color="primary" %}} 

Det här ämnet handlar om att tillämpa stilar på celler, så vi kommer att försöka täcka nästan allt som kan användas för att tillämpa stil på en cell. Förutom några grundläggande formateringsinställningar kommer vi också att diskutera hur man ritar gränser och ställer in talformat för celler i detalj.

{{% /alert %}} 
## **Tillämpa en anpassad stil på en Cell - ett exempel**
För att ändra teckensnitt och färg på en cell med Aspose.Cells.GridDesktop, följ stegen nedan:

-  Få åtkomst till alla önskade**Arbetsblad**
-  Tillgång a**Cell** på vilken vi vill tillämpa en**Stil**
-  Skaffa sig**Stil** av**Cell**
-  Uppsättning**Stil** egenskaper enligt dina anpassade behov
-  Slutligen, ställ in**Stil** av**Cell** med den uppdaterade

 Det finns många användbara egenskaper och metoder som erbjuds av**Stil** objekt som kan användas av utvecklare för att anpassa stilen efter deras krav. I koden nedan visas hur man tillämpar anpassad stil på cellen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-ApplyStyle.cs" >}}
## **Rita gränser för Cells**
 Använder sig av**Stil**objekt, kan vi rita gränser för en cell mycket enkelt. Kanterna kan ritas i valfri färg. Dessutom har utvecklare också flexibiliteten att välja en specifik typ av linje som kommer att användas för att rita gränser runt cellen. Utvecklare kan använda**SetBorderLine** och**SetBorderColor** metoder för**Stil** objekt för att rita kanter av valfri typ och färg. På samma sätt, för att få gränsinformation för vilken cell som helst, kan utvecklare också använda sig av**GetBorderLine** och**GetBorderColor** metoder för**Stil** objekt.
### **Typer av gränser**
Det finns sex typer av gränser som stöds av Aspose.Cells.GridDesktop enligt följande:

- **Vänster** , representerar vänster kant
- **Höger** , representerar höger kant
- **Topp** , representerar övre kant
- **Botten** , representerar den nedre kanten
- **DiagonalDown** , representerar diagonal nedåtkant
- **DiagonalUp** , representerar diagonalt upp kant
### **Typer av gränslinjer**
En kant är sammansatt av en linje. Genom att ändra typ av linje, ändrar utseendet på en kant. Det finns många typer av gränslinjer som stöds av Aspose.Cells.GridDesktop, som också listas nedan:

- **Ingen** , representerar ingen gräns
- **Tunn** , representerar heldragen gräns
- **Medium** , representerar heldragen linjekant med linjebredd lika med 2f
- **Streckad** , representerar en streckad linjekant
- **Prickad** , representerar en streckad linjekant
- **Tjock** , representerar heldragen linjekant med linjebredd lika med 3f
- **Medelstreckad** , representerar streckad linjekant med linjebredd lika med 2f
- **ThinDashDotted** , representerar streckprickad kantlinje
- **MediumDashPrickad** , representerar streckad streckad linjekant med linjebredd lika med 2f
- **ThinDashDotDotted** , representerar en streckad prickad linjekant
- **MediumDashDotDotted** , representerar streckad prickad linjekant med linjebredden lika med 2f
## **Summering All Together - Exempel**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SummingUp.cs" >}}
## **Ställa in talformat**
Aspose.Cells.GridDesktop har också en stark funktion för att ställa in talformat för de värden som skrivs in i celler. Det finns 58 inbyggda nummerformat som erbjuds av Aspose.Cells.GridDesktop. För att se en komplett lista över alla talformat som stöds, se[Talformat som stöds.](/cells/sv/net/list-of-supported-number-formats/)

 Alla inbyggda talformat är tilldelade en**Index** siffra.**Till exempel** de**Index** antal**0,00E+00** nummerformat är**11** . För att använda ett inbyggt talformat i valfri cell kan utvecklare ställa in NumberFormat-egenskapen för**Stil** invända mot**Index** nummer för det specifika talformatet. Men om utvecklare behöver ha sitt eget anpassade nummerformat kan de också använda Custom-egenskapen för**Stil** objekt.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SetNumberFormat.cs" >}}
