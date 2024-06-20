---
title: Hantera bilder i ett kalkylblad
type: docs
weight: 100
url: /sv/net/aspose-cells-griddesktop/manage-pictures-in-a-worksheet/
keywords: GridDesktop, bild, bilder
description: Denna artikel introducerar hur man arbetar med bild i kalkylbladet i GridDesktop.
---

{{% alert color="primary" %}} 

De flesta tror att en bild kan förklara saker bättre än ord. Därför stöder Aspose.Cells.GridDesktop att lägga till bilder i kalkylblad för att utföra människors tro. I det här ämnet kommer vi att diskutera att lägga till och manipulera bilder i kalkylblad.

{{% /alert %}} 
## **Lägga till bilder**
För att lägga till en hyperlänk till en cell med Aspose.Cells.GridDesktop, följ stegen nedan:

- Lägg till Aspose.Cells.GridDesktop kontroll till din **Form**
- Kom åt något önskat **Kalkylblad**
- Lägg till ** Bild ** på kalkylbladet genom att ange filvägen till bilden och cellnamnet där bilden ska infogas

** Bilder ** -samlingen i ** Worksheet ** -objektet tillhandahåller en överbelastad ** Lägg till ** metod. Utvecklare kan använda vilken överbelastad version av ** Lägg till ** metod enligt deras specifika behov. Genom att använda dessa överbelastade versioner av ** Lägg till ** metoden är det möjligt att lägga till en bild från fil, ström eller ** Bild ** -objekt.

Nedan finns exempelkoden för att lägga till bilder i kalkylblad.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AddingPictures.cs" >}}
## **Komma åt bilder**
För att komma åt och modifiera en befintlig bild i kalkylbladet kan utvecklare komma åt bilden från ** Bilder ** -samlingen av ** Worksheet ** genom att ange cellen (använda cellnamn eller dess placering i termer av rad- och kolumnnummer) i vilken bilden är infogad. När bilden nås kan utvecklare ändra dess bild vid körning.

Nedan finns exempelkoden för att komma åt och ändra bilderna i ett kalkylblad.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AccessAndModifyPicture.cs" >}}
## **Ta bort Bilder**
För att ta bort en befintlig bild kan utvecklare enkelt komma åt ett önskat kalkylblad och sedan ta bort bilden från ** Bilder ** -samlingen av ** Worksheet ** genom att ange cellen (använda dess namn eller rad- och kolumnnummer) som innehåller bilden.

I koden nedan visas hur man tar bort bilder från ett kalkylblad.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-RemovePicture.cs" >}}
