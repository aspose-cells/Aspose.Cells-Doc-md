---
title: Lägga till eller infoga en kolumn i arbetsbladet
type: docs
weight: 10
url: /sv/net/adding-or-inserting-a-column-into-worksheet/
---
{{% alert color="primary" %}} 

I det här ämnet kommer vi att beskriva den grundläggande funktionen för att lägga till och infoga kolumner i kalkylbladen vid körning med hjälp av API:et för Aspose.Cells.GridDesktop. Den grundläggande skillnaden mellan tillägg och infogning är att dessutom läggs kolumn till i slutet av kolumnsamlingen i kalkylbladet, där kolumnen, precis som vid infogning, kan läggas till på valfri specificerad position i kalkylbladet.

{{% /alert %}} 
## **Lägga till en kolumn i arbetsbladet**
För att lägga till en ny kolumn i kalkylbladet, följ stegen nedan:

-  Lägg till Aspose.Cells.GridDesktop-kontroll till din**Form**
-  Få åtkomst till alla önskade**Arbetsblad**
-  Lägg till**Kolumn** till**Arbetsblad**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertColumn-AddColumn.cs" >}}
## **Infoga en kolumn i arbetsbladet**
För att infoga en ny kolumn i kalkylbladet på en angiven plats, följ stegen nedan:

-  Lägg till Aspose.Cells.GridDesktop-kontroll till din**Form**
-  Få åtkomst till alla önskade**Arbetsblad**
-  Föra in**Kolumn** in i**Arbetsblad** (vid en specifik position genom att ange indexet för kolumnen där det ska infogas)

{{< highlight "java" >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting column to the worksheet to the first position.

sheet.Cells.InsertColumn(0);

{{< /highlight >}}
