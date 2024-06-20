---
title: Lägg till cellkontroller i arbetsblad
type: docs
weight: 120
url: /sv/net/aspose-cells-griddesktop/add-cell-controls-in-worksheets/
keywords: GridDesktop,add,control,button,checkbox,combobox
description: Den här artikeln introducerar hur man lägger till kontroller i ett arbetsblad i GridDesktop.
---

{{% alert color="primary" %}} 

Cellkontroller är faktiskt de kontroller som kan läggas till i arbetsblad. Vi kallar dem **Cellkontroller** eftersom dessa kontroller visas i celler. I det här ämnet kommer vi att diskutera att lägga till och hantera händelserna för dessa cellkontroller.

{{% /alert %}} 
## **Introduktion**
För närvarande stödjer Aspose.Cells.GridDesktop att lägga till tre typer av cellkontroller, vilket inkluderar följande:

- **Knapp**
- **Kryssruta**
- **Kombinationsruta**

Alla dessa kontroller härstammar från en abstrakt klass, **CellControl**. Varje arbetsblad innehåller en samling av **Kontroller**. Nya cellkontroller kan läggas till och befintliga kan kommas åt med hjälp av denna **Kontroller**-samling enkelt.

**VIKTIGT:** Om du vill lägga till cellkontroller i alla celler i en kolumn istället för att lägga till en i taget kan du hänvisa till [Hantera cellkontroller i kolumner.](/cells/sv/net/aspose-cells-griddesktop/adding-cell-controls-in-worksheets/)
### **Lägga till en knapp**
För att lägga till en knapp i arbetsbladet med Aspose.Cells.GridDesktop, följ stegen nedan:

- Lägg till Aspose.Cells.GridDesktop-kontroll till din **Form**
- Öppna valfritt **Arbetsblad**
- Lägg till **Knapp** i **Kontroller**-samlingen för **Arbetsbladet**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingButton.cs" >}}


Vid tillägg av **Knapp** kan vi ange cellens plats (där den ska visas), bredd och höjd samt knappens text.
#### **Händelsehantering av knapp**
Vi har diskuterat att lägga till **Knapp**-kontroll i **Arbetsbladet** men vad är fördelen med att ha en knapp i arbetsbladet om vi inte kan använda den. Så här kommer behovet av händelsehantering av knappen.

För att hantera händelsen **Klick** av **Knappen**-kontrollen, tillhandahåller Aspose.Cells.GridDesktop händelsen **CellButtonClick** som bör implementeras av utvecklarna enligt deras behov. Till exempel har vi just visat ett meddelande när knappen klickas enligt nedan:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingButton.cs" >}}
#### **Ange en bakgrundsbild för knappkontrollen**
Vi kan ställa in en bakgrundsbild/foto för knappkontrollen med dess etikett/text enligt koden nedan:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-SetBackground.cs" >}}


**VIKTIGT:** Alla händelser för cellkontroller innehåller en **CellControlEventArgs**-argument som ger rad- och kolumnnummer för den cell som innehåller cellkontrollen (vars händelse utlöses).
### **Lägger till kryssruta**
För att lägga till en kryssruta i arbetsbladet med hjälp av Aspose.Cells.GridDesktop, följ stegen nedan:

- Lägg till Aspose.Cells.GridDesktop-kontroll till din **Form**
- Öppna valfritt **Arbetsblad**
- Lägg till **CheckBox** i **Controls**-samlingen av **Arbetsbladet**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCheckbox.cs" >}}


Vid läggning av **CheckBox** kan vi ange cellens plats (där den ska visas) och kryssrutans status.
#### **Händelshantering av checkbox**
Aspose.Cells.GridDesktop tillhandahåller en **CellCheckedChanged**-händelse som utlöses när kryssrutans **Checked**-status ändras. Utvecklare kan hantera denna händelse enligt sina krav. Till exempel har vi bara visat ett meddelande för att visa kryssrutans **Checked**-status i koden nedan:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCheckbox.cs" >}}
### **Lägger till Combobox**
För att lägga till en combobox i arbetsbladet med hjälp av Aspose.Cells.GridDesktop, följ stegen nedan:

- Lägg till Aspose.Cells.GridDesktop-kontroll till din **Form**
- Öppna valfritt **Arbetsblad**
- Skapa en array av element (eller värden) som ska läggas till i **ComboBox**
- Lägg till **ComboBox** i **Controls**-samlingen av **Arbetsbladet** genom att ange platsen för cellen (där comboboxen ska visas) och elementen/värden som ska visas när comboboxen klickas på



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCombobox.cs" >}}
#### **Händelshantering av Combobox**
Aspose.Cells.GridDesktop tillhandahåller en **CellSelectedIndexChanged**-händelse som utlöses när **Selected Index** för comboboxen ändras. Utvecklare kan hantera denna händelse enligt sina önskemål. Till exempel har vi bara visat ett meddelande för att visa det **Selected Item** för comboboxen:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCombobox.cs" >}}
