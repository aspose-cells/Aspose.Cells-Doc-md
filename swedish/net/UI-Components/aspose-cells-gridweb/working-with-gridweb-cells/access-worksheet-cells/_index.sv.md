---
title: Åtkomst till arbetsblad Cells
type: docs
weight: 10
url: /sv/net/access-worksheet-cells/
---
{{% alert color="primary" %}} 

Det här ämnet diskuterar celler och tittar på Aspose.Cells.GridWebs mest grundläggande funktion: åtkomst till celler.

{{% /alert %}} 
## **Åtkomst till Cells i ett arbetsblad**
Varje kalkylblad innehåller en egenskap med namnet Cells som faktiskt är en samling GridCell-objekt där ett GridCell-objekt representerar en cell i Aspose.Cells.GridWeb. Det är möjligt att komma åt vilken cell som helst med Aspose.Cells.GridWeb. Det finns två föredragna metoder, som var och en diskuteras nedan.


### **Använder Cell Namn**
Alla celler har ett unikt namn. Till exempel A1, A2, B1, B2 etc. Aspose.Cells.GridWeb tillåter utvecklare att komma åt vilken cell som helst genom att använda cellnamnet. Skicka helt enkelt cellnamnet (som ett index) till samlingen Cells i GridWorksheet.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByName.cs" >}}


### **Använda rad- och kolumnindex**
En cell kan också kännas igen på sin plats i termer av rad- och kolumnindex. Skicka bara en cells rad- och kolumnindex till Cells-samlingen i GridWorksheet. Detta tillvägagångssätt är snabbare än ovanstående.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByRowColumnIndex.cs" >}}
