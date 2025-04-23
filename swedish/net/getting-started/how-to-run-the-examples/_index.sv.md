---
title: Hur man kör exemplen
type: docs
weight: 140
url: /sv/net/how-to-run-the-examples/
---

## **Mjukvarukrav**
Se till att du uppfyller följande krav innan du laddar ner och kör exemplen.

1. Visual Studio 2015 eller senare
1. NuGet Package Manager installerat i Visual Studio. Det är oftast redan installerat i Visual Studio 2015. För detaljer om hur man installerar NuGet package manager, vänligen kolla: [Installation av NuGet-klientverktyg](https://docs.microsoft.com/en-us/nuget/install-nuget-client-tools)
1. Gå till Verktyg->Alternativ->NuGet Package Manager->Paketsökvägar och se till att alternativet **nuget.org** är markerat
1. Exempelprojekt använder NuGet automatisk pakethämtning funktionen, därför bör du ha en aktiv internetanslutning. Om du inte har en aktiv internetanslutning på den maskin där exempel ska köras, var god kontrollera [Installation](/cells/sv/net/installation-and-deployment/) och manuellt lägg till referensen till Aspose.Cells.dll i exempelprojektet.
## **Ladda ned från GitHub**
Alla exempel på Aspose.Cells for .NET är hostade på [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET).
## **Aspose.Cells Exempel**
- Du kan antingen klona depån med din favorit GitHub klient eller ladda ner ZIP-filen från [här](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip).
- Packa upp innehållet i ZIP-filen till valfri mapp på din dator. Alla exemplen finns i mappen **Exempel**.
- Det finns en Visual Studio-lösning fil för C# exempel dvs. **Aspose.Cells.Examples.CSharp.sln**.
- Projektet är skapat och underhållet i Visual Studio 2015.
- Öppna lösningen i Visual Studio och bygg projektet.
- Vid första körningen kommer beroendena automatiskt att laddas ner via NuGet. Du kan även ladda ner DLL-filerna separat från [här](https://downloads.aspose.com/cells/net).
- **Data** mappen i rotmappen för **Exempel** innehåller inmatningsfiler som CSharp exempel använder. Det är obligatoriskt att du laddar ner **Data** mappen tillsammans med exempelprojektet.
- Öppna **RunExamples.cs**, alla exempel körs härifrån.
- Ta bort kommentaren från exemplen du vill köra inom projektet.
## **Aspose.Cells.GridDesktop Exempel**
- Aspose.Cells.GridDesktop exempel ingår också i [Aspose.Cells GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET) depån och kommer att finnas tillgänglig som en del av ZIP-filen som kan laddas ner från [här](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip).
- Alla exempel finns i **Examples_GridDesktop** mappen.
- Liksom Aspose.Cells exempel, är GridWeb exempel lösningen filens namn **Aspose.Cells.GridDesktop.Examples.CSharp.sln**.
- Öppna lösningen i Visual Studio och bygg projektet.
- Alla beroenden ingår som en del av exempelprojekten. Du kan även ladda ner DLL-filerna separat från [här](https://downloads.aspose.com/cells/net).
- **Data** mappen i rotmappen för **Examples_GridDesktop** innehåller inmatningsfiler som används av exempel. Det är obligatoriskt att du laddar ner **Data** mappen tillsammans med exempelprojektet.
- Öppna och kör projektet.
- Klicka på exemplet i menyn som du vill köra inom formuläret.
## **Aspose.Cells.GridWeb Exempel**
- Aspose.Cells.GridWeb exempel ingår också i [Aspose.Cells GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET) depån och kommer att finnas tillgänglig som en del av ZIP-filen som kan laddas ner från [här](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip).
- Alla exempel finns i **Examples_GridWeb** mappen.
- Liksom Aspose.Cells exempel, är GridWeb exempel lösningen filens namn **Aspose.Cells.GridWeb.Examples.CSharp.sln**.
- Öppna lösningen i Visual Studio och bygg projektet.
- Alla beroenden ingår som en del av exempelprojekten. Du kan även ladda ner DLL-filerna separat från [här](https://downloads.aspose.com/cells/net).
- **Data** mappen i rotmappen för **Examples_GridWeb** innehåller inmatningsfiler som används av exempel. Det är obligatoriskt att du laddar ner **Data** mappen tillsammans med exempelprojektet.
- Öppna och kör **Examples.aspx** i exempelprojektet.
- Klicka på exemplet i webbläsaren som du vill köra inom projektet.
{{< app/cells/assistant language="csharp" >}}
