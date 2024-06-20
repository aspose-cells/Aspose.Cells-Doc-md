---
title: Åtkomst och ändring av värdet på en cell
type: docs
weight: 20
url: /sv/net/aspose-cells-griddesktop/accessing-and-modifying-the-value-of-a-cell/
keywords: GridDesktop,cell,modify cell,get cell,modify cell value,get cell value
description: Denna artikel introducerar hur man får och modifierar cellvärdet i GridDesktop.
---

{{% alert color="primary" %}} 

I vårt tidigare ämne har vi diskuterat om åtkomst till celler i ett arbetsblad. I det här ämnet kommer vi helt enkelt att utöka det ämnet för att visa utvecklare hur de kan få åtkomst till och ändra värdena på celler med hjälp av Aspose.Cells.GridDesktops API.

{{% /alert %}} 
## **Åtkomst och ändring av cellvärde med hjälp av Aspose.Cells.GridDesktop**
Innan du får åtkomst till och ändrar värdet på en cell bör vi veta hur man får åtkomst till celler. Det finns tre tillvägagångssätt för att få åtkomst till celler i ett arbetsblad. För mer information om dessa tre tillvägagångssätt, vänligen [Åtkomst till celler i ett arbetsblad.](/cells/sv/net/accessing-cells-in-a-worksheet/)

Varje cell har en egenskap med namnet Värde. Så när en cell har fått åtkomst kan utvecklare få åtkomst till och ändra innehållet i Värde-egenskapen för att få åtkomst till och ändra värdet på en cell.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingValue.cs" >}}


**Viktigt:** Att använda cellens Värde-egenskap för att ändra dess värde är ett bra tillvägagångssätt för att ställa in värdet på en eller ett fåtal celler. Om du behöver ställa in värdena på många celler kommer prestandan för detta tillvägagångssätt inte att vara bra. Så för att ställa in värdena på många celler bör du använda cellens **SetCellValue**-metod för att förbättra prestandan i dina applikationer. En modifierad version av ovanstående kodsnutt med **SetCellValue**-metoden visas nedan.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingSetCellValue.cs" >}}
