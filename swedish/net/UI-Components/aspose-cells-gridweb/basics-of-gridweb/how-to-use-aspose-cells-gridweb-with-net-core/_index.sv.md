---
title: Hur man använder Aspose.Cells.GridWeb med .NET Core
type: docs
weight: 40
url: /sv/net/how-to-use-aspose-cells-gridweb-with-net-core/
---
{{% alert color="primary" %}} 

Det här avsnittet förklarar hur du använder Aspose.Cells.GridWeb med .NET Core-applikationer med Visual Studio.NET 2019. Det här ämnet är användbart för utvecklare på nybörjarnivå som arbetar med Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Använd Aspose.Cells.GridWeb med .NET Core**
Det här ämnet visar hur du använder Aspose.Cells.GridWeb genom att göra en exempelwebbplats i Visual Studio 2019. Processen har delats upp i steg.
### **Steg 1: Skapa ett nytt projekt**
1. Öppna Visual Studio 2019.
1.  Från**Fil** menyn, välj**Ny** , då**Projekt**.
 Skapa ett nytt projekt dialogrutan öppnas.
1.  Välj**ASP.NET Core Web Application** från Visual Studio installerade projektmallar och klicka**Nästa**.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_1.jpg)

1.  Ange en plats där platsen och namnet på projektet och klicka**Skapa**.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_2.jpg)

1.  Välj**Webbapplikation (Model-View-Controller)** mall och se till att**ASP .NET Core 2.1** är vald.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_3.jpg)

1.  Klick**Skapa**.
### **Steg 2: Kontrollera den ursprungliga vyn**
Att köra det nyskapade projektet visar standardmallen i webbläsaren som visas i bilden nedan.



![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_4.jpg)
### **Steg 3: Lägger till Aspose.Cells.GridWeb**
1. Lägg till följande Nuget-paket till projektet

<PackageReference Include="Microsoft.AspNetCore.App" />
<PackageReference Include="Microsoft.AspNetCore.Razor.Design" Version="2.1.2" PrivateAssets="All" />
<PackageReference Include="Newtonsoft.Json" Version="12.0.3" />
<PackageReference Include="System.Drawing.Common" Version="4.7.0" />
<PackageReference Include="System.Text.Encoding.CodePages" Version="4.7.0" />

1. Lägg till Aspose.Cells.GridWeb Package

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_5.jpg)

1. Lägg till följande i filen **_ViewImports.cshtml** i mappen Views.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-ViewImports.cs" >}}

Filen kommer att se ut så här efter ändringarna

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_6.jpg)

1. Lägg in följande kod i HomeController's Index-metoden.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-HomeController.cs" >}}

{{% alert color="primary" %}} 

Kom ihåg att uppdatera SessionStorePath och ImportExcelFile-sökvägen.

{{% /alert %}} 

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_7.jpg)

1.  Lägg till följande kod i**Index.cshtml** fil i Visa > Hemkatalog.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-IndexView.cs" >}}

Filen kommer att se ut så här efter ändringen.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_8.jpg)

1. Lägg till sessionsstöd och GridScheduedService i filen Startup.cs
 1. Lägg till följande kodavsnitt i metoden ConfigureServices.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup1.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_9.jpg)

1. Lägg till följande kodavsnitt i konfigureringsmetoden.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup2.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_10.jpg)

1. Lägg den senaste acw_clienten i katalogen: **wwwroot/js** {{% alert color="primary" %}} {{% /alert %}}
1.  Lägg till**AcwController** Controllers för att hantera acw-ruttkartan som kan tillhandahålla alla standardoperationer för allmänna redigeringsåtgärder.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-AcwController.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_11.jpg)
### **Steg 4: Testa appen**
Om du kör appen kommer resultatet att likna det som visas i bilden nedan.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_12.jpg)
