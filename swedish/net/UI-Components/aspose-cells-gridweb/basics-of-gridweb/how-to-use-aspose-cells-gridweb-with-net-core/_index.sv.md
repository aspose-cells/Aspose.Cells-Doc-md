---
title: Hur man använder Aspose.Cells.GridWeb med .NET Core
type: docs
weight: 40
url: /sv/net/aspose-cells-gridweb/how-to-use-aspose-cells-gridweb-with-net-core/
keywords: GridWeb,dotnetcore
description: Denna artikel introducerar hur man använder GridWeb i .net core webapplikation
---

{{% alert color="primary" %}} 

Denna artikel förklarar hur man använder Aspose.Cells.GridWeb med .NET Core-applikationer med Visual Studio.NET 2019. Denna artikel är användbar för utvecklare på nybörjarnivå som arbetar med Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Använd Aspose.Cells.GridWeb med .NET Core**
Denna artikel visar hur man använder Aspose.Cells.GridWeb genom att skapa en exempelwebbplats i Visual Studio 2019. Processen har delats upp i steg.
### **Steg 1: Skapa ett nytt projekt**
1. Öppna Visual Studio 2019.
1. Från **Fil**-menyn, välj **Ny**, sedan **Projekt**.
   Skapa ett nytt projektfönster öppnas.
1. Välj **ASP.NET Core Web Application** från Visual Studio installerade projektmallar och klicka på **Nästa**.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_1.jpg)

1. Ange en plats där platsen och namnet på projektet och klicka på **Skapa**.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_2.jpg)

1. Välj mallen **Webbapplikation (Modell-Visnings-Controller)** och se till att **ASP .NET Core 2.1** är valt. 

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_3.jpg)

1. Klicka på **Skapa**.
### **Steg 2: Kontrollera den initiala vyn**
Att köra det nyss skapade projektet visar standardmallen i webbläsaren enligt bilden nedan.



![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_4.jpg)
### **Steg 3: Lägga till Aspose.Cells.GridWeb**
1. Lägg till följande Nuget-paket i projektet

<PackageReference Include="Microsoft.AspNetCore.App" />
<PackageReference Include="Microsoft.AspNetCore.Razor.Design" Version="2.1.2" PrivateAssets="All" />
<PackageReference Include="Newtonsoft.Json" Version="12.0.3" />
<PackageReference Include="System.Drawing.Common" Version="4.7.0" />
<PackageReference Include="System.Text.Encoding.CodePages" Version="4.7.0" />

1. Lägg till Aspose.Cells.GridWeb-paket

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_5.jpg)

1. Lägg till följande i filen **_ViewImports.cshtml** i mappen Vy.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-ViewImports.cs" >}}

Filen kommer att se ut så här efter modifieringarna

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_6.jpg)

1. Lägg följande kod i HomeController's Index-metod.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-HomeController.cs" >}}

{{% alert color="primary" %}} 

Kom ihåg att uppdatera SessionStorePath och ImportExcelFile-sökvägen.

{{% /alert %}} 

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_7.jpg)

1. Lägg till följande kod i filen **Index.cshtml** i View > Home-katalogen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-IndexView.cs" >}}

Filen kommer se ut så här efter ändringen.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_8.jpg)

1. Lägg till Session-stöd och GridScheduedService i filen Startup.cs.
   1. Lägg till följande kodsnutt i metoden ConfigureServices.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup1.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_9.jpg)

1. Lägg till följande kodsnutt i metoden Configure.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup2.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_10.jpg)

1. Placera den senaste acw_client i katalogen: **wwwroot/js** {{% alert color="primary" %}}   {{% /alert %}}
1. Lägg till **AcwController** i Controllers för att hantera acw-routekartan som kan tillhandahålla alla standardåtgärder för allmän redigering.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-AcwController.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_11.jpg)
### **Steg 4: Testa appen**
Att köra appen kommer att ge utdata liknande den som visas i bilden nedan.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_12.jpg)
