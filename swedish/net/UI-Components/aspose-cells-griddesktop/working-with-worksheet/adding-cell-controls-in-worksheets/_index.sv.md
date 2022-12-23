---
title: Lägger till Cell kontroller i kalkylblad
type: docs
weight: 120
url: /sv/net/adding-cell-controls-in-worksheets/
---
{{% alert color="primary" %}} 

 Cell kontroller är i själva verket de kontroller som kan läggas till i kalkylblad. Vi kallar dem**Cell Kontroller** eftersom dessa kontroller visas i celler. I det här ämnet kommer vi att diskutera hur man lägger till och hanterar händelserna för dessa cellkontroller.

{{% /alert %}} 
## **Introduktion**
För närvarande stöder Aspose.Cells.GridDesktop att lägga till tre typer av cellkontroller, som inkluderar följande:

- **Knapp**
- **Kryssruta**
- **Kombinationsrutan**

Alla dessa kontroller är härledda från en abstrakt klass,**CellControl**Varje arbetsblad innehåller en samling av**Kontroller**. Nya cellkontroller kan läggas till och befintliga kan nås med detta**Kontroller**insamling enkelt.

**VIKTIG:**Om du vill lägga till cellkontroller till alla celler i en kolumn istället för att lägga till en efter en kan du referera till[Hantera Cell kontroller i kolumner.](/cells/sv/net/adding-cell-controls-in-worksheets/)
### **Lägga till knapp**
För att lägga till en knapp i kalkylbladet med Aspose.Cells.GridDesktop, följ stegen nedan:

- Lägg till Aspose.Cells.GridDesktop-kontroll till din**Form**
- Få åtkomst till alla önskade**Arbetsblad**
- Lägg till**Knapp**till**Kontroller**samling av**Arbetsblad**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingButton.cs" >}}


Medan du lägger till**Knapp**, kan vi ange cellens plats (var den ska visas), bredd och höjd och rubriken för knappen.
#### **Händelsehantering av knappen**
Vi har diskuterat om att lägga till**Knapp**kontroll till**Arbetsblad**men vad är fördelen med att bara ha en knapp i kalkylbladet om vi inte kan använda den. Så här kommer behovet av händelsehantering av knappen.

Att hantera**Klick**händelse av**Knapp**kontroll, Aspose.Cells.GridDesktop ger**CellButtonClick**händelse som bör genomföras av utvecklarna enligt deras behov. Till exempel har vi precis visat ett meddelande när knappen klickas som visas nedan:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingButton.cs" >}}
#### **Ange en bakgrundsbild för knappkontrollen**
Vi kan ställa in bakgrundsbild/bild för knappkontrollen med dess etikett/text som visas i koden nedan:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-SetBackground.cs" >}}


**VIKTIG:**Alla händelser av cellkontroller innehåller en**CellControlEventArgs**argument som ger rad- och kolumnnumren för cellen som innehåller cellkontrollen (vars händelse utlöses).
### **Lägger till kryssruta**
För att lägga till en kryssruta i kalkylbladet med Aspose.Cells.GridDesktop, följ stegen nedan:

- Lägg till Aspose.Cells.GridDesktop-kontroll till din**Form**
- Få åtkomst till alla önskade**Arbetsblad**
- Lägg till**Kryssruta**till**Kontroller**samling av**Arbetsblad**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCheckbox.cs" >}}


Medan du lägger till**Kryssruta**, kan vi ange cellens plats (var den ska visas) och status för kryssrutan.
#### **Händelsehantering av CheckBox**
Aspose.Cells.GridDesktop tillhandahåller**CellCheckedChanged**händelse som utlöses när**Kontrollerade**status för kryssrutan ändras. Utvecklare kan hantera denna händelse enligt deras krav. Till exempel har vi precis visat ett meddelande för att visa**Kontrollerade**status för kryssrutan i koden nedan:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCheckbox.cs" >}}
### **Lägger till ComboBox**
För att lägga till en kombinationsruta i kalkylbladet med Aspose.Cells.GridDesktop, följ stegen nedan:

- Lägg till Aspose.Cells.GridDesktop-kontroll till din**Form**
- Få åtkomst till alla önskade**Arbetsblad**
- Skapa en uppsättning objekt (eller värden) som kommer att läggas till**Kombinationsrutan**
- Lägg till**Kombinationsrutan**till**Kontroller**samling av**Arbetsblad**genom att ange platsen för cellen (där kombinationsrutan kommer att visas) och objekten/värdena som kommer att visas när kombinationsrutan ska klickas



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCombobox.cs" >}}
#### **Händelsehantering av ComboBox**
Aspose.Cells.GridDesktop tillhandahåller**CellSelectedIndexChanged**händelse som utlöses när**Valt index**av kombinationsrutan ändras. Utvecklare kan hantera denna händelse enligt deras önskemål. Till exempel har vi precis visat ett meddelande för att visa**Valt objekt**av kombinationsrutan:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCombobox.cs" >}}
