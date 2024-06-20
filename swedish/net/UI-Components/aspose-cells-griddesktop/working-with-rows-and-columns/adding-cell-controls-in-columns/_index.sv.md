---
title: Lägga till cellkontroller i kolumner
type: docs
weight: 90
url: /sv/net/aspose-cells-griddesktop/add-cell-controls-in-columns/
keywords: GridDesktop,add,control,controls
description: Den här artikeln presenterar hur man lägger till kontroller i kolumn i GridDesktop.
---

{{% alert color="primary" %}} 

I våra senare diskussioner har vi diskuterat om att lägga till och hantera cellkontroller i kalkylarket. Men, med hjälp av dessa metoder kan vi lägga till cellkontroller till enskilda celler en i taget. Vad händer om någon vill lägga till cellkontroller till alla celler i en eller flera kolumner? I sådana fall, för att minska utvecklarnas ansträngningar, erbjuder Aspose.Cells.GridDesktop möjligheten att lägga till cellkontroller per kolumnbasis. Det innebär att utvecklare endast kan välja en önskad kolumn och ange en cellkontroll. Den angivna cellkontrollen kommer att läggas till alla celler i den angivna kolumnen. Låt oss se hur vi kan använda den här funktionen.

{{% /alert %}} 
## **Introduktion**
För närvarande stödjer Aspose.Cells.GridDesktop att lägga till tre typer av cellkontroller, vilket inkluderar följande:

- **Knapp**
- **Kryssruta**
- **Kombinationsruta**

Alla dessa kontroller härstammar från en abstrakt klass, **CellControl**.

**VIKTIGT:** Om du vill lägga till cellkontroller till en enda cell istället för hela kolumnen kan du hänvisa till [Lägga till cellkontroller i kalkylblad.](/cells/sv/net/adding-cell-controls-in-worksheets/)
### **Lägga till en knapp**
För att lägga till knappar i en kolumn med Aspose.Cells.GridDesktop, följ följande steg:

- Lägg till Aspose.Cells.GridDesktop kontroll till din **Form**
- Kom åt något önskat **Kalkylblad**
- Lägg till **Knapp** till valfri **Kolumn** i **Kalkylbladet**

**OBS:** När du lägger till **Knapp** kan vi specificera bredd, höjd och bildtext för knappen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingButton.cs" >}}


Ovanstående kodsnutt lägger till knappar i alla celler i den angivna kolumnen. När någon cell i den specifika kolumnen väljs blir en knapp synlig. För mer information om hanteringen av händelser för knappar, vänligen hänvisa till [Händelshantering av en knappkontroll.](/cells/sv/net/adding-cell-controls-in-worksheets/#event-handling-of-button)
### **Lägger till kryssruta**
För att lägga till kryssrutor i en kolumn med hjälp av Aspose.Cells.GridDesktop, följ stegen nedan:

- Lägg till Aspose.Cells.GridDesktop kontroll till din **Form**
- Kom åt något önskat **Kalkylblad**
- Lägg till en **Kryssruta** i vald **Kolumn** på **Arbetsbladet**

**OBS:** Vid tillägg av en **Kryssruta** kan vi även specificera kryssrutans tillstånd.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCheckbox.cs" >}}


Ovanstående kodsnutt lägger till kryssrutor i alla celler i den angivna kolumnen. För mer information om händelsehantering av kryssrutor, se [Händelsehantering av en kryssrutestyrning.](/cells/sv/net/adding-cell-controls-in-worksheets/#event-handling-of-checkbox)
### **Lägger till Combobox**
För att lägga till comboboxar i en kolumn med hjälp av Aspose.Cells.GridDesktop, följ stegen nedan:

- Lägg till Aspose.Cells.GridDesktop kontroll till din **Form**
- Kom åt något önskat **Kalkylblad**
- Skapa en matris med objekt (eller värden) som kommer att läggas till i **ComboBox**
- Lägg till en **ComboBox** (med objekt eller värden) i vald **Kolumn** på **Arbetsbladet



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCombobox.cs" >}}


Ovanstående kodsnutt lägger till comboboxar i alla celler i den angivna kolumnen. När en cell i den specifika kolumnen är vald blir en combobox synlig. För mer information om händelsehantering av comboboxar, se [Händelsehantering av en ComboBox-styrning.](/cells/sv/net/adding-cell-controls-in-worksheets/#event-handling-of-combobox)
