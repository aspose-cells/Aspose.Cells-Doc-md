---
title: Installera Aspose Cells via NuGet
type: docs
weight: 30
url: /sv/net/installation/
---


## **Installera Aspose.Cells for .NET via NuGet**
NuGet är det enklaste sättet att ladda ner och installera Aspose API: er för .NET. Öppna Microsoft Visual Studio och NuGet-paketet. Sök efter "aspose" för att hitta den önskade Aspose API: en. Klicka på "Installera", den valda API: en kommer att laddas ner och refereras i ditt projekt.

Observera: Du kan besöka nugets webbsida för aspose.cells för mer information: 
[Aspose.Cells for .NET NuGet-paket](https://www.nuget.org/packages/Aspose.Cells/)

### **Installera Aspose.Cells med hjälp av Package Manager GUI**
Följ dessa steg för att referera till Aspose.Cells-komponenten med hjälp av pakethanterargränssnittet: 

- Öppna din lösning/projekt i Visual Studio.
- Klicka på **Verktyg** -> **Bibliotekspaketshanteraren** -> **Hantera NuGet-paket** från lösningen. Du kan även enkelt komma åt samma alternativ via Lösningens Utforskar. Högerklicka på lösningen eller projektet och välj **Hantera NuGet-paket** från snabbmenyn.
- Välj **Online** från menyn till vänster och skriv "Aspose.Cells" i sökrutan för att hitta Aspose.Cells .NET-paketet.
- Klicka på **Installera** -knappen bredvid entrén Aspose.Cells for .NET för att installera den senaste versionen i ditt projekt.
### **Installera Aspose.Cells med hjälp av Package Manager-konsolen**
Du kan följa stegen nedan för att referera till Aspose.Cells-komponenten med hjälp av pakethanterarkonsolen:

- Öppna din lösning/projekt i Visual Studio.
- Välj **Verktyg** -> **Bibliotekspaketshanterare** -> **Pakethanterarkonsol** från menyn för att öppna pakethanterarkonsolen.
  - Skriv in kommandot "Install-Package Aspose.Cells" och tryck på enter för att installera den senaste fullständiga versionen i din applikation. Alternativt kan du lägga till suffixet "-prerelease" till kommandot för att ange att den senaste versionen med snabbkorrigeringar också ska installeras.
- Du ser att tipset "Laddar ner Aspose.Cells..." visas längst ner till vänster i fönstret och indikerar att nedladdningen pågår.
- När nedladdningen är klar ser du följande bekräftelsemeddelanden. Om du inte är bekant med Aspose EULA är det en bra idé att läsa licensen som hänvisas i URL:en.
- Du bör nu se att Aspose.Cells har lagts till och refererats i din applikation för dig.
## **Referera Aspose.Cells från ett .NET-projekt**
För att använda Aspose.Cells i en applikation, lägg till en referens till den. För att lägga till en referens med Visual Studio:

1. I **Lösningsexplorer**, expandera projekt noden du vill lägga till en referens till.
1. Högerklicka på **Referenser** noden för projektet och välj **Lägg till referens** från menyn.
1. I dialogrutan **Lägg till referens**, välj .NET-fliken (vald som standard). Om du installerade med MSI-installationsprogrammet kommer Aspose.Cells att visas i det övre fönstret.
1. Markera den och klicka på **Välj**.

Om du har laddat ner eller packat upp endast DLL:

1. Lokalisera Aspose.Cells.dll-filen med knappen **Bläddra**. Aspose.Cells bör visas i **Valda komponenter**-fönstret i dialogrutan.
1. Klicka på **OK**. Aspose.Cells-referensen visas under **Referenser**-noden i projektet.
### **Referera komponenten från ett VS.NET 2010 Client Profile-projekt**
Om målet för ditt projektsramverk är .NET Framework 3.5/4 Client Profile, använd Aspose.Cells.dll-komponentfilen som finns i net_ClientProfile-mappen i installationsmappen. Till exempel:

- I **Lösningsexplorer** i VS.NET 2010 för ditt projekt, högerklicka på **Referenser** och välj **Lägg till referens**.
- Välj **Bläddra**-fliken i dialogrutan och klicka på Välj i rullgardinsmenyn.
- Hitta och markera Aspose.Cells.dll-komponentfilen i din installationsmapp, till exempel: .../Program Files/Aspose/Aspose.Cells for .NET/Bin/net_ClientProfile/ **(Se till att du har installerat produkten med MSI-installationsprogrammet på din dator.)**
- Klicka på **OK** för att stänga dialogrutan

{{% alert color="primary" %}} 

Om ditt VS.NET 2010-projektets målramverk är ".NET Framework 4" eller annat, använd sedan helt enkelt filen Aspose.Cells.dll-komponenten som finns i mappen net4.0/net2.0.

{{% /alert %}} 
## **Referensering av Aspose.Cells Grid Controls från ett .NET-projekt**
För att använda en rutreglage i din applikation, lägg till en referens till den. För att referera till ett rutreglage i Visual Studio gör du följande:

- I **Solution Explorer**, expandera projektnoden som du vill lägga till en referens till.
- Högerklicka på **References**-noden för projektet och välj **Add Reference** i menyn.
- I dialogrutan **Add Reference**, välj fliken **.NET** (vald som standard). Om du har använt MSI-installationsprogrammet för att installera Aspose.Cells for .NET visas Aspose.Cells.GridDesktop och Aspose.Cells.GridWeb i det övre fönstret.
- Välj dem och klicka på **Välj**.
- Referenserna Aspose.Cells.GridDesktop och Aspose.Cells.GridWeb visas under noden References för projektet.

Om du har laddat ner och packat upp endast DLL:

- Lokalisera filerna Aspose.Cells.GridDesktop.dll och Aspose.Cells.GridWeb.dll med hjälp av knappen Bläddra. Aspose.Cells Grid Suite har refererats och bör visas i **Ändrade komponenter**-fönstret i dialogrutan.
- Klicka på **OK.**
## **Avinstallera Aspose.Cells for .NET**
Om du har använt MSI-installationsprogrammet för att distribuera Aspose.Cells for .NET, följ dessa steg för att helt ta bort komponenten och reglagen, de associerade demoversionerna och dokumentationerna:

- Från **Start**-menyn väljer du **Inställningar**, följt av **Kontrollpanelen**.
- Klicka på **Lägg till/ta bort program**.
- Välj Aspose.Cells for .NET (version).
- Klicka på **Ändra/Ta bort** för att ta bort Aspose.Cells.
