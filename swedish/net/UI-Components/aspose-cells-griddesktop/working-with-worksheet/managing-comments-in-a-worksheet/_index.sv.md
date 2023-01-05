---
title: Hantera kommentarer i ett arbetsblad
type: docs
weight: 110
url: /sv/net/managing-comments-in-a-worksheet/
---
{{% alert color="primary" %}} 

MS Excel måste du vara bekant med kommentarsfunktionen som låter användare lägga till kommentarer i celler. Den här funktionen är användbar i de fall då det krävs att ge viss information till användarna när de ska skriva in värden i cellerna. Närhelst en användare placerar sin muspekare på en kommenterad cell, visas ett litet popup-meddelande för att ge viss information till användaren. Med hjälp av Aspose.Cells.GridDesktop kan utvecklare skapa kommentarer på celler. I det här ämnet kommer vi att förklara användningen av den här funktionen i detalj.

{{% /alert %}} 
## **Lägger till kommentarer**
För att lägga till en kommentar till en cell med Aspose.Cells.GridDesktop, följ stegen nedan:

-  Lägg till Aspose.Cells.GridDesktop-kontroll till din**Form**
-  Få åtkomst till alla önskade**Arbetsblad**
-  Lägg till**Kommentar** till kalkylbladet genom att ange cellen (med dess namn eller rad- och kolumnnummer) där kommentaren ska läggas till.

 Koden nedan kommer att lägga till kommentarer till**b2** och**b4** celler i arbetsbladet.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AddingComments.cs" >}}


**Kommentarer** samling i**Arbetsblad** objekt ger en överbelastad**Lägg till** metod. Utvecklare kan använda vilken överbelastad version som helst av**Lägg till** metod enligt deras specifika behov.
## **Åtkomst till kommentarer**
För att komma åt och ändra en befintlig kommentar i kalkylbladet kan utvecklare komma åt kommentaren från**Kommentarer** samling av**Arbetsblad** genom att ange cellen (med cellnamn eller dess plats i termer av rad- och kolumnnummer) där kommentaren infogas. När kommentaren har nåtts kan utvecklare ändra dess text under körning.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AccessingComments.cs" >}}
## **Ta bort kommentarer**
 För att ta bort en befintlig kommentar kan utvecklare helt enkelt komma åt ett önskat kalkylblad och sedan**Ta bort** kommentar från**Kommentarer** samling av**Arbetsblad** genom att ange cellen (med dess namn eller rad- och kolumnnummer) som innehåller kommentaren.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-RemovingComments.cs" >}}
