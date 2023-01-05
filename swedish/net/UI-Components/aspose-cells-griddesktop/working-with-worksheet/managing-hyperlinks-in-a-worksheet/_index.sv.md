---
title: Hantera hyperlänkar i ett arbetsblad
type: docs
weight: 90
url: /sv/net/managing-hyperlinks-in-a-worksheet/
---
{{% alert color="primary" %}} 

Med Aspose.Cells.GridDesktop är det också möjligt att lägga till hyperlänkar till enkla värden lagrade i celler i ett kalkylblad. Låt oss säga att i vissa celler kan du ha några värden som du skulle vilja länka till mer detaljerad information på en webbsida. I så fall skulle det vara önskvärt att lägga till en hyperlänk till den cellen så att om en användare klickar på cellen så kommer han att dirigeras till den webbsidan. I det här ämnet kommer vi att förklara hur utvecklare kan lägga till och manipulera hyperlänkar i sina kalkylblad.

{{% /alert %}} 
## **Lägga till hyperlänkar**
För att lägga till en hyperlänk till en cell med Aspose.Cells.GridDesktop, följ stegen nedan:

-  Lägg till Aspose.Cells.GridDesktop-kontroll till din**Form**
-  Få åtkomst till alla önskade**Arbetsblad**
-  Få tillgång till en önskad**Cell** i kalkylbladet som kommer att hyperlänkas
- Lägg till ett värde till cellen som ska hyperlänkas
-  Lägg till**Hyperlänk** till kalkylbladet genom att ange cellnamnet som hyperlänken ska tillämpas på

**Hyperlänkar** samling i**Arbetsblad** objekt ger en överbelastad**Lägg till** metod. Utvecklare kan använda vilken överbelastad version som helst av**Lägg till** metod enligt deras specifika behov.

 Nedanstående kod kommer att lägga till en hyperlänk till**B2** och**C3** celler i arbetsbladet.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AddHyperlink.cs" >}}
## **Åtkomst till hyperlänkar**
När en hyperlänk väl kommer att läggas till i en cell, kan det också krävas att man kommer åt och ändrar hyperlänken under körning. För att göra det kan utvecklare helt enkelt komma åt hyperlänken från**Hyperlänkar** samling av**Arbetsblad** genom att ange cellen (med cellnamn eller dess plats i termer av rad- och kolumnnummer) som hyperlänken läggs till. När hyperlänken har nåtts kan utvecklare ändra dess URL under körning.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AccessHyperlink.cs" >}}
## **Ta bort hyperlänkar**
 För att ta bort en befintlig hyperlänk kan utvecklare helt enkelt komma åt ett önskat kalkylblad och sedan**Ta bort** hyperlänk från**Hyperlänkar** samling av**Arbetsblad** genom att ange den hyperlänkade cellen (med dess namn eller rad- och kolumnnummer).



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-RemoveHyperlink.cs" >}}

{{% alert color="primary" %}} 

Om du vill lägga till en hyperlänk till en cell och vill visa hyperlänkens URL i cellen istället för något värde, lägg inte till något värde i cellen utan lägg bara till hyperlänken till den cellen. Om du gör det kommer cellen att hyperlänkas och hyperlänkens URL kommer också att visas i cellen som dess värde.

{{% /alert %}}
