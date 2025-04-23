---
title: Sammanfoga och dela upp celler
description: Aspose.Cells är ett Python bibliotek för att arbeta med kalkylbladsfiler, vilket stöder sammanslagning och olaslagning av celler. Denna artikel introducerar hur man sammanfogar och ogillande celler med Aspose.Cells för Python via .NET biblioteket, samt hur man anpassar den sammanfogade cellens stil.
keywords: Aspose.Cells för Python via .NET, .NET bibliotek, kalkylblad, slå ihop celler, dela upp celler, stilinställningar, anpassade stilar
type: docs
weight: 190
url: /sv/python-net/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells för Python via .NET stöder denna funktion och kan även slå ihop celler i ett kalkylblad. Du kan dela upp eller splittra de sammanfogade cellerna också. En sammanfogad cells cellreferens är referensen för det övre vänstra cellen i det ursprungliga området.

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

### **Sammanfoga celler med Aspose.Cells för Python via .NET**
Klassen Aspose.Cells.Cells har några användbara metoder för uppgiften. Till exempel sammanslår metoden Merge() cellerna till en enda cell inom ett angivet område.

Följande exempel visar hur man slår samman celler (C6:E7) i en arbetsbok.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-MergingCellsInWorksheet.-1.py" >}}

## **Avfussning (delning) av sammanslagna celler**
### **Använda Microsoft Excel**
Följande steg beskriver hur man delar sammanslagna celler med hjälp av Microsoft Excel.

1. Markera den sammanfogade cellen. När celler har slagits ihop är **Slå samman och centrera** valt på **Formatering**-verktygsfältet.
1. Klicka på **Slå samman och centrera** på **Formateringsverktygsfältet**.

### **Användning av Aspose.Cells för Python via .NET**
Klassen Aspose.Cells.Cells har en metod som heter UnMerge() som delar upp cellerna i deras ursprungliga tillstånd. Metoden avsammanslår cellerna med hjälp av cellens referens i det sammanslagna cellområdet.

Följande exempel visar hur man delar de sammanslagna cellerna (C6). Exemplet använder filen som skapades i det föregående exemplet och delar de sammanslagna cellerna.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UnMergingtheMergedCells-1.py" >}}


## **Fortsatta ämnen**
- [Identifiera sammanslagna celler i ett kalkylblad](/cells/sv/python-net/detect-merged-cells-in-a-worksheet/)

