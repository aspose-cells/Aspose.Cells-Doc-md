---
title: Installera Aspose Cells till NuGet
type: docs
weight: 30
url: /sv/net/installation/
---
## **Installera Aspose.Cells for .NET till NuGet**
NuGet är det enklaste sättet att ladda ner och installera Aspose API:er for .NET. Öppna Microsoft Visual Studio och NuGet pakethanterare. Sök "aspose" för att hitta önskad Aspose API. Klicka på "Installera", den valda API kommer att laddas ner och refereras till i ditt projekt.

Obs: Du kan besöka nuget webbsida för aspose.cells för mer information:
[Aspose.Cells for .NET NuGet Paket](https://www.nuget.org/packages/Aspose.Cells/)

### **Installera Aspose.Cells med Package Manager GUI**
Följ dessa steg för att referera till Aspose.Cells-komponenten med pakethanterarens GUI:

- Öppna din lösning/projekt i Visual Studio.
- Klick**Verktyg** -> **Bibliotekspakethanterare** -> **Hantera NuGet Paket**från Solution. Du kan också enkelt komma åt samma alternativ genom lösningsutforskaren. Högerklicka på lösningen eller projektet och välj**Hantera NuGet Paket**från snabbmenyn.
- Välj**Uppkopplad**från menyn till vänster och skriv "Aspose.Cells" i sökrutan för att hitta paketet Aspose.Cells .NET.
- Klicka på**Installera**knappen bredvid posten Aspose.Cells for .NET för att installera den senaste versionen i ditt projekt.
### **Installera Aspose.Cells med Package Manager Console**
Du kan följa stegen nedan för att referera till Aspose.Cells-komponenten med hjälp av pakethanterarens konsol:

- Öppna din lösning/projekt i Visual Studio.
- Välj**Verktyg** -> **Bibliotekspakethanterare** -> **Package Manager Console**från menyn för att öppna pakethanterarens konsol.
 Skriv kommandot "Install-Package Aspose.Cells" och tryck på enter för att installera den senaste fullständiga versionen i din applikation. Alternativt kan du lägga till suffixet "-prerelease" till kommandot för att specificera att den senaste versionen inklusive snabbkorrigeringar också ska installeras.
- Du kommer att se att tipset "Hämtar Aspose.Cells..." visas nere till vänster i fönstret, vilket indikerar att nedladdningen pågår.
- När du har laddat ner kommer du att se följande bekräftelsemeddelanden. Om du inte är bekant med Aspose EULA så är det en bra idé att läsa licensen som hänvisas till i URL:en.
- Du bör nu upptäcka att Aspose.Cells framgångsrikt har lagts till och refererat till i din ansökan åt dig.
## **Refererar till Aspose.Cells från ett .NET-projekt**
För att använda Aspose.Cells i en applikation, lägg till en referens till den. Så här lägger du till en referens med Visual Studio:

1.  I den**Lösningsutforskare**expandera projektnoden du vill lägga till en referens till.
1.  Högerklicka på**Referenser** nod för projektet och välj**Lägg till referens** från menyn.
1.  I den**Lägg till referens** dialogrutan, välj fliken .NET (vald som standard). Om du installerade med MSI-installationsprogrammet, visas Aspose.Cells i den övre rutan.
1.  Välj den och klicka**Välj**.

Om du endast har laddat ner eller packat upp DLL:n:

1.  Leta reda på filen Aspose.Cells.dll med hjälp av**Bläddra** knapp. Aspose.Cells ska visas i**Valda komponenter** rutan i dialogrutan.
1.  Klick**OK** . Referensen Aspose.Cells visas under**Referenser** noden för projektet.
### **Referera till komponenten från ett VS.NET 2010 klientprofilprojekt**
Om ditt projekts målramverk är .NET Framework 3.5/4 Client Profile, använd komponentfilen Aspose.Cells.dll som finns i mappen net_ClientProfile i din installationskatalog. Till exempel:

-  I**Lösningsutforskare** av VS.NET 2010 för ditt projekt, högerklicka**Referenser** och välj**Lägg till referens**.
-  Välj**Bläddra** fliken i dialogrutan och klicka på Sök efter rullgardinsmenyn.
- Hitta och välj komponentfilen Aspose.Cells.dll i din installationskatalog, till exempel: .../Program Files/Aspose/Aspose.Cells for .NET/Bin/net_ClientProfile/ **(Se till att du har installerat produkten med MSI-installationsprogrammet på din maskin .)**
-  Klick**OK** för att stänga dialogrutan

{{% alert color="primary" %}} 

Om ditt VS.NET 2010-projekts målramverk är ".NET Framework 4" eller annat, använd helt enkelt komponentfilen Aspose.Cells.dll som finns i mappen net4.0/net2.0.

{{% /alert %}} 
## **Refererar till Aspose.Cells Grid Controls från ett .NET-projekt**
För att använda en rutnätskontroll i din applikation, lägg till en referens till den. Gör följande för att referera till en rutnätskontroll i Visual Studio:

-  I**Lösningsutforskare**expandera projektnoden du vill lägga till en referens till.
-  Högerklicka på**Referenser** nod för projektet och välj**Lägg till referens** från menyn.
-  I den**Lägg till referens** dialogrutan, välj**.NET tab** (valt som standard). Om du har använt MSI-installeraren för att installera visas Aspose.Cells for .NET, Aspose.Cells.GridDesktop och Aspose.Cells.GridWeb i den övre rutan.
-  Välj dem och klicka**Välj**.
- Referenserna Aspose.Cells.GridDesktop och Aspose.Cells.GridWeb visas under projektets referensnod.

Om du endast laddade ner och packade upp DLL:n:

-  Leta upp filerna Aspose.Cells.GridDesktop.dll och Aspose.Cells.GridWeb.dll med hjälp av knappen Bläddra. Aspose.Cells Grid Suite har refererats till och bör visas i**Valda komponenter** rutan i dialogrutan.
-  Klick**OK.**
## **Avinstallerar Aspose.Cells for .NET**
Om du har använt MSI-installeraren för att distribuera Aspose.Cells for .NET, följ dessa steg för att helt ta bort komponenten och kontrollerna, tillhörande demonstrationer och dokumentation:

-  Från**Start** menyn, välj**inställningar** , följd av**Kontrollpanel**.
-  Klick**Lägg till/ta bort program**.
- Välj Aspose.Cells for .NET (version).
-  Klick**Ändra/ta bort** för att ta bort Aspose.Cells.
