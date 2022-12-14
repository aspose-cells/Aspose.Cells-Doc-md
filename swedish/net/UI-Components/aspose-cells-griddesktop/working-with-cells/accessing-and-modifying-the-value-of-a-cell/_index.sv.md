---
title: Få åtkomst till och ändra värdet på en Cell
type: docs
weight: 20
url: /sv/net/accessing-and-modifying-the-value-of-a-cell/
---
{{% alert color="primary" %}} 

vårt tidigare ämne har vi diskuterat om åtkomst till celler i ett kalkylblad. I det här ämnet kommer vi helt enkelt att utöka det ämnet för att visa utvecklare att hur de kan komma åt och ändra värdena på celler med hjälp av API:et för Aspose.Cells.GridDesktop.

{{% /alert %}} 
## **Få åtkomst till och ändra Cell Värde med Aspose.Cells.GridDesktop**
 Innan vi kommer åt och ändrar värdet på en cell, bör vi veta hur man kommer åt celler. Det finns tre sätt att komma åt celler i ett kalkylblad. För mer information om dessa tre tillvägagångssätt, vänligen[Åtkomst till Cells i ett arbetsblad.](/cells/sv/net/accessing-cells-in-a-worksheet/)

Varje cell har en egenskap som heter Value . Så när en cell väl har nåtts kan utvecklare komma åt och ändra innehållet i egenskapen Value för att komma åt och ändra värdet på en cell.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingValue.cs" >}}


**VIKTIG:**Att använda Value-egenskapen för en cell för att ändra dess värde är ett bra tillvägagångssätt för att ställa in värdet för en enstaka eller få celler. Om du behöver ställa in värdena för många celler så skulle prestandan för detta tillvägagångssätt inte vara bra. Så, för att ställa in värdena för många celler, bör du använda**SetCellValue** cellens metod för att förbättra prestandan för dina applikationer. En modifierad version av ovanstående kodavsnitt som använder**SetCellValue** metoden visas nedan.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingSetCellValue.cs" >}}
