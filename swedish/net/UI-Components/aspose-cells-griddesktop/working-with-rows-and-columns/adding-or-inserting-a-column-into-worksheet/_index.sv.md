---
title: Lägga till eller infoga en kolumn i arbetsbladet
type: docs
weight: 10
url: /sv/net/aspose-cells-griddesktop/add-or-insert-a-column-into-worksheet/
keywords: GridDesktop,infoga,lägga till,kolumn,infoga kolumn,infoga rad
description: Den här artikeln introducerar hur man infogar eller lägger till en kolumn i GridDesktop.
---

{{% alert color="primary" %}} 

I detta ämne beskriver vi den grundläggande funktionen att lägga till och infoga kolumner i arbetsblad vid körning med hjälp av API:et Aspose.Cells.GridDesktop. Den grundläggande skillnaden mellan tillägg och infogning är att vid tillägg läggs en kolumn till i slutet av kolumnernas samling i arbetsbladet medan vid infogning kan en kolumn läggas till på vilken specificerad position som helst i arbetsbladet.

{{% /alert %}} 
## **Lägger till en kolumn i arbetsbladet**
För att lägga till en ny kolumn i arbetsbladet, följ stegen nedan:

- Lägg till Aspose.Cells.GridDesktop kontroll till din **Form**
- Kom åt något önskat **Kalkylblad**
- Lägg till en **Kolumn** på **Arbetsbladet**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertColumn-AddColumn.cs" >}}
## **Infoga en kolumn i arbetsbladet**
För att infoga en ny kolumn i arbetsbladet på en specificerad position, följ stegen nedan:

- Lägg till Aspose.Cells.GridDesktop kontroll till din **Form**
- Kom åt något önskat **Kalkylblad**
- Infoga en **Kolumn** i **Arbetsbladet** (på en specifik position genom att ange index för kolumnen där den ska infogas)

{{< highlight java >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting column to the worksheet to the first position.

sheet.Cells.InsertColumn(0);

{{< /highlight >}}
