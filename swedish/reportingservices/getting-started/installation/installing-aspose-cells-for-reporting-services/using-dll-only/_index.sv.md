---
title: Använder endast DLL
type: docs
weight: 20
url: /sv/reportingservices/using-dll-only/
---
## Så här installerar du Aspose.Cells for Reporting Services med endast DLL:n:

- Besök Aspose.Cells for Reporting Services[nedladdningssida](https://downloads.aspose.com/cells/reportingservices) och ladda ner**Aspose.Cells for Reporting Services (zip)** arkiv som innehåller den senaste versionen av komponenten och den installerade dokumentationen.
 - Det finns 7 typer av versioner Aspose.Cells.ReprotingSerivces.dll i Aspose.Cells.ReportingServices.DLLs_xx.xx.zip. De stöder olika Microsoft rapportserverprodukter.
 - Aspose.Cells.ReportingServices.dll i SSRS2005-mappstöd Microsoft SQL Server 2005 Reporting Services.
 - Aspose.Cells.ReportingServices.dll i SSRS2008-mappstöd Microsoft SQL Server 2008 Reporting Services.
 - Aspose.Cells.ReportingServices.dll i SSRS2008R2-mappstöd Microsoft SQL Server 2008R2/2012/2014 Reporting Services.
 - Aspose.Cells.ReportingServices.dll i SSRS2016-mappstöd Microsoft SQL Server 2016/2017/2019 Reporting Services.
   
- Packa upp arkivet i en katalog på din hårddisk.

- Installera Aspose.Cells for Reporting Services Rapportdesigner:
 - Registrera**Aspose.Cells.ReportingServices.Client.dll**med hjälp av verktyget Regasm.exe.
 - Lägg till Aspose.Cells for Reporting Services tillägg i Excel.
   
- Installera Aspose.Cells for Reporting Services för Microsoft SQL Server Reporting Services tjänstekomponenten:
 - Sätta**Aspose.Cells.ReportingServices.dll** till ${Microsoft installationsmappen för SQL Server Reporting Services}\ReportServer\bin-mappen.
 - Lägg till Aspose.Cells for Reporting Services renderertillägg:
 - Öppna**${Microsoft Installationsmapp för SQL Server Reporting Services}\ReportServer\rsreportserver.config**
 - Lägg till följande rader i<Render>……</Render> element:
{{< highlight "xml" >}}

 <Render>

...

<!--Start here.-->

<Extension Name="ACXLS" Type="Aspose.Cells.ReportingServices.XlsRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACXLSX" Type="Aspose.Cells.ReportingServices.Excel2007XlsxRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACXLSX(Data Only)" Type="Aspose.Cells.ReportingServices.Excel2007SimpleXlsxRenderer,Aspose.Cells.ReportingServices"/>

<Extension Name="ACXLSB" Type="Aspose.Cells.ReportingServices.XlsbRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACXLSM" Type="Aspose.Cells.ReportingServices.Excel2007XlsmRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACXML" Type="Aspose.Cells.ReportingServices.SpreadsheetMLRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACHTML" Type="Aspose.Cells.ReportingServices.HtmlRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACCSV" Type="Aspose.Cells.ReportingServices.CSVRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACODS" Type="Aspose.Cells.ReportingServices.ODSRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACTXT" Type="Aspose.Cells.ReportingServices.TabDelimitedRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACXPS" Type="Aspose.Cells.ReportingServices.XpsRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACMD" Type="Aspose.Cells.ReportingServices.MarkdownRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACTIFF" Type="Aspose.Cells.ReportingServices.TIFFRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACPDF" Type="Aspose.Cells.ReportingServices.PDFRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACPNG" Type="Aspose.Cells.ReportingServices.PNGRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACJPG" Type="Aspose.Cells.ReportingServices.JPGRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACEMF" Type="Aspose.Cells.ReportingServices.EMFRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACDIF" Type="Aspose.Cells.ReportingServices.DifRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACSVG" Type="Aspose.Cells.ReportingServices.SvgRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACJSON" Type="Aspose.Cells.ReportingServices.JsonRenderer,Aspose.Cells.ReportingServices" />
<!--End here.-->

</Render>

{{< /highlight >}}
 - Lägg till Aspose.Cells for Reporting Services behörigheter för att köra:
 - Öppna**${Microsoft Installationsmapp för SQL Server Reporting Services}\ReportServer\rssrvpolicy.config** och a
 - Lägg till följande som den sista punkten i den andra till den yttre<CodeGroup> element (vilket borde vara<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. "> ): 

{{< highlight "xml" >}}

 <CodeGroup>

...

<CodeGroup>

...

<!--Start here.-->

<CodeGroup class="UnionCodeGroup" version="1" PermissionSetName="FullTrust" Name="Aspose.Cells_for_Reporting_Services" Description="This code group grants full trust to the Aspose.Cells for Reporting Services assembly.">

<IMembershipCondition class="StrongNameMembershipCondition" version="1" PublicKeyBlob="00240000048000009400000006020000002400005253413100040000010001002780c08eaa89aedfb00b1b96137cca3e15f32826e0e4fd1da3c98d1e3968a03a019aa7b7228b151f6e5dae4dcb00f98479770f507626b04e786e5e93ec3757c1cc4ed1ac4b72c7649c4438e9d3a5f44d8b7522043686a2e8c2a495e04b917e0505d3201015c828e3c15afc8a46ab78293574b9e0475df68627bbabc5b564addd" />

</CodeGroup>

<!--End here.-->

</CodeGroup>

</CodeGroup>

{{< /highlight >}}

## Kontrollera att Aspose.Cells for Reporting Services har installerats:
1. Öppna rapporthanteraren och kontrollera listan över tillgängliga exporttyper för en rapport. (Starta Report Manager genom att öppna en webbläsare och skriv URL:en för Report Manager i adressfältet. (Som standard är URL:en http://<ComputerName>/Rapporter).
 1. Välj en av rapporterna på servern och öppna**Välj Format** lista.
 Du bör se listan över exportformat som tillhandahålls av Aspose.Cells for Reporting Services.
 1. Välj**XLS – Excel-arbetsbok via Aspose.Cells**.
 1. Klicka**Exportera**.
 Rapporten genereras i valt format.
 1. Skicka den till klienten och öppna den i en lämplig applikation. I det här fallet öppnas rapporten i Microsoft Excel.

Grattis, du har framgångsrikt installerat Aspose.Cells for Reporting Services och genererat en rapport som en Microsoft Excel-fil!


 Det finns 7 typer av versioner Aspose.Cells.ReprotingSerivces.dll i Aspose.Cells.ReportingServices.DLLs_xx.xx.zip. De stöder olika Microsoft rapportserverprodukter.