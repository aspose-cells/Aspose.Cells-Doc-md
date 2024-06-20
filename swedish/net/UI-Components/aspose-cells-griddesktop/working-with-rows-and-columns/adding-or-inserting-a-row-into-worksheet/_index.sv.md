---
title: Lägga till eller infoga en rad i arbetsbladet
type: docs
weight: 30
url: /sv/net/aspose-cells-griddesktop/add-or-insert-a-row-into-worksheet/
keywords: GridDesktop,insert,add,row,insert row,add row
description: Den här artikeln introducerar hur man lägger till eller infogar en rad i GridDesktop.
---

{{% alert color="primary" %}} 

Liknande ett av våra tidigare ämnen, beskriver detta ämne funktionen att lägga till och infoga rader i arbetsblad vid körning med hjälp av API:et Aspose.Cells.GridDesktop. Den grundläggande skillnaden mellan tillägg och infogning är att vid tillägg läggs en rad till i slutet av radernas samling i arbetsbladet medan vid infogning kan en rad läggas till på vilken specificerad position som helst i arbetsbladet.

{{% /alert %}} 
## **Lägga till en rad i arbetsblad**
För att lägga till en ny rad i arbetsbladet, följ följande steg:

- Lägg till Aspose.Cells.GridDesktop kontroll till din **Form**
- Kom åt något önskat **Kalkylblad**
- Lägg till **Rad** till **Arbetsbladet**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertRow-AddRow.cs" >}}
## **Infoga en rad i arbetsbladet**
För att infoga en ny rad i arbetsbladet på en angiven position, följ följande steg:

- Lägg till Aspose.Cells.GridDesktop kontroll till din **Form**
- Kom åt något önskat **Kalkylblad**
- Infoga **Rad** i **Arbetsbladet** (på en specifik position genom att ange index för raden där den ska infogas)

{{< highlight java >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting row to the worksheet to the first position.

sheet.Cells.InsertRow(0);

{{< /highlight >}}
