---
title: Sammanfoga och dela upp celler
description: Aspose.Cells är ett .NET bibliotek för att arbeta med kalkylbladsfiler, vilket stöder sammanslagning och uppdelning av celler. Denna artikel kommer att introducera hur man sammanslår och delar upp celler med hjälp av Aspose.Cells biblioteket, och hur man anpassar sammanslagna cellers stil.
keywords: Aspose.Cells, .NET bibliotek, kalkylblad, sammanslagning av celler, uppdelning av celler, stilmallar, anpassade stilar
type: docs
weight: 190
url: /sv/net/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells stöder den här funktionen och kan också sammanslå celler i ett kalkylblad. Du kan också dela upp eller splittra de sammanslagna cellerna. En sammanslagen cells cellreferens är referensen för den översta vänstra cellen i det ursprungliga markerade området.

{{% /alert %}} 
## **Introduktion**
Du vill inte alltid ha samma antal celler i varje rad eller kolumn. Till exempel kan du vilja lägga en titel i en cell som spänner över flera kolumner. Eller om du skapar en faktura kan du vilja ha färre kolumner för den totala summan. För att göra en cell från två eller flera celler, sammanslag dem. Microsoft Excel låter användare välja filer och sammanfoga dem för att strukturera kalkylbladet på önskat sätt.

{{% alert color="primary" %}} 

Observera att när celler sammanslås behålls endast data i de översta vänstra cellerna. Om det finns data i de andra cellerna i området raderas denna data.
Formatering är också baserad på referenscellen så att när du sammanslår celler tillämpas formateringsinställningarna för den översta vänstra cellen i området på den sammanslagna cellen. När cellen splittas behåller de nya cellerna sina ursprungliga formateringsinställningar.

{{% /alert %}} 
## **Sammanslagning av celler i ett kalkylblad**
### **Sammanslagning av celler i Microsoft Excel**
Följande steg beskriver hur man sammanslår celler i kalkylbladet med hjälp av MS Excel.

1. Kopiera den data du vill ha till den övre vänstra cellen inom området.
1. Välj cellerna du vill sammanfoga.
1. För att sammanfoga celler i en rad eller kolumn och centrera cellinnehållet klickar du på ikonen **Sammanfoga och centrerat** på verktygsfältet **Formatering**.
### **Sammanslagning av celler med Aspose.Cells**
Klassen Aspose.Cells.Cells har några användbara metoder för uppgiften. Till exempel sammanslår metoden Merge() cellerna till en enda cell inom ett angivet område.

Följande exempel visar hur man slår samman celler (C6:E7) i en arbetsbok.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}
## **Avfussning (delning) av sammanslagna celler**
### **Använda Microsoft Excel**
Följande steg beskriver hur man delar sammanslagna celler med hjälp av Microsoft Excel.

1. Välj den sammanslagna cellen.
   När cellerna har kombinerats väljs **Slå samman och centrera** på **Formateringsverktygsfältet**.
1. Klicka på **Slå samman och centrera** på **Formateringsverktygsfältet**.
### **Använda Aspose.Cells**
Klassen Aspose.Cells.Cells har en metod som heter UnMerge() som delar upp cellerna i deras ursprungliga tillstånd. Metoden avsammanslår cellerna med hjälp av cellens referens i det sammanslagna cellområdet.

Följande exempel visar hur man delar de sammanslagna cellerna (C6). Exemplet använder filen som skapades i det föregående exemplet och delar de sammanslagna cellerna.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-UnMergingtheMergedCells-1.cs" >}}


## **Fortsatta ämnen**
- [Identifiera sammanslagna celler i ett kalkylblad](/cells/sv/net/detect-merged-cells-in-a-worksheet/)
