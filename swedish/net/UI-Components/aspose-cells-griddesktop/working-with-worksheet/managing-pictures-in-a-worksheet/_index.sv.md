---
title: Hantera bilder i ett arbetsblad
type: docs
weight: 100
url: /sv/net/managing-pictures-in-a-worksheet/
---
{{% alert color="primary" %}} 

De flesta tror att en bild kan förklara saker bättre än ord. Det är därför Aspose.Cells.GridDesktop stöder att lägga till bilder i kalkylblad för att verkställa folkets tro. I det här ämnet kommer vi att diskutera hur man lägger till och manipulerar bilder i kalkylblad.

{{% /alert %}} 
## **Lägga till bilder**
För att lägga till en hyperlänk till en cell med Aspose.Cells.GridDesktop, följ stegen nedan:

-  Lägg till Aspose.Cells.GridDesktop-kontroll till din**Form**
-  Få åtkomst till alla önskade**Arbetsblad**
-  Lägg till**Bild** till kalkylbladet genom att ange sökvägen till bilden och cellnamnet där bilden ska infogas

**Bilder** samling i**Arbetsblad** objekt ger en överbelastad**Lägg till** metod. Utvecklare kan använda vilken överbelastad version som helst av**Lägg till** metod enligt deras specifika behov. Att använda dessa överbelastade versioner av**Lägg till** metod är det möjligt att lägga till en bild från fil, stream eller**Bild** objekt.

Nedan är exempelkoden för att lägga till bilder i kalkylblad.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AddingPictures.cs" >}}
## **Tillgång till bilder**
 För att komma åt och ändra en befintlig bild i kalkylbladet kan utvecklare komma åt bilden från**Bilder** samling av**Arbetsblad** genom att ange cellen (med cellnamn eller dess plats i termer av rad- och kolumnnummer) där bilden infogas. När bilden har nåtts kan utvecklare ändra dess bild under körning.

Nedan finns exempelkoden för att komma åt och ändra bilderna i ett kalkylblad.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AccessAndModifyPicture.cs" >}}
## **Ta bort bilder**
 För att ta bort en befintlig bild kan utvecklare helt enkelt komma åt ett önskat kalkylblad och sedan**Ta bort** bild från**Bilder** samling av**Arbetsblad** genom att ange cellen (med dess namn eller rad- och kolumnnummer) som innehåller bilden.

I koden nedan visas hur man tar bort bilder från kalkylbladet.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-RemovePicture.cs" >}}
