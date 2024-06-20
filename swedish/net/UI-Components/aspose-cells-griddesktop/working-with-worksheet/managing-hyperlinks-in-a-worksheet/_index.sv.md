---
title: Hantera hyperlänkar i ett arbetsblad
type: docs
weight: 90
url: /sv/net/aspose-cells-griddesktop/manage-hyperlinks-in-a-worksheet/
keywords: GridDesktop, hyper, länk, hyperlänk, hyperlänkar
description: Den här artikeln introducerar hur man arbetar med hyperlänkar i GridDesktop.
---

{{% alert color="primary" %}} 

Med Aspose.Cells.GridDesktop är det också möjligt att lägga till hyperlänkar till enkla värden som lagras i celler i ett arbetsblad. Föreställ dig att du i vissa celler har några värden som du vill länka till mer detaljerad information på en webbsida. I det fallet skulle det vara önskvärt att lägga till en hyperlänk till den cellen så att om en användare klickar på cellen hänvisas han till den webbsidan. I det här ämnet kommer vi att förklara hur utvecklare kan lägga till och manipulera hyperlänkar i sina arbetsblad.

{{% /alert %}} 
## **Lägga till hyperlänkar**
För att lägga till en hyperlänk till en cell med Aspose.Cells.GridDesktop, följ stegen nedan:

- Lägg till Aspose.Cells.GridDesktop kontroll till din **Form**
- Kom åt något önskat **Kalkylblad**
- Kom åt en önskad **Cell** i arbetsbladet som ska ha en hyperlänk
- Lägg till något värde i cellen som ska ha en hyperlänk
- Lägg till **Hyperlänk** i arbetsbladet genom att ange cellnamnet på vilket hyperlänken ska tillämpas

**Hyperlänkar** -samlingen i **Worksheet** -objektet tillhandahåller en överbelastad **Add** -metod. Utvecklare kan använda vilken överbelastad version av **Add** -metoden enligt deras specifika behov.

Nedan kod kommer att lägga till en hyperlänk till cellerna ** B2 ** och ** C3 ** i kalkylbladet.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AddHyperlink.cs" >}}
## **Åtkomst av hyperlänkar**
När en hyperlänk har lagts till en cell kan det också vara nödvändigt att komma åt och modifiera hyperlänken vid körning. För att göra detta kan utvecklare enkelt komma åt hyperlänken från ** Hyperlinks ** -samlingen av ** Worksheet ** genom att ange cellen (använda cellnamn eller dess placering i termer av rad- och kolumnnummer) till vilken hyperlänken läggs till. När hyperlänken nås kan utvecklare ändra dess URL vid körning.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AccessHyperlink.cs" >}}
## **Ta bort hyperlänkar**
För att ta bort en befintlig hyperlänk kan utvecklare enkelt komma åt ett önskat kalkylblad och sedan ta bort hyperlänken från ** Hyperlinks ** -samlingen av ** Worksheet ** genom att ange den hyperlänkade cellen (använda dess namn eller rad- och kolumnnummer).



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-RemoveHyperlink.cs" >}}

{{% alert color="primary" %}} 

Om du vill lägga till en hyperlänk till en cell och vill visa hyperlänkens URL i cellen istället för något värde, lägg inte till något värde i cellen och lägg helt enkelt till hyperlänken till den cellen. Genom att göra det kommer cellen att vara hyperlänkad och hyperlänkens URL kommer också att visas i cellen som dess värde.

{{% /alert %}}
