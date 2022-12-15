---
title: Hur man kör exemplen
type: docs
weight: 140
url: /sv/net/how-to-run-the-examples/
---
## **Programvarukrav**
Se till att du uppfyller följande krav innan du laddar ner och kör exemplen.

1. Visual Studio 2015 eller senare
1. NuGet Package Manager installerad i Visual Studio. Det är för det mesta redan installerat i Visual Studio 2015. För detaljer om hur man installerar NuGet pakethanterare, kontrollera:[Installerar NuGet klientverktyg](https://docs.microsoft.com/en-us/nuget/install-nuget-client-tools)
1.  Gå till Verktyg->Alternativ->NuGet Pakethanterare->Paketkällor och se till att alternativet**nuget.org** är kontrollerad
1.  Exempelprojekt använder NuGet funktionen Automatisk paketåterställning, därför bör du ha en aktiv internetanslutning. Om du inte har en aktiv internetanslutning på maskinen där exempel ska utföras, kontrollera[Installation](/cells/sv/net/installation-and-deployment/) och manuellt lägg till referens till Aspose.Cells.dll i exempelprojektet.
## **Ladda ner från GitHub**
Alla exempel på Aspose.Cells for .NET finns på[GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET).
## **Aspose.Cells Exempel**
-  Du kan antingen klona förvaret med din favorit GitHub-klient eller ladda ner ZIP-filen från[här](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip).
-  Extrahera innehållet i ZIP-filen till valfri mapp på din dator. Alla exempel finns i**Exempel** mapp.
- Det finns en Visual Studio-lösningsfil för C# Exempel dvs**Aspose.Cells.Examples.CSharp.sln**.
- Projektet skapas och underhålls i Visual Studio 2015.
- Öppna lösningsfilen i Visual Studio och bygg projektet.
-  Vid första körningen kommer beroenden automatiskt att laddas ner via NuGet. Du kan också ladda ner DLL:erna separat från[här](https://downloads.aspose.com/cells/net).
- **Data** mapp i rotmappen för**Exempel**innehåller indatafiler som CSharp-exempel använde. Det är obligatoriskt att ladda ner**Data** mapp tillsammans med exempelprojektet.
-  Öppna**RunExamples.cs**, alla exempel kallas härifrån.
- Avkommentera de exempel du vill köra inifrån projektet.
## **Aspose.Cells.GridDesktop Exempel**
-  Aspose.Cells.GridDesktop-exempel ingår också i[Aspose.Cells GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET) repository och kommer att vara tillgänglig som en del av ZIP-filen som kan laddas ner från[här](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip).
-  Alla exempel finns i**Exempel_GridDesktop**mapp.
- I likhet med Aspose.Cells exempel, är GridWeb exempel lösning filnamn**Aspose.Cells.GridDesktop.Examples.CSharp.sln**.
- Öppna lösningsfilen i Visual Studio och bygg projektet.
- Alla beroenden ingår som en del av exempelprojektet. Du kan också ladda ner DLL-filerna separat från[här](https://downloads.aspose.com/cells/net).
- **Data** mapp i rotmappen för**Exempel_GridDesktop** innehåller indatafiler som används av exempel. Det är obligatoriskt att ladda ner**Data** mapp tillsammans med exempelprojektet.
- Öppna och kör projektet.
- Klicka på exemplet i menyn som du vill köra från formuläret.
## **Aspose.Cells.GridWeb Exempel**
- Aspose.Cells.GridWeb-exempel ingår också i[Aspose.Cells GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET)repository och kommer att vara tillgänglig som en del av ZIP-filen som kan laddas ner från[här](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip).
- Alla exempel finns i**Exempel_GridWeb**mapp.
- I likhet med Aspose.Cells exempel, är GridWeb exempel lösning filnamn**Aspose.Cells.GridWeb.Examples.CSharp.sln**.
- Öppna lösningsfilen i Visual Studio och bygg projektet.
- Alla beroenden ingår som en del av exempelprojekten. Du kan också ladda ner DLL-filerna separat från[här](https://downloads.aspose.com/cells/net).
- **Data**mapp i rotmappen för**Exempel_GridWeb**innehåller indatafiler som används av exempel. Det är obligatoriskt att ladda ner**Data**mapp tillsammans med exempelprojektet.
- Öppna och spring**Exempel.aspx**i exempelprojektet.
- Klicka på exemplet i webbläsaren som du vill köra från projektet.
