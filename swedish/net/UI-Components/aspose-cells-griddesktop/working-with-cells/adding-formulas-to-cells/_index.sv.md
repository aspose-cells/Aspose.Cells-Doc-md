---
title: Lägg till formel i cell
type: docs
weight: 30
url: /sv/net/aspose-cells-griddesktop/adding-formula-to-cell/
keywords: GridDesktop, formel
description: Den här artikeln introducerar hur man hämtar eller anger en formel i cellen i kalkylarket i GridDesktop.
---

{{% alert color="primary" %}} 

En cell kan innehålla inte bara ett enkelt värde som en numerisk figur eller någon text, utan också en formel som dess värde. En formel används i en cell när cellens värde behöver bestämmas efter några beräkningar. I det här avsnittet kommer vi att diskutera hur man kommer åt och modifierar en formel som tillämpas på en cell.

{{% /alert %}} 
## **Lägg till formel i en cell**
Att lägga till formel i en cell är precis som att ställa in värdet av en cell som vi har diskuterat i vårt tidigare ämne: [Åtkomst och ändring av värdet för en cell](/cells/sv/net/accessing-and-modifying-the-value-of-a-cell/) förutom att i det fallet lade vi till enkla värden till celler. Nu kommer vi att lägga till formler. Utvecklare kan använda värdet av en cell för att komma åt och modifiera formeln eller så kan också **SetCellValue**-metoden för cellen användas för att lägga till eller ändra formeln i en cell.

**VIKTIGT:** Den grundläggande skillnaden mellan att använda värdet motsatt **SetCellValue**-metoden för en cell är att värdet använder **RunAllFormulas**-metoden av Grid automatiskt för att omberäkna värdena för alla formler där som i fallet med **SetCellValue**-metoden måste utvecklare ringa **RunAllFormulas**-metoden explicit efter att formlerna har lagts till cellerna. Faktum är att när vi använder **SetCellValue**-metoden för en cell, ställer denna metod värdet för cellen till endast **FormulaType** och beräknar inte formeln. Dessutom är det inte nödvändigt att alltid ringa **RunAllFormulas**-metoden. Om du vill lägga till många formler i cellerna i ett kalkylblad kan du ringa **RunAllFormulas**-metoden bara en gång i slutet.

En formel läggs till en cell som en strängvärde. Dessutom måste formelstrukturen vara kompatibel med formelstrukturen i MS Excel. Alla formler måste börja med ett **lika med-tecken (=)**.

I exemplet nedan har vi lagt till en formel för att multiplicera värdena av två celler i kalkylarket och lagra resultatet i en annan cell. **RunAllFormulas**-metoden kallas också i slutet.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddingCellFormulas-1.cs" >}}



Kör nu applikationen. Om du dubbelklickar på cellen där formeln lades till kommer du att märka att värdet ersätts av formeln som faktiskt beräknar värdet på backend.

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop stöder de flesta av de vanligt använda funktionerna i MS Excel. För mer information om listan över stödda funktioner, vänligen [klicka här.](/cells/sv/net/list-of-supported-functions/)

{{% /alert %}}
