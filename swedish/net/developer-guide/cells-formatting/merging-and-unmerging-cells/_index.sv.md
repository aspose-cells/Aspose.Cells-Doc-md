---
title: Sammanfogning och upphävande Cells
description: Aspose.Cells är ett .NET-bibliotek för att arbeta med kalkylarksfiler, som stöder sammanfogning och upphävande av celler. Den här artikeln kommer att introducera hur man sammanfogar och tar bort celler med hjälp av Aspose.Cells-biblioteket, och hur man anpassar den sammanslagna cellstilen.
keywords: Aspose.Cells, NET library, spreadsheet, merge cells, unmerge cells, style settings, custom styles
type: docs
weight: 190
url: /sv/net/merging-and-unmerging-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells stöder den här funktionen och kan även slå samman celler i ett kalkylblad. Du kan ta bort sammanslagningen eller dela de sammanslagna cellerna också. En sammanslagen cells cellreferens är referensen för den övre vänstra cellen i det ursprungliga valda området.

{{% /alert %}} 
##  **Introduktion**
Du vill inte alltid ha samma antal celler i varje rad eller kolumn. Du kanske till exempel vill sätta en titel i en cell som sträcker sig över flera kolumner. Eller, om du skapar en faktura, kanske du vill ha färre kolumner för summan. För att göra en cell från två eller flera celler, slå samman dem. Microsoft Excel låter användare välja filer och slå samman dem för att strukturera kalkylarket som de vill.

{{% alert color="primary" %}} 

Observera att när celler slås samman behålls endast data i de övre vänstra cellerna. Om det finns data i de andra cellerna i området raderas denna data.
Formatering baseras på samma sätt på referenscellen så att när du slår samman celler tillämpas formateringsinställningarna för den övre vänstra cellen i intervallet på den sammanslagna cellen. När cellen delas upp behåller de nya cellerna sina ursprungliga formatinställningar.

{{% /alert %}} 
##  **Slår samman Cells i ett arbetsblad**
###  **Slår ihop Cells i Microsoft Excel**
Följande steg beskriver hur du slår samman celler i kalkylbladet med MS Excel.

1. Kopiera de data du vill ha till den övre vänstra cellen inom intervallet.
1. Välj de celler du vill slå samman.
1.  Klicka på för att slå samman celler i en rad eller kolumn och centrera cellinnehållet**Slå samman och centrera** ikonen på**Formatering** verktygsfältet.
###  **Slår ihop Cells med Aspose.Cells**
Klassen Aspose.Cells.Cells har några användbara metoder för uppgiften. Till exempel slår metoden Merge() samman cellerna till en enda cell inom ett specificerat intervall.

Följande exempel visar hur man slår samman celler (C6:E7) i ett kalkylblad.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}
##  **Avsluta (delning) Sammanfogad Cells**
###  **Använder Microsoft Excel**
Följande steg beskriver hur man delar upp sammanslagna celler med Microsoft Excel.

1. Välj den sammanslagna cellen.
 När cellerna har kombinerats,**Slå samman och centrera** väljs på**Formatering** verktygsfältet.
1.  Klick**Slå samman och centrera** på**Formatering** verktygsfältet.
###  **Använder Aspose.Cells**
Klassen Aspose.Cells.Cells har en metod som heter UnMerge() som delar upp cellerna till deras ursprungliga tillstånd. Metoden tar bort sammanslagningen av cellerna med hjälp av cellens referens i det sammanslagna cellområdet.

Följande exempel visar hur man delar de sammanslagna cellerna (C6). Exemplet använder filen som skapades i föregående exempel och delar upp de sammanslagna cellerna.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-UnMergingtheMergedCells-1.cs" >}}


##  **Förhandsämnen**
- [Identifiera sammanslagna Cells i ett kalkylblad](/cells/sv/net/detect-merged-cells-in-a-worksheet/)
