---
title: Lägger till formler till Cells
type: docs
weight: 30
url: /sv/net/adding-formulas-to-cells/
---
{{% alert color="primary" %}} 

En cell kan inte bara innehålla ett enkelt värde som en numerisk figur eller någon text utan vi kan också infoga en formel i en cell som dess värde. En formel används i en cell när värdet på en cell måste bestämmas efter vissa beräkningar. I det här ämnet kommer vi att diskutera hur vi kan komma åt och ändra en formel som tillämpas på en cell.

{{% /alert %}} 
## **Lägger till formel till en Cell**
 Att lägga till formel till en cell är precis som att ställa in värdet på en cell som vi har diskuterat i vårt tidigare ämne:[Få åtkomst till och ändra värdet på en Cell](/cells/sv/net/accessing-and-modifying-the-value-of-a-cell/) förutom att i så fall lade vi bara till enkla värden till celler. Nu kommer vi att lägga till formler. Utvecklare kan använda värdeegenskapen för en cell för att komma åt och ändra formeln eller på annat sätt**SetCellValue** metoden för cellen kan också användas för att lägga till eller ändra formeln i en cell.

**VIKTIG:** Den grundläggande skillnaden mellan att använda Value-egenskapen eller**SetCellValue** metoden för en cell är att egenskapen Value anropar**Kör Alla Formler** metod för Grid automatiskt för att räkna om värdena för alla formler där som i fallet med**SetCellValue** metodutvecklare måste ringa**Kör Alla Formler** metod explicit efter att formlerna har lagts till i celler. Faktiskt, när vi använder**SetCellValue** metod för en cell så ställer den här metoden värdet på cellen till**FormelTyp** bara och beräkna inte formeln. Dessutom ringer**Kör Alla Formler**metod varje gång är inte nödvändigt. Om du vill lägga till många formler i cellerna i ett kalkylblad kan du ringa**Kör Alla Formler** metod bara en gång i slutet.

 En formel läggs till i en cell som ett strängvärde. Dessutom måste formelstrukturen vara kompatibel med formelstrukturen i MS Excel. Alla formler måste börja med en**Lika tecken (=)**.

 I exemplet nedan har vi lagt till en formel för att multiplicera värdena för två celler i kalkylbladet och lagra resultatet i en annan cell.**Kör Alla Formler** metoden åberopas också i slutet.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddingCellFormulas-1.cs" >}}



Kör nu applikationen. Om du dubbelklickar på cellen där formeln lades till skulle du märka att värdet kommer att ersättas av formeln som faktiskt beräknar värdet på back-end.

{{% alert color="primary" %}} 

 Aspose.Cells.GridDesktop stöder de flesta av de vanligaste funktionerna i MS Excel. För mer information om listan över funktioner som stöds, vänligen[Klicka här.](/cells/sv/net/list-of-supported-functions/)

{{% /alert %}}
