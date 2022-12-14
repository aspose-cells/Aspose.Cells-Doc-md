---
title: Lägga till eller infoga en rad i arbetsbladet
type: docs
weight: 30
url: /sv/net/adding-or-inserting-a-row-into-worksheet/
---
{{% alert color="primary" %}} 

I likhet med ett av våra tidigare ämnen, beskriver det här ämnet funktionen att lägga till och infoga rader i kalkylbladen vid körning med API:et Aspose.Cells.GridDesktop. Den grundläggande skillnaden mellan tillägg och infogning är att dessutom läggs en rad till i slutet av radsamlingen i kalkylbladet där som vid infogning kan en rad läggas till på valfri angiven position i kalkylbladet.

{{% /alert %}} 
## **Lägga till en rad i arbetsbladet**
För att lägga till en ny rad i kalkylbladet, följ stegen nedan:

-  Lägg till Aspose.Cells.GridDesktop-kontroll till din**Form**
-  Få åtkomst till alla önskade**Arbetsblad**
-  Lägg till**Rad** till**Arbetsblad**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertRow-AddRow.cs" >}}
## **Infoga en rad i arbetsbladet**
För att infoga en ny rad i kalkylbladet på en angiven plats, följ stegen nedan:

-  Lägg till Aspose.Cells.GridDesktop-kontroll till din**Form**
-  Få åtkomst till alla önskade**Arbetsblad**
-  Föra in**Rad** in i**Arbetsblad**(vid en specifik position genom att ange indexet för raden där det ska infogas)

{{< highlight "java" >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting row to the worksheet to the first position.

sheet.Cells.InsertRow(0);

{{< /highlight >}}
