---
title: Hantera kommentarer i ett arbetsblad
type: docs
weight: 110
url: /sv/net/aspose-cells-griddesktop/manage-comments-in-a-worksheet/
keywords: GridDesktop, kommentar, kommentarer
description: Den här artikeln introducerar hur man arbetar med kommentarer i GridDesktop.
---

{{% alert color="primary" %}} 

I MS Excel måste du vara bekant med kommentarsfunktionen som tillåter användare att lägga till kommentarer till celler. Den här funktionen är användbar i de fall då det krävs att ge viss information till användarna när de ska ange värden i cellerna. När en användare placerar sin muspekare på en kommenterad cell visas ett litet popup-meddelande för att ge information till användaren. Med Aspose.Cells.GridDesktop kan utvecklare skapa kommentarer på celler. I det här ämnet kommer vi att förklara användningen av den här funktionen i detalj.

{{% /alert %}} 
## **Lägga till kommentarer**
För att lägga till en kommentar till en cell med hjälp av Aspose.Cells.GridDesktop, följ stegen nedan:

- Lägg till Aspose.Cells.GridDesktop kontroll till din **Form**
- Kom åt något önskat **Kalkylblad**
- Lägg till **Kommentar** i arbetsbladet genom att ange cellen (använda dess namn eller rad- och kolumnnummer) där kommentaren skulle läggas till.

Koden nedan kommer att lägga till kommentarer i **b2** och **b4** celler i arbetsbladet.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AddingComments.cs" >}}


**Kommentarer** -samlingen i **Worksheet** -objektet tillhandahåller en överbelastad **Add** -metod. Utvecklare kan använda vilken överbelastad version av **Add** -metoden enligt deras specifika behov.
## **Åtkomst till kommentarer**
För att komma åt och ändra en befintlig kommentar i arbetsbladet kan utvecklare komma åt kommentaren från **Kommentarer** -samlingen av **Worksheet** genom att ange cellen (använda cellnamnet eller dess plats i form av rad- och kolumnnummer) där kommentaren är infogad. När kommentaren har kommit åt kan utvecklare ändra dess text under körning.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AccessingComments.cs" >}}
## **Ta bort kommentarer**
För att ta bort en befintlig kommentar kan utvecklare helt enkelt komma åt ett önskat arbetsblad och sedan **Ta bort** kommentaren från **Kommentarer** -samlingen av **Worksheet** genom att ange cellen (använda dess namn eller rad- och kolumnnummer) som innehåller kommentaren.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-RemovingComments.cs" >}}
